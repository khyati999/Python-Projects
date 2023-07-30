import pyshorteners


def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url= s.tinyurl.short(url)
    return shortened_url
if __name__=="__main__":
    long_url="https://betterprogramming.pub/build-a-hand-pose-detector-web-app-powered-by-machine-learning-62131ec43db5"
    shortened_url=shorten_url(long_url)
    print("Shortened URL: ",shortened_url)