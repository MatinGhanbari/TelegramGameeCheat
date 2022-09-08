import json
import time
from random import Random
import hashlib

import requests


class Gamee:
    url: str
    gameData: json
    gameStatus: json
    header: json
    optionsHeader: json
    gamePlayId: json
    options: json

    def __init__(self):
        super(Gamee, self).__init__()

    def setGame(self, url: str):
        if url is not None:
            self.url = url
            self.trimUrl()

    @staticmethod
    def generateRandomPlayTime(score: int) -> int:
        playTime = (Random().random() + 0.5) * (score + 0.1) * 3
        return round(playTime)

    @staticmethod
    def generateCheckSum(score: int, playTime: int, url: str, gameStateData: str = ''):
        checksum_string = f'{score}:{playTime}:{url}:{gameStateData}:crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen'
        checksum = hashlib.md5(checksum_string.encode('utf-8')).hexdigest()
        return checksum

    def trimUrl(self) -> str:
        return self.url[self.url.find('/game-bot'): self.url.find('#')]

    def initOptions(self):
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
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/103.0.0.0 Safari/537.36',
        }

        options = requests.options('https://api.service.gameeapp.com/', headers=headers)
        self.options = options.json()
        return options.json()

    def initGameData(self):
        headers = {
            'authority': 'api.service.gameeapp.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.9,fa;q=0.8,en-US;q=0.7',
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
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/103.0.0.0 Safari/537.36',
            'x-install-uuid': 'cc284b8a-3ed9-4dd0-88a1-ca8af75fb1ec',
        }

        data = '{"jsonrpc": "2.0", "id": "game.getWebGameplayDetails", "method": "game.getWebGameplayDetails",' \
               '"params": {' \
               f'"gameUrl": "{self.url}"' \
               '}}'
        response = requests.post('https://api.service.gameeapp.com/', headers=headers, data=data,
                                 params=self.initOptions())
        self.gameData = response.json()
        # self.gameStatus = self.gameData['']
        return response.json()

    @staticmethod
    def saveData(file: str, data, method: str = 'w+') -> None:
        with open(file, method) as dataFile:
            dataFile.write(str(data).replace("\'", "\""))

    @staticmethod
    def readData(file: str) -> list[str]:
        with open(file, 'r+') as dataFile:
            return dataFile.readlines()

    def updateGame(self, score: int):
        pass
