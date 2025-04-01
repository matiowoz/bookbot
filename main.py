import sys
from stats import get_num_words, get_count_character, get_report

def get_book_text(path):
    with open(path) as f:
        return f.read()
  
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_dict = get_count_character(text)
    report = get_report(characters_dict)

    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {book_path}")
    print("-" * 10 + " Word Count " + "-" * 10)
    print(f"Found {num_words} total words")
    print("-" * 9 + " Character Count " + "-" * 7)

    for char_dict in report:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")

    print("=" * 13 + " END " + "=" * 15)
   
main()
                  
