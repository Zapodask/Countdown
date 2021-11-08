from time import sleep
from os import system


class Countdown:
    def __init__(self):
        days = input('Days: ')
        days = self.validation(days)

        nh = 0
        while nh == 0:
            hours = input('Hours: ')
            hours = self.validation(hours)

            if hours > 23:
                print('Max hours is 23')
            else:
                nh += 1

        nm = 0
        while nm == 0:
            minutes = input('Minutes: ')
            minutes = self.validation(minutes)
                
            if minutes > 59:
                print('Max minutes is 59')
            else:
                nm += 1

        ns = 0
        while ns == 0:
            seconds = input('Seconds: ')
            seconds = self.validation(seconds)

            if seconds > 59:
                print('Max seconds is 59')
            else:
                ns += 1

        time = days * 86400 + hours * 3600 + minutes * 60 + seconds

        while time != 0:
            sleep(1)

            time -= 1

            if seconds == 0 and minutes == 0 and hours == 0:
                days -= 1
                hours = 23
                minutes = 59
                seconds = 59
            elif seconds == 0 and minutes == 0:
                hours -= 1
                minutes = 59
                seconds = 59
            elif seconds == 0:
                minutes -= 1
                seconds = 59
            else:
                seconds -= 1

            system('cls')
            print(f'Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}')

        system('cls')
        print('End of countdown')

    def validation(self, i):
        if i == '' or i.isdecimal() == False:
            return 0
        else:
            return int(i)


def main():
    n = 0
    while n == 0:
        system('cls')

        Countdown()

        again = input('Start another countdown?(y/n): ')

        if again != 'y':
            n += 1

if __name__ == '__main__':
    main()
