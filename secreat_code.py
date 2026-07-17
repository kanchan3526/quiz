# write a python progrm to translate a message into secret code language.Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains 3 characters,remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
# simply reverse the string

# Decoding:
# if the word contains less than 3 characters,reverse it
# else:
# remove 3 random characters from start and end.Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

# message = input("Enter Your Message:")
# if len(message) == 3:
#     re = message.remove()
#     app = message.append(re)
#     print(message)

import random
import string


# Function to generate 3 random letters
def random_chars():
    return "".join(random.choice(string.ascii_letters) for _ in range(3))


choice = input("Do you want to Code or Decode? (c/d): ").lower()

message = input("Enter your message: ")

words = message.split()

result = []

if choice == "c":
    # Coding
    for word in words:
        if len(word) >= 3:
            # Remove first letter and append it to the end
            new_word = word[1:] + word[0]

            # Add 3 random letters at the start and end
            coded_word = random_chars() + new_word + random_chars()

            result.append(coded_word)
        else:
            # Reverse the word
            result.append(word[::-1])

    print("\nCoded Message:")
    print(" ".join(result))

elif choice == "d":
    # Decoding
    for word in words:
        if len(word) < 3:
            # Reverse the word
            result.append(word[::-1])
        else:
            # Remove first and last 3 characters
            word = word[3:-3]

            # Move last letter to the beginning
            decoded_word = word[-1] + word[:-1]

            result.append(decoded_word)

    print("\nDecoded Message:")
    print(" ".join(result))

else:
    print("Invalid choice! Please enter 'c' for Code or 'd' for Decode.")
