def mohit(radius):
    return radius * radius * 3.14


def masahat(radius):
    return (radius + radius) * 3.14


radius = int(input("Enter Radius : "))

print("Masahat ->", masahat(radius))
print("Mohit ->", mohit(radius))
