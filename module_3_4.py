def single_root_words(root_word, *other_words):
    same_word = []
    for word in other_words:
        #print(word)
        if word.lower() in root_word.lower():
            same_word.append(word)
        if root_word.lower() in word.lower():
            same_word.append(word)
    return same_word

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))