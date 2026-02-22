class StringReverser:
    def __init__(self, text):
        self.text = text
    
    def reverse_words(self):
        """Reverse the order of words in the string."""
        words = self.text.split()
        return ' '.join(reversed(words))
    
    def __str__(self):
        return self.reverse_words()


# Example usage
if __name__ == "__main__":
    str1=input("enter a sentence:") 
    reverser = StringReverser(str1)
    print(reverser.reverse_words())  