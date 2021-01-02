from errors.exception import RepoError
import pickle

class RepoStudentsPickle(object):
    def __init__(self,rs):
        self.__students =self.read_binary_file(rs)
        self.__rs=rs

    def read_binary_file(self,file_name):
        result = []

        try:
            f = open(file_name, "rb")
            return pickle.load(f)
        except EOFError:

            """
                This is raised if input file is empty
            """
            return []
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e

        return result

    def write_binary_file(self,file_name, students):
        f = open(file_name, "wb")
        pickle.dump(students, f)
        f.close()



    def add(self, std):
        if std in self.__students:
            raise RepoError("student already exist")
            # return
        self.__students.append(std)
        self.write_binary_file(self.__rs,self.__students)
        return std


    def update(self, name, ids):
        for i in range(len(self.__students)):
            if self.__students[i].getIds() == ids:
                x = self.__students[i].getName()
                self.__students[i].setName(name)
                stud = self.__students[i]
                self.write_binary_file(self.__rs, self.__students)
                return stud, x

    def remove(self, ids):
        i = 0
        while i < len(self.__students):
            if self.__students[i].getIds() == ids:
                stud = self.__students[i]

                self.__students.remove(self.__students[i])
                i -= 1
                self.write_binary_file(self.__rs, self.__students)
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


class RepoDisciplinesPickle(object):

    def __init__(self,rs):
        self.__disciplines = self.read_binary_file(rs)
        self.__rs = rs

    def read_binary_file(self,file_name):
        result = []
        try:
            f = open(file_name, "rb")
            return pickle.load(f)
        except EOFError:

            """
                This is raised if input file is empty
            """
            return []
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e

        return result

    def write_binary_file(self,file_name, disciplines):
        f = open(file_name, "wb")
        pickle.dump(disciplines, f)
        f.close()

    def add(self, discipline):
        if discipline in self.__disciplines:
            raise RepoError("discipline already exist")
            # return
        self.__disciplines.append(discipline)
        self.write_binary_file(self.__rs, self.__disciplines)
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
                self.write_binary_file(self.__rs, self.__disciplines)
                return dis, x

    def remove(self, idd):
        i = 0
        while i < len(self.__disciplines):
            if self.__disciplines[i].get_idd() == idd:
                dis = self.__disciplines[i]
                self.__disciplines.remove(self.__disciplines[i])
                i -= 1
                self.write_binary_file(self.__rs, self.__disciplines)
                return dis
            i += 1
        return self.__disciplines

    def get_dis_by_id(self, idd):
        for dis in self.__disciplines:
            if dis.get_idd() == idd:
                return dis
        raise RepoError("elem inexistent")

class RepoGradesPickle(object):

        def __init__(self,rs):
            self.__grades = self.read_binary_file(rs)
            self.__rs = rs

        def write_binary_file(self, file_name, grades):
            f = open(file_name, "wb")
            pickle.dump(grades, f)
            f.close()

        def read_binary_file(self, file_name):
            result = []
            try:
                f = open(file_name, "rb")
                return pickle.load(f)
            except EOFError:

                """
                    This is raised if input file is empty
                """
                return []
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
            self.write_binary_file(self.__rs, self.__grades)



        def remove_grade(self, idg):
            i = 0
            while i < len(self.__grades):
                if self.__grades[i].get_idg() == idg:
                    self.__grades.remove(self.__grades[i])
                    i -= 1
                self.write_binary_file(self.__rs, self.__grades)
                i += 1
            return self.__grades

        def get_all(self):
            return self.__grades[:]