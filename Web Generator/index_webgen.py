import webbrowser

def createHTML():
    f = open("index.html","w")
    f.write("<html>\n \
<body>\n\
<p>Stay tuned for our amazing summer sale!</p>\n\
</body>\n\
</html>")
    f.close()

webbrowser.open("index.html","w")



if __name__ == "__main__":
    createHTML()
