###
### Sample code to demonstrate how to visually query a media file, taking into account the audio and video of it.
###

import videoinsights_client
from examples.common.api_key_settings import get_api_key
from videoinsights_client import MediaFileList, MediaFileQuery, MediaFile
from videoinsights_client.rest import ApiException

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

        # Listing all the uploaded media files
        print("The response of Media List:\n")
        for m in media_list:
            m: MediaFile
            print(m)

        # Selecting a single media file to query
        m_file = media_list.files[0]
        print(m_file)

        # Construct the visual query request. Note the 'visual_query' parameter set to True
        # This means it takes into account the audio and video of the medial file
        media_query = MediaFileQuery(media_id=m_file.id, query="Describe the clothing of the people in this video", visual_query=True)

        # Send the request to the API and capture response
        query_response = query_instance.media_file_query_v1(media_query)
        print(query_response)

    except ApiException as e:
        print(e)
