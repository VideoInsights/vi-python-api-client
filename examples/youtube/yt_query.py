###
### Sample code to demonstrate how to query a YouTube video, taking into account only the audio but not the video of it.
###

import videoinsights_client
from examples.common.api_key_settings import get_api_key
from videoinsights_client import YTQuery
from videoinsights_client.rest import ApiException

api_key_dict = {'VideoInsightsAuthentication': get_api_key()}
configuration = videoinsights_client.Configuration(api_key=api_key_dict)


with videoinsights_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class

    api_instance = videoinsights_client.QueryApi(api_client)

    try:
        print("Calling Youtube Query endpoint")
        # Contruct the query with the youtube video ID
        # E.g. https://www.youtube.com/watch?v=3EI08o-IGYk -> video_id = 3EI08o-IGYk
        q = YTQuery(query="What is this video about ?", video_id="3EI08o-IGYk")

        # Send the request to the API and capture response
        api_response = api_instance.yt_query_v1(q)

        print("The response for the query:\n")
        print(api_response)
    except ApiException as e:
        print(f"Exception when calling Youtube Query endpoint: %s\n{e}")
