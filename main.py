def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words in the document")
    print(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    lowered_text = text.lower()
    for i in lowered_text:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()
    


main()


        