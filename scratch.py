#Read a file into a list
f = open("data.txt")
lines = f.read().split('\n')
f.close()

print(type(lines))
print(lines)


# Write a list out to a file
l = ["Hello", "World", "This", "Is really cool", "Text"]

f = open("output.txt", "w")
lines = str.join("\n", l)
f.write(lines)
f.close()