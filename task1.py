from collections import  Counter
message = input()

while True:
    command = input().split(":|:")
    name = command[0]
    if name == "Reveal" :
        break
    func = command[1]

    if name == "InsertSpace":
        message = list(message)
        message.insert(int(func), " ")
        print("".join(message))
        continue

    elif name == "Reverse":
        if func in message:
            cutted_word = list((Counter(message)-Counter(func)).elements())
            func = list(func)
            func.reverse()
            message = cutted_word + func
            print("".join(message))
        else:
            print("error")

    elif name == "ChangeAll":
        last_func = command[2]
        message = message.replace(func, last_func)
        print(message)

x = "".join(message)
print(f'You have a new text message: {x}')

# Hello, I was here