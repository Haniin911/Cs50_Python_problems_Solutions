text=input("Expression: ")
x,y,z=text.split(" ")
x=int(x)
z=int(z)

if y=='+' :
   print(f"{x + z:.1f}")
elif y=='-':
    print(f"{x - z:.1f}")
elif y=='*':
    print(f"{x * z:.1f}")
elif y=='/' and z!=0 :
   print(f"{x / z:.1f}")

