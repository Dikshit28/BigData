from audioop import avg
from statistics import mean
from mrjob.job import MRJob
from mrjob.step import MRStep

class CityTemp(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer_max),
            MRStep(reducer=self.reducer_min)
        ]
    def mapper(self, _, line):
        loc,temp=line.split(',')
        temp=float(temp)
        yield loc, temp

    def reducer(self, loc, temp):
        yield loc, mean(temp)
    
    def reducer_max(self, loc,temp):
        yield loc,max(temp)
    
    def reducer_min(self, loc,temp):
        yield loc, min(temp)

if __name__ == '__main__':
    CityTemp.run()