class OldToModernSpellingPair(object):
    def __init__(self, original, modern):
        self.modern = modern
        self.original = original

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        if self.modern == other.modern and self.original == other.original:
            return True

        return False

    def __hash__(self):
        return hash((self.original, self.modern))


