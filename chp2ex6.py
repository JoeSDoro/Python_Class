# Program by Joe Doro
# Chapter 2, EX 6, PG 78

stateST = 0.05
countyST = 0.025

def main():

    purchase = float(input('Enter the amount of purchase: '))

    stateTotal = purchase * stateST
    countyTotal = purchase * countyST
    totalTax = stateTotal + countyTotal
    total = purchase + totalTax

    print('The Amount of your Purchase was:', purchase)
    print('The State Tax equals:', stateTotal)
    print('The County Tax equals:', countyTotal)
    print('The Total Tax equals:', totalTax)
    print('The Total Purchase with Tax is:', total)

main()
