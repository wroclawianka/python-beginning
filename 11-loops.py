# FOR LOOP
for x in "Python":
    print(x)

print('##########')

for x in [1, 2, 3]:
    print(x)

print('##########')

for x in range(5):
    print(x)

# range is not list, is range object
# it take a small amount of memory
# is iterable

# FOE ELSE
names = ['John', 'Kajetan']
for name in names:
    if(name.startswith("D")):
        print("Found")
        break
else:
    print("Not found")

# WHILE
guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
