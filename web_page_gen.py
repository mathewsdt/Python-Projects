import webbrowser

def createHTML():
    f = open("index.html","w")
    f.write("Stay tuned for our amazing sale!")
    f.close()

if __name__ == "__main__":
    createHTML()
