def count_consonants(in_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    in_str = in_str.lower()
    total_count = 0
    for c in list(in_str):
        if c not in vowels:
            if c.isalpha():
                total_count += 1

    return total_count


def count_vowels(in_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    in_str = in_str.lower()
    total_count = 0
    for v in vowels:
        total_count += in_str.count(v)
    return total_count


def count_space(in_str):
    return in_str.count(" ")


def word_demography(in_str):
    str_len = len(in_str)
    consonants_count = count_consonants(in_str)
    vowels_count = count_vowels(in_str)
    space_count = count_space(in_str)
    others_count = str_len - consonants_count - vowels_count - space_count
    return str_len, consonants_count, vowels_count, space_count, others_count


def main():
    # my_str = "a quick brown fox1"
    my_str = "Testing 1 2 3"
    (str_len, consonants_count, vowels_count, space_count, others_count) = word_demography(my_str)
    print("String length = " + str(str_len))
    print("Consonants count = " + str(consonants_count))
    print("Vowels count = " + str(vowels_count))
    print("Whitespace count = " + str(space_count))
    print("Others count = " + str(others_count))


if __name__ == '__main__':
    main()
