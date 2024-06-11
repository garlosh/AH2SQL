import schedule

def schedule_once(minutes: int, func: function, *args, **kwargs) -> None:
    def wrapper():
        func(*args, **kwargs)
        return schedule.CancelJob
    
    schedule.every(minutes).minutes.do(wrapper)

def log_message(message, log_file='log.txt', print = True) -> None:
    if print:
        print(message)
    with open(log_file, 'a') as file:
        file.write(message + '\n')