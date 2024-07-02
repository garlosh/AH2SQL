import schedule
import time
from tokenHandler.tokenHandler import *
from classes import *
from utils import *
from datetime import datetime

def main_extractor(token_acesso: tokenHandler, motor: ah2Sql) -> None:
    if not token_acesso.is_valid():
        token_acesso.get_access_token()
        motor.change_token(token_acesso.ACCESS_TOKEN)
        log_message('Token de acesso invalido, executando novamente o processo')
    
    if motor.verify_engine():
        try:
            log_message(f'Executando extração {datetime.now()}')
            motor.extract_data()
            log_message(f'Extração realizada com sucesso {datetime.now()}')
            log_message(f'Próxima extração em {datetime.now() + timedelta(hours=1)}')
        except Exception as err:
            mins: int = 5
            log_message(f'Erro na extração, agendando nova extração para {datetime.now() + timedelta(minutes= mins)}')
            print(err)
            schedule_once(mins, main_extractor, token_acesso, motor)

if __name__ == '__main__':
    
    token_acesso = tokenHandler('https://oauth.battle.net/token', 'dadc296d33ad4d89b461625e765dab61', 'IhTLcEUksRNtisRQKwylUmBf91teqZZH')
    token_acesso.get_access_token()
    motor = ah2Sql('mysql', 'pymysql', 'root', '', 'localhost', '3306', 'ah2sql', 'summary', token_acesso.ACCESS_TOKEN)
    schedule.every(1).hours.do(main_extractor, token_acesso, motor)
    main_extractor(token_acesso, motor)
    while True:
        schedule.run_pending() 
        time.sleep(5) 