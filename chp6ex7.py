# Program by Joe Doro
# Chapter 6, EX 7, PG. 289
import random

def main():
    myfile = open('test.txt', 'w')

    number = int(input('How many random numbers should be added to the file? '))

    for x in range(number):
        ranNum = random.randint(1, 501)
        myfile.write(str(ranNum) + '\n')

    myfile.close()
    print(number, ' random numbers were added to test.txt.')
    

main()
