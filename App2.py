

import App


def print_App2():
    name = (__name__)
    return name

if __name__ ==  "__main__":
     # The following is calling code within this script
     print("I am running code from {}".format(print_App2()))

     # The following is calling from the impoted App.py
     print("I am running code from {}".format(App.print_App()))
