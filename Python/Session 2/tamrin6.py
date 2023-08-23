class User:
    def __init__(self):
        self.name = ""
        self.family = ""
        self.age = 0

    def set_variables(self, data):
        user_name = data.get("name", "")
        user_family = data.get("family", "")
        user_age = data.get("age", "")
        if user_name:
            self.name = user_name
        if user_family:
            self.family = user_family
        if user_age:
            self.age = user_age


a = User()
a.set_variables({"name": "arshia", "family": "tamimi"})

print(a.name)
print(a.family)
print(a.age)

a.set_variables({"age": 22})

print(a.age)
