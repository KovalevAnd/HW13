from flask import Flask, request, render_template, send_from_directory
from functions import read_json, get_hash_tag, get_post_by_tag, add_post

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', hash_tags=get_hash_tag(read_json(POST_PATH)))


@app.route("/tag")
def page_tag():
    tag = request.args.get('tag')
    if not tag:
        return 'abort(400)'
    posts = get_post_by_tag(read_json(POST_PATH), tag)
    return render_template('post_by_tag.html', tag=tag, posts=posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == 'GET':
        return render_template('post_form.html')
    content = request.form.get('content')
    picture = request.files.get('picture')
    if not content or not picture:
        print('abort 400')
    path = f'{UPLOAD_FOLDER}/{picture.filename}'
    post = {
        'content': content,
        'pic': f'/{path}'
    }
    picture.save(path)
    add_post(post, POST_PATH)
    return render_template('post_uploaded.html', post=post)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)

