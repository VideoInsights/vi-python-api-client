###
### Sample code to demonstrate how to programmatically upload a media file to the system.
### For this sample, change the LOCAL_MEDIA_FILE_PATH to a valid local file path.
###

import videoinsights_client
from examples.common.api_key_settings import get_api_key
from examples.common.media_file_util import get_media_file_information, upload_file_to_video_insights
from videoinsights_client import MediaFileList, MediaFileUploadPresignedURL, FileUploadUpdate, MediaFile
from videoinsights_client.rest import ApiException

LOCAL_MEDIA_FILE_PATH = "../example_files/example_video.mp4"

api_key_dict = {'VideoInsightsAuthentication': get_api_key()}
configuration = videoinsights_client.Configuration(api_key=api_key_dict)

# Enter a context with an instance of the API client
with videoinsights_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = videoinsights_client.MediaApi(api_client)
    query_instance = videoinsights_client.QueryApi(api_client)

    try:
        print("Calling media endpoint")
        media_list: MediaFileList = api_instance.media_list()

        # Listing all the currently uploaded media files
        print(f"Number of uploaded media files in the library: {len(media_list.files)}")

        # In order to upload a media file, we need to get some information about the file
        # For example, the local path of the file, the name of the file and the filesize in bytes
        file_name, file_size_bytes = get_media_file_information(LOCAL_MEDIA_FILE_PATH)
        if not file_name or not file_size_bytes:
            print(f"Error getting media file information for {LOCAL_MEDIA_FILE_PATH}")
            print("Exiting...")
            exit(1)
        print(f"Media file name: {file_name}, File size in bytes: {file_size_bytes}")
        presigned_url_response: MediaFileUploadPresignedURL = api_instance.get_presigned_url_for_upload(file_name, file_size_bytes)
        print(f"Got a presigned URL")

        # This url is used to upload the file to the system. The file_uuid becomes important for confirming the upload after completion
        # The link is valid for 30 minutes
        presigned_url = presigned_url_response.presigned_url
        file_uuid = presigned_url_response.file_uuid

        # Upload the file from the local path to VideoInsights using the presigned URL
        result_success = upload_file_to_video_insights(presigned_url, LOCAL_MEDIA_FILE_PATH)
        if not result_success:
            print("File upload failed. Exiting...")
            exit(1)

        # The last step is to confirm the upload of the file has succeeded
        # This will start the pre-processing of the file on the VideoInsights platform
        print("File transmission successful. Confirming the upload...")
        update_request = FileUploadUpdate(file_name=file_name, file_uuid=file_uuid)
        confirmation_response = api_instance.media_upload_update(update_request)
        print(f"File upload confirmed: {confirmation_response}")

        # Checking that the additional file is availble now
        media_list: MediaFileList = api_instance.media_list()

        # Listing all the currently uploaded media files
        for f in media_list.files:
            f: MediaFile
            print(f"File name: {f.name}, Parsing complete: {f.audio_parsed}, File ID: {f.id}, MD5: {f.md5}")
        print(f"Number of uploaded media files in the library: {len(media_list.files)}")

    except ApiException as e:
        print(e)
