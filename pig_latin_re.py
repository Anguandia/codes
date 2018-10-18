import re

def pig_latin(word):
    #check presence of atleast a vowel
    if re.search(r'[a,e,i,o,u]', word, re.IGNORECASE):
        #check word starts with alphabet
        if re.match(r'[a-z]', word, re.IGNORECASE):
            #check word has valid english characters
            if word.isalnum():
                #check if word starts vowel
                if re.match(r'[a,e,i,o,u]', word, re.IGNORECASE):
                    pig_version=word+'way'
                else:
                    #locate first vowel
                    first_vowel = re.search(r'[a,e,i,o,u]', word, re.IGNORECASE).start()
                    pig_version = word[first_vowel:]+word[:first_vowel]+'ay'
                return pig_version
            return 'word not english'
        return 'word must start with alphabet'
    return 'no vowel in word'

for word in ['wIll', 'dog', 'Category', 'dmtry', 'chatter', 'trash', 'andela', 'electrician', '2twa']:
    print(pig_latin(word))