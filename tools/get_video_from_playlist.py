import youtube_dl as dowloader
import sys
from argparse import ArgumentParser


playlist_url = "https://www.youtube.com/playlist?list=PL0TdR9CwSBeHdMq5uaToGbYwUI6XgwBsG"


def get_playlist_links(playlist_url):
    ydl_opts = {}
    with dowloader.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(playlist_url, download=False)
    return True

def check_is_youtube_link(playlist_link, parser):
    if ("youtube.com" not in playlist_link) and ("youtu.be" not in playlist_link):
        print()
        print("This link is invalid!")
        print()
        parser.print_help()
        return False

    else:
        return True

    

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-l", "--link", dest="playlist",
                        help="youtube playlist link to download")

    args = parser.parse_args()

    if not (args.playlist):
        print("No arguments found!!!")
        print()
        parser.print_help()

    else:
        playlist_link = args.playlist
        if check_is_youtube_link(playlist_link, parser):
            get_playlist_links(playlist_link)