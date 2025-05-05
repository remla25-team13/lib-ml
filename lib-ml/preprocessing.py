import re
import string

from typing import List


class Preprocessor:
    def __init__(self):
        self.punctuation_table = str.maketrans("", "", string.punctuation)

    def preprocess(self, text: str) -> str:
        """Clean and normalize a single input string."""
        text = text.lower()                          
        text = text.strip()                         
        text = self.remove_urls(text)
        text = self.remove_punctuation(text)
        text = re.sub(r"\s+", " ", text)            
        return text

    def preprocess_batch(self, texts: List[str]) -> List[str]:
        """Clean and normalize a list of strings."""
        return [self.preprocess(t) for t in texts]

    def remove_punctuation(self, text: str) -> str:
        return text.translate(self.punctuation_table)

    def remove_urls(self, text: str) -> str:
        return re.sub(r"http\S+|www\S+|https\S+", "", text)
