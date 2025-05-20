import art
print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(original_text, shift_amount, encode_or_decode):
    cypher = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for each_letter in original_text:
        if each_letter not in alphabet:
            cypher += each_letter
        else:
            shifted_position = (alphabet.index(each_letter) + shift_amount) % 26  #to remove the index error
            cypher += alphabet[shifted_position]

    print(f"Here is the{encode_or_decode}d result: {cypher}")




should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again, otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")






