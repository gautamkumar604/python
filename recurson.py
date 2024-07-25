def recurson(n):
    if(n==1):
       print("process: ",1)
       return n
    else:
       r = n * recurson((n-1))
       print("process: ",r)
       return r

num = int(input("Enter number for calculate factorial: "))
# fac = 1
if(num<0):
   print("Sorry,factorial does not exists of nagative numbers")

elif(num==0):
   print("Factorial of 0 is 1")
else:
    print(f"factorial of" , num , "is equal to",recurson(num))

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\nRecursion Example Results")
tri_recursion(6)
