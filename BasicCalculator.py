print("Enter option:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n")
o=int(input())

n1=int(input("Enter n1="))
n2=int(input("Enter n2="))

if o==1:
      print(f"Anser={n1+n2}")
elif 0==2:
      print(f"Answer={n1-n2}")
elif 0==3:
      print(f"Answer={n1*n2}")
elif o==4:
      print(f"Answer={n1/n2}")
else:
      print("Invalid option.")
