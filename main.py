from stats import word_count
from stats import character_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    return text
book_text = main()
w_count = word_count(book_text)
print(f"Found {w_count} total words")
c_count = character_count(book_text)
print(c_count)
main()