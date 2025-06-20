print ("Hi, This is a little interactive bot I created.")

name = input("What is your name? ").lower()

if name == "filippo":
    print("Oh, my name is Filippo too! What a coincidence!")
else:
    print(f"Hello, {name}! Nice to meet you. I'm Filippo")

age = input("How old are you? ")

while True:
    if age.isdigit():
        age = int(age)
        if age == 28:
            print("I'm 28 too! We are the same age!")
        elif age < 28:
            print("You're young! I am 28 years old.")
        else:
            print("Wow, you're older than me! I'm 28 years old.")
        break
    else:
        print("I'd like you to put the age in numbers, thank you!")
        age = input("How old are you? ")


color = input("And tell me, what is your favorite color? ").lower()

if color == "yellow":
    print("Blue is a great color! It's my favorite too!")
else:
    print(f"{color.} is a nice color! I like yellow more, though.")

print("Well, it was nice talking to you! Have a great day!")