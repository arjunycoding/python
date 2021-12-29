username = input("What is your username? ")
password = input("What is your password? ")
passwordLen = len(password)
hiddenPassword = "*" * passwordLen
print(f'Hello {username}, your password, {hiddenPassword}, is {passwordLen} letters long')
