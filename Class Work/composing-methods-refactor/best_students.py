# By Kamran Bigdely Nov. 2020

class Employer:
    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')


class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")


class School:
    def __init__(self, students) -> None:
        self.students = students
        self.min_gpa = 2.5
        self.employers = [Employer('Microsoft'), Employer(
            'Free Software Foundation'), Employer('Google')]

    def print_students(self, students, header):
        for s in students:
            print(s.name)

    def __passing_students(self):
        '''Return a list of students who passed.'''
        passed_students = []
        for s in self.students:
            if s.get_gpa() > self.min_gpa:
                passed_students.append(s)

        return passed_students

    def __top_students(self, students):
        '''Return a list of 10% of students.'''
        students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(students))
        top_10_percent = students[index:]

        return top_10_percent

    def process_graduation(self):
        passed_students = self.__passing_students()

        self.print_students(passed_students, "*** Student who graduated ***")

        # Send congrat emails to them.
        for s in passed_students:
            s.send_congrat_email()

        # Find the top 10% of them and send their contact to the top employers
        top_10_percent = self.__top_students(passed_students)
        for e in self.employers:
            e.send(top_10_percent)


students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2, 'kami'), Student(3, 'sarah')]
school = School(students)
school.process_graduation()
