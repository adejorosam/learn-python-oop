'''Write a class called Wordplay. It should have a field that holds a list of words. The user
of the class should pass the list of words they want to use to the class. There should be the
following methods:
• words_with_length(length) — returns a list of all the words of length length
• starts_with(s) — returns a list of all the words that start with s
• ends_with(s) — returns a list of all the words that end with s
• palindromes() — returns a list of all the palindromes in the list
• only(L) — returns a list of the words that contain only those letters in L
• avoids(L) — returns a list of the words that contain none of the letters in L
'''

class WordPlay:
    def __init__(self,list_words):
        self.list_words = list_words

    def words_with_length(self,length):
        self.length = length
        m = length.split()
        return m

    def starts_with(self,s):
        self.s = s.lower()
        c = s.split()
        return [i for i in c if i.startswith('s')]

    def ends_with(self,s):
        self.s = s.lower()
        u = s.split()
        return [i for i in u if i.endswith('s')]

    def palindromes(self):
        return [i for i in self.list_words if i == i[::-1]]
    
    def only(self,L):
        return [i for i in L if i in L]

    def avoid(self,L):
        return [i for i in L if i not in L]
                

    
        


s = ['samson',"joshua",'silas']
f = WordPlay(s)
print(f.words_with_length('Hi fellas!'))
print(f.starts_with("What's good bro. My name is samson"))
print(f.ends_with('Hi, how are you boss'))
print(f.palindromes())
print(f.only(L))
print(f.avoid(L))
        
        
