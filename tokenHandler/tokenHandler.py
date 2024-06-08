from datetime import datetime, timedelta
from dataclasses import dataclass
import requests

@dataclass
class tokenHandler:
    __URL: str
    __CLIENT_ID: str 
    __CLIENT_SECRET: str
    __TOKEN_LIFETIME: int = 86400

    def get_access_token(self) -> str:
        response = requests.post(
            self.__URL,
            data={'grant_type': 'client_credentials'},
            auth=(self.__CLIENT_ID, self.__CLIENT_SECRET),
        )
        self.ACCESS_TOKEN = response.json()['access_token']
        self.TOKEN_EXPIRATION = datetime.now() + timedelta(seconds = self.__TOKEN_LIFETIME)
        return response.json()['access_token']
    
    def is_valid(self) -> bool:
        if datetime.now() > self.TOKEN_EXPIRATION:
            return False
        else:
            return True
        
if __name__ == '__main__':
    
    #import requests 
    x = tokenHandler('https://oauth.battle.net/token', 'dadc296d33ad4d89b461625e765dab61', 'IhTLcEUksRNtisRQKwylUmBf91teqZZH')
    x.get_access_token()
    print(x.ACCESS_TOKEN)
    
