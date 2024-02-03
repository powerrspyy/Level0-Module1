age = int(input("Enter your age: "))
outp = "ages: "
for i in range(age+1):
    if i == 0:
        i = 0
    elif age == i+1:
        outp = outp + f"{i}, and "
    elif age == i:
        outp = outp + f"{i}"
    else:
        outp = outp + f"{i}, "
print(outp)