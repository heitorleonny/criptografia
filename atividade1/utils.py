def charRange(c1: str, c2: str) -> str:
    alphabet: list = []
    for character in range(ord(c1), ord(c2)+1):
        alphabet.append(chr(character))
    return alphabet

def removeSpaces(text: str):
    newText = ""
    for character in text:
        if character != " ":
            newText = newText + character
    return newText

def specialCharacter(character: chr):
    if character.lower() in "âãáàä":
        return "a"
    elif character.lower() in "éèêẽë":
        return "e"
    elif character.lower() in "íìĩîï":
        return "i"
    elif character.lower() in "óòôõö":
        return "o"
    elif character.lower() in "úùũûü":
        return "u"
    elif character.lower() in "ç":
        return "c"
    else:
        return ""

if __name__ == "__main__":
    print(charRange("a", "z"))
    print(removeSpaces("Texto com ESPAÇOS haham    "))
    print(specialCharacter("Ç"))