x = "10"
x = x + ","
print(x) # 10,
y = 3
x = y*x
print(x) # 10,10,10,
x = x.split(",")
print(x)

for w in x:
    if w == "":
        x.remove(w)


print(x)
