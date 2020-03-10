import requests
import json

from settings import DOBIE_HOST, DOBIE_PORT


def send_data_to_dobie(job_description):
    """
    This function sends a POST request to the skill annotation tool (Dobie) providing it with the proper input.
    :param payload_dict: The json file used as input for dobie.
    :return:
    Return response text
    Examples:
    >>>send_data_to_dobie({"tasks":[{"label":"95671c903a5b97a9", "jobDescription":"job_text"}]})

    """
    url = "http://{}:{}/annotate".format(DOBIE_HOST, DOBIE_PORT)

    headers = {
        'Content-Type': "application/json",
        'Postman-Token': "53181693-dfea-47df-8a4e-2d7124aeb47a",
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, data=job_description, headers=headers)
    print(response.text)
    return response.text