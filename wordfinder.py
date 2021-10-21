"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    
    def __init__(self, words.txt):
        wordsFile = open("words", "r")
        
        self.words = self.parse(wordsFile)
        print(f"{len(self.words)}" words read)

    def parse(self, wordsFile):

        return [w.strip() for w in wordsFile]

    def random(self):

        return random.choice(self.words)    

class SpecialWordFinder(WordFinder):

        def parseComment(self, wordsFile)

        return [w.strip() for w in wordsFile
            if w.strip() and not w.startswith("#")]

