#this program will open the provided link in browser after every 1 hour.currently it runs 3 times.
import webbrowser
import time
print "program started on "+time.ctime()
i=0
while(i<3):
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=kIll0-AyMa0")
    i += 1
