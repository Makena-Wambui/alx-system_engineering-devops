#!/usr/bin/python3

"""
First install the DATADOG API CLIENT.

pip install datadog

Before making API calls, you'll need your Datadog API key and application key

"""

from datadog import initialize, api

APPLICATION_KEY = ''

API_KEY = ''

options = {
        'api_key': API_KEY,
        'app_key': APPLICATION_KEY
        }

"""
The initialize function is used to auntenticate your API calls
"""

initialize(**options)

def get_all_dashboards():
    """
    This function retrieves all dashboards.
    """
    dashboards = api.Dashboard.get_all() # this retrieves all dashboards associated with your dd account.

    for db in dashboards['dashboards']:
        print(f"Title: {db['title']}, ID: {db['id']}")


if __name__ == "__main__":
    get_all_dashboards()
