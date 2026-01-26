class Tokenizer:
    def __init__(self, prefix="TOKEN"):
        self.mapping = {}
        self.counter = 1
        self.prefix = prefix

    def tokenize(self, value: str) -> str:
        if value not in self.mapping:
            token = f"{self.prefix}_{self.counter:03d}"
            self.mapping[value] = token
            self.counter += 1
        return self.mapping[value]
