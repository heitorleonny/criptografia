from atividade1.utils import charRange, removeSpaces, specialCharacter


def cleanText(text: str) -> str:
    alphabet = charRange("a", "z")
    text = removeSpaces(text)
    newText = ""
    for character in text:
        if character.lower() in alphabet:
            newText = newText + character.lower()
        else:
            newText = newText + specialCharacter(character)
        
    return(newText)
    
if __name__ == "__main__":
    while True:
        text = input()
        print(cleanText(text))