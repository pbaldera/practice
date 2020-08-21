prompt = "\nTell me your age and I will tell you the price of the ticket: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
        break
    else:
        message = int(message)
    if message < 3:
        print("The price of your ticket is free")
        continue
    elif message >= 3 and message < 12:
        print("The price of your ticket is $10")
        continue
    else:
        print("The price of your ticket is $15")