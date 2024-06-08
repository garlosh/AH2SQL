import schedule
from tokenHandler.tokenHandler import *
from ah2Sql.ah2Sql import *

def main() -> None:
    if(~token_acesso.is_valid()):
        token_acesso.get_access_token()
        motor.change_token(token_acesso.ACCESS_TOKEN)
    
    if(motor.verify_engine()):
        try:
            motor.extract_data()
        except Exception as err:
            print('erro')

if __name__ == '__main__':
    motor = ah2Sql('mysql', 'pymysql', 'usuario', 'pass', 'localhost', '3306', 'teste')
    token_acesso = tokenHandler('https://oauth.battle.net/token', 'dadc296d33ad4d89b461625e765dab61', 'IhTLcEUksRNtisRQKwylUmBf91teqZZH')
    token_acesso.get_access_token()

    schedule.every(2).hours.do(main)