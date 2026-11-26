usernames = []

emails = []

username_num = 0

for num in range(1, 6):
    username_num += 1
    username = input(f"Enter username {username_num}: ")
    usernames.append(username)
print()
print("Here are the contents of your 'username' list:\n")

for username in usernames:
    print(username)
print()
print("Here are all of the usernames that have less than 7 letters:\n")

for username in usernames:
    if len(username) < 7:
        print(username)
print()
print("Here are the email addresses created from 'usernames':\n")

for username in usernames:
    useraddress = username + "@cwhq"
    emails.append(useraddress)

for address in emails:
    print(address)
