def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = book_words(text)
    #print(f"{word_count} words found in the document")
    letters_count = book_letters(text)
    print(letters_count)


def get_book_text(path):  
    with open(path) as f:
        return f.read()

def book_words(text):
    words = text.split()
    return len(words)

def book_letters(text):
    letters = {}
    for l in text.lower():
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

            
        

main()
