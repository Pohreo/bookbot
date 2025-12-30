def word_count(book_text):
    text_count = len(book_text.split())
    return text_count

def character_count(text):
    lower_text = text.lower()
    characters = {}
    for character in lower_text:
        if character in characters:
            characters[character] += 1
        else: 
            characters[character] = 1
    return characters

def sorter(s):
    return s["num"]

def sort_char(text):
    sort_list = []
    for k in text:
        if k.isalpha():
            sort_list.append({'char':k, 'num':text[k]})
    sort_list.sort(key=sorter, reverse=True)
    return sort_list