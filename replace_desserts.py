with open('index.html', 'r') as f:
    content = f.read()

with open('old_desserts.html', 'r') as f:
    old = f.read()

with open('new_desserts.html', 'r') as f:
    new = f.read()

content = content.replace(old, new)

with open('index.html', 'w') as f:
    f.write(content)

print("Replaced desserts")
