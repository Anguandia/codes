def pig_latin(word):
    a={'a','e','i','o','u'}
    #make vowels case insensitive
    vowels=a|set(b.upper() for b in a)
    if word[0].isalpha():
        if any(i in vowels for i in word):
            if word.isalnum():
                if word[0] in vowels:
                    pig_version=word+'way'
                else:
                    first_vowel=min(word.find(vowel) for vowel in vowels if vowel in word)
                    #alternative way to locate first vowelin word
                    #first_vowel = next((i for i, ch  in enumerate(word) if ch in vowels),None)
                    pig_version = word[first_vowel:]+word[:first_vowel]+'ay'
                return pig_version
            return 'word not english'
        return 'no vowel in word'
    return 'word must start with alphabet'

#for word in ['wIll', 'dog', 'Category', 'chatter', 'trash','andela', 'mo$es', 'electrician', '2twa']:
 #   print(pig_latin(word))