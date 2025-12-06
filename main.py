from stats import get_count_by_character, get_num_words

def main():
    """Main entry point for the book analysis application."""
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    char_count = get_count_by_character(text)
    print(char_count)

def get_book_text(filepath):
    """Read and return the contents of a book file as a string."""
    with open(filepath) as f:
        return f.read()


main()