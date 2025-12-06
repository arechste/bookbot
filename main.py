
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    count_words_in_book(text)

def get_book_text(filepath):
    #contents = ""
    with open(filepath) as f:
        return f.read()

def count_words_in_book(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

main()