import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Downloads the best video and audio quality
        'outtmpl': '%(title)s.%(ext)s',  # Saves the file as video title
        'merge_output_format': 'mp4',  # Ensures output is in mp4 format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
