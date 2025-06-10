import random
import string
print("Welcome to Password Manager")
def generate_password(length=12):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range(length))
    return password
def save_password(label,password):
    with open('saved_passwords.txt','a')as file:
        file.write(f'{label}:{password}\n')
def view_saved_passwords():
    try:
        with open('saved_passwords.txt','r') as file:
            content=file.read()
            print('\nSaved Passwords:')
            print(content)
    except FileNotFoundError:
        print('\nNo saved passwords found')
def main():
    while True:
        print('\n---Password Manager---')
        print('1. Generate a new password')
        print('2. View saved passwords')
        print('3.Exit')

        choice=input('Enter your choice(1,2,3):')

        if choice=='1':
            label=input('Enter a label for the password:')
            try:
                length=int(input('Enter desired password length:'))
            except ValueError:
                print('Invalid length')
                length=12
            password=generate_password(length)
            print(f'\nGenerated password: {password}')
            save_password(label,password)
            print('Password saved successfully!')
        elif choice=='2':
            view_saved_passwords()
        elif choice=='3':
            print('Goodbye')
            break
        else:
            print('Invalid choice. Enter 1,2, or 3.')
if __name__=='__main__':
    main()
