"""
x = 5
print("hello")

def print_lyrics():
    print("I am a lumberjack, and I am OK.")
    print("I sleep all night and work all day.")
print("yo!")
print_lyrics()
x = x + 2
print(x)


def greet(lang):
    if lang == "es":
        print("hola")
    elif lang == "eng":
        print("hello")
    else:
        print("你好！")
greet("es")
greet("eng")
greet("让我们说中文！")


def greet():
    return "hello"
print(greet(), "Pipi")
print(greet(), "Tutu")

def greet(lang):
    if lang == "es":
        return "hola"
    elif lang == "eng":
        return "hello"
    else:
        return ("你好！")
print(greet("es"), "Pipi")
print(greet("eng"), "Pipi")
print(greet("让我们说中文"), "Pipi")
"""

def addtwo(a, b):
    added = a + b
    return added
x = addtwo(2,6)
print(x)