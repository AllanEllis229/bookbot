def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = book_words(text)
    #print(f"{word_count} words found in the document")
    book_letters(text)


def get_book_text(path):  
    with open(path) as f:
        return f.read()

def book_words(text):
    words = text.split()
    return len(words)

def book_letters(text):
    letters = {}
    for l in text.lower():

main()
