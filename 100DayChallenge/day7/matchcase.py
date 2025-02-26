# match case statement in python 3.10



name = input("Enter your name: ")

match name:
    case "Alychi":
        print("Hello Alychi")
    case "Tea":
        print("Hello Tea")
    case _ if name == "Alychi" or name == "Tea":
        print("Hello Alychi or Tea")
    case _:
        print("Hello")