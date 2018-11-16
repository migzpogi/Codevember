import time

def countdown(time_in_seconds):
    while time_in_seconds:
        mins, secs = divmod(time_in_seconds, 60)
        if mins > 59:
            hours, mins = divmod(mins, 60)
            if hours > 24:
                days, hours = divmod(hours, 24)
                if days > 365:
                    years, days = divmod(days, 365)
                else:
                    years = 0
            else:
                days = 0
                years = 0
        else:
            hours = 0
            days = 0
            years = 0

        timeformat = '{:02d}:{:02d}:{:02d}:{:02d}:{:02d}'.format(years, days, hours, mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_in_seconds -= 1

if __name__ == '__main__':
    # 8760 hours in 1 year, or 31536000 seconds
    countdown(31536000 * 5000000000)