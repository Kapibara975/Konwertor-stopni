from math import *
import time

while True:
        
        Chcę_przeliczyć_stopnie = input("Co chcesz przeliczyć? c=°C,f=°F,k=°K >>> ")

        print()

        Chcę_przeliczyć_na_stopnie = input("Na co chcesz przeliczyć? c=℃,f=℉,k=°K >>> ")

        print()
        try:
                a=float(input("Ile? >>> "))
        except ValueError:
                print('to nie jest liczba!')
                print('ustawiam wybór na 0°')
                a=0

        print()
        print()

        if Chcę_przeliczyć_stopnie=='c' and Chcę_przeliczyć_na_stopnie=='c':
                print(a, '℃')

        elif Chcę_przeliczyć_stopnie=='f' and Chcę_przeliczyć_na_stopnie=='f':
                print(a, '℉')

        elif Chcę_przeliczyć_stopnie=='k' and Chcę_przeliczyć_na_stopnie=='k':
                print(a, '°K')

        elif Chcę_przeliczyć_stopnie=='c' and Chcę_przeliczyć_na_stopnie=='f':
                print(a*1.8+32, '℉')

        elif Chcę_przeliczyć_stopnie=='f' and Chcę_przeliczyć_na_stopnie=='c':
                print((a-32)/1.8, '℃')

        elif Chcę_przeliczyć_stopnie=='c' and Chcę_przeliczyć_na_stopnie=='k':
                print(a+273.15, '°K')

        elif Chcę_przeliczyć_stopnie=='k' and Chcę_przeliczyć_na_stopnie=='c':
                print(a-273.15, '℃')

        elif Chcę_przeliczyć_stopnie=='f' and Chcę_przeliczyć_na_stopnie=='k':
                print(((a-32)/1.8)+273.15, '°K')

        elif Chcę_przeliczyć_stopnie=='k' and Chcę_przeliczyć_na_stopnie=='f':
                print(((a-273.15)*1.8)+32, '℉')

        else:
                print("BŁĄD")
        print()
        try:
                jraz=int(input("Jeszcze raz? enter-TAK 1-NIE >>> "))
                if jraz==1:
                        print("Wychodzę",end="")
                        time.sleep(0.30)
                        print(".",end="")
                        time.sleep(0.30)
                        print(".",end="")
                        time.sleep(0.30)
                        print(".",end="")
                        time.sleep(0.30)
                        exit(code=123)
                else:
                        print("Uznaję, że jeszcze raz.")
                        print("-----------------------------")
        except ValueError:
                print('OK!')
                print("-----------------------------")
        
        
