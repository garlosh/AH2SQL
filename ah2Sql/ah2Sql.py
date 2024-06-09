from dataclasses import dataclass
from sqlalchemy import create_engine
import pandas as pd
import requests
from datetime import datetime
import numpy as np

@dataclass()
class ah2Sql:
    __DB_TYPE: str  # ou 'postgresql', 'sqlite', etc.
    __DB_DRIVER: str  # driver apropriado para o seu banco de dados
    __DB_USER: str
    __DB_PASS: str
    __DB_HOST: str
    __DB_PORT: str  # porta apropriada para o seu banco de dados
    __DB_NAME: str
    __DB_TABLE: str
    __ACCESS_TOKEN: str

    def __post_init__(self):
        self.__API_URL = f'https://us.api.blizzard.com/data/wow/connected-realm/4408/auctions/6?namespace=dynamic-classic-us&locale=en_US&access_token={self.__ACCESS_TOKEN}'
        DATABASE_URI = f'{self.__DB_TYPE}+{self.__DB_DRIVER}://{self.__DB_USER}:{self.__DB_PASS}@{self.__DB_HOST}:{self.__DB_PORT}/{self.__DB_NAME}'
        self.__ENGINE = create_engine(DATABASE_URI)


    def verify_engine(self) -> bool:
        try:
            self.__ENGINE.connect()
            return True
        except:
            return False

    def __get_api_data(self):
        try:
            response = requests.get(self.__API_URL)
            return response
        except:
            return False

    def change_token(self, token) -> None:
        self.__ACCESS_TOKEN = token
    
    
    def extract_data(self) -> None:
        #Resposta da Api
        response = self.__get_api_data()
        
        #Tratando o json para o pandas
        data = response.json()
        data = data['auctions']
        df = pd.DataFrame(data)
        
        #Limpando os dados
        df['item'] = df['item'].apply(lambda x: x['id'])
        df = df.groupby('item')
        df = df['buyout'].describe()
        df['data'] = datetime.now()
        df.rename_axis("item").reset_index()
        df = df.drop(columns= ['25%', '75%'])
        df = df.rename(columns= {'count':'contagem', 'std': 'desvio', 'min':'minimo', '50%':'mediana', 'max':'maximo'})
        df.to_sql(self.__DB_TABLE, con=self.__ENGINE, if_exists='append', index=False)

if __name__ == '__main__':
    
    #from sqlalchemy import create_engine
    #x = ah2Sql('mysql', 'pymysql', 'root', '', 'localhost', '3306', 'ah2sql','data','')
    #print(x.verify_engine())
    datetime.now()