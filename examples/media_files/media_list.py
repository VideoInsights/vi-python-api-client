###
### Sample code to demonstrate how to query a media file, taking into account only the audio but not the video of it.
###

import videoinsights_client
from examples.common.api_key_settings import get_api_key
from videoinsights_client import MediaFileList, MediaFileQuery, MediaFile
from videoinsights_client.rest import ApiException

api_key_dict = {'VideoInsightsAuthentication': get_api_key()}
configuration = videoinsights_client.Configuration(api_key=api_key_dict, host="http://localhost:8000")

# Enter a context with an instance of the API client
with videoinsights_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = videoinsights_client.MediaApi(api_client)
    query_instance = videoinsights_client.QueryApi(api_client)

    try:
        print("Calling media endpoint")
        media_list: MediaFileList = api_instance.media_list()

        # Listing all the uploaded media files
        print("The response of Media List:\n")
        print(f"Page: {media_list.page}, Total Pages: {media_list.max_pages}, Has more pages: {media_list.has_more_pages}")
        print(f"Got {len(media_list.files)} media files")
        for m in media_list:
            m: MediaFile
            print(m)


        second_list: MediaFileList = api_instance.media_list(page=2)

        # Listing all the uploaded media files
        print("The response of Media List:\n")
        print(f"Page: {second_list.page}, Total Pages: {second_list.max_pages}, Has more pages: {second_list.has_more_pages}")
        print(f"Got {len(second_list.files)} media files")
        for m in second_list:
            m: MediaFile
            print(m)

    except ApiException as e:
        print(e)
