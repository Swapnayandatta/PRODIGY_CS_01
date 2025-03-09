a = input('Enter the string: ')
shift = int(input("Enter the amount of shift: "))

def convert_encrypt():
    result = ""
    for char in a :
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97 ) % 26 + 97)
        else:
            result += char
        
    return result

def convert_decrypt():
    result = ""
    for char in a :
        if char.isupper():
            result += chr((ord(char) - shift -65)%26 +65)
        elif char.islower():
            result += chr((ord(char) - shift -97)%26 +97)
        else:
            result += char

    return result

print("1 for encryption")
print("2 for decryption")
choice = int(input("Enter your choise: "))
if choice == 1 :
    data = convert_encrypt()
    print(data)
elif choice == 2 :
    data = convert_decrypt()
    print(data)
else:
    print("Enter a valid choise")
    print("have a good day")
