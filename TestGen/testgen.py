import re
from random import choice, randint, random

with open('Test Data/commonNames.txt', 'r') as file:
    common_names = file.readline().strip().split(',')
with open('Test Data/commonWords.txt', 'r') as file:
    common_words = file.readline().strip().split(',')


def random_hex(hex_len=120):
    return "{0:0{1}x}".format(randint(0, (16**hex_len) - 1), hex_len)


def random_phone(country="+353", prefixes=["83", "85", "86", "87", "89"]):
    return country + choice(prefixes) + \
        "{0:0{1}}".format(randint(0, (10**7) - 1), 7)


def random_descrp(descrp_len=50):
    descrp = ''.join([choice(common_words) +
                      ("" if random() > 0.1 else choice(['!', ',', '.'])) +
                      " " for _ in range(descrp_len)])
    descrp = re.sub(r'(^|[.!]\s+)([a-z])',
                    lambda x: x.group(0).upper(), descrp)

    if descrp[-2] == ',':
        descrp = descrp[:-2] + choice(['!', '.'])
    elif descrp[-2] in ['!', '.']:
        descrp = descrp[:-1]
    else:
        descrp = descrp[:-1] + choice(['!', '.'])

    return descrp


def base_58(
        num,
        numerals="123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or \
        (base_58(num // 58, numerals).lstrip(numerals[0]) + numerals[num % 58])


def random_id(length=28):
    gen_str = base_58(randint(0, (58**length) - 1))
    return (length - len(gen_str)) * "0" + gen_str
