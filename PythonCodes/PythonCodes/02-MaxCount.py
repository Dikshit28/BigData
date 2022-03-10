from mrjob.job import MRJob
from mrjob.step import MRStep

class WordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_max_count)
        ]

    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield (word.lower(), 1)
        
    def reducer(self, word, counts):
        yield word, sum(counts)

    def reducer_max_count(self, _, word_count_pair):
        yield max(word_count_pair)
    

if __name__ == '__main__':
    WordCount.run()