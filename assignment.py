from mrjob.job import MRJob
from mrjob.step import MRStep

class assignment(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)
        ]

    def mapper_get_words(self, _, line):
        id,name,salary,rating=line.split(',')
        print(id,name,salary,rating)
        yield [id,name],rating

    def reducer_count_words(self, id,rating):
        yield None,(rating,id)

    def reducer_find_max_word(self,_,word_count_pairs):
        for rating,id in sorted(word_count_pairs,reverse=True)[:5]:
            yield rating,id

if __name__ == '__main__':
    assignment.run()