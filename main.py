from stats import count_words
from stats import count_characters
from stats import snorted
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = sys.argv[1] 
    results = get_book_text(book)
    num_words = count_words(results)
    num_chars = count_characters(results)
    char_dict = snorted(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for each in char_dict:
        if each[0].isalpha():
            print(each[0] + ":" , each[1])
main()

