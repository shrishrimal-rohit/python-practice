import webbrowser
import time

i = 0
while i != 4:
    time.sleep(20)
    url = "www.youtube.com"
    webbrowser.get('safari').open_new(url)
    i = i + 1
