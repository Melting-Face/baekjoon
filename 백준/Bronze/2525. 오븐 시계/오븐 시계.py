from sys import stdin
from datetime import datetime, timedelta

start_time_txt, interval = [data.strip() for data in stdin.readlines()]
start_time = datetime.strptime(start_time_txt, "%H %M")
interval = timedelta(minutes=int(interval))
end_time = start_time + interval
hour = int(datetime.strftime(end_time, "%H"))
minute = int(datetime.strftime(end_time, "%M"))
print(f'{hour} {minute}')