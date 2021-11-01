import json
import boto3
import requests
import datetime
from datetime import date


def lambda_handler(event, context):
    url = "https://bubble.io/apiservice/doapicallfromserver"
    payload = json.dumps({
        "service_name": "bubblebot",
        "call_name": "GetReleaseNotes",
        "prev": None,
        "properties": {
            "provider": "bubblebot.GetReleaseNotes",
            "timestamp": 1627889385051,
            "deployment_messages": False
        },
        "authentication": None,
        "call_location": {
            "_raw": {
                "%n": {
                    "%p": {
                        "%d2": True,
                        "%sf": "timestamp"
                    },
                    "%x": "Message",
                    "%nm": "sorted"
                },
                "%p": {
                    "provider": "bubblebot.GetReleaseNotes",
                    "timestamp": {
                        "%n": {
                            "%x": "Message",
                            "%nm": "get_data"
                        },
                        "%p": {
                            "%ei": "bTHVt"
                        },
                        "%x": "GetElement"
                    },
                    "deployment_messages": {
                        "%n": {
                            "%n": {
                                "%a": "releases",
                                "%x": "Message",
                                "%nm": "equals"
                            },
                            "%x": "Message",
                            "%nm": "custom.showing_"
                        },
                        "%p": {
                            "%ei": "bTHUt"
                        },
                        "%x": "GetElement"
                    }
                },
                "%x": "GetDataFromAPI"
            },
            "current_eval_node": "%p3.bTHVj.%el.bTIWH.%el.bTMQJ.%el.bTVGI.%el.bTVGJ.%p.%ds"
        },
        "serialized_context": {
            "skip_property_security": True
        },
        "page_load_time": 1633073384869,
        "app_last_change": "6539983701",
        "ret_properties": True
    })
    headers = {
        'authority': 'bubble.io',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'x-bubble-utm-data': '{}',
        'x-bubble-fiber-id': '1633073390411x751036293018932500',
        'x-bubble-pl': '1633073385055x1452',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'content-type': 'application/json',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-bubble-r': 'https://bubble.io/releases',
        'x-requested-with': 'XMLHttpRequest',
        'x-bubble-breaking-revision': '5',
        'sec-ch-ua-platform': '"Linux"',
        'origin': 'https://bubble.io',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://bubble.io/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'meta_live_u2main=1632981373931x655892226767088400; meta_live_u2main.sig=bagc_icb6QQJPSH4pzNKxp0HkXA; _ga=GA1.2.1788901889.1632981376; _gid=GA1.2.389320091.1632981376; ajs_anonymous_id=%22f92ac83b-f89a-4911-bdd6-ca7d74e4dad5%22; _gcl_au=1.1.1620800449.1632981377; _fbp=fb.1.1632981376697.695200571; _scid=3ee150e1-a0e9-475b-a6ea-81c03da1dedd; _sctr=1|1632940200000; meta_u1main=1632981373788x921765364553416300; meta-firebase_workflow=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2lkZW50aXR5dG9vbGtpdC5nb29nbGVhcGlzLmNvbS9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdHl0b29sa2l0LnYxLklkZW50aXR5VG9vbGtpdCIsImlhdCI6MTYzMzA3MDE3NywiZXhwIjoxNjMzMDczNzc3LCJpc3MiOiJmaXJlYmFzZS1hZG1pbnNkay14ZnhoYkBidWJibGUtd29ya2Zsb3cuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzdWIiOiJmaXJlYmFzZS1hZG1pbnNkay14ZnhoYkBidWJibGUtd29ya2Zsb3cuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJ1aWQiOiIxNjMyOTgxMzczNzg4eDkyMTc2NTM2NDU1MzQxNjMwMCIsImNsYWltcyI6eyJhcHBfaWQiOiJtZXRhIiwidXNlcl9pZCI6IjE2MzI5ODEzNzM3ODh4OTIxNzY1MzY0NTUzNDE2MzAwIn19.WRUOVhN_Fl-IaKaJB8XObVUzbAzoAn6XRXIoGYBpZB1juoTfWXHJsglz4npQiLZpBXdPlUu6G_0m0vf2rhZf55XqDBaCRxZXxDYA9unloRF7rDXfuIbjSxhJlIjGM0tu0vyfYDxmqlnKopHmVYNVPZnPJWAZw-9zp7XYDDNI8KHFZQ1KNSDv-JRSmOXajIct9n-hLhv1kcQ5aQyJho3eZPK4CTJbj_v9pbJkR-GKOoxhkCyFvXDEVLPoK6ULnzytMzujV2d0hHuOM0rv0nYlSHTAobETUSMTTG7EuhuBur8IFzGq7INkQD_N4sfDXA8cP3ASpJYYKAmp8Ra0Qj82lA; _gat=1; _uetsid=2058b7e021b311ecbf58c10e1020f54c; _uetvid=2058ece021b311ecbc54d71b0b659bd2'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    list = json.loads(response.text)['ret']

    list.reverse()

    new_list = []

    # new_list.append(list[0]['note'])

    for x in list:
        new_list.append(x['note'])

    new_string = ','.join(new_list)

    db = boto3.resource('dynamodb')

    test_table = db.Table('bubble-data')

    today = date.today()

    data = test_table.get_item(
        TableName='bubble-data',
        Key={
            'id': '123445'

        }
    )

    old_string = data['Item']['data']

    if new_string == old_string:
        msg = "Data Already Updated"

    else:

        test_item = {
            'id': '123445',
            'loaded-date': today.strftime("%b-%d-%Y"),
            'data': new_string
        }

        test_table.put_item(Item=test_item)
        msg = "New feature Updated Successfully!"

    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }
