def get_num_words(texts):
    words = texts.split()
    return len(words)

def get_num_chars(texts):
    res = {}
    for char in texts:
        res[char.lower()] = 1 + res.get(char.lower(), 0)
    return res

def sort_on(items):
    return items["num"]

def get_sorted_list(dict):
    new_list = []
    for char in dict:
        pair = {}
        pair["char"] = char
        pair["num"] = dict[char]
        new_list.append(pair)

    new_list.sort(reverse=True, key=sort_on)
    return new_list