# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo
print(logo)

running = True
dictionary = {}
while running:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    dictionary[name] = bid

    more = input("Are there any more bidders? type 'yes' or 'no'").lower()
    if more == 'yes':
        print('\n' * 200)
        continue
    else:
        print('\n' * 200)
        break

max_key = max(dictionary, key=dictionary.get)
max_value = max(dictionary.values())
print(f"The highest bidder is {max_key} with {max_value}")

