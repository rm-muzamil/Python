# Create a function to check if two strings are anagrams.
def anagram(str1,str2):
    str1_result = "".join(sorted(str1)).lower()
    str2_result = "".join(sorted(str2)).lower()
    if str1_result == str2_result:
        return f"The both Strings {str1} and {str2} are anagram"
str1,str2=input("Enter first string: "),input("Enter secound string: ")
result = anagram(str1,str2)
print(result)