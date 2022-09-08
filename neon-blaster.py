import hashlib

import requests


def getOptions():
    headers = {
        'authority': 'api.service.gameeapp.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.9,fa;q=0.8,en-US;q=0.7',
        'access-control-request-headers': 'authorization,client-language,x-install-uuid',
        'access-control-request-method': 'POST',
        'origin': 'https://prizes.gamee.com',
        'referer': 'https://prizes.gamee.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    options = requests.options('https://api.service.gameeapp.com/', headers=headers)
    return options.json()


def generateCheckSum(score: int, playTime: int, url: str, gameStateData: str = ''):
    checksum_string = f'{score}:{playTime}:{url}:{gameStateData}:crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen'
    return hashlib.md5(checksum_string.encode('utf-8')).hexdigest()


url = "https://prizes.gamee.com/game-bot/neonblast2-7f5c5ca29cb07efc4705f86189974ed11d752114#tgShareScoreUrl=tgb%3A" \
      "%2F%2Fshare_game_score%3Fhash%3DmrCLgPmWXPTAEiKSlUWY"
url = url[url.find("/game"):url.find("#")]

score = 73062
playTime = 112
coins = 25187
pet = 1
ballSpeed = 0.098
pet_ballSpeed = 0.09
guns = 1
damage = 16
skin = 5

gameState = '{' \
            f'"Coins":{coins},"Pet":{pet},"Ball_Speed":{ballSpeed},"Pet_Ball_Speed":{pet_ballSpeed},"Guns":{guns},' \
            f'"Add_Ball_HP":260,"Damage":{damage},"Skin":{skin},"Unlock_Plasma":1,"Unlock_Shield":1,"Unlock_Vortex":1,' \
            f'"Select_Special":1,"Level":172,"Request_Tiny_ball":96,"Request_Medium_ball":52,"Request_Large_ball":14,' \
            f'"Request_Extra_Large_ball":4,"Request_Little_Boss":1,"Request_Big_Boss":1,"Request_Flying_Enemie":6,' \
            f'"Request_Special_Level":1,"Special_Skin_Unlock":1,"Special_Coins_Unlock":1' \
            '}'
checksum = generateCheckSum(score, playTime, url, gameState)
print(checksum)
gameState = gameState.replace('"', '\\"')

data = '{"jsonrpc":"2.0","id":"game.saveWebGameplay",' \
       '"method":"game.saveWebGameplay",' \
       '"params":{"gameplayData":{"gameId":241,' \
       f'"score":{score},"playTime":{playTime},' \
       f'"gameUrl":"{url}",' \
       '"metadata":{"gameplayId":526},"releaseNumber":14,' \
       f'"gameStateData":"{gameState}","createdTime":"2022-07-14T17:32:41+04:30",' \
       f'"checksum":"{checksum}","replayVariant":null,' \
       '"replayData":null,"replayDataChecksum":null,"isSaveState":false,"gameplayOrigin":"game"}}}'
headers = {
    'authority': 'api.service.gameeapp.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9,fa;q=0.8,en-US;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOiIxNjU4MTUxODQ4IiwidXNlcklkIjoyNjY2NDA4NywiaW5zdGFsbFV1aWQiOiJjYzI4NGI4YS0zZWQ5LTRkZDAtODhhMS1jYThhZjc1ZmIxZWMiLCJ0eXBlIjoiYXV0aGVudGljYXRpb25Ub2tlbiIsImF1dGhvcml6YXRpb25MZXZlbCI6ImJvdCIsInBsYXRmb3JtIjoiYm90LXRlbGVncmFtIn0.ObGNP8cwYLVy9pvY2nJW3efiIjYF9XCKfGmCnMvtUBE',
    'client-language': 'en',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://prizes.gamee.com',
    'referer': 'https://prizes.gamee.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-install-uuid': 'cc284b8a-3ed9-4dd0-88a1-ca8af75fb1ec',
}
response = requests.post('https://api.service.gameeapp.com/', headers=headers, data=data, params=getOptions())
print(response.json())
