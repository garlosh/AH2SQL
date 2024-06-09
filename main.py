import schedule
from tokenHandler.tokenHandler import *
from ah2Sql.ah2Sql import *

def main(token_acesso, motor) -> None:
    if not token_acesso.is_valid():
        token_acesso.get_access_token()
        motor.change_token(token_acesso.ACCESS_TOKEN)
        main()
    if motor.verify_engine():
        try:
            motor.extract_data()
        except Exception as err:
            print('erro')

if __name__ == '__main__':
    
    token_acesso = tokenHandler('https://oauth.battle.net/token', 'dadc296d33ad4d89b461625e765dab61', 'IhTLcEUksRNtisRQKwylUmBf91teqZZH')
    token_acesso.get_access_token()
    #print(token_acesso.ACCESS_TOKEN)
    motor = ah2Sql('mysql', 'pymysql', 'root', '', 'localhost', '3306', 'ah2sql', 'data', token_acesso.ACCESS_TOKEN)
    motor.extract_data()
    #main(token_acesso=token_acesso, motor=motor)
    #schedule.every(2).hours.do(main)