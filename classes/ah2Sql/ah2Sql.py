from dataclasses import dataclass
from datetime import datetime
from ..sqlHandler import sqlHandler
import pandas as pd
import requests


@dataclass()
class ah2Sql(sqlHandler):
    ACCESS_TOKEN: str
    def __post_init__(self):
        super().__post_init__()
        self.API_URL = f'https://us.api.blizzard.com/data/wow/connected-realm/4408/auctions/6?namespace=dynamic-classic-us&locale=en_US&access_token={self.ACCESS_TOKEN}'
    
    def get_api_data(self):
        try:
            response = requests.get(self.API_URL).json()
            return response
        except:
            return False

    def change_token(self, token) -> None:
        self.ACCESS_TOKEN = token
    
    def extract_data(self) -> None:
        #Resposta da Api
        response = self.get_api_data()
        
        #Tratando o json para o pandas
        df = pd.DataFrame(response['auctions'])
        del response

        #Pegando a database de nomes para merge
        relacao_itens = self.query_database('SELECT * FROM item_db')
        relacao_itens['item'] = relacao_itens['item'].astype(str)
        
        #Limpando os dados
        df['item'] = df['item'].apply(lambda x: x['id'])
        df['buyout'] = df['buyout'].apply(lambda x: x/10000)
        df.drop(df[df['buyout'] == 0].index, inplace = True)
        df['buyout'] = df.apply(lambda x: x['buyout']/x['quantity'], axis=1)
        df = df.groupby('item')
        df = df['buyout'].describe()
        df['safra'] = datetime.now()
        df = df.rename_axis("item").reset_index()
        df = df.drop(columns= ['25%', '75%'])
        df = df.rename(columns= {'count':'contagem', 'std': 'desvio', 'min':'minimo', 'mean':'media','50%':'mediana', 'max':'maximo'})
        df['item'] = df['item'].astype(str)
        df = df.merge(relacao_itens, how='left', on = 'item')

        df.to_sql(self.DB_TABLE, con=self.ENGINE, if_exists='append', index=False)
        self.ENGINE.dispose()
        return None

if __name__ == '__main__':
    
    #from sqlalchemy import create_engine
    x = ah2Sql('mysql', 'pymysql', 'root', '', 'localhost', '3306', 'ah2sql','data','')
    print(x.verify_engine())
