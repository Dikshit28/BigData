from mrjob.job import MRJob
from mrjob.step import MRStep

class Rating(MRJob):

    def step(self):
        return [MRStep(mapper=self.mapper,reducer=self.reducer)]

    def mapper(self, _, record):
        (user_id,movie_id,rating,timestamp)=record.split('\t')
        yield rating, 1
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    Rating.run()