def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_character(text):
    character_dict = {}
    for character in text.lower():
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict   

def get_report(dict):
    list = [] 
    for char, count in dict.items():
        if char.isalpha(): 
            list.append({"char": char,"count": count})

    def sort_on(dict_item):
        return dict_item["count"]
    
    list.sort(reverse = True, key = sort_on)
    return list

