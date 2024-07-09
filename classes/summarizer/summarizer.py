from dataclasses import dataclass
from ..sqlHandler import sqlHandler
from datetime import datetime, timedelta
import pandas as pd

@dataclass
class summarizer(sqlHandler):
    LIMIT_DATE: int = 90

    def __post_init__(self):
        super().__post_init__()
    
    def verify_summarization(self) -> None:
        #Calcula self.LIMIT_DATE dias no passado
        dados_passados = datetime.now() - timedelta(days= self.LIMIT_DATE)

        #Remove os registros que estão mais que self.LIMIT_DATE dias no passado
        self.execute_query(f'DELETE FROM summary WHERE DATE(safra) < DATE({dados_passados})')
        return None
        


