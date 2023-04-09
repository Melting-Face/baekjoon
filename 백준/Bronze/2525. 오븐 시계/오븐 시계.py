from sys import stdin

start_time, interval = [data.strip() for data in stdin.readlines()]
start_hour, start_minute = [int(data) for data in start_time.split()]

hour, minute = divmod(int(interval), 60)

remain_hour, end_minute = divmod(start_minute + minute, 60)

end_hour = start_hour + remain_hour + hour
end_hour = int(end_hour % 24)

print(end_hour, end_minute)