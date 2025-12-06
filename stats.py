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


def sort_character_count(char_dict):
    """Convert character dictionary to sorted list of dicts, sorted by count (greatest to least)."""

    # Helper function to get the count value for sorting
    def get_count(dict_item):
        return dict_item["num"]

    # Convert dict to list of dicts with "char" and "num" keys
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    # Sort by count in descending order (greatest to least)
    char_list.sort(key=get_count, reverse=True)

    return char_list