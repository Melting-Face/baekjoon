from sys import stdin

texts = [text.strip() for text in stdin.readlines()]

count = 0

for text in texts[1:]:
    before_word = None
    word_set = set()
    group_word = True
    for word in text:
        if not before_word:
            word_set.add(word)
        elif before_word != word and word not in word_set:
            word_set.add(word)
        elif before_word != word and word in word_set:
            group_word = False
            break
        before_word = word

    if group_word:
        count += 1

print(count)