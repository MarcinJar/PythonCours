import os

os.system('clear')

prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie: "
prompt += "\nNapisz 'koniec', aby zkończyć działanie programu. "


while True:
    message = input(prompt)
    if message.lower() == 'koniec':
        break
    print(message)