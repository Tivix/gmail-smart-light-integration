from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from time import time,sleep

#for light control:
import tinytuya

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    #light configuration part:
    srvnn_bedroom_light={
                    "name": "saravanan bedroom tube",
                    "key": "<your-key-here>",
                    "mac": "<your-mac-here>",
                    "id": "<your-light-id-here>",
                    "ver": 3.3,#verison is mostly 3.3 , change if your version is different
                    "ip": "<your-ip-here>"
                    }
    light = tinytuya.BulbDevice(srvnn_bedroom_light['id'], srvnn_bedroom_light['ip'], srvnn_bedroom_light['key'])
    light.set_version(srvnn_bedroom_light['ver'])  
    light.set_socketPersistent(True) 

    #gmail api part:
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    flag = 0
    while True:
        try:
            service = build('gmail', 'v1', credentials=creds)
            results = service.users().messages().list(userId='me',q="is:unread").execute()
            print(results)
            messages=results.get('messages',[])
            if messages:
                "turn light colors"
                flag = 1
                print("new message/s received")
                light.set_colour(255, 1, 1) #r g b
            elif flag==1:
                #resetting the colors
                flag=0
                light.set_colour(255,255,255) 
        except HttpError as error:
            print(f'An error occurred: {error}')
        sleep(60-time()%60)


if __name__ == '__main__':
    main()