import requests
import os

def get_media_file_information(local_media_file_path) -> tuple[str, int] | tuple[None, None]:
    """
    This function gets the media file basename and size in bytes of a local file.
    Args:
        local_media_file_path (str): The path to the local media file.
    Returns:
        Tuple[str, int]: A tuple containing the file basename and the file size in bytes.
    """

    file_name = file_size = None

    try:
        with open(local_media_file_path, "rb") as file:
            file_name = os.path.basename(file.name)
            file_size = len(file.read())
    except Exception as e:
        print(f"Error getting media file information")
        print(e)

    return file_name, file_size


def upload_file_to_video_insights(presigned_url: str, local_media_file_path: str) -> bool:
    """
    This function uploads a local media file to VideoInsights using a presigned URL.

    :param presigned_url: The presigned URL retrieved via the API earlier
    :param local_media_file_path:  The path to the local media file
    :return: true if the upload was successful, false otherwise
    """
    try:
        with open(local_media_file_path, 'rb') as local_file_data:
            # Prepare the file as multipart form-data
            files = {'file': local_file_data}

            print("Uploading the file")
            # Use requests to perform a POST with multipart form-data
            response = requests.post(presigned_url, files=files)

            print(f"Upload response: {response.status_code}")

            if response.status_code not in [200, 204]:
                print(f"Upload failed with status code: {response.status_code}")
                print(response.text)
                return False
        return True
    except Exception as e:
        print("Error uploading file to VideoInsights")
        print(e)
        return False
