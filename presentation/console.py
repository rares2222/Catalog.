from errors.exception import ValidError,RepoError


class UI(object):
    
    
    def __ui_add_student(self,params):
        if len(params)!=2:
            print("invalid numbers of params!")
            return
        ids=int(params[0])
        name=params[1]    
        self.__srvStudent.add_student(ids,name)
    

    def __ui_print_students(self,params):
        students = self.__srvStudent.get_students()
        if len(students)==0:
            print("list of students is empty")
            return 
        for student in students:
            print(student)
        

    
    def __ui_add_disciplie(self,params):
        if len(params)!=2:
            print("invalid numbers of params!")
        idd=int(params[0])
        name = params[1]
        self.__srvDiscipline.add_discipline(idd,name)    
    
    
    def  __ui_print_disciplines(self,params):
        disciplines=self.__srvDiscipline.get_all_disciplines()
        if len(disciplines)==0:
            print("list of disciplines is empty")
            return
        for discipline in disciplines:
            print(discipline)
    
    
    def __ui_update_student(self,params):
        if len(params)!=2:
            print("invalid numbers of params!")
        ids=int(params[0])
        name = params[1]
        self.__srvStudent.update_student(name,ids)
    
    
    def __ui_update_discipline(self,params):
        if len(params)!=2:
            print("invalid numbers of params!")
        idd=int(params[0])
        name = params[1]
        self.__srvDiscipline.update_discipline(name,idd)
    
    
    def __ui_remove_student(self,params):
        if len(params)!=1:
            print("invalid numbers of params!")
        ids=int(params[0])
        self.__srvStudent.remove_student(ids)
    
    
    def __ui_remove_discipline(self,params):
        if len(params)!=1:
            print("invalid numbers of params!")
        idd=int(params[0])
        self.__srvDiscipline.remove_discipline(idd)
    
    
    def __ui_grade_st(self,params):
        if len(params)!=4:
            print("invalid numbers of params!")
        idg = int(params[0])
        ids = int(params[1])
        idd = int(params[2])
        grade = int(params[3])
        if grade<0 or grade>10:
            print("invalid grade value!")
            return   
        self.__srvGrade.add_grade(idg,ids,idd,grade)
    
    
    def __ui_print_grades(self,params):
        grades=self.__srvGrade.get_all_grades()
        if len(grades)==0:
            print("list of grades is empty")
            return
        for grade in grades:
            print(grade)
    
    
    def __ui_remove_std(self,params):
        if len(params)!=1:
            print("invalid numbers of params!")
        ids=int(params[0])
        self.__srvGrade.remove_std_grade_by_id(ids)  
          
    def __ui_remove_dis(self,params):
        if len(params)!=1:
            print("invalid numbers of params!")
        idd=int(params[0])
        self.__srvGrade.remove_dis_by_id(idd)   
    
    def __ui_search_disciplines(self,params):
        if len(params)!=1:
            print("invalid numbers of params!")
        name=params[0]
        new=self.__srvDiscipline.search_disciplines(name)
        for n in new:
            print(n)
            
    def __ui_search_students(self,params):   
        if len(params)!=1:
            print("invalid numbers of params!")
        name=params[0]
        new=self.__srvStudent.search_students(name)
        for n in new:
            print(n)     
            
    
    def __ui_bad_students(self,params):
        
        bad_students=self.__srvGrade.statistic_1()
        if len(bad_students)==0:
            print("list of bad_students is empty")
            return
        for i in bad_students:
            print(i)
        
    
    
    def __ui_best_students(self,params):
        top=int(input("top of:"))
        best_std=self.__srvGrade.statistic_2(top)
        if len(best_std)==0:
            print("list of best_students is empty")
            return
        for i in best_std:
            print(i[0],"with the avarage:",i[1])
            
    
    
    def __ui_dis_rank(self,params):
        top=int(input("top of:"))
        disciplines=self.__srvGrade.statistic_3(top)    
        if len(disciplines)==0:
            print("list of disciplines is empty")
            return
        for i in disciplines:
            print(i[0],"with the avarage:",i[1])
    
    
    def ui_undo(self,params):
        self.__strUndo.undo()
    
    
    def ui_redo(self,params):
        self.__strUndo.redo()
    
    
    def __init__(self, srvStudent, srvDiscipline, srvGrade, srvUndo):
        self.__srvStudent = srvStudent
        self.__srvDiscipline = srvDiscipline
        self.__srvGrade = srvGrade
        self.__strUndo = srvUndo
        self.__comenzi={"add_student":self.__ui_add_student,
                        "print_students":self.__ui_print_students,
                        "add_discipline":self.__ui_add_disciplie,
                        "print_disciplines":self.__ui_print_disciplines,
                        "update_student":self.__ui_update_student,
                        "update_discipline":self.__ui_update_discipline,
                        "remove_student":self.__ui_remove_student,
                        "remove_discipline":self.__ui_remove_discipline,
                        "grading":self.__ui_grade_st,
                        "print_grades":self.__ui_print_grades,
                        "remove_std":self.__ui_remove_std,
                        "remove_dis":self.__ui_remove_dis,
                        "search_disciplines":self.__ui_search_disciplines,
                        "search_students":self.__ui_search_students,
                        "lazy_students":self.__ui_bad_students,
                        "best_students":self.__ui_best_students,
                        "disciplines_rank":self.__ui_dis_rank,
                        "undo":self.ui_undo,
                        "redo":self.ui_redo}

        
    def __process_comands(self,cmd):
        cmd=cmd.strip()
        parts=cmd.split()
        return parts[0],parts[1:]    
  
            
   
    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                print("Bye")
                return
            cmd_name,params = self.__process_comands(cmd)
            if cmd_name in self.__comenzi:
                try:
                    self.__comenzi[cmd_name](params)
                except ValueError:
                    print("invalid value!")
                except ValidError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)        
            else:
                print("Invalid comand")

    
    
    
    
    

