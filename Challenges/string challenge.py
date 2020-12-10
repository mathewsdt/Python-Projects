Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> D = "Welcome to the party"
>>> d
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> D
'Welcome to the party'
>>> o = """welcome to the python,
	   party mr mathews,
	   this should be,
	   all types of fun."""
>>> o
'welcome to the python,\n\t   party mr mathews,\n\t   this should be,\n\t   all types of fun.'
>>> m = "I can do it!"
>>> print(m[2:6])
can 
>>> print(m[4])
n
>>> print(len(m))
12
>>> txt = "   best   "
>>> x = txt.strip()
>>> print("I will be the",x, "python devloper some day")
I will be the best python devloper some day
>>> print(D.upper())
WELCOME TO THE PARTY
>>> c = D + m
>>> print(c)
Welcome to the partyI can do it!
>>> c = D + " " + m
>>> print(c)
Welcome to the party I can do it!
>>> txt = "Dominique Mathews is showing his "abilities" in the python course"
SyntaxError: invalid syntax
>>> "Dominique Mathews is showing his \"abilities\" in the python course"
'Dominique Mathews is showing his "abilities" in the python course'
>>> txt = "dom mathes is showing his \"abilities\" in the python course,"
>>> txt
'dom mathes is showing his "abilities" in the python course,'
>>> 