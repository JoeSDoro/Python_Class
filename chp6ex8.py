# Program by Joe Doro
# Chapter 6, EX 8, PG. 289

def main():
    count = 0
    total = 0
    
    myfile = open('numbers.txt', 'r')

    line = myfile.readline()

    while line != '':

        count = count + 1
        number = float(line)

        total = total + number

        print(number)

        line = myfile.readline()

    myfile.close()

    print('The total of the numbers in the file is', total)
    print('There are', count, 'numbers in the file')
    

main()
