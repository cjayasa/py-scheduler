resources = []

while True:
    item = []
    name = input("Enter name")
    if name == "quit":
        break;
    item.append(name)
    time = input("Enter time")
    item.append(time)
    resources.append(item)

print(resources)