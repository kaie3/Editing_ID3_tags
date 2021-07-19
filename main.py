import os
import pathlib
import re
import shutil
import pprint

from mutagen.aiff import AIFF


def set_id3_tag(
    file_path: str,
    title=None,
    artist=None,
    albumartist=None,
    album=None,
    genre=None,
    track_num=None,
    total_track_num=None,
    disc_num=None,
    total_disc_num=None,
):
    print(file_path)
    tags = AIFF(file_path)
    pprint.pprint(tags)
    if title:
        tags["title"] = title
    if artist:
        tags["artist"] = artist
    if albumartist:
        tags["albumartist"] = albumartist
    if album:
        tags["album"] = album
    if genre:
        tags["genre"] = genre
    if total_track_num:
        if track_num:
            tags["tracknumber"] = "{}/{}".format(track_num, total_track_num)
        else:
            tags["tracknumber"] = "/{}".format(total_track_num)
    else:
        if track_num:
            tags["tracknumber"] = "{}".format(track_num)
    if total_disc_num:
        if disc_num:
            tags["discnumber"] = "{}/{}".format(disc_num, total_disc_num)
        else:
            tags["discnumber"] = "/{}".format(total_disc_num)
    else:
        if track_num:
            tags["discnumber"] = "{}".format(disc_num)

    # tags.save()


def show_id3_tags(file_path):
    tags = AIFF(file_path)
    print(tags.pprint())


# pathから各種データ取得
def get_data_from_paths(paths):
    paths_data = []
    for path in paths:
        if path.is_file():
            album = (
                str(path.parents[0])
                .replace(str(path.parents[1]) + "/", "")
                .replace("　", " ")  # 全角スペース
                .replace("  ", " ")  # 半角スペース2個
            )
            artist = (
                str(path.parents[1])
                .replace(str(path.parents[2]) + "/", "")
                .replace("　", " ")  # 全角スペース
                .replace("  ", " ")  # 半角スペース2個
            )
            title = (
                re.sub(r".+-", "", path.stem).replace("　", " ").replace("  ", " ")
            )  # 全角スペース,半角スペース2個
            extension = path.suffix
            paths_data.append((str(path), album, artist, title, extension))
    return paths_data


# 取得ディレクトリにコピー
def make_out_file(paths_data):
    id3_tags = []
    for path, album, artist, title, extension in paths_data:
        new_dir_path = f"out/music/{album}/"
        if not os.path.exists(new_dir_path):  # ディレクトリの存在確認
            os.makedirs(new_dir_path, exist_ok=True)
        if not os.path.isfile(new_dir_path + title):  # ファイルの存在確認
            # shutil.copy2(path, new_dir_path + title + extension)
            print("fileコピー中:" + new_dir_path + title + extension)
            id3_tags.append((new_dir_path + title + extension, album, artist, title))

    print("コピー完了!")
    return id3_tags


# サブディレクトリも含めてすべてのファイルパスを取得
paths = list(pathlib.Path("./scr").glob("**/*"))
paths_data = get_data_from_paths((paths))
id3_tags = make_out_file(paths_data)
for path, album, artist, title in id3_tags:
    set_id3_tag(file_path=path, title=title, artist=artist, album=album)
# 結果表示
for path, _album, _artist, _title in id3_tags:
    show_id3_tags(path)
