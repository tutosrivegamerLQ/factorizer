def getHelp():
    with open("resources/help", "r", encoding="utf-8") as hl: 
        info = hl.read()
        return info