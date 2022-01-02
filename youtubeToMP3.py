from __future__ import unicode_literals
import youtube_dl
import getopt, sys


def download_url(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'continue_dl': True,
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



def main(argv):
   try:
      opts, args = getopt.getopt(argv,'hu:', ["url="])
   except getopt.GetoptError:
      print('youtubeToMP3.py -u <url>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('youtubeToMP3.py -u <url>')
         print ("im HERE 2")
         sys.exit()
      elif opt in ("-u", "--url"):
         download_url(arg)


if __name__ == "__main__":
   main(sys.argv[1:])