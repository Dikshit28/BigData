from mrjob.job import MRJob
from mrjob.step import MRStep

class WordCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_maxcount)
        ]
    def mapper(self, _, line):
        for word in line.split(","):
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word.lower(), sum(counts)
    
    def reducer_maxcount(self, _,word_count_pair):
        yield max(word_count_pair)

if __name__ == '__main__':
    WordCount.run()