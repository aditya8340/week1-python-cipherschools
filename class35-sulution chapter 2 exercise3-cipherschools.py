name, char = input("enter coma seperated name and character : ").split(",")
print(f"leangth of your name is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}")