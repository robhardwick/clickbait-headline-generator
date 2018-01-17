import random


class Model:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.values = f.read().splitlines()

    def get(self):
        return random.choice(self.values)


genres = Model('data/genres.txt')
subjects = Model('data/subjects.txt')
outcomes = Model('data/outcomes.txt')
