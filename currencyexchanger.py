import requests
from bs4 import BeautifulSoup as bs



headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

base_url = 'https://ifin.kz/bank/halykbank/currency-rate/aktau'

def fin_parser(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    a = []
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'tbl-td rate-value'})
        for currency in divs:
            currency = currency.text.strip()
            a.append(currency)

        # Переменные епта
        usd_buy = a[0]
        usd_sell = a[1]
        eur_buy = a[2]
        eur_sell = a[3]
        rub_buy = a[4]
        rub_sell = a[5]

        print("Доступны:\nС тенге - на иностранные валюты, с иностранных валют на тенге")
        print("")
        print("Для:\nС тенге - на иностр введите: fromkz")
        print("С иност - на тенге введите: tokz")

        vvod = input('Введите что вы хотите:')

        # С тенге на иностранные валюты
        if vvod.lower() == "fromkz":
            print("")
            print("Выберите на какую валюту вы хотите перевести тенге: ")
            print("USD, EUR, RUB")
            vvod2 = input("Введите один из допустимых валют\n>")
            print("")
            if vvod2.lower() == "usd":
                your_balance = float(input("Введите сумму в тенге: "))
                usd_summ = your_balance / float(usd_sell)
                print(f"Ваша сумма в USD: {usd_summ}")
            elif vvod2.lower() == "eur":
                your_balance = float(input("Введите сумму в тенге: "))
                eur_summ = your_balance / float(eur_sell)
                print(f"Ваша сумма в EUR:\n>{eur_summ}")
            elif vvod2.lower() == "rub":
                your_balance = float(input("Введите сумму в тенге: "))
                rub_summ = your_balance / float(rub_sell)
                print(f"Ваша сумма в RUB:\n>{rub_summ}")
            else:
                print("Вы ввели что-то неправильное")
                print("Доступно только\n> usd, eur, rub")
        # С иностранных валют в тенге
        elif vvod.lower() == "tokz":
            print("")
            print("Выберите какую валюту вы хотите перевести в тенге: ")
            print("USD, EUR, RUB")
            vvod2 = input("Введите один из допустимых валют\n>")
            print("")
            if vvod2.lower() == "usd":
                your_balance = float(input("Введите вашу сумму в USD: "))
                usd_summ = your_balance * float(usd_buy)
                print(f"Ваша сумма в KZT: {usd_summ}")
            elif vvod2.lower() == "eur":
                your_balance = float(input("Введите вашу сумму в EUR: "))
                eur_summ = your_balance * float(eur_buy)
                print(f"Ваша сумма в KZT: {eur_summ}")
            elif vvod2.lower() == "rub":
                your_balance = float(input("Введите вашу сумму в RUB: "))
                rub_summ = your_balance * float(rub_buy)
                print(f"Ваша сумма в KZT: {rub_summ}")
            else:
                print("Вы ввели что-то неправильное")
                print("Доступно только\n>usd, eur, rub")
        else:
            print("")
            print("Вы ввели что то неправильное")
            print("Доступно только\n> fromkz, tokz")



    else:
        print('BAD')

fin_parser(base_url, headers)
