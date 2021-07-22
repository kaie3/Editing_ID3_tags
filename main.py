import os
import pathlib
import pprint
import shutil

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
                .replace("～", "~")
            )
            artist = (
                str(path.parents[1])
                .replace(str(path.parents[2]) + "/", "")
                .replace("　", " ")  # 全角スペース
                .replace("  ", " ")  # 半角スペース2個
                .replace("～", "~")
            )
            title = (
                str(path.stem)
                .replace("　", " ")  # 全角スペース
                .replace("  ", " ")  # 半角スペース2個
                .replace("～", "~")
            )
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
            new_file_path = new_dir_path + title + extension
            new_file_path = new_file_path.replace("/", "\\")
            id3_tags.append((new_file_path, album, artist, title))

    print("コピー完了!")
    return id3_tags


def writing_to_txt(id3_tags):
    tags = []
    # %_filename_ext% / %album% / %artist% / %title%
    for new_file_path, album, artist, title in id3_tags:
        tags.append(f"{new_file_path}/{album}/{artist}/{title}")

    with open("./tags.txt", mode="w", encoding="utf_8_sig") as f:
        f.writelines("\n".join(tags))


# サブディレクトリも含めてすべてのファイルパスを取得
paths = list(pathlib.Path("./scr").glob("**/*"))
paths_data = get_data_from_paths((paths))
id3_tags = make_out_file(paths_data)
writing_to_txt(id3_tags)
