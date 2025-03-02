from stats import count_words

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    words_count = count_words(book_text)
    print(f"{words_count} words found in the document")

main()
