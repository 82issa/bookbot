from stats import count_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    results = get_book_text("books/frankenstein.txt")
    num_words = count_words(results)
    print(f"{num_words} words found in the document")
main()

