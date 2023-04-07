def find_word_count(word, file_path):
  
    word_count = 0

    with open(file_path, 'r') as file:
        text = file.read().lower()
        text_length = len(text)
        word_length = len(word)

        if text_length < word_length:
            return 0

        # Başlangıç belirleme
        left = 0
        right = word_length - 1

        while right < text_length:
            if text[left:right + 1] == word:
                word_count += 1

            # Sol yönlü arama
            if text[left] == word[0]:
                left += 1
                right += 1
            # Sağ yönlü arama
            elif text[right] == word[word_length - 1]:
                left += 1
                right += 1
            else:
                left += 2
                right += 2

    return word_count



word1 = "upon "
file_path = "dosya.txt "
word_count1 = find_word_count(word1.lower(), file_path)
print("'{0}' kelimesi dosyada {1} kez geçmektedir.".format(word1, word_count1))


word2 = "sigh "
word_count2 = find_word_count(word2.lower(), file_path)
print("'{0}' kelimesi dosyada {1} kez geçmektedir.".format(word2, word_count2))


word3 = "Dormouse "
word_count3 = find_word_count(word3.lower(), file_path)
print("'{0}' kelimesi dosyada {1} kez geçmektedir.".format(word3, word_count3))



word4 = "jury-box "
word_count4 = find_word_count(word4.lower(), file_path)
print("'{0}' kelimesi dosyada {1} kez geçmektedir.".format(word4, word_count4))


word5 = "swim "
word_count5 = find_word_count(word5.lower(), file_path)
print("'{0}' kelimesi dosyada {1} kez geçmektedir.".format(word5, word_count5))
