import schedule
import threading
import time
from tokenHandler.tokenHandler import *
from classes import *
from utils import *
from datetime import datetime

#def corpo_main():
@run_in_thread
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

@run_in_thread
def main_summarizer(token_acesso: tokenHandler, sumarizador: summarizer) -> None:
    if not token_acesso.is_valid():
        token_acesso.get_access_token()
        motor.change_token(token_acesso.ACCESS_TOKEN)
        log_message('Token de acesso invalido, executando novamente o processo')
    if sumarizador.verify_engine():
        try:
            log_message(f'Executando extração {datetime.now()}')
            sumarizador.extract_data()
            log_message(f'Extração realizada com sucesso {datetime.now()}')
            log_message(f'Próxima extração em {datetime.now() + timedelta(hours=1)}')
        except Exception as err:
            mins: int = 5
            log_message(f'Erro na extração, agendando nova extração para {datetime.now() + timedelta(minutes= mins)}')
            print(err)
            schedule_once(mins, main_extractor, token_acesso, motor)

if __name__ == '__main__':
    #Instanciado o token
    token_acesso = tokenHandler('https://oauth.battle.net/token', 'dadc296d33ad4d89b461625e765dab61', 'IhTLcEUksRNtisRQKwylUmBf91teqZZH')
    token_acesso.get_access_token()

    #Instanciando o motor SQL
    motor = ah2Sql('mysql', 'pymysql', 'root', '', 'localhost', '3306', 'ah2sql', 'summary', token_acesso.ACCESS_TOKEN)
    motor_sum = summarizer('mysql', 'pymysql', 'root', '', 'localhost', '3306', 'ah2sql', 'summary', token_acesso.ACCESS_TOKEN)

    #Executando a função 1 vez
    main_extractor(token_acesso, motor)

    #Criando o loop
    schedule.every(1).hours.do(main_extractor, token_acesso, motor)
    schedule.every().day.at("00:00").do(main_summarizer, token_acesso, motor_sum)
    
    while True:
        schedule.run_pending() 
        time.sleep(5) 