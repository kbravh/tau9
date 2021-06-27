from cachetools import cached
from cachetools.keys import hashkey

alphaValues = {
  "'": "1",
  "-": "1",
  "a": "2",
  "á": "2",
  "à": "2",
  "â": "2",
  "ä": "2",
  "ã": "2",
  "b": "2",
  "c": "2",
  "ç": "2",
  "d": "3",
  "e": "3",
  "é": "3",
  "è": "3",
  "ê": "3",
  "ë": "3",
  "f": "3",
  "g": "4",
  "h": "4",
  "i": "4",
  "í": "4",
  "ì": "4",
  "î": "4",
  "ï": "4",
  "j": "5",
  "k": "5",
  "l": "5",
  "m": "6",
  "n": "6",
  "ñ": "6",
  "o": "6",
  "ó": "6",
  "ò": "6",
  "ö": "6",
  "p": "7",
  "q": "7",
  "r": "7",
  "s": "7",
  "t": "8",
  "u": "8",
  "ú": "8",
  "ù": "8",
  "ü": "8",
  "v": "8",
  "w": "9",
  "x": "9",
  "y": "9",
  "z": "9"
}

def wordToKeypad(word):
  """
  Converts a word to the sequence it would need to be typed on a telephone keypad.
  For example: "spider" => 774337
  Apostrophes and hyphens are assigned to 1, since that key is unused on the keypad.
  """
  return ''.join([alphaValues.get(letter, "0") for letter in word])

@cached(cache={}, key=lambda _, sequence: hashkey(sequence))
def filterBySequence(wordlist, sequence):
  """
  Takes an array of words {word, sequence} and filters it down to words that match
  the sequence as typed thus far. Returns a list of words {word, sequence}.
  """
  filtered_list = [entry["word"] for entry in wordlist if entry["sequence"].startswith(sequence)]
  return filtered_list