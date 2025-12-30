from stats import word_count, character_count, sort_char
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content   

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    return text
book_text = main()
w_count = word_count(book_text)
print(f"Found {w_count} total words")
c_count = character_count(book_text)
sorted_words = sort_char(c_count)
for item in sorted_words:
    print(f"{item['char']}: {item['num']}")