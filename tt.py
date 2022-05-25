m = (input("Число: "))
m = m.split(" ")
a = int(m[0])
b = int(m[1])
c = int(m[2])
d = int(m[3])
# print(type(a))
if b>=d:
    print(a)
else:
    e =int(d-b)
    print(int(a+c*e))