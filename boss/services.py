from domain.entities import Student,Discipline,Grade,GradeDTO
from boss.undo_redo import *


class ServiceStudent(object):
       
    def __init__(self, validStudent, repoStudent,undo):
        self.__validStudent = validStudent
        self.__repoStudent = repoStudent
        self.__undo = undo
    
     
    def add_student(self,ids,name):
        ''' f that add a new valid student '''
        st = Student(ids,name)
        self.__validStudent.validateStudent(st)
        stud=self.__repoStudent.add(st) 
        
        undo = FunctionCall(self.__repoStudent.remove, stud.getIds())
        redo = FunctionCall(self.__repoStudent.add, stud)
        op = Operation(undo, redo) 
        self.__undo.reecord(op)
        
    def update_student(self,name,ids):
        '''function update a name of a student(given by id) with a new given name'''
        stud=self.__repoStudent.update(name,ids)
        undo = FunctionCall(self.__repoStudent.update,stud[1], stud[0].getIds())
        redo = FunctionCall(self.__repoStudent.update, stud[0].getName(),stud[0].getIds())
        op = Operation(undo, redo) 
        self.__undo.reecord(op)
        
    def remove_student(self,ids):
        '''function remove a student(given by id)from the repository'''
        stud=self.__repoStudent.remove(ids)      
        undo = FunctionCall(self.__repoStudent.add, stud)
        redo = FunctionCall(self.__repoStudent.remove, stud.getIds())
        op = Operation(undo, redo) 
        self.__undo.reecord(op)
   
    def get_students(self):
        return self.__repoStudent.get_all()
    
    def lenght(self):
        return len(self.__repoStudent)
    
    def search_students(self,name):
        '''function searches all students that contain a given string and
         creates a new list with them.
         If the string does not match with any students, the new list will contain the
         "students not found" message '''
        students=self.__repoStudent.get_all()
        new = []
        for s in students:          
            if s.getName().lower().find(name.lower())!=-1:
                new.append(s)
        if new == []:
            new.append("students not found")
        return new 
    
    
    
    
class ServiceDiscipline(object):
        
    def __init__(self, validDiscipline, repoDicipline,undo):
        self.__validDiscipline = validDiscipline
        self.__repoDicipline = repoDicipline
        self.__undo = undo
   
    def add_discipline(self,idd,name):
        '''function add a new valid discipline 
        input:idd,name'''
        discipline = Discipline(idd,name)
        self.__validDiscipline.validateDiscipline(discipline)
        dis=self.__repoDicipline.add(discipline)
        undo = FunctionCall(self.__repoDicipline.remove, dis.get_idd())
        redo = FunctionCall(self.__repoDicipline.add, dis)
        op = Operation(undo, redo) 
        self.__undo.reecord(op)
        
    def get_all_disciplines(self):
        return self.__repoDicipline.get_all()
            
    def update_discipline(self,name,idd):
        '''function update a name of a discipline(given by id) with a new given name
         input:name,idd'''
        dis=self.__repoDicipline.update(name,idd)
        undo = FunctionCall(self.__repoDicipline.update,dis[1], dis[0].get_idd())
        redo = FunctionCall(self.__repoDicipline.update, dis[0].get_name(),dis[0].get_idd())
        op = Operation(undo, redo) 
        self.__undo.reecord(op)
 
    def remove_discipline(self,idd):
        '''function remove a discipline(given by id)from the repository'''
        dis=self.__repoDicipline.remove(idd)
        redo = FunctionCall(self.__repoDicipline.remove, dis.get_idd())
        undo = FunctionCall(self.__repoDicipline.add, dis)
        op = Operation(undo, redo) 
        self.__undo.reecord(op)
 
    def search_disciplines(self,name):
        '''function searches all disciplines that contain a given string and
         creates a new list with them.
         if the string does not match with any disciplines, the new list will contain the
         "disciplines not found" message '''
        disciplines=self.__repoDicipline.get_all()
        new = []
        for discipline in disciplines:
            if discipline.get_name().lower().find(name.lower())!=-1:
                new.append(discipline)
        if new == []:
            new.append("disciplines not found")             
        return new        
   

