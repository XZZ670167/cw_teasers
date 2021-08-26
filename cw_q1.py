def countVowels(in_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    in_str = in_str.lower()
    total_count = 0
    for v in vowels:
        total_count += in_str.count(v)
    return total_count


print(countVowels("a quick brown fox"))

# BTW, the question is wrong to named the function as countVowels. It should
# be count_vowels according to the naming convention in Python
