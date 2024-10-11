
def main():
    # shift = shift % 26
    while True:
        option = input('Encod or Decode (E/D/Exit): ').lower()
        
        if option == 'e':  
            user_inupt  = input('Enter: ')
            shift = int(input('shft: '))
            name = encode_name(user_inupt, shift)
            print(name)
            continue
            
        elif option == 'd':
            user_inupt  = input('Enter: ')
            shift = int(input('shft: '))
            decoded = decode_name(user_inupt, shift)
            print(decoded)
            continue
        
        else:
            print('Good Bye')
            break



def encode_name(user_input, shift):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    name = ''

    for i in user_input:
        if i in alpha:
            index = alpha.index(i)
            new_index = (index + shift) % 26
            name += alpha[new_index]
        else:
            name += i

    return name

def decode_name(encoded_name, shift):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decoded_name = ''

    for i in encoded_name:
        if i in alpha:
            index = alpha.index(i)
            new_index = (index - shift) % 26
            decoded_name += alpha[new_index]
        else:
            decoded_name += i

    return decoded_name


main()