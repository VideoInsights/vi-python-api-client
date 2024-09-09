##
## This file contains a helper function to get the API key from the .env file.
##


from dotenv import load_dotenv
import os

def get_api_key() -> str:
    """
    This is just a helper function to get the API key from the .env file.
    You can your own method to securely retrieve the API key from your storage.

    This function uses the `python-dotenv` package to load environment variables
    from a .env file located in the root directory of the project. It then retrieves
    the value of the environment variable `vi_api_key`.

    The format of the returned key is vi_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_xxxxxxxx

    Returns:
        str: The value of the `vi_api_key` environment variable, or None if the variable is not found.
    """
    load_dotenv()
    return os.getenv("vi_api_key", None)