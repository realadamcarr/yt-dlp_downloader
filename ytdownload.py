from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']


# x = input()
# with YoutubeDL() as ydl:
#     ydl.download(x)

def download_video(url):
    try:
        # Create a YouTube object using the provided URL

        # Display the video title
        print(f"Downloading {yt.title}")

        # Get the highest resolution stream and download it
        yt.streams.get_highest_resolution().download()
        print('Download completed!')

    except Exception as e:
        # Print any error that occurs during the download process
        print(f"An error occurred: {e}")


# Prompt the user to enter the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Call the download_video function with the provided URL
with YoutubeDL() as ydl:
    ydl.download(video_url)