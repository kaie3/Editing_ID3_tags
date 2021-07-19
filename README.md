# Editing_ID3_tags

## 目的

家族のiTunesなし古いiPod nanoから楽曲データを取り出してみたらID3タグ情報がなかったため追加する
要望により出力ディレクトリ構造を[CD名/曲名.拡張子]にする

## 楽曲データの取り出し方

古のソフト,pod野郎をつかい以下の構成となるよう取り出した
おそらくこうなっているはず
歌手名/CD名/歌手名-曲名.拡張子
CD名がなしときは[Music]となる
!["directory structure"](./img/directory_structure.PNG)

## 参考元

["Pythonでmp3などのID3タグを編集するmutagenの使い方"](https://note.nkmk.me/python-mutagen-mp3-id3/)
