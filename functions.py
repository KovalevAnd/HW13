import json


def read_json(file):
    with open(file, encoding='utf-8') as f:
        return json.load(f)


def get_hash_tag(raw_json):
    hash_tag_word = set()
    for i in raw_json:
        content = i['content']
        words = content.split()
        for j in words:
            if j.startswith('#'):
                hash_tag_word.add(j[1:])
    return hash_tag_word

