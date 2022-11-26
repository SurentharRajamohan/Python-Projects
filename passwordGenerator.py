import secrets
import string

passwordLength = input('How long is the password? : ')
isSpecialCharacterPresent = input('Do you wanna add special characters? : ')
numberOfPasswords = input('How many passwords do you wanna create? : ')

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
specialCharacters = string.punctuation

if(isSpecialCharacterPresent.lower == 'yes'):
    passwordContents = lowercase + uppercase + specialCharacters + numbers
else:
    passwordContents = lowercase + uppercase + numbers

passwordLists = []

for i in range (int(numberOfPasswords)):
    pwd = ''
    for j in range(int(passwordLength)):
        pwd += ''.join(secrets.choice(passwordContents))
    # print(pwd)
    passwordLists += [pwd]

print("Generated password:")
for x in passwordLists:
    print(x)
