


mySentence = 'loves the color'

color_list = ['red','blue','teal','purple','green']



def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name,mySentence,i)
        lst.append(msg)
    return lst


def get_name():
    go = True
    while go:
        name = input('what is your name? ')
        if name == '':
            print("you need to provide your name!")
        elif name == 'Sally':
            print("na")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()






    
