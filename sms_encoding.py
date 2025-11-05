def sms_encoding(data):
    vowels = "aeiouAEIOU"
    words = data.split()
    encoded_words = []
    
    for word in words:
        # If word has only vowels, keep it as it is
        if all(ch in vowels for ch in word):
            encoded_words.append(word)
        else:
            # Keep only consonants
            new_word = ''.join([ch for ch in word if ch not in vowels])
            encoded_words.append(new_word)
    
    # Join the encoded words with space
    return ' '.join(encoded_words)


# Test
data = "I love Python"
print(sms_encoding(data))
