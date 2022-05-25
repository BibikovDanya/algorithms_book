from datetime import datetime

start_time = datetime.now()
def karatsuba(numb1,numb2):
    # numb1 = list(numb1)  # вводим первое число
    # numb2 = list(numb2)   # вводим второе число
    len1 = int((int(len(numb1)))/2)
    len2 = int((int(len(numb2)))/2)
    a = numb1[:len1]
    a = int(''.join((str(i) for i in a)))
    b = numb1[len1:]
    b = int(''.join((str(i) for i in b)))
    c = numb2[:len2]
    c = int(''.join((str(i) for i in c)))
    d = numb2[len2:]
    d = int(''.join((str(i) for i in d)))
# print(a,b,c,d)
    ac = a*c
    bd = b*d
    abcd = (a+b)*(c+d)
    subtract = abcd - ac - bd
# print(ac,bd,abcd,subtract)
    step5 = ac*10**4 + subtract*10**2 + bd
    print(step5)
# print(datetime.now() - start_time)
karatsuba(612384863438463,4643643843846)