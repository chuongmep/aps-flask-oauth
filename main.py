# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
import os
from aps_toolkit import Auth

app = Flask(__name__)

@app.route('/')
def hello_world():
    result = "Welcome to APS Toolkit"
    text1 = "<a href='/auth2leg'>Auth 2 legged</a>"
    text2 = "<a href='/auth3leg'>Auth 3 legged</a>"
    text3 = "<a href='/auth3legPkce'>Auth 3 legged PKCE</a>"
    return result + "<br>" + text1 + "<br>" + text2 + "<br>" + text3


@app.route('/auth2leg')
def auth2leg():
    client_id = os.environ.get('APS_CLIENT_ID')
    client_secret = os.environ.get('APS_CLIENT_SECRET')
    auth = Auth(client_id, client_secret)
    token = auth.auth2leg()
    print(token.access_token)
    return token.access_token

@app.route('/auth3leg')
def auth3leg():
    client_id = os.environ.get('APS_CLIENT_ID')
    client_secret = os.environ.get('APS_CLIENT_SECRET')
    auth = Auth(client_id, client_secret)
    redirect_uri = "http://localhost:8080/api/auth/callback"
    scopes = 'data:read viewables:read'
    token = auth.auth3leg(redirect_uri, scopes)
    print(token.refresh_token)
    return token.access_token


@app.route('/auth3legPkce')
def auth3legPkce():
    client_id = os.environ.get('APS_CLIENT_PKCE_ID')
    auth = Auth()
    redirect_uri = "http://localhost:8080/api/auth/callback"
    scopes = 'data:read viewables:read'
    token = auth.auth3legPkce(client_id, redirect_uri, scopes)
    print(token.refresh_token)
    return token.access_token


if __name__ == '__main__':
    app.run()
