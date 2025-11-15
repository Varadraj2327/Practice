# scope resolution = (LEGB) Local --> Enclosed --> Global --> Bulit-in
# variable scope = where a variable is visible and accessible

def func1():
    x = 1 
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()
