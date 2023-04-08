import hashlib
import string
from langdetect import detect
from Cryptodome.Hash import MD2, MD4, TupleHash128, SHA3_256


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


def sha256(*args: str):
    hash = hashlib.sha256(str("".join(args)).encode('utf-8'))
    return hash.hexdigest()


def sha224(*args: str):
    hash = hashlib.sha224(str("".join(args)).encode('utf-8'))
    return hash.hexdigest()


def sha384(*args: str):
    hash = hashlib.sha384(str("".join(args)).encode('utf-8'))
    return hash.hexdigest()


def sha1(*args: str):
    hash = hashlib.sha1(str("".join(args)).encode('utf-8'))
    return hash.hexdigest()


def sha512(*args: str):
    hash = hashlib.sha512(str("".join(args)).encode('utf-8'))
    return hash.hexdigest()


def md5(*args: str):
    hash = hashlib.md5(str("".join(args)).encode('utf-8'))
    return hash.hexdigest()


def md2(*args: str):
    h = MD2.new()
    h.update(str("".join(args)).encode('utf-8'))
    return h.hexdigest()


def md4(*args: str):
    h = MD4.new()
    h.update(str("".join(args)).encode('utf-8'))
    return h.hexdigest()


def tuple_hash256(*args: str, digest: int):
    hd = TupleHash128.new(digest_bytes=digest)
    hd.update(str("".join(args)).encode('utf-8'))
    return hd.hexdigest()


def sha3_256(*args):
    hd = SHA3_256.new()
    hd.update(str("".join(args)).encode('utf-8'))
    return hd.hexdigest()


if __name__ == "__main__":
    print(sha3_256("123"))
