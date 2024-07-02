from dataclasses import dataclass
from ..sqlHandler import sqlHandler
from datetime import datetime, timedelta
import pandas as pd

@dataclass
class summarizer(sqlHandler):
    def __post_init__(self):
        super().__post_init__()
    
    def verify_summarization(self) -> None:
        resultado = self.query_database(f'SELECT DISTINCT safra FROM {self.DB_TABLE}')
        ontem = datetime.now() - timedelta(days=1)
        ontem.replace
        resultado
        


