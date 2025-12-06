from stats import get_count_by_character, get_num_words, sort_character_count

def main():
    """Main entry point for the book analysis application."""
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_count_by_character(text)
    sorted_chars = sort_character_count(char_count)

    # Print formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Filter for alphabetical characters only and print report
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

def get_book_text(filepath):
    """Read and return the contents of a book file as a string."""
    with open(filepath) as f:
        return f.read()


main()