from Student import *

class Gradebook(object):
    def __init__(self):
        self._students = {}
    
    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

if __name__ == '__main__':
    book = Gradebook()
    albert = book.student('Albert Einstein')
    comp = albert.subject('Computer')
    comp.report_grade(10, 0.9)
    math = albert.subject('Math')
    math.report_grade(80, 0.10)
    print(albert.average_grade())
