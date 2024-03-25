
def find_and_print_word(data, word):
    for key, value in data.items():
        if key == word:
            print(f"{word}: {value}")

# Nhập từ cần dịch
input_word = input("Nhập từ tiếng Anh cần tra cứu: ")

# Tìm từ cần dịch
translated_word = find_and_print_word(data, input_word)

if translated_word is None:
    print(f"Từ '{input_word}' không có trong từ điển.")