def count_words(text):
    word_count = {}
    words = text.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "This is a sample text to demonstrate word counting. This text contains some repetitive words."
print(count_words(text))
