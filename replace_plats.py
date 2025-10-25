with open('index.html', 'r') as f:
    content = f.read()

with open('old_plats.html', 'r') as f:
    old = f.read()

with open('new_plats.html', 'r') as f:
    new = f.read()

content = content.replace(old, new)

with open('index.html', 'w') as f:
    f.write(content)

print("Replaced plats")
