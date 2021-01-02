from domain.entities import Student, Discipline, Grade,GradeDTO
from depo.repo import RepoStudents, RepoDisciplines, RepoGrades
from errors.exception import RepoError,ValidError
from boss.services import ServiceStudent, ServiceDiscipline, ServiceGrade
from validation.validators import ValidatorStudent,ValidatorDiscipline,ValidatorGrade
import unittest
from boss.undo_redo import UndoService


            


class TestDomain(unittest.TestCase):
    
    
    def setUp(self):
        idg = 1
        student = "ana"
        discipline = "math"
        grade = 7

        self.__g = Grade(idg, student, discipline, grade)
        self.__g1 = Grade(idg, student, discipline, grade)
        self.__gd = GradeDTO(idg, student, discipline, grade)
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def test_domain_student(self):
        idd = 1
        name = "Diego"
        s = Student(idd,name)
        s1=Student(idd,name)
        self.assertEqual(s.getIds(),1)
        self.assertEqual(s.getName(),"Diego")       
        s.setName("Carlo")        
        self.assertEqual(s.__str__(),"1 Carlo\n")
        self.assertEqual(s.__eq__(s1),True)
         
    
    def test_domain_discipline(self):
        id=1
        name="Algebra"        
        d=Discipline(id,name)
        d1 = Discipline(id, name)
        
        self.assertEqual(d.get_idd(),1)
        self.assertEqual(d.get_name(),"Algebra")
        d.set_name("FP")
        self.assertEqual(str(d),"1 FP\n")
        self.assertEqual(d.__eq__(d1), True)
    
    def test_grades(self):

        self.assertEqual(self.__g.get_idg(),1)
        self.assertEqual(self.__g.get_student(),"ana")
        self.assertEqual(self.__g.get_discipline(),"math")
        self.assertEqual(self.__g.get_grade(),7)
        self.__g.set_grade(9)
        self.assertEqual(self.__g.get_grade(),9)
        self.assertEqual(self.__g.__eq__(self.__g1), True)
        self.assertEqual(self.__gd.__str__(),"1 ana math 7 \n")
    

