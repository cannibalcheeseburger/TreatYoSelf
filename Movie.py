import webbrowser
import sys

search = " ".join(sys.argv[1:])

netflix = "https://www.netflix.com/search?q=" + search
prime = "https://www.primevideo.com/search/ref=atv_nb_sr?phrase=" + search +"&ie=UTF8"
hotstar = "https://www.hotstar.com/in/search?q="+search+"&utm_source=gwa"

webbrowser.open(netflix)
webbrowser.open_new_tab(prime)
webbrowser.open_new_tab(hotstar)
