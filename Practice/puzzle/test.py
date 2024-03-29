s = "10000010010100010010111000001000100000010000110000100001101111000011000110000111"
a = [s[i:i + 8] for i in range(0, len(s), 8)]
a_int = [int(a[i], 2) for i in range(len(a))]
d = {
    0: "NUL",
    1: "SOH",
    2: "STX",
    3: "ETX",
    4: "EOT",
    5: "ENQ",
    6: "ACK",
    7: "BEL",
    8: "BS",
    9: "TAB",
    10: "LF",
    11: "VT",
    12: "FF",
    13: "CR",
    14: "SO",
    15: "SI",
    16: "DLE",
    17: "DC1",
    18: "DC2",
    19: "DC3",
    20: "DC4",
    21: "NAK",
    22: "SYN",
    23: "ETB",
    24: "CAN",
    25: "EM",
    26: "SUB",
    27: "ESC",
    28: "FS",
    29: "GS",
    30: "RS",
    31: "US",
    32: "Пробел",
    33: "!",
    34: "&quot",
    35: "#",
    36: "$",
    37: "%",
    38: "&",
    39: "'",
    40: "(",
    41: ")",
    42: "*",
    43: "+",
    44: ",",
    45: "-",
    46: ".",
    47: "/",
    48: "0",
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    54: "6",
    55: "7",
    56: "8",
    57: "9",
    58: ":",
    59: ";",
    60: "<",
    61: "=",
    62: ">",
    63: "?",
    64: "@",
    65: "A",
    66: "B",
    67: "C",
    68: "D",
    69: "E",
    70: "F",
    71: "G",
    72: "H",
    73: "I",
    74: "J",
    75: "K",
    76: "L",
    77: "M",
    78: "N",
    79: "O",
    80: "P",
    81: "Q",
    82: "R",
    83: "S",
    84: "T",
    85: "U",
    86: "V",
    87: "W",
    88: "X",
    89: "Y",
    90: "Z",
    91: "[",
    92: "backslash",
    93: "]",
    94: "^",
    95: "_",
    96: "`",
    97: "a",
    98: "b",
    99: "c",
    100: "d",
    101: "e",
    102: "f",
    103: "g",
    104: "h",
    105: "i",
    106: "j",
    107: "k",
    108: "l",
    109: "m",
    110: "n",
    111: "o",
    112: "p",
    113: "q",
    114: "r",
    115: "s",
    116: "t",
    117: "u",
    118: "v",
    119: "w",
    120: "x",
    121: "y",
    122: "z",
    123: "{",
    124: "|",
    125: "}",
    126: "~",
    127: "Delete",
    128: "Ђ",
    129: "Ѓ",
    130: "‚",
    131: "ѓ",
    132: "„",
    133: "…",
    134: "†",
    135: "‡",
    136: "€",
    137: "‰",
    138: "Љ",
    139: "‹",
    140: "Њ",
    141: "Ќ",
    142: "Ћ",
    143: "Џ",
    144: "Ђ",
    145: "‘",
    146: "’",
    147: "“",
    148: "”",
    149: "•",
    150: "–",
    151: "—",
    152: "Начало строки",
    153: "™",
    154: "љ",
    155: "›",
    156: "њ",
    157: "ќ",
    158: "ћ",
    159: "џ",
    160: "Неразрывный пробел",
    161: "Ў",
    162: "ў",
    163: "Ј",
    164: "¤",
    165: "Ґ",
    166: "¦",
    167: "§",
    168: "Ё",
    169: "©",
    170: "Є",
    171: "«",
    172: "¬",
    173: "Мягкий перенос",
    174: "®",
    175: "Ї",
    176: "°",
    177: "±",
    178: "І",
    179: "і",
    180: "ґ",
    181: "µ",
    182: "¶",
    183: "·",
    184: "ё",
    185: "№",
    186: "є",
    187: "»",
    188: "ј",
    189: "Ѕ",
    190: "ѕ",
    191: "ї",
    192: "А",
    193: "Б",
    194: "В",
    195: "Г",
    196: "Д",
    197: "Е",
    198: "Ж",
    199: "З",
    200: "И",
    201: "Й",
    202: "К",
    203: "Л",
    204: "М",
    205: "Н",
    206: "О",
    207: "П",
    208: "Р",
    209: "С",
    210: "Т",
    211: "У",
    212: "Ф",
    213: "Х",
    214: "Ц",
    215: "Ч",
    216: "Ш",
    217: "Щ",
    218: "Ъ",
    219: "Ы",
    220: "Ь",
    221: "Э",
    222: "Ю",
    223: "Я",
    224: "а",
    225: "б",
    226: "в",
    227: "г",
    228: "д",
    229: "е",
    230: "ж",
    231: "з",
    232: "и",
    233: "й",
    234: "к",
    235: "л",
    236: "м",
    237: "н",
    238: "о",
    239: "п",
    240: "р",
    241: "с",
    242: "т",
    243: "у",
    244: "ф",
    245: "х",
    246: "ц",
    247: "ч",
    248: "ш",
    249: "щ",
    250: "ъ",
    251: "ы",
    252: "ь",
    253: "э",
    254: "ю",
    255: "я",
}
for i in range(256):
    word = [i]
    for n in a_int:
        word.append(d[(n+i)%256])
    print(word)