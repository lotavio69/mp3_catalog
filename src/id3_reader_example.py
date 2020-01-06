from eyed3 import id3

FILEPATH = "/Users/lantunes/Music/Beatles/George Harrison Collection/04 - Dark Horse/George Harrison - Ding Dong, Ding Dong.mp3"

tag = id3.Tag()
tag.parse(FILEPATH)

artist = tag.artist
print(artist)
title = tag.title
print(title)
track_path = tag.file_info.name
print(track_path)