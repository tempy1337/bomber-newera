import os

from services import services
from tools.check_inputs import CheckInput
from tools.colors import BOLD, FG, RESET_ALL
from tools.texts import banner, cursor, replace


def clear_screen():
    return (
        os.system("cls") if os.sys.platform == "win32" else os.system("clear")
    )


def main():
    clear_screen()
    print(banner, replace + "Введите номер телефона(без +):" + RESET_ALL, sep="\n")
    phone = input(cursor)
    phone = CheckInput().verification_phone(phone)

    print(replace + "Введите кол-во циклов:" + RESET_ALL)
    count = input(cursor)
    count = CheckInput().verification_cycles(count)
    clear_screen()
    print(banner)
    if count >= 10:
        print(
            f"{FG.green}*Вы ввели больше 10 кругов, "
            f"после 5-го скорость спама уменьшается{RESET_ALL}"
        )
    send_requests(phone, count)
    clear_screen()
    print(
        BOLD + f"{FG.green}Успешно!",
        f"Телефон: {FG.purple}{phone}",
        f"{FG.green}Колличество кругов: {FG.purple}{count}",
        sep="\n",
    )


if __name__ == "__main__":
    main()
