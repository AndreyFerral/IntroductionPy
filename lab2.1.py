# Китайский гороскоп
year = int(input("Введите год: "))
match year%12:
    case 0: print("Год обезьяны")
    case 1: print("Год петуха")
    case 2: print("Год собаки")
    case 3: print("Год свиньи")
    case 4: print("Год крысы")
    case 5: print("Год быка")
    case 6: print("Год тигра")
    case 7: print("Год кролика")
    case 8: print("Год дракона")
    case 9: print("Год змеи")
    case 10: print("Год лошади")
    case 11: print("Год козы")