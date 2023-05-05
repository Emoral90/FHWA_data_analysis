import pandas
import requests
import json
import math

url = "https://one.nhtsa.gov/webapi/api/CivilPenalties?format=json"

def get_api_res(url_str):
    response = requests.get(url_str)
    json_resp = response.json()
    results = json_resp["Results"]
    return results

def sort_amount(e):
    return e['Amount']

def sort_company(a):
    return a['Company']


mmenu_choice = None
while mmenu_choice != "5":
    print("\nMain Menu")
    print("==============================")
    print("1) Display all Civil Penalties")
    print("2) Sort penalties by amount")
    print("3) Sort penalties by company")
    print("4) Display correlations")
    print("5) Quit")
    mmenu_choice = input("> ")
    print()


    if mmenu_choice == "1":
        results = get_api_res(url)
        for entry in results:
            print(f"-"*150, "\n")
            print(f"{entry}\n")
        print()

    if mmenu_choice == "2":
        sub_menu2_choice = None
        while sub_menu2_choice != "6":
            print("Sort claim amounts by: ")
            print("==========================")
            print("1) Display average amount")
            print("2) Display max amount")
            print("3) Display min amount")
            print("4) Order from least to greatest")
            print("5) Order from greatest to least")
            print("6) Return to main menu")
            sub_menu2_choice = input("> ")
            print()

            if sub_menu2_choice == "1":
                results = get_api_res(url)
                amount_list = []
                for entry in results:
                    amount_list.append(int(entry.get('Amount')))

                avg = sum(amount_list) / len(amount_list)
                avg_formatted = "{:,.2f}".format(avg)
                print(f"Average fined amount paid: ${avg_formatted}\n")
                

            if sub_menu2_choice == "2":
                results = get_api_res(url)
                amount_list = []
                for entry in results:
                    amount_list.append(int(entry.get('Amount')))

                max = max(amount_list)
                max_formatted = "{:,.2f}".format(max)
                print(f"Maximum fined amount paid: ${max_formatted}\n")

            if sub_menu2_choice == "3":
                results = get_api_res(url)
                amount_list = []
                for entry in results:
                    amount_list.append(int(entry.get('Amount')))

                min = min(amount_list)
                min_formatted = "{:,.2f}".format(min)
                print(f"Minimum fined amount paid: ${min_formatted}\n")

            if sub_menu2_choice == "4":
                results = get_api_res(url)

                results.sort(key=sort_amount)
                for j in results:
                    print(f"{j}\n")
                    print("-"*150)

            if sub_menu2_choice == "5":
                results = get_api_res(url)

                results.sort(key=sort_amount,reverse=True)
                for j in results:
                    print(f"{j}\n")
                    print("-"*150)

    if mmenu_choice == "3":
        print("Claims are presented in alphabetical order\n"
                "==========================================\n")
        results = get_api_res(url)
        results.sort(key=sort_company)
        for j in results:
            print(f"{j}\n")
            print("-"*150)
        print("\n==========================================\n")
        print("Claims are presented in alphabetical order\n")

        continue
    continue

    # print("End of program\n")
    # break