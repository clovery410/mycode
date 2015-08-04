def type_tag(x):
    return type_tag.tags[type(x)]

class HN_record(object):
    """A student record formatted via Hamilton's standard"""
    def __init__(self, name, grade):
        """name is a string containing the student's name, and grade is a grade object"""
        self.student_info = [name, grade]

class JO_record(object):
    """A student record formatted via Julia's standard"""
    def __init__(self, name, grade):
        """name is a string containing the student's name, and grade is a grade object"""
        self.student_info = {'name': name, 'grade': grade}

type_tag.tags = {HN_record: 'HN', JO_record: 'JO'}

def get_name(record):
    types = type_tag(record)
    return get_name.implementations[types](record)

def get_grade(record):
    types = type_tag(record)
    return get_grade.implementations[types](record)

get_name.implementations = {}
get_name.implementations['HN'] = lambda x: x.student_info[0]
get_name.implementations['JO'] = lambda x: x.student_info['name']
get_grade.implementations = {}
get_grade.implementations['HN'] = lambda x: x.student_info[1]
get_grade.implementations['JO'] = lambda x: x.student_info['grade']

class HN_grade(object):
    def __init__(self, total_points):
        if total_points > 90:
            letter_grade = 'A'
        else:
            letter_grade = 'F'
        self.grade_info = (total_points, letter_grade)

class JO_grade(object):
    def __init__(self, total_points):
        self.grade_info = total_points

type_tag.tags[HN_grade] = 'HN'
type_tag.tags[JO_grade] = 'JO'


def get_points(grade):
    types = type_tag(grade)
    return get_points.implementations[types](grade)

def compute_average_total(records):
    total = 0
    for rec in records:
        grade = get_grade(rec)
        total = total + get_points(grade)
    return total / len(records)

get_points.implementations = {}
get_points.implementations['HN'] = lambda x: x.grade_info[0]
get_points.implementations['JO'] = lambda x: x.grade_info

class AK_record(object):
    """A student record formatted via John's standard"""
    def __init__(self, name_str, grade_num):
        """Note: name_str must be a string, grade_num must be a number"""
        
def convert_to_AK(records):
    list_of_AK = []
    for rec in records:
        name = get_name(rec)
        grade = get_grade(rec)
        points = get_points(grade)
        list_of_AK.append(AK_record(name, points))
    return list_of_AK

if __name__ == "__main__":
    lily = JO_record('Lily', 3)
    print(get_name(lily))
    print(get_grade(lily))
