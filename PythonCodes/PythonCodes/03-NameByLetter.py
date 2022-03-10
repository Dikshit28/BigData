#calculate total count of birth grouped by first letter of name
from mrjob.job import MRJob

class CountName(MRJob):

    def mapper(self, key, record):
        split = record.split(",")
        yield split[0][0], int(split[2])
    
    def reducer(self, letter, birth):
        yield letter, count(birth)

if __name__ == '__main__':
    CountName.run()