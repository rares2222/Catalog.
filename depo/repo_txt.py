from domain.entities import Student, Discipline
from errors.exception import RepoError


class RepoStudentsText(object):
    def __init__(self,rs):
        self.__students =self.read_text_file(rs)
        self.__rs=rs



    def write_text_file(self,file_name):
        f = open(file_name, "w")
        try:
            for s in self.__students:
                student_str = str(s.getIds()) + ";" + s.getName() + "\n"
                f.write(student_str)
            f.close()
        except Exception as e:
            print("An error occurred -" + str(e))

    def read_text_file(self,file_name):
        result = []
        try:
            f = open(file_name, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                result.append(Student(int(line[0]), line[1]))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e

        return result


    def add(self, std):
        if std in self.__students:
            raise RepoError("student already exist")
            # return
        self.__students.append(std)
        self.write_text_file(self.__rs)
        return std


    def update(self, name, ids):
        for i in range(len(self.__students)):
            if self.__students[i].getIds() == ids:
                x = self.__students[i].getName()
                self.__students[i].setName(name)
                stud = self.__students[i]
                self.write_text_file(self.__rs)
                return stud, x

    def remove(self, ids):
        i = 0
        while i < len(self.__students):
            if self.__students[i].getIds() == ids:
                stud = self.__students[i]

                self.__students.remove(self.__students[i])
                i -= 1
                self.write_text_file(self.__rs)
                return stud
            i += 1
        return self.__students

    def get_all(self):
        return self.__students[:]

    def __len__(self):
        return len(self.__students)

    def get_std_by_id(self, ids):
        for std in self.__students:
            if std.getIds() == ids:
                return std

class RepoDisciplinesText(object):

    def __init__(self,rs):
        self.__disciplines = self.read_text_file(rs)
        self.__rs = rs

    def write_text_file(self, file_name):
        f = open(file_name, "w")
        try:
            for s in self.__disciplines:
                discipline_str = str(s.get_idd()) + ";" + s.get_name() + "\n"
                f.write(discipline_str)
            f.close()
        except Exception as e:
            print("An error occurred -" + str(e))

    def read_text_file(self, file_name):
        result = []
        try:
            f = open(file_name, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                result.append(Discipline(int(line[0]), line[1]))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e

        return result
    def add(self, discipline):
        if discipline in self.__disciplines:
            raise RepoError("discipline already exist")
            # return
        self.__disciplines.append(discipline)
        self.write_text_file(self.__rs)
        return discipline

    def get_all(self):
        return self.__disciplines[:]

    def __len__(self):
        return len(self.__disciplines)

    def update(self, name, idd):
        for i in range(len(self.__disciplines)):
            if self.__disciplines[i].get_idd() == idd:
                x = self.__disciplines[i].get_name()
                self.__disciplines[i].set_name(name)
                dis = self.__disciplines[i]
                self.write_text_file(self.__rs)
                return dis, x

    def remove(self, idd):
        i = 0
        while i < len(self.__disciplines):
            if self.__disciplines[i].get_idd() == idd:
                dis = self.__disciplines[i]
                self.__disciplines.remove(self.__disciplines[i])
                i -= 1
                self.write_text_file(self.__rs)
                return dis
            i += 1
        return self.__disciplines

    def get_dis_by_id(self, idd):
        for dis in self.__disciplines:
            if dis.get_idd() == idd:
                return dis
        raise RepoError("elem inexistent")

class RepoGradesText(object):

        def __init__(self, rs):
            self.__grades = self.read_text_file(rs)
            self.__rs = rs

        def write_text_file(self, file_name):
            f = open(file_name, "w")
            try:
                for s in self.__grades:
                    grade_str = str(s.get_idg()+ ";" +s.get_student().getName() + ";" + s.get_discipline().get_name() + ";" + s.get_grade() + "\n")
                    f.write(grade_str)
                f.close()
            except Exception as e:
                print("An error occurred -" + str(e))

        def read_text_file(self, file_name):
            result = []
            try:
                f = open(file_name, "r")
                line = f.readline().strip()
                while len(line) > 0:
                    line = line.split(";")
                    result.append(Discipline(int(line[0]), line[1]))
                    line = f.readline().strip()
                f.close()
            except IOError as e:
                """
                    Here we 'log' the error, and throw it to the outer layers 
                """
                print("An error occured - " + str(e))
                raise e

            return result

        def add(self, grade):
            if grade in self.__grades:
                raise RepoError("grade already exist")
            self.__grades.append(grade)
            self.write_text_file(self.__rs)

        def remove_grade(self, idg):
            i = 0
            while i < len(self.__grades):
                if self.__grades[i].get_idg() == idg:
                    self.__grades.remove(self.__grades[i])
                    i -= 1
                self.write_text_file(self.__rs)
                i += 1
            return self.__grades

        def get_all(self):
            return self.__grades[:]