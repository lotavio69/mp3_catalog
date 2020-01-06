import os
from eyed3 import id3

#ROOT = "/Volumes/User Backup/Musica"
ROOT = "/Users/lantunes/Music/MP3 Cleaning"
CD_PREFIX = "disk_"
ACCEPTED_FILE_TYPES = [".mp3", ".mp2"]

def main():
    traverse_music_tree()

def traverse_music_tree():
    cd_list = os.listdir(ROOT)
    for cd in cd_list:
        if cd.startswith (CD_PREFIX):
            dirname = os.path.join(ROOT, cd)
            print("processing directory " + dirname)
            cd_files = os.listdir(dirname)
            for entry in cd_files:
                extension = os.path.splitext(entry)[1]
                if extension and (extension.lower() in ACCEPTED_FILE_TYPES):
                    filepath = os.path.join(dirname, entry)
                    extract_id3(filepath)
                else:
                    print("File " + entry + " is not accepted! Skipping...")
        else:
            print("Directory " + cd + " is not a disk. Skipping...")

def extract_id3(filepath):
    tag = id3.Tag()
    tag.parse(filepath)

    artist = tag.artist
    # print(artist)
    # title = tag.title
    # print(title)
    track_path = tag.file_info.name
    if not artist:
        print(track_path)

def add_to_db(d):
    print("Added to DB!")

if __name__== "__main__" :
    main()