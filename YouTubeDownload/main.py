import yt_dlp
import os

def download_playlist_as_m4a(playlist_url, output_folder):
    """
    Downloads a YouTube playlist as audio in .m4a format, forcing .m4a output.

    Args:
        playlist_url (str): The URL of the YouTube playlist.
        output_folder (str): The path to the folder where audio files will be saved.
    """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best available audio
        'outtmpl': os.path.join(output_folder, '%(title)s.m4a'),
        'nocheckcertificate': True,
        'ignoreerrors': True,  # Keep going if any errors occur during download
        'extractaudio': True,  # Extract audio from videos
         'postprocessor_args': ['-vn', '-acodec', 'libfdk_aac', '-f', 'm4a', '-ab', '192k'], # Force encoding to m4a
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
            print(f"\nPlaylist downloaded successfully to: {output_folder}")
    except Exception as e:
        print(f"Error during download: {e}")


if __name__ == "__main__":
    playlist_url = "YouTube Playlist URL"
    output_folder = r"Folder path"  # Raw string for Windows paths

    download_playlist_as_m4a(playlist_url, output_folder)