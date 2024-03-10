def main():
    path = "books/frankenstein.txt"
    text = contents(path)
    num_words = num_of_word(text)
    count_letter = count_letters(text)
    new_dict_list = sort_dict(count_letter)
    print(f"the number of words in the book is : {num_words}")
    print()
    for item in new_dict_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")


def contents(path):
    with open(path) as f:
        return f.read()


def num_of_word(path):
    words = path.split()
    return len(words)


# need to checkout this function, know what it does but can't explain why
def count_letters(path):
    frank_dict = {}
    for tex in path:
        lower = tex.lower()
        if lower in frank_dict:
            frank_dict[lower] += 1
        else:
            frank_dict[lower] = 1
    return frank_dict


def sort_on(d):
    return d["num"]


def sort_dict(path_dict):
    new_list = []
    for pat in path_dict:
        new_list.append({"char": pat, "num": path_dict[pat]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list


main()
