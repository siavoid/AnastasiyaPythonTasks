import database


def print_title() -> None:
    title = "|{:<22}|{:<14}|{:<9}|".format("Название", "Жанр", "Рейтинг")
    print(f"+{"":-<22}+{"":-<14}+{"":-<9}+")
    print(title)
    print(f"+{"":-<22}+{"":-<14}+{"":-<9}+")


def print_format_film(film : list) -> None:
    f = "{:<25}{:<15}{:<10}".format(film[0], film[1], film[2])
    print(f)


def print_all_films(films_arg):
    print_title()
    for f in films_arg:
        print_format_film(f)


# ДОМАШКА!!
def print_films_by_rating(films : list) -> None:
    pass


def print_films_by_genre(films : list) -> None:
    genre = input("Введите жанр фильма:")
    genre = genre.lower()
    print_title()
    for f in films:
        if f[1] == genre:
            print_format_film(f)
    pass


def logo():
    print("""
    ██████╗ ██╗███╗   ██╗ ██████╗ ████████╗███████╗██╗  ██╗
    ██╔══██╗██║████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
    ██████╔╝██║██╔██╗ ██║██║   ██║   ██║   █████╗   ╚███╔╝ 
    ██╔═══╝ ██║██║╚██╗██║██║   ██║   ██║   ██╔══╝   ██╔██╗ 
    ██║     ██║██║ ╚████║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
    ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                    
       ▄▄ ▄▄                                  
      ██████▄                                
     ▄▄███▀▀▀▀▀▀▄                            
    ▀▀▀█▄▀▀▀▀▀▄███                           
     ▀▀▀▀▀▀▀▀▀                               
    """)


def read_command():
    cmd = -1
    print()
    print("Доступные команды:")
    print("1. Вывести все фильмы")
    print("2. Выведи фильмы по жанру")
    print("3. Выйти")
    while True:
        try:
            cmd = int(input("Введите команду:")) # добавить обработчик ошибок try-exept
        except:
            pass
        if cmd > 0:
            break
        else:
            print("[ERROR] Введте положительное число")
    return cmd


def main(films):
    logo()
    while True:
        cmd = read_command()
        if cmd == 1:
            print_all_films(films)
        elif cmd == 2:
           print_films_by_genre(films)
        elif cmd == 3:
            break
        else:
            print("Неизвестная команда")





if __name__ == "__main__":
    films = database.ReadFilmsFromDB()
    main(films)




