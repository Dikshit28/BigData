#total count of words grouped by gender
from itertools import count
from mrjob.job import MRJob
from mrjob.step import MRStep

class CountName(MRJob):

    def step(self):
        return [MRStep(mapper=self.filterGender),
        MRStep(mapper=self.mapper,reducer=self.reducer)]
        
    def filterGender(self, key,record):
        splits=record.split(',')
        if splits[1] == 'F':
            yield splits[1], (splits[0]+","+ splits[2])

    def mapper(self, key, record):
        splits=record.split(',')
        yield splits[0][0], int(splits[2])
        

    def reducer(self, letter, birth):
        yield letter, count(birth)

if __name__ == '__main__':
    CountName.run()