from yt_dlp import YoutubeDL



# Prompt the user to enter the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Call the download_video function with the provided URL
with YoutubeDL() as ydl:
    ydl.download(video_url)