from mrjob.job import MRJob

class WordCount(MRJob):
    def mapper(self, _, line):
        for word in line.split(","):
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word.lower(), sum(counts)
    
    

if __name__ == '__main__':
    WordCount.run()