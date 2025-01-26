def main():
    with open("books/frankenstein.txt", "r") as file:
        file_content = file.read()
        count = count_words(file_content)
        char_dict = character_frequency(file_content)
        print_report(count, char_dict)


def count_words(text):
    return sum(1 for word in text.split())


def character_frequency(text):
    if not text:
        return {}
    frequency = {}
    for character in text.lower():
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1
    return frequency


def print_report(word_count, char_dict):
    print("--- Begin report ---")
    print(f"{word_count} words found in the document\n")
    sorted_chars = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


main()
