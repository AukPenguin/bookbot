def get_num_words(text):
    words = text.split()
    words_count = len(words)

    return (f"Found {words_count} total words")


def get_num_charachters(text):
    lowered_text = text.lower()
    count = {}

    for charachter in lowered_text:

        if charachter not in count:
            count[charachter] = 0

        count[charachter] += 1

    return count


def for_sorting(item: dict) -> int:
    return item["num"]


def sort(count: dict):
    sorted_character_count = []

    for character, num in count.items():
        if character.isalpha():
            sorted_character_count.append({"char": character, "num": num})

    sorted_character_count.sort(reverse=True, key=for_sorting)

    return sorted_character_count

