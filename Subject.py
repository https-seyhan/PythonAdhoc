import collections
Grade = collections.namedtuple('Grade', ('score', 'weight'))

class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))
        
    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            print("Grade !!", grade)
            total += grade.score * grade.weight
            total_weight += grade.weight
        
        print("Total Weight", total_weight)
        return total 
        
        
