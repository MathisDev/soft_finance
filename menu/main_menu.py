from menu.config_dir.config_json import *
from pprint import pprint
import inquirer
import json

#   ------------- Menu for search asset do you whant ------------ #
class Menu_search:
        def desc():
                questions = [
                        inquirer.List(
                                "company",
                                message="Set your stat max of asset",
                                choices= ["volacity","CAP","RSI"]
                        ),
                ]
                answers = inquirer.prompt(questions)
                return answers['company']

        def clean_prompt():
                import os
                os.system("clear")

        def main_menu():
                list_menu = ["s","segond"," "]
                Menu_search.clean_prompt()
                list_menu[1] = Menu_search.desc()
                print("How many :")
                value_stat = input()
                list_menu[2] = value_stat
                return list_menu

# ------ Menu for get info of asset ---------- #
class Menu_info:
        def choices_menu_company():
                questions = [
                        inquirer.List(
                                "company",
                                message="What company do you need?",
                                choices= config.extract_list(),
                        ),
                ]
                answers = inquirer.prompt(questions)
                return answers['company']

        def choices_menu_time():
                questions = [
                        inquirer.List(
                                "time",
                                message="What Time do you need?",
                                choices=["1d", "1mo", "1y", "5y", "10y"],
                        ),
                ]
                answers = inquirer.prompt(questions)
                return answers['time']

        def clean_prompt():
                import os
                os.system("clear")

        def main_menu():
                list_menu = ["i","segond"," "]
                Menu_info.clean_prompt()
                list_menu[1] = Menu_info.choices_menu_company()
                if (list_menu[1] == 'add'):
                        print("Wath's the company you whant add :")
                        company_add = input()
                        config.add_company(company_add)
                        Menu_info.main_menu()
                        Menu_info.clean_prompt()
                list_menu[2] = Menu_info.choices_menu_time()
                return list_menu

# ------- Menu for know what you whant ------------- #
class Main_menu:
    def Quiz():
            questions = [
                            inquirer.List(
                                   "Recherche",
                                    message="What do you need?",
                                    choices= ["Recherche d'info sur un actif","Recherche d'actif selon des critere"]
                        ),
            ]
            answers = inquirer.prompt(questions)
            return answers['Recherche']
        
    def main():
        tab_info = []
        menu_return = Main_menu.Quiz()
        if menu_return == "Recherche d'info sur un actif":
            tab_info= Menu_info.main_menu()
        elif menu_return == "Recherche d'actif selon des critere":
            tab_info = Menu_search.main_menu()
        return tab_info

    class Menu_info:
            def choices_menu_company():
                    questions = [
                            inquirer.List(
                                    "company",
                                    message="What company do you need?",
                                    choices= config.extract_list(),
                            ),
                    ]
                    answers = inquirer.prompt(questions)
                    return answers['company']

            def choices_menu_time():
                    questions = [
                            inquirer.List(
                                    "time",
                                    message="What Time do you need?",
                                    choices=["1d", "1mo", "1y", "5y", "10y"],
                            ),
                    ]
                    answers = inquirer.prompt(questions)
                    return answers['time']

            def clean_prompt():
                    import os
                    os.system("clear")

            def main_menu():
                    list_menu = ["i","segond"," "]
                    Menu_info.clean_prompt()
                    list_menu[1] = Menu_info.choices_menu_company()
                    if (list_menu[1] == 'add'):
                            print("Wath's the company you whant add :")
                            company_add = input()
                            config.add_company(company_add)
                            Menu_info.main_menu()
                            Menu_info.clean_prompt()
                    list_menu[2] = Menu_info.choices_menu_time()
                    return list_menu

class reMenu_info:
        def choices_menu_company(tab):
                questions = [
                        inquirer.List(
                                "company",
                                message="What company do you need?",
                                choices= tab,
                        ),
                ]
                answers = inquirer.prompt(questions)
                return answers['company']

        def choices_menu_time():
                questions = [
                        inquirer.List(
                                "time",
                                message="What Time do you need?",
                                choices=["1d", "1mo", "1y", "5y", "10y"],
                        ),
                ]
                answers = inquirer.prompt(questions)
                return answers['time']

        def main_menu(tab):
                list_menu = ["i","segond"," "]
                Menu_info.clean_prompt()
                tab.append('end')
                list_menu[1] = reMenu_info.choices_menu_company(tab)
                if (list_menu[1] == 'end'):
                        Menu_info.clean_prompt()
                        return []
                list_menu[2] = Menu_info.choices_menu_time()
                return list_menu

