def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)

    dict_of_counted_char = character_counter(file_contents)
    
    list_of_dicts = list_of_letters(dict_of_counted_char)

    list_of_dicts.sort(key=sort_on, reverse=True)
    
    generate_report(file_contents, list_of_dicts)
    

def generate_report(text, lst):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_counter(text)} words found in the document")
    print()
    for i in lst:
        print(f"The '{i['letter']}' character was found {i['occurance']} times")

def sort_on(dict):
    return dict["occurance"]

def sort_list(l, k):
    return l.sort(key=k, reverse=True)

def list_of_letters(characters_dict):
    l = []
    for i in characters_dict:
        if i.isalpha():
            l.append({ "letter": i, "occurance" : characters_dict[i] })
    return l

def character_counter(text):
    characters = {}
    for i in text.lower():
        if i in characters:
            characters[i] = characters[i] + 1
        else:
            characters[i] = 1
    return characters

def word_counter(text):
    formated_to_count = text.split()
    return len(formated_to_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()