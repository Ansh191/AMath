import os as _os

dir_path = _os.path.dirname(_os.path.realpath(__file__))
with open(dir_path + _os.sep + 'words.txt') as word_list:
    eng_words = set(word.strip().lower() for word in word_list)

del dir_path

ascii = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
         "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
         "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
         "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8",
         "9", "0", "`", "-", "=", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(",
         ")", "[", "]", "\\", ";", "'", ", ", ".", "/", "_", "+", "{", "}", "|", ":", "\"", " < ", ">", "?"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
           "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
           "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
           "T", "U", "V", "W", "X", "Y", "Z"]
chars = ["`", "-", "=", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(",
         ")", "[", "]", "\\", ";", "'", ", ", ".", "/", "_", "+", "{", "}", "|", ":", "\"", " < ", ">", "?"]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

ascii_table = {0: "\x00", 1: "\x01", 2: "\x02", 3: "\x03", 4: "\x04", 5: "\x05", 6: "\x06", 7: "\x07", 8: "\x08",
               9: "\x09",
               10: "\n",
               11: "\x0b", 12: "\x0c", 13: "\x0d", 14: "\x0e", 15: "\x0f", 16: "\x10", 17: "\x11", 18: "\x12",
               19: "\x13",
               20: "\x14", 21: "\x15",
               22: "\x16", 23: "\x17", 24: "\x18", 25: "\x19", 26: "\x1a", 27: "\x1b", 28: "\x1c", 29: "\x1d",
               30: "\x1e",
               31: "\x1f", 32: "\x20",
               33: "\x21", 34: "\x22", 35: "\x23", 36: "\x24", 37: "\x25", 38: "\x26", 39: "\x27", 40: "\x28",
               41: "\x29",
               42: "\x2a",
               43: "\x2b", 44: "\x2c", 45: "\x2d", 46: "\x2e", 47: "\x2f", 48: "\x30", 49: "\x31", 50: "\x32",
               51: "\x33",
               52: "\x34",
               53: "\x35", 54: "\x36", 55: "\x37", 56: "\x38", 57: "\x39", 58: "\x3a", 59: "\x3b", 60: "\x3c",
               61: "\x3d",
               62: "\x3e",
               63: "\x3f", 64: "\x40", 65: "\x41", 66: "\x42", 67: "\x43", 68: "\x44", 69: "\x45", 70: "\x46",
               71: "\x47",
               72: "\x48",
               73: "\x49", 74: "\x4a", 75: "\x4b", 76: "\x4c", 77: "\x4d", 78: "\x4e", 79: "\x4f", 80: "\x50",
               81: "\x51",
               82: "\x52",
               83: "\x53", 84: "\x54", 85: "\x55", 86: "\x56", 87: "\x57", 88: "\x58", 89: "\x59", 90: "\x5a",
               91: "\x5b",
               92: "\x5c",
               93: "\x5d", 94: "\x5e", 95: "\x5f", 96: "\x60", 97: "\x61", 98: "\x62", 99: "\x63", 100: "\x64",
               101: "\x65",
               102: "\x66", 103: "\x67", 104: "\x68", 105: "\x69", 106: "\x6a", 107: "\x6b", 108: "\x6c", 109: "\x6d",
               110: "\x6e",
               111: "\x6f", 112: "\x70", 113: "\x71", 114: "\x72", 115: "\x73", 116: "\x74", 117: "\x75", 118: "\x76",
               119: "\x77",
               120: "\x78", 121: "\x79", 122: "\x7a", 123: "\x7b", 124: "\x7c", 125: "\x7d", 126: "\x7e", 127: "\x7f",
               128: "\x80",
               129: "\x81", 130: "\x82", 131: "\x83", 132: "\x84", 133: "\x85", 134: "\x86", 135: "\x87", 136: "\x88",
               137: "\x89",
               138: "\x8a", 139: "\x8b", 140: "\x8c", 141: "\x8d", 142: "\x8e", 143: "\x8f", 144: "\x90", 145: "\x91",
               146: "\x92",
               147: "\x93", 148: "\x94", 149: "\x95", 150: "\x96", 151: "\x97", 152: "\x98", 153: "\x99", 154: "\x9a",
               155: "\x9b",
               156: "\x9c", 157: "\x9d", 158: "\x9e", 159: "\x9f", 160: "\xa0", 161: "\xa1", 162: "\xa2", 163: "\xa3",
               164: "\xa4",
               165: "\xa5", 166: "\xa6", 167: "\xa7", 168: "\xa8", 169: "\xa9", 170: "\xaa", 171: "\xab", 172: "\xac",
               173: "\xad",
               174: "\xae", 175: "\xaf", 176: "\xb0", 177: "\xb1", 178: "\xb2", 179: "\xb3", 180: "\xb4", 181: "\xb5",
               182: "\xb6",
               183: "\xb7", 184: "\xb8", 185: "\xb9", 186: "\xba", 187: "\xbb", 188: "\xbc", 189: "\xbd", 190: "\xbe",
               191: "\xbf",
               192: "\xc0", 193: "\xc1", 194: "\xc2", 195: "\xc3", 196: "\xc4", 197: "\xc5", 198: "\xc6", 199: "\xc7",
               200: "\xc8",
               201: "\xc9", 202: "\xca", 203: "\xcb", 204: "\xcc", 205: "\xcd", 206: "\xce", 207: "\xcf", 208: "\xd0",
               209: "\xd1",
               210: "\xd2", 211: "\xd3", 212: "\xd4", 213: "\xd5", 214: "\xd6", 215: "\xd7", 216: "\xd8", 217: "\xd9",
               218: "\xda",
               219: "\xdb", 220: "\xdc", 221: "\xdd", 222: "\xde", 223: "\xdf", 224: "\xe0", 225: "\xe1", 226: "\xe2",
               227: "\xe3",
               228: "\xe4", 229: "\xe5", 230: "\xe6", 231: "\xe7", 232: "\xe8", 233: "\xe9", 234: "\xea", 235: "\xeb",
               236: "\xec",
               237: "\xed", 238: "\xee", 239: "\xef", 240: "\xf0", 241: "\xf1", 242: "\xf2", 243: "\xf3", 244: "\xf4",
               245: "\xf5",
               246: "\xf6", 247: "\xf7", 248: "\xf8", 249: "\xf9", 250: "\xfa", 251: "\xfb", 252: "\xfc", 253: "\xfd",
               254: "\xfe", 255: "\xff"}


def whitespace(s):
    if type(s) != str:
        raise TypeError("s must be a string")
    return " ".join(s.split())


def word(w, suppress=False):
    from urllib.parse import urlencode
    from urllib.request import urlopen
    from urllib.error import URLError
    global eng_words
    if type(w) is not str:
        raise TypeError("s must be a string")
    fixed = whitespace(w)
    if fixed.lower() in eng_words:
        return True

    def wolfram_cloud_call(**args):
        arguments = dict([(key, arg) for key, arg in list(args.items())])
        try:
            result = urlopen("http://www.wolframcloud.com/objects/bdf9bbc4-6b59-4821-9053-9d453f7a9b39",
                             urlencode(arguments).encode("ascii"))
        except URLError:
            if not suppress:
                print("Internet connection required for full dictionary, only providing small dictionary currently")
            return b"{}"
        else:
            return result.read()

    textresult = wolfram_cloud_call(x=fixed)
    if textresult == b"{}":
        return False
    else:
        # r = textresult[2:-2]
        # eng_words.add(r)
        # eng_words = set(list(eng_words).sort())
        # with open("C:\\Users\\ansg1\\PycharmProjects\\AMath\\amath\\string_proccessing\\words2.txt", 'w') as w:
        #     pass
        return True


def pgenerator(length, words=False):
    if type(length) is not int:
        raise TypeError("length must be an integer")
    if not words:
        import os
        l = []
        i = 0
        while i < length:
            t = os.urandom(1)
            if t in ascii:
                i += 1
                l.append(t)
        return "".join(l)
    elif words:
        import random as _r
        _r.seed(_os.urandom(1024))
        x = whitespace("".join("{0} ".format(_r.choice(list(eng_words))) for _ in range(length)))
        return x
    else:
        raise TypeError("words must be a bool value")


def wordcount(s):
    if type(s) is not str:
        raise TypeError("s must be a string")
    fixed = whitespace(s)
    all_words = fixed.split()
    return len(all_words)

del _os
