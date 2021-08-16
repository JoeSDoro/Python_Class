# Program by Joe Doro
# Chapter 4, EX 6, PG. 162

def main():
    print('Celsius\tFahrenheit')
    print('-------------------')

    for tempC in range(1, 21):
        tempF = tempC * 1.8 + 32
        print(tempC, '\t', tempF)

main()
