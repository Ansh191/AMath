from amath.Errors.Errors import Failure

eng_words = None
with open("C:\\Users\\Anshul\\PycharmProjects\\AMath\\amath\string_proccessing\words.txt") as word_list:
    eng_words = set(word.strip().lower() for word in word_list)

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


def whitespace(s):
    if type(s) != str:
        raise TypeError("s must be a string")
    return " ".join(s.split())


def word(w):
    from urllib import urlencode
    from urllib2 import urlopen
    if type(w) is not str:
        raise TypeError("s must be a string")
    fixed = whitespace(w)
    if fixed.lower() in eng_words:
        return True

    def wolfram_cloud_call(**args):
        arguments = dict([(key, arg) for key, arg in args.iteritems()])
        try:
            result = urlopen("http://www.wolframcloud.com/objects/bdf9bbc4-6b59-4821-9053-9d453f7a9b39",
                             urlencode(arguments))
        except:
            raise Failure("Internet connection required for full dictionary, only providing small dictionary currently")
        return result.read()

    textresult = wolfram_cloud_call(x=fixed)
    if textresult == "{}":
        return False
    else:
        return True


def pgenerator(length, words=False):
    if type(length) is not int:
        raise TypeError("length must be an integer")
    if not words:
        import random as _r
        import os as _os
        _r.seed(_os.urandom(1024))
        x = "".join(_r.choice(ascii) for i in range(length))
        return x
    elif words:
        import random as _r
        import os as _os
        _r.seed(_os.urandom(1024))
        x = whitespace("".join("{0} ".format(_r.choice(list(eng_words))) for i in range(length)))
        return x
    else:
        raise TypeError("words must be a bool value")


def wordcount(s):
    if type(s) is not str:
        raise TypeError("s must be a string")
    fixed = whitespace(s)
    all_words = fixed.split()
    return len(all_words)

del Failure