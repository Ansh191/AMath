
def test():
    import urllib2
    try:
        response = urllib2.urlopen('https://www.google.com', timeout = 1)
    except urllib2.URLError:
        print("Please check your internet connection.")
    finally:
        del urllib2
