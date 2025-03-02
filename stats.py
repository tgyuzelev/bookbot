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

def sort_on(dict):
    return dict["count"]

def sort_characters_count(data):
    list_data = []

    for [key, value] in data.items():
        list_data.append({ "symbol": key, "count": value })
    
    list_data.sort(reverse=True, key=sort_on)
    return list_data

