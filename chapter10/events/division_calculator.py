import os

os.system("clear")

print("Podaj dwie liczby które zostaną podzielone.")
print("Wpisz 'q', aby zakończyć działanie programu.")

while True:
    first_number = input("\nPierwsza liczba: ")
    if first_number == 'q':
        break

    second_number = input("Druga liczba: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")
    except ValueError:
        print("Musisz podać liczby nie inne znaki")
    except:
        print("Jakiś nie określony wyjątek")
    else:
        print(answer)




