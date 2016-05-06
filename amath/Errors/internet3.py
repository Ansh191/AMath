def test():
    import urllib
    try:
        urllib.request.urlopen('https://www.google.com')
    except urllib.request.URLError as err:
        print("Please check your internet connection.")
    finally:
        del urllib