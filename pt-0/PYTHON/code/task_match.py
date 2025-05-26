cmd = 'BOTTOM'


match cmd.upper():
    case "TOP":
        print("Команда "+ cmd.lower())

    case "BOTTOM":
        print("Команда " + cmd.lower())

    case "RIGHT":
        print("Команда " + cmd.lower())

    case "LEFT":
        print("Команда " + cmd.lower())

    case _:
        print("Неверная команда" )
        


match input().lower():
    case command:
        if command in ('top', 'bottom', 'right', 'left'):
            print(f'Команда {command}')
        else:
            print('Неверная команда')