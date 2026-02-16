ch=str(input('enter a day:'))
match ch:
    case monday:
        print('today is monday')
    case tuesday:
        print('today is tuesday')
    case _:
        print('default is working')

days= input("Enter a day: ").lower()
match days:
    case "saturday"|"sunday":
        print("weekend")
    case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
        print("weekdays")
    case _:
        print("Invalid day")

