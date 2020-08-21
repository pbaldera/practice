prompt = "\nWhich toppings would you like to add to your pizza? "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"We will add {message} to your pizza!")