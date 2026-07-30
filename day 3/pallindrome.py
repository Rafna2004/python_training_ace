def is_palindrome(word: str) -> bool:
    """Check if a given word is a palindrome."""
    cleaned_word = word.lower()
    return cleaned_word == cleaned_word[::-1]


word = "racecar"

if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