class TestRepository(unittest.TestCase):
    
    def setUp(self):
        self.__repoStudents=RepoStudents()
        self.__repoDisciplines=RepoDisciplines()
        self.__repoGrades=RepoGrades()
        
        self.__repoStudents.add(Student(1,"ana"))
        self.__repoStudents.add(Student(2,"anca"))
        self.__repoStudents.add(Student(3,"ania"))
              
        self.__repoDisciplines.add(Discipline(1,"Math"))
        self.__repoDisciplines.add(Discipline(2,"History"))
        self.__repoDisciplines.add(Discipline(3,"ASC"))
      
        
        self.__repoGrades.add(Grade(1,1,1,9))
        self.__repoGrades.add(Grade(2,2,1,8))
        self.__repoGrades.add(Grade(3,2,2,7))
        self.__repoGrades.add(Grade(4,3,3,10))
        
        
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def test_get_st(self):
        self.assertEqual(len(self.__repoStudents.get_all()),3)
        self.assertEqual( self.__repoStudents.get_all()[0].getIds(), 1)
        self.assertEqual( self.__repoStudents.get_all()[1].getIds(), 2)
        self.assertEqual( self.__repoStudents.get_all()[2].getIds(), 3)
    
    
    def test_add_St(self):
        self.__repoStudents.add(Student(6,"briana"))
        self.assertEqual(len(self.__repoStudents.get_all()),4)
        self.assertEqual( self.__repoStudents.get_all()[3].getIds(), 6)
        try:
            self.__repoStudents.add(Student(6, "briana"))
        except RepoError as re:
            self.assertEqual(str(re),"student already exist")
        self.assertEqual(len(self.__repoStudents.get_all()), 4)
    
    def test_remove_St(self):
        self.__repoStudents.remove(2)
        self.assertEqual(len(self.__repoStudents.get_all()),2)
        self.assertEqual( self.__repoStudents.get_all()[1].getIds(), 3)
        self.__repoStudents.remove(-1)
        self.assertEqual(len(self.__repoStudents.get_all()), 2)
        
        
    def test_update_St(self):
        self.__repoStudents.update("Marian",1)       
        self.assertEqual(len(self.__repoStudents.get_all()),3)
        self.assertEqual( self.__repoStudents.get_all()[0].getIds(), 1)
        self.assertEqual( self.__repoStudents.get_all()[0].getName(), "Marian")
        
        
    def test_get_st_by_id(self):
        ok=self.__repoStudents.get_std_by_id(2)        
        self.assertEqual(ok,self.__repoStudents.get_all()[1])



    def test_get_dis(self):
        self.assertEqual(len(self.__repoDisciplines.get_all()),3)
        self.assertEqual( self.__repoDisciplines.get_all()[0].get_idd(), 1)
        self.assertEqual( self.__repoDisciplines.get_all()[1].get_idd(), 2)
        self.assertEqual( self.__repoDisciplines.get_all()[2].get_idd(), 3)
        
        
    def test_add_dis(self):
        self.__repoDisciplines.add(Discipline(4,"FP"))
        self.assertEqual(self.__repoDisciplines.__len__(),4)
        self.assertEqual( self.__repoDisciplines.get_all()[3].get_idd(), 4)
        try:
            self.__repoDisciplines.add(Discipline(4,"FP"))
        except RepoError as re:
            self.assertEqual(str(re), "discipline already exist")
        
        
    def test_remove_dis(self):
        self.__repoDisciplines.remove(3)
        self.assertEqual(len(self.__repoDisciplines.get_all()),2)
        self.assertEqual( self.__repoDisciplines.get_all()[1].get_idd(), 2)


    def test_update_dis(self):
        self.__repoDisciplines.update("Optional", 1)
        self.assertEqual(len(self.__repoDisciplines.get_all()),3)
        self.assertEqual(self.__repoDisciplines.get_all()[0].get_name(),"Optional")
    
    
    def test_get_dis_by_id(self):
        ok=self.__repoDisciplines.get_dis_by_id(1)
        self.assertEqual(ok,self.__repoDisciplines.get_all()[0])
        try:
            self.__repoDisciplines.get_dis_by_id(111)
        except RepoError as re:
            self.assertEqual(str(re), "elem inexistent")


        
    

    def test_get_all_grades(self):  
        self.assertEqual(len(self.__repoGrades.get_all()),4)
        
    
    def test_add_grade(self):
        self.__repoGrades.add(Grade(5,1,1,10))
        self.assertEqual(len(self.__repoGrades.get_all()),5)
        self.assertEqual(self.__repoGrades.get_all()[4].get_idg(),5)
        self.assertEqual(self.__repoGrades.get_all()[4].get_student(),1)
        self.assertEqual(self.__repoGrades.get_all()[4].get_discipline(),1)
        self.assertEqual(self.__repoGrades.get_all()[4].get_grade(),10)
        try:
            self.__repoGrades.add(Grade(5, 1, 1, 10))
        except RepoError as re:
            self.assertEqual(str(re), "grade already exist")

    def test_remove_grade(self):
        self.__repoGrades.remove_grade(1)
        self.assertEqual(len(self.__repoGrades.get_all()),3)
        self.assertEqual(self.__repoGrades.get_all()[2].get_idg(),4)
        self.assertEqual(self.__repoGrades.get_all()[2].get_student(),3)
        self.assertEqual(self.__repoGrades.get_all()[2].get_discipline(),3)
        self.assertEqual(self.__repoGrades.get_all()[2].get_grade(),10)
       
       
       
