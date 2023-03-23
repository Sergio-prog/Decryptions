import string
from langdetect import detect


def caesar_cipher(text: str, step: int = 1):
    if detect(text) == "ru":
        abc = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    else:
        abc = string.ascii_letters
    whitespaces = string.whitespace

    text = list(text)
    result = []
    for letter in text:
        if letter in whitespaces:
            result.append(letter)
            continue

        if letter.isdigit():
            result.append(str(int(letter) + step))
            continue

        ind = abc.index(letter)
        if 52 < (ind + step):
            ind2 = ind + step
            result.append(abc[ind2 - 52 * (ind2 // 52)])
            continue

        result.append(abc[ind + step])

    return "".join(result)


def A1Z26(text: str):
    if detect(text) == "ru":
        abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    else:
        abc = string.ascii_lowercase
    whitespaces = string.whitespace

    result = []
    for i in text.lower():
        if i in whitespaces or i.isdigit():
            result.append(i)
            continue
        result.append(f"-{abc.index(i) + 1}")

    enum = "".join(result).split(" ")
    result = []
    for j, k in enumerate(enum):
        k = k.replace("-", "", 1) if k[0] == "-" else k
        result.append(f"{k} ")
    return "".join(result)


if __name__ == "__main__":
    print(A1Z26("abc123"))
    print(caesar_cipher("abc123", step=2))
