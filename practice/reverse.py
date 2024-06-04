def reverse(s):
    vowels = 'aeiouAEIOU'
    reversed_string = s[::-1]
    vowel_count = sum(1 for char in reversed_string if char in vowels)
    print("Reversed String: " + reversed_string + "\nVowel Count: " + str(vowel_count))