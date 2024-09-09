###
### Sample code to demonstrate how to get the user information about your account
###


import videoinsights_client
from examples.common.api_key_settings import get_api_key
from videoinsights_client import UserInformation
from videoinsights_client.rest import ApiException

api_key_dict = {'VideoInsightsAuthentication': get_api_key()}
configuration = videoinsights_client.Configuration(api_key=api_key_dict)

# Enter a context with an instance of the API client
with videoinsights_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = videoinsights_client.UserApi(api_client)
    try:
        print("Calling user information endpoint")
        api_response: UserInformation = api_instance.user_information()

        print("The response of UserInfo:\n")
        print(api_response)

    except ApiException as e:
        print(f"Exception when calling user information endpoint: %s\n{e}")
