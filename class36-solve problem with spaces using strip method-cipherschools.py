name = "   Aditya    "
dots = "..........."
print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)
name = "     Adi    tya     "
print(name.replace(" ","") + dots)
name, char = input("enter coma seperated name and character : ").split(",")
print(f"leangth of your name is {len(name)}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}")