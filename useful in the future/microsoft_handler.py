import json
import msal
import logging
import requests
import pandas
from pymstodo import ToDoConnection
import requests_oauthlib

'''
Todo list:
1. Get Todo password from Settings
2. Pull all lists from Microsoft Todo List
3. Display on window

app secret: 0jk8Q~IzHks--tU1.JuU2q.zMIOp_CvjZ.7uOaYR
app name: Graph Python Quickstart
app ID (or client ID): aaa995d4-cd05-4f22-80f6-97d4084d4121
redirect ID: https://localhost/login/authorized
'''

client_id = 'aaa995d4-cd05-4f22-80f6-97d4084d4121'
client_secret = 'baa205fd-4435-465e-aa8b-2d8f3c1faa1b'

auth_url = ToDoConnection.get_auth_url(client_id)
redirect_resp = input(f'Go here and authorize:\n{auth_url}\n\nPaste the full redirect URL below:\n')
token = ToDoConnection.get_token(client_id, client_secret, redirect_resp)
todo_client = ToDoConnection(client_id=client_id, client_secret=client_secret, token=token)

lists = todo_client.get_lists()
task_list = lists[0]
tasks = todo_client.get_tasks(task_list.list_id)

print(task_list)
print(*tasks, sep='\n')

# Globals
# token = None
# graphApiVersion = "beta"
# uri = "https://graph.microsoft.com/{v}/{r}"
# headers = None
#
#
# # Functions
# def authenticate():
#     global token
#     global headers
#     authority = "https://login.microsoftonline.com/contosocm.onmicrosoft.com"
#     appID = "aaa995d4-cd05-4f22-80f6-97d4084d4121"
#     appSecret = "0jk8Q~IzHks--tU1.JuU2q.zMIOp_CvjZ.7uOaYR"
#     scope = ["https://graph.microsoft.com/.default"]
#
#     app = msal.ConfidentialClientApplication(
#         appID, authority=authority, client_credential=appSecret)
#     token = app.acquire_token_silent(scope, account=None)
#     if not token:
#         token = app.acquire_token_for_client(scopes=scope)
#     headers = {'Authorization': 'Bearer' + token['access_token']}
#     return
#
#
# def lists(Format=True):
#     return query(graphApiVersion, "https://graph.microsoft.com/v1.0/me/todo/lists", Format)
#
#
# def query(v, r, Format=True):
#     dest = uri.format(v=v, r=r)
#     result = requests.get(dest, headers=headers).json()
#     if Format:
#         print(pandas.json_normalize(result["value"]))
#     else:
#         print(result["value"])
#         return result["value"]
#
#
# authenticate()
# lists()
