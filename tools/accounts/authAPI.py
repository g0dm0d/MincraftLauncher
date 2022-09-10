from contextlib import redirect_stderr
import requests
import json
import webbrowser

from .httpserver import mslog


def msauth():
    #MAIN-TOKEN------------------------------------------------------
    webbrowser.open('https://login.live.com/oauth20_authorize.srf?client_id=1a4b9403-1f4d-46f3-9dcb-08aa6f0667e6&response_type=code&redirect_uri=http://localhost:9397&scope=XboxLive.signin%20offline_access&state=NOT_NEEDED', new=2)
    code = mslog()
    #DEFAULT-VARIABLE------------------------------------------------
    client_id='1a4b9403-1f4d-46f3-9dcb-08aa6f0667e6'
    client_secrete = "SUa7Q~fDB1P8JOtUG6mfK8d4A9H_VJLUnmnwF"
    redirect_uri = 'http://localhost:9397'
    #FIRST-TOKEN----------------------------------------------------- MICROSOFT ACC
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = f"client_id={client_id}&client_secret={client_secrete}&code={code}&grant_type=authorization_code&redirect_uri={redirect_uri}"
    code = requests.post("https://login.live.com/oauth20_token.srf", data=data, headers=headers)
    jsontext = str(json.loads(code.text)).replace("'",'"')
    parsed = json.loads(jsontext)
    access_token = parsed["access_token"]
    refresh_token = parsed["refresh_token"]
    #SECOND-TOKEN---------------------------------------------------- XBOX LIVE
    data = '''{
        "Properties": {
            "AuthMethod": "RPS",
            "SiteName": "user.auth.xboxlive.com",
            "RpsTicket": "d='''+access_token+'''"
        },
        "RelyingParty": "http://auth.xboxlive.com",
        "TokenType": "JWT"
    }'''
    headers = {'Content-Type': 'application/json'}
    xboxlive = requests.post("https://user.auth.xboxlive.com/user/authenticate", data=data, headers=headers)
    jsontext = str(xboxlive.text)
    parsed = json.loads(jsontext)
    token = parsed["Token"]
    #THIRD-TOKEN----------------------------------------------------- XSTS
    data = '''{
        "Properties": {
            "SandboxId": "RETAIL",
            "UserTokens": [
                "'''+token+'''"
            ]
        },
        "RelyingParty": "rp://api.minecraftservices.com/",
        "TokenType": "JWT"
    }
    '''
    xsts = requests.post("https://xsts.auth.xboxlive.com/xsts/authorize", data=data, headers=headers)
    jsontext = str(xsts.text)
    parsed = json.loads(jsontext)
    token = parsed["Token"]
    uhs = parsed['DisplayClaims']['xui'][0]['uhs']
    #FOURTH-TOKEN----------------------------------------------------- Minecraft account
    data = '''{
        "identityToken" : "XBL3.0 x='''+uhs+''';'''+token+'''",
        "ensureLegacyEnabled" : true
    }'''
    loginxbox=requests.post("https://api.minecraftservices.com/authentication/login_with_xbox", data=data, headers=headers)
    jsontext = loginxbox.text
    parsed = json.loads(jsontext)
    access_token = parsed["access_token"]
    return access_token
