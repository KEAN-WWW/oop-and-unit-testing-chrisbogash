from app.calculator import Calculator


if __name__ == "__main__":
    print("Hello World!")
    a = 0
    b = 1

    c = a + b
    print(c)

   # d = add(a, b)
    #print(d)

#calculator1 = Calculator()
#calculator2 = Calculator()

#e = calculator1.addition(a,b)
#print(e)

e = Calculator.addition(a, b)
print (e)

