A=int(input("type the first number :"))
B=int(input("type the second number :"))
OP=input("type the operation :")
if OP == "+" :
  print("the result is :", A+B)
elif OP == "-" :
  print("the result is :", A-B)
elif OP == "*" :
 print("the result is :", A*B)
elif OP == "/" :
 print("the result is :",A/B)
elif OP == "%" :
 print("the result is :",A%B)
else :
 print("operator does not exist")
