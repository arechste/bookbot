def get_num_words(text):
    """Count and return the number of words in the given text."""
    words = text.split()
    return len(words)

def get_count_by_character(text):
    """Count occurrences of each character in text, normalized to lowercase."""
    characters = text.lower()
    char_dict = {}

    for c in characters:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict