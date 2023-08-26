import random

characters = "abcdefghijklmnopqrstuvwxyz"
characters = characters + characters.upper()
characters = characters + "1234567890"

length = int(input("Enter Password Length : "))

answer = ""

for i in range(length):
    answer += random.choice(characters)

print("password ->", answer)
