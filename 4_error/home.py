

def check_phone_namber(namber):
    # 1
    if namber.startwith("8"):
        namber.replace("8", "+7", 1)
    if not namber.startwith("+7"):
        return "error"
    # 2
    namber = namber.replace(" ", "")
    # 3
    if "(" in namber or ")" in namber:
        if namber.count("(") != namber.count(")"):
            return "error"
        if namber.count("(") > 1 or namber.count(")") > 1:
            return "error"
        if namber.find("(") > namber.find(")"):
            return "error"

    for char in namber:
        if not char.isdigit() and char != "+":
            namber = namber.replace(char, "")

    if len(namber) != 12:
        return "error"

    return namberdef check_phone_namber(namber):
     #1
    if namber.startwith("8"):
        namber.replace("8", "+7", 1)
    if not namber.startwith("+7"):
        return "error"
    #2
    namber = namber.replace(" ", "")
    #3
    if "("in namber or")" in namber:
        if namber.count("(") != namber.count(")"):
            return "error"
        if namber.count("(") >1 or namber.count(")") >1:
            return "error"
        if namber.find("(") > namber.find(")"):
            return "error"

    for char in namber:
        if not char.isdigit() and char != "+":
            namber = namber.replace(char, "")

    if len(namber) != 12:
        return "error"



    return namber