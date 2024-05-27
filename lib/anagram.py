# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)


    def match(self, words):
        return [anagram for anagram in words if sorted(anagram.lower()) == self.sorted_word]