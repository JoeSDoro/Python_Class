# Program by Joe Doro
# Chapter 5, EX 17, PG. 232

def main():
    num = int(input('Enter a number: '))

    state = is_prime(num)

    if (state == True):
        print ('The number', num, 'is prime!')
    else:
        print ('The number', num, 'is not prime!')

def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            status = False
            break
    else:
        status = True
    return status

main()
