def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = book_words(text)
    letters_count = book_letters(text)
    count_dict = dict_sort(letters_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")

    for item in count_dict:
        if not item['char'].isalpha():
            continue
        print(f"The '{item['char']}' chracter was found {item['count']} times")
    
    print("--- End report ---")


def get_book_text(path):  
    with open(path) as f:
        return f.read()

def book_words(text):
    words = text.split()
    return len(words)

def book_letters(text):
    letters = {}
    for l in text.lower():
        if l.isalpha():
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
    return letters

def dict_sort(letters_count):
    char_dict = letters_count
    list_of_dicts = []

    for char, count in letters_count.items():
        new_dict = {'char': char, 'count': count}
        list_of_dicts.append(new_dict)

    def sort_on(item):
        return item['count']

    list_of_dicts.sort(reverse=True, key=sort_on)

    return(list_of_dicts)

            
        

main()
