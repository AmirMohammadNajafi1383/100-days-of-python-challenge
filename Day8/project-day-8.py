alphabet = 'abcdefghijklmnopqrstuvwxyz'


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == 'decode':
                shift_amount *= -1
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f'The {cipher_direction}d text is {end_text}')


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input('Type your message: ')
    shift = int(input('Type the shift number: '))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise, type 'no': ")
    if result == 'no':
        should_continue = False
        print('Goodbye')
