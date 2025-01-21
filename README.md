# YouTubeVideoToAudioDownload

This project provides a Python script to download YouTube playlists as audio files in .m4a format using the yt_dlp library. The script ensures that the best available audio is downloaded and converted to .m4a format with a specified bitrate.

---

## Table of Contents

1. [🎨 Features](#-features)
2. [📝 Installation](#-installation)
3. [🔧 Usage](#-usage)
5. [📊 Script Overview](#-script-overview)
6. [💭 Example](#-example)
7. [📊 Contributing](#-contributing)
8. [⚖️ License](#-license)

---

## 🎨 Features

- Download YouTube playlists as audio files in .m4a format.
- Ensures the best available audio quality.
- Converts audio to .m4a format with a specified bitrate.
- Handles errors and continues downloading remaining files.

---

## 📝 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/KamiVo/YouTubeVideoToAudioDownload.git
   cd YouTubeVideoToAudioDownload
   ```
2. Install the required dependencies:
```sh
  pip install yt-dlp
```

---

## 🔧 Usage

1. Set the playlist_url and output_folder variables in the main.py script:
```Python
if __name__ == "__main__":
    playlist_url = "YouTube Playlist URL"
    output_folder = r"Folder path"  # Raw string for Windows paths

    download_playlist_as_m4a(playlist_url, output_folder)
```
2. Run the script:
```sh
  python main.py
```

---

## 📊 Script Overview
The script contains a function download_playlist_as_m4a which takes two arguments:

- **`playlist_url`** (str): The URL of the YouTube playlist.
- **`output_folder`** (str): The path to the folder where audio files will be saved.

The function downloads the best available audio, converts it to .m4a format with a specified bitrate, and saves it to the specified output folder.

---

## 💭 Example

```Python
  if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=EXAMPLE"
    output_folder = r"C:\Users\Username\Downloads\YouTubeAudio"

    download_playlist_as_m4a(playlist_url, output_folder)
```

---

## 📊 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

---

## ⚖️ License

This project is licensed under the [Apache License 2.0 License](LICENSE).
