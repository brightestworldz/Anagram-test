# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(str1, str2):
    # [assignment] Add your code here
    str1 = 'kate'
    str2 = 'take'
    str1_anagram = sorted(str1)
    str2_anagram = sorted(str2)

    if str1_anagram == str2_anagram:
        return True
    else:
        return False

print(find_anagrams('kate', 'take'))

