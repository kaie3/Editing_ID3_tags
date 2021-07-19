import pprint

from mutagen.aac import AAC


def set_id3_tag(file_path: str):
    print(file_path)
    tags = AAC(file_path)
    pprint.pprint(tags)


def show_id3_tags(file_path):
    tags = AAC(file_path)
    print(tags.info)


set_id3_tag(file_path="Anything.m4a")
# 結果表示
show_id3_tags("Anything.m4a")
