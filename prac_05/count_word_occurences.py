def main():
    words = {}
    text = input("Text: ")
    split_text = text.lower().split()
    for word in split_text:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    sorted_words = sorted(words.keys())
    max_length = 0
    for word in sorted_words:
        if len(word) > max_length:
            max_length = len(word)
    for word in sorted_words:
        print("{:{}} : {}".format(word, max_length, words[word]))

main()
