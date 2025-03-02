def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    data = {}
    for character in book_text:
        lowered = character.lower()

        if lowered not in data:
            data[lowered] = 0
        
        data[lowered] += 1
    
    return data

