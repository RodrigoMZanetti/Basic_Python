from time import sleep
phrase=str(input('\033[1;31mType a phrase: \033[m'))
clean_phrase=phrase.replace(" ","").lower()

print(f'\033[1m{clean_phrase}\033[m')
reversed_phrase = clean_phrase[::-1]
print(f'\033[1m{reversed_phrase}\033[m')
if clean_phrase == reversed_phrase:
    print('\033[1;34mPalindrome!\033[m')
else:
    print('\033[1;31mNot Palindrome!\033[m')