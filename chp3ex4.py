# Program by Joe Doro
# Chapter 3, EX 4, PG. 116

def main():
    number = int(input('Enter a number 1 through 10: '))

    if number == 1:
        print ('The roman numeral for 1 is I')
    else:
        if number == 2:
            print ('The roman numeral for 2 is II')
        else:
            if number == 3:
                print ('The roman numeral for 3 is III')
            else:
                if number == 4:
                    print ('The roman numeral for 4 is IV')
                else:
                    if number == 5:
                        print ('The roman numeral for 5 is V')
                    else:
                        if number == 6:
                            print ('The roman numeral for 6 is VI')
                        else:
                            if number == 7:
                                print ('The roman numeral for 7 is VII')
                            else:
                                if number == 8:
                                    print ('The roman numeral for 8 is VIII')
                                else:
                                    if number == 9:
                                        print ('The roman numeral for 9 is IX')
                                    else:
                                        if number == 10:
                                            print ('The roman numeral for 10 is X')
                                        else:
                                            print ('Your number is not between 1 and 10')
                                            

main()
