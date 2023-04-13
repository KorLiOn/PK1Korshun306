
ukrainian_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

def remove_non_ukrainian_letters(text):
    text_without_punctuation = ''
    for char in text:
        if char.lower() in ukrainian_alphabet:
            text_without_punctuation += char.lower()
    return text_without_punctuation

def remove_non_ukrainian_letters_Spase(text):
    text_without_punctuation = ''
    for char in text:
        if char.lower() in ukrainian_alphabet or char == " ":
            if char == " ":
                text_without_punctuation += "_"
            else:
                text_without_punctuation += char.lower()
    return text_without_punctuation



text = input('Введіть текст: ')
text = text.lower()
text_without_punctuation = remove_non_ukrainian_letters(text)
text_without_punctuation_Spase = remove_non_ukrainian_letters_Spase(text)
print('Текст без знаків пунктуації та інших символів:', text_without_punctuation)
print('Текст без знаків пунктуації та інших символів з пробілами:', text_without_punctuation_Spase)