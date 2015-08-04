class Student(object):

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def introduce(self):
        print("Student ID: %d, Name: %s" % (self.student_id, self.name))

if __name__ == '__main__':
    qianhui = Student(123, 'qianhui')
    qianhui.introduce()
