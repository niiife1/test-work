message = input()

while True:
    command = input().split(":|:")
    name = command[0]
    if name == "Reveal" :
        break
    func = command[1]
  #  last_func = command[2]

    if name == "InsertSpace":
        message = list(message)
        message.insert(int(func), " ")
        message = "".join(new)
        print(message)

    if name == "Reverse":
        if func in message:
            final_string = list(message) - list(func)
            func.reverse()
            message.append(func)

   # if name == "ChangeAll":

print(message)