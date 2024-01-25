def check_input(func):
    def uscor(v0,v,t):
        try:
            v0 = float(v0)
            v = float(v)
            t = float(t)
        except ValueError:
            print("учи цифры дурной")
            return
        if t ==0:
            print("ты совсем дурной?")
            return
        return func(v0,v,t)
    return uscor
@check_input
def a(v0,v,t):
    return (v - v0)/ t

@check_input
def distance(v0,v,t):
    return (v0+v)*t/2

v0 =input("введи начальную скорость: ")
v =input("введи  скорость: ")
t =input("введи время: ")
acc =a(v0,v,t)
if acc:
    print("Ускорение:",acc)

dist =distance(v0,v,t)
if dist:
    print("расстояние:", dist)
