from dataclasses import dataclass
from sqlalchemy import create_engine
import pandas as pd

@dataclass
class sqlHandler:
    __DB_TYPE: str  # ou 'postgresql', 'sqlite', etc.
    __DB_DRIVER: str  # driver apropriado para o seu banco de dados
    __DB_USER: str
    __DB_PASS: str
    __DB_HOST: str
    __DB_PORT: str  # porta apropriada para o seu banco de dados
    __DB_NAME: str
    __DB_TABLE: str

    def __post_init__(self) -> None:
        DATABASE_URI = f'{self.__DB_TYPE}+{self.__DB_DRIVER}://{self.__DB_USER}:{self.__DB_PASS}@{self.__DB_HOST}:{self.__DB_PORT}/{self.__DB_NAME}'
        self.__ENGINE = create_engine(DATABASE_URI)

    def __query_database(self, query) -> None:
        resultado = pd.read_sql(query, con= self.__ENGINE)
        self.__ENGINE.dispose()
        return resultado
    
    def verify_engine(self) -> bool:
        try:
            self.__ENGINE.connect()
            self.__ENGINE.dispose()
            return True
        except:
            return False