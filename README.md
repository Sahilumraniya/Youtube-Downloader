# YouTube Playlist Downloader

This is a simple Python script to download either a single YouTube video or an entire playlist. It utilizes the `pytube` library to interact with YouTube and download videos.

## Prerequisites

Before running the script, make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

Additionally, install the `pytube` library using pip:

````bash
pip install pytube
````

## Usage

1. Clone this repository or download the `youtube_downloader.py` script.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using Python:

````bash
python youtube_downloader.py
````

4. Follow the instructions prompted by the script:

   - Enter `1` to download a single video.
   - Enter `2` to download an entire playlist.
   - Enter `3` to exit the script.

## How it Works

- To download a single video, provide the URL of the video when prompted. The script will download the highest resolution available.
  
- To download a playlist, provide the URL of the playlist when prompted. The script will iterate through all the videos in the playlist and download them into a folder named after the playlist.

## Note

- Make sure you have a stable internet connection while downloading videos, especially for larger playlists.

- Some videos may be restricted from downloading due to privacy settings or copyright issues. In such cases, the script will display an error message.

## Disclaimer

This script is intended for educational and personal use only. Downloading copyrighted material without permission may violate the terms of service of YouTube and could potentially infringe on the rights of content creators. Use it responsibly and respect the rights of content creators.
