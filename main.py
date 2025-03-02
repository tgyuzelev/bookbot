from stats import count_words, count_characters, sort_characters_count

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    words_count = count_words(book_text)
    print(f"{words_count} words found in the document")
    data = count_characters(book_text)
    print(sort_characters_count(data))

main()
