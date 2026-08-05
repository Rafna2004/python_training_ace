def print_word_ladder(word: str) -> None:
    
    for i in range(len(word)):
        print(word[i:], end=" ")


if __name__ == "__main__":
    
    word = input("Enter a word (press Enter for default 'PYTHON'): ").strip()
    if not word:
        word = "PYTHON"

    print("Word Ladder Pattern:")
    print_word_ladder(word)
