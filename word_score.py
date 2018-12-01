


def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_word(words):
    count=0
    x=input("enter the string:")
    ans=len(list(map(lambda x:is_vowel(x),list(words))))
    if len%2==0:
        count=+2
    else:
        count=+1
