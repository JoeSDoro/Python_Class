# Program by Joe Doro
# Chapter 5, EX 18, PG. 232

def main():
    print('These are all the prime numbers from 1 to 100: ', end='')

    for num in range(1, 101):
        state = is_prime(num)
        if (state == True):
            print (num, end =", ")
          


def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            status = False
            break
    else:
        status = True
    return status

main()
