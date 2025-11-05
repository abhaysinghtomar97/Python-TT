def encrypt_sentence(sentence):
    words = sentence.split()
    vowels = "aeiouAEIOU"
    encrypted_words = []

    for i in range(len(words)):
        word = words[i]
        # Odd-positioned word (1-indexed)
        if (i + 1) % 2 != 0:
            encrypted_words.append(word[::-1])
        else:
            consonants = ""
            vowels_part = ""
            for ch in word:
                if ch in vowels:
                    vowels_part += ch
                else:
                    consonants += ch
            encrypted_words.append(consonants + vowels_part)

    return " ".join(encrypted_words)


# Test
sentence = "the sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
