class WrongFormat(Exception):
    pass


def check_phone_namber(namber):
     #1
    if namber.startwith("8"):
        namber.replace("8", "+7", 1)
    if not namber.startwith("+7"):
        raise WrongFormat("Некорректный код страны")

    #2
    namber = namber.replace(" ", "")

    #3
    if "("in namber or")" in namber:
        if namber.count("(") != namber.count(")"):
            raise WrongFormat("Неверный формат скобок")
        if namber.count("(") >1 or namber.count(")") >1:
            raise WrongFormat("Неверный формат скобок")
        if namber.find("(") > namber.find(")"):
            raise WrongFormat("Неверный формат скобок")

    if "-" in namber and (namber[-1] == "-" or namber[0] == "-" or "--" in namber):
        raise WrongFormat("Неверно поставлены "-" ")



    for char in namber:
        if not char.isdigit() and char != "+":
            namber = namber.replace(char, "")

    if len(namber) != 12:
        raise WrongFormat("Неверное количество символов")



    return namber