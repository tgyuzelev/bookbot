from stats import count_words, count_characters, sort_characters_count

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def print_book_report(book_file_path, words_count, characters_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    for char_data in characters_count:
        symbol = char_data["symbol"]

        if symbol.isalpha() == False:
            continue
        
        count = char_data["count"]
        print(f"{symbol}: {count}")

    print("============= END ===============")

def main():
    book_file_path = "books/frankenstein.txt"
    book_text = get_book_text(book_file_path)

    words_count = count_words(book_text)

    data = count_characters(book_text)
    sorted_data = sort_characters_count(data)

    print_book_report(book_file_path, words_count, sorted_data)

main()