class ServiceGrade(object):
    
    
    def __init__(self, validGrade, repoStudent, repoDicipline, repoGrade,undo):
        self.__validGrade = validGrade
        self.__repoStudent = repoStudent
        self.__repoDicipline = repoDicipline
        self.__repoGrade = repoGrade
        self.__undo = undo
    
    def add_grade(self,idg,ids,idd,grade):
        '''function grades a given student(given by id) at a given discipline(given by id)
         the grade will have a unique id and a value(between 0 ant 10)'''
        student=self.__repoStudent.get_std_by_id(ids)
        discipline=self.__repoDicipline.get_dis_by_id(idd)
        grade = Grade(idg,student,discipline,grade)
        self.__validGrade.validateGrade(grade)
        self.__repoGrade.add(grade)

    def get_all_grades(self):
        '''function return all grades and use dtos to return the data in an elegant way:
        for students and disciplines will return name instead of id '''
        grades=self.__repoGrade.get_all()
        grades_dtos=[]  
        for grade in grades:
            idg=grade.get_idg()
            st_name=grade.get_student().getName()
            dis_name=grade.get_discipline().get_name()
            grade=grade.get_grade()
            greade_dto=GradeDTO(idg,st_name,dis_name,grade)
            grades_dtos.append(greade_dto)
        return grades_dtos    

    def remove_std_grade_by_id(self,ids):
        '''the funcion removes a student which corresponds to a given id
            and all student's grades '''
        grades=self.__repoGrade.get_all()
        list=[]        
        for grade in grades:
            
            if grade.get_student().getIds()==ids:
                list.append(grade)
                self.__repoGrade.remove_grade(grade.get_idg())
        stud=self.__repoStudent.remove(ids)        
        undo = FunctionCall(self.reverse_undo_std,list,stud)
        redo = FunctionCall(self.redo_remove_std,ids)
        op = Operation(undo, redo) 
        self.__undo.reecord(op)
        
    def reverse_undo_std(self,grades,stud):
        for grade in grades:
            self.__repoGrade.add(grade)
        self.__repoStudent.add(stud)
        
    def redo_remove_std(self,ids):   
        grades=self.__repoGrade.get_all()
        list=[]  
        for grade in grades:
            if grade.get_student().getIds()==ids:
                list.append(grade)
                self.__repoGrade.remove_grade(grade.get_idg())
        stud=self.__repoStudent.remove(ids)        
        
    
    
    def remove_dis_by_id(self,idd):
        '''the funcion removes a discipline which corresponds to a given id
            and all grades for that discipline'''
        grades=self.__repoGrade.get_all()
        list = []
        for grade in grades:
            if grade.get_discipline().get_idd()==idd:
                self.__repoGrade.remove_grade(grade.get_idg())
        dis=self.__repoDicipline.remove(idd)  
        undo = FunctionCall(self.reverse_undo_dis,list,dis)
        redo = FunctionCall(self.redo_remove_dis,idd)
        op = Operation(undo, redo) 
        self.__undo.reecord(op)         
        
        
    def reverse_undo_dis(self,grades,dis):
        for grade in grades:
            self.__repoGrade.add(grade)
        self.__repoDicipline.add(dis)
        
    def redo_remove_dis(self,idd):   
        grades=self.__repoGrade.get_all()
        list=[]  
        for grade in grades:
            if grade.get_discipline().get_idd()==idd:
                list.append(grade)
                self.__repoGrade.remove_grade(grade.get_idg())
        dis=self.__repoDicipline.remove(idd)        
        
    
    def statistic_1(self):
        '''the function creates a list with all students failing
         at one or more disciplines (students having an average 
         <5 for a discipline are failing it)'''
        
        grades=self.__repoGrade.get_all()
        students= self.__repoStudent.get_all()
        disciplines=self.__repoDicipline.get_all()
        bad_students=[]
        for i in students:
            ok=0
            for j in disciplines:
                s=0
                nr=0               
                for k in grades:
                    if k.get_student().getIds() == i.getIds() and k.get_discipline().get_idd() == j.get_idd():
                        s+=k.get_grade()
                        nr+=1
                if nr>0:        
                    medie=s/nr 
                if medie<5 and nr>0:
                    ok=1
            if ok==1:
                bad_students.append(i.getName())

        return bad_students                   
                  
    def statistic_2(self,top):
        '''the function creates a list with Students with the best school situation, sorted in descending
         order of their aggregated average (the average between their average grades per discipline)
         the number of people is given from keyboard'''
        
        grades=self.__repoGrade.get_all()
        students= self.__repoStudent.get_all()
        best_students=[]
        for i in students:
            s=0
            nr=0
            for j in grades:
                if j.get_student().getIds()==i.getIds():
                    s+=j.get_grade()
                    nr+=1
            if nr>0: 
                medie=s/nr       
                best_students.append([i.getName(),medie])

        best_students.sort(key=lambda x: x[1], reverse=True)

        return best_students[:top]      
                
    def statistic_3(self,top):
        grades=self.__repoGrade.get_all()
        disciplines= self.__repoDicipline.get_all()
        dis_rank=[]
        for i in disciplines:
            s=0
            nr=0
            for j in grades:
                if j.get_discipline().get_idd()==i.get_idd():
                    s+=j.get_grade()
                    nr+=1
            if nr>0: 
                medie=s/nr       
                dis_rank.append([i.get_name(),medie])   
        dis_rank.sort(key=lambda x: x[1], reverse=True) 
        return dis_rank[:top]                  
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      