class TestSrv(unittest.TestCase):  
    def setUp(self):  
        self.__srvUndo=UndoService()
        self.__repoStudent=RepoStudents()
        self.__repoDiscipline=RepoDisciplines()
        self.__repoGrade=RepoGrades()
        self.__validStudent = ValidatorStudent()
        self.__validDiscipline = ValidatorDiscipline()
        self.__validGrade = ValidatorGrade()
        self.__srvStudent = ServiceStudent(self.__validStudent,self.__repoStudent,self.__srvUndo)
        self.__srvDiscipline = ServiceDiscipline( self.__validDiscipline,  self.__repoDiscipline,self.__srvUndo)
        self.__srvGrade = ServiceGrade( self.__validGrade, self.__repoStudent, self.__repoDiscipline, self.__repoGrade,self.__srvUndo)
        
        
        
        self.__repoStudent.add(Student(1,"ana"))
        self.__repoStudent.add(Student(2,"anca"))
        self.__repoStudent.add(Student(3,"ania"))
        
              
        self.__repoDiscipline.add(Discipline(1,"Math"))
        self.__repoDiscipline.add(Discipline(2,"History"))
        self.__repoDiscipline.add(Discipline(3,"ASC"))
      
        
        self.__repoGrade.add(Grade(1,Student(1,"ana"),Discipline(1,"Math"),9))
        self.__repoGrade.add(Grade(2,Student(2,"anca"),Discipline(1,"Math"),8))
        self.__repoGrade.add(Grade(3,Student(2,"anca"),Discipline(2,"History"),7))
        self.__repoGrade.add(Grade(4,Student(3,"ania"),Discipline(3,"ASC"),10))
        
    
   
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
     
    
    def test_service_std_getALL(self):
        self.assertEqual(self.__srvStudent.lenght(),3)
        self.assertEqual( self.__srvStudent.get_students()[0].getIds(), 1)
        self.assertEqual( self.__srvStudent.get_students()[1].getIds(), 2)
        self.assertEqual( self.__srvStudent.get_students()[2].getIds(), 3)
        
        self.assertEqual( self.__srvStudent.get_students()[0].getName(), "ana")
        self.assertEqual( self.__srvStudent.get_students()[1].getName(), "anca")
        self.assertEqual( self.__srvStudent.get_students()[2].getName(), "ania")
     
     
    def test_service_dis_getALL(self):
        self.assertEqual(len(self.__srvDiscipline.get_all_disciplines()),3)
        self.assertEqual( self.__srvDiscipline.get_all_disciplines()[0].get_idd(), 1)
        self.assertEqual( self.__srvDiscipline.get_all_disciplines()[1].get_idd(), 2)
        self.assertEqual( self.__srvDiscipline.get_all_disciplines()[2].get_idd(), 3)
        
        self.assertEqual( self.__srvDiscipline.get_all_disciplines()[0].get_name(), "Math")
        self.assertEqual( self.__srvDiscipline.get_all_disciplines()[1].get_name(), "History")
        self.assertEqual( self.__srvDiscipline.get_all_disciplines()[2].get_name(), "ASC") 
      
   
                
    def test_service_add(self):

        self.assertEqual(self.__srvUndo.undo(),False)
        self.__srvStudent.add_student(20, "angel")
        self.assertEqual(self.__srvUndo.redo(), False)
        self.assertEqual(self.__srvStudent.lenght(),4)
        self.assertEqual( self.__srvStudent.get_students()[3].getIds(), 20)
        self.__srvUndo.undo()
        self.assertEqual(self.__srvStudent.lenght(),3)
        self.__srvUndo.redo()
        self.assertEqual(self.__srvStudent.lenght(),4)
        
        self.__srvDiscipline.add_discipline(5, "E")
        self.assertEqual(len(self.__srvDiscipline.get_all_disciplines()),4)
        self.assertEqual( self.__srvDiscipline.get_all_disciplines()[3].get_idd(), 5)  
        self.__srvUndo.undo()
        self.assertEqual(len(self.__srvDiscipline.get_all_disciplines()),3)
        self.__srvUndo.redo()
        self.assertEqual(len(self.__srvDiscipline.get_all_disciplines()),4)
              
        self.__srvGrade.add_grade(6,1,1,10)
        x=self.__repoGrade.get_all()
        self.assertEqual(len(x),5)
        
        
        

    def test_service_update(self):
        self.__srvStudent.update_student("angel",1 )
        self.assertEqual(self.__srvStudent.lenght(),3)
        self.assertEqual( self.__srvStudent.get_students()[0].getName(),"angel")
        self.__srvUndo.undo()
        self.assertEqual(self.__srvStudent.lenght(),3)
        self.assertEqual( self.__srvStudent.get_students()[0].getName(),"ana")
        self.__srvUndo.redo()   
        self.assertEqual(self.__srvStudent.lenght(),3)
        self.assertEqual( self.__srvStudent.get_students()[0].getName(),"angel")
        
        self.__srvDiscipline. update_discipline( "E",1)
        self.assertEqual(len(self.__srvDiscipline.get_all_disciplines()),3)
        self.assertEqual(self.__srvDiscipline.get_all_disciplines()[0].get_name(), "E")
        self.__srvUndo.undo()
        self.assertEqual(len(self.__srvDiscipline.get_all_disciplines()),3)
        self.assertEqual(self.__srvDiscipline.get_all_disciplines()[0].get_name(), "Math")
        self.__srvUndo.redo()   
        self.assertEqual(self.__srvDiscipline.get_all_disciplines()[0].get_name(), "E")
        
    def test_service_remove(self):
        self.__srvStudent.remove_student(1)
        self.assertEqual(self.__srvStudent.lenght(),2)   
        self.assertEqual( self.__srvStudent.get_students()[0].getName(),"anca")
        
        self.__srvDiscipline.remove_discipline(1)
        self.assertEqual(len(self.__srvDiscipline.get_all_disciplines()),2)
        self.assertEqual( self.__srvDiscipline.get_all_disciplines()[0].get_name(),"History")

     
    def test_service_remove2(self): 
        self.__srvGrade.remove_std_grade_by_id(1)
        self.assertEqual(self.__srvStudent.lenght(),2)
        self.assertEqual( self.__srvStudent.get_students()[0].getName(),"anca")
        self.__srvUndo.undo()
        self.assertEqual(self.__srvStudent.lenght(), 3)
        self.__srvUndo.redo()
        self.assertEqual(self.__srvStudent.lenght(), 2)
        self.__srvGrade.remove_dis_by_id(1)
        self.assertEqual(len(self.__srvDiscipline.get_all_disciplines()),2)
        self.assertEqual( self.__srvDiscipline.get_all_disciplines()[0].get_name(),"History")
        x=self.__repoGrade.get_all()
        self.assertEqual(len(x),2)
        self.__srvUndo.undo()
        x = self.__repoGrade.get_all()
        self.assertEqual(len(x), 2)
        self.__srvUndo.redo()
        x = self.__repoGrade.get_all()
        self.assertEqual(len(x), 2)
        
    def test_search_by_name(self):
        
        new=self.__srvStudent.search_students("a")
        self.assertEqual(len(new),3)
        
        new=self.__srvStudent.search_students("xx")
        self.assertEqual(len(new),1)
        self.assertEqual(new,["students not found"])
        
        new2=self.__srvDiscipline.search_disciplines("a")
        self.assertEqual(len(new2),2)
        
        new2=self.__srvDiscipline.search_disciplines("xx")
        self.assertEqual(len(new2),1)
        self.assertEqual(new2,["disciplines not found"])

    def test_get_all_grade(self):
        self.assertEqual(len(self.__srvGrade.get_all_grades()),4)

           
    def test_statistics(self):


        self.__repoGrade.add(Grade(8,Student(1,"ana"),Discipline(1,"Math"),1))
        self.__repoGrade.add(Grade(7,Student(1,"ana"),Discipline(1,"Math"),1))
        self.__repoGrade.add(Grade(6,Student(1,"ana"),Discipline(1,"Math"),1))
        self.__repoGrade.add(Grade(9,Student(3,"anca"),Discipline(2,"History"),3))

        x=self.__repoGrade.get_all()
        self.assertEqual(len(x),8)
        stat1=self.__srvGrade.statistic_1()
        self.assertEqual(stat1,['ana', 'ania'])
        stat2=self.__srvGrade.statistic_2(3)
        self.assertEqual(stat2,[['anca', 7.5], ['ania', 6.5], ['ana', 3.0]])
        stat3 = self.__srvGrade.statistic_3(3)
        self.assertEqual(stat3, [['ASC', 10.0], ['History', 5.0], ['Math', 4.0]])





