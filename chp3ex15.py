# Program by Joe Doro
# Chapter 3, EX 15, PG. 119

def main():
    seconds = int(input('Enter a number of seconds: '))

    if seconds >= 60:
        minutes = seconds/60
        print ('There are ', minutes, ' minutes in your number of seconds.')

    if seconds >= 3600:
        hours = seconds/3600
        print ('There are ', hours, ' hours in your number of seconds.')

    if seconds >= 86400:
        days = seconds/86400
        print ('There are ', days, ' days in your number of seconds.')
                  

main()
