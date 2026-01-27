class FakeNameGenerator:
    def __init__(self):
        self.fake_names = [
            "Rohan Mehta",
            "Amit Sharma",
            "Neha Verma",
            "Pooja Iyer",
            "Arjun Rao"
        ]
        self.mapping = {}
        self.index = 0

    def get_fake_name(self, real_name):
        if real_name not in self.mapping:
            self.mapping[real_name] = self.fake_names[self.index % len(self.fake_names)]
            self.index += 1
        return self.mapping[real_name]
