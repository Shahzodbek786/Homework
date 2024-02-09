# 21-chi masalaning javobi
#list1 = []
#list2 = []
#num1=int(input("Birinchi ro'yhatning elementlar soni:"))
#for i in range(1, num1 + 1):
#    a = int(input("Ro'yhat ichiga  elementlarni kiriting:"))
#    list1.append(a)

#num2= int(input("Ikkinchi ro'yhatning elemntlar soni:"))
#for i in range(1, num2 + 1):
#    b = int(input("Ro'yhat ichiga  elementlarni kiriting:"))
#    list2.append(b)

#list3=list1+list2
#list3.sort()
#print("Ikkita ro'yhatni jamlab tartiblab berilgan ro'yhat:", list3)



list1 = [1,2,2,1]
list2 = []
list2 = list1[::-1]
if list1 == list2:
    print(True)
else:
    print(False)