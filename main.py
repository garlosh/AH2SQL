import schedule
import time
from tokenHandler.tokenHandler import *
from ah2Sql.ah2Sql import *

# Agendamento da tarefa a cada 5 minutos
#schedule.every(5).minutes.do(fetch_and_store_data)
#fetch_and_store_data()
# Loop para manter o script rodando e executar as tarefas agendadas
#while True:
    #schedule.run_pending()
    #time.sleep(1)
x = tokenHandler('https://oauth.battle.net/token', 'dadc296d33ad4d89b461625e765dab61', 'IhTLcEUksRNtisRQKwylUmBf91teqZZH')
x.get_access_token()
print(x.ACCESS_TOKEN)