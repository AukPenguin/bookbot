from stats import get_num_words
from stats import get_num_charachters
from stats import sort
import sys

def get_book_text(filepath):

    with open(filepath) as file:
        text = file.read()
        return text


def main():

    if len(sys.argv) == 2:

        path = sys.argv[1]
        text = get_book_text(path)
        
        words = get_num_words(text)
        count = get_num_charachters(text)
        sorted_characters = sort(count)

        lines = []
        for item in sorted_characters:
            lines.append(f"{item['char']}: {item['num']}")
        char_report = "\n".join(lines)
        
        result = (
            "============ BOOKBOT ============\n"
            f"Analyzing book found at {path}...\n"
            "----------- Word Count ----------\n"
            f"{words}\n"
            "--------- Character Count -------\n"
            f"{char_report}\n"
            "============= END ==============="
        )

        print(result)
    
    else:

        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
