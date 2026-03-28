def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

word = input("Enter a string: ")

if is_palindrome(word):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")