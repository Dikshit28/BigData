#total count of words grouped by first letter of name
from itertools import count
from mrjob.job import MRJob

class CountName(MRJob):
    def mapper(self, key, record):
        splits=record.split(',')
        yield splits[0][0], 1

    def reducer(self, letter, birth):
        yield letter, sum(birth)

if __name__ == '__main__':
    CountName.run()