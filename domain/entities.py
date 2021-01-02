'''
Created on Nov 15, 2020

@author: Rares
'''

class Student:
    

    def __init__(self, ids,name):
         
        """ Create a new student with the given ids, name """

        self.__ids = ids
        self.__name = name
        
    
    def getIds(self):
        return self.__ids
    
    
    def getName(self):
        return self.__name  
    
    def setName(self,name):
        self.__name=name
    
        
    
    def __eq__(self,student):
        
        """  Verify equality: return True if the current student equals with other student (have the same id)"""
        return self.getIds()==student.getIds()
    
    def __str__(self):
        return str(self.__ids)+" "+self.__name+"\n"
    

        
class Discipline:

    
    def __init__(self, idd, name):
        self.__idd = idd
        self.__name = name

    def get_idd(self):
        return self.__idd


    def get_name(self):
        return self.__name


    def set_name(self, value):
        self.__name = value

    def __eq__(self,other): 
        return self.__idd==other.__idd   
        
    def __str__(self):
        return str(self.__idd)+" "+self.__name+"\n"
    
    
    
    


class Grade(object):
    
    
    def __init__(self, idg, student, discipline, grade):
        self.__idg = idg
        self.__student = student
        self.__discipline = discipline
        self.__grade = grade

    def get_idg(self):
        return self.__idg


    def get_student(self):
        return self.__student


    def get_discipline(self):
        return self.__discipline


    def get_grade(self):
        return self.__grade


    def set_grade(self, value):
        self.__grade = value

    def __eq__(self,other): 
        return self.__idg==other.__idg  



class GradeDTO(object):
    
    
    def __init__(self, idg, st_name, dis_name, grade):
        self.__idg = idg
        self.__st_name = st_name
        self.__dis_name = dis_name
        self.__grade = grade
    
    def __str__(self):
        return str(self.__idg)+" "+self.__st_name+" "+self.__dis_name+" "+str(self.__grade)+" \n"



