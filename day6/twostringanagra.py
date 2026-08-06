from collections import Counter


def is_anagram(str1: str, str2: str) -> bool:
    """
    Check whether two strings are anagrams of each other.
    Ignores spaces and case differences.
    """
    # Clean the strings by ignoring spaces and converting to lowercase
    cleaned_str1 = [char.lower() for char in str1 if char.isalnum()]
    cleaned_str2 = [char.lower() for char in str2 if char.isalnum()]

    # Two strings are anagrams if character counts are equal
    return Counter(cleaned_str1) == Counter(cleaned_str2)


# Example usage
if __name__ == "__main__":
    string1 = "Listen"
    string2 = "Silent"

    if is_anagram(string1, string2):
        print(f"'{string1}' and '{string2}' are anagrams.")
    else:
        print(f"'{string1}' and '{string2}' are NOT anagrams.")

    # Additional Test Case
    s1 = "Hello"
    s2 = "World"
    if is_anagram(s1, s2):
        print(f"'{s1}' and '{s2}' are anagrams.")
    else:
        print(f"'{s1}' and '{s2}' are NOT anagrams.")
