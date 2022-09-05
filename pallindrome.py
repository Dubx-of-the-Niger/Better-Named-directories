def palindrome(string):
    b = string.replace(' ', '')
    a = b[::-1]
    if a == b:
        print('True')
    else:
        print('False')


n = True
while n:
    string = input('Enter the word you want to check for palindrome\n')
    palindrome(string)
    n = input('again?\n')

