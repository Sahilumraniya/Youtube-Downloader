from pytube import Playlist, YouTube
import os

def download_video(video, output_path="downloads"):
    try:
        # Download the highest resolution available
        video_stream = video.streams.get_highest_resolution()
        video_stream.download(output_path=output_path)
        print(f"Downloaded: {video.title}")
    except Exception as e:
        print(f"Failed to download {video.title}. Error: {e}")

def download_playlist(playlist_url, output_path="downloads"):
    # Create a Playlist object
    playlist = Playlist(playlist_url)
    print(f"Downloading playlist: {playlist.title}")

    # Ensure output path exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    download_path = os.path.join(output_path, playlist.title)
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Iterate through all videos in the playlist and download them
    for video_url in playlist.video_urls:
        try:
            video = YouTube(video_url)
            download_video(video, download_path)
        except Exception as e:
            print(f"Failed to process video URL: {video_url}. Error: {e}")

if __name__ == "__main__":
    print("Welcome to the YouTube Playlist Downloader!")
    print("1. Download a single video")
    print("2. Download a playlist")
    print("3. Exit")

    choice = int(input("Enter your choice (1/2/3): "))

    while True:
        match choice:
            case 1:
                video_url = input("Enter the URL of the video: ")
                video = YouTube(video_url)
                download_video(video)
            case 2:
                playlist_url = input("Enter the URL of the playlist: ")
                download_playlist(playlist_url)
            case 3:
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")
                choice = input("Enter your choice (1/2/3): ")
