def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("Alla"))
print(is_palindrome("Stepan"))
print(is_palindrome("a"))
print(is_palindrome("ab"))
print(is_palindrome("A man a plan a canal Panama"))