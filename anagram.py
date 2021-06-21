def anagram(str1=input("Enter the first string: "), str2=input("Enter the second string: ")):
    if sorted(str1) == sorted(str2):
        print("This is an anagram!")
        return True
    else:
        print("This is not an anagram!")
        return False


anagram()
