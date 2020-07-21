a = "ABCDIFG"
a[-1]  # last character
a[0:3]  # char from 0 to 3
a[:3]  # char from 0 to 3
a[3:]  # char from 3 to end (length as second parameter)
msg = "Python \nProgramming"  # two lines

multi = """ 
dsadsadsadsadas
453443543
fdsfsdfsdfsdfds
jghjhgjhgjhgjghjhg
"""

# multilines
print(multi)

# expressions
a = "Dorota"
b = "z Wroclawia"
full = f"{a} {b}"
print(full)

# methods
a.upper()
a.lower()

title = "dorota z wroclawia".title()  # Dorota Z Wroclawia
print(title)

spaces = "  LOL lol "
spaces.strip()  # "LOL lol"

a.find("dor")  # returns index, -1 as case sensitive
a.replace("D", "A")

print("Dor" in a)  # boolean
