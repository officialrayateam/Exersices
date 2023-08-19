data = "this is A TEST String THat I Want To Do Something With It."

data = data.lower()
data = data.replace("a", "@")

print(data)

# Or

data = data.lower().replace("a", "@")
print(data)

# Or

print(data.lower().replace("a", "@"))
