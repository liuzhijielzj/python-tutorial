currentNum = 1
while currentNum < 5:
    print(currentNum)
    currentNum += 1

prompt = "tell me w hat, enter 'quit' to exit\n"
msg = ''
while msg != 'quit':
    msg = input(prompt)
    print(msg)

# work with list/dictionary
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    # Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
