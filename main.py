'''
Created on Nov 14, 2020

@author: Rares
'''
import unittest
from testing.tests import TestDomain,TestRepository,TestSrv
from validation.validators import ValidatorStudent, ValidatorDiscipline, ValidatorGrade
from depo.repo import RepoStudents, RepoGrades, RepoDisciplines
from boss.services import ServiceStudent, ServiceDiscipline, ServiceGrade
from presentation.console import UI
from boss.undo_redo import *
from depo.repo_p import *
from depo.repo_txt import *
from jproperties import Properties

if __name__ == '__main__':
    unittest.main(exit=False)
    srvUndo=UndoService()
    validStudent = ValidatorStudent()
    validDiscipline = ValidatorDiscipline()
    validGrade = ValidatorGrade()
    configs = Properties()
    with open('settings.properties', 'rb') as config_file:
        configs.load(config_file)
    repo_type = configs.get("repository").data
    if repo_type == "inmemory":
        repoStudent = RepoStudents()
        repoDicipline = RepoDisciplines()
        repoGrade = RepoGrades()
    elif repo_type == "binary":
        repoStudent = RepoStudentsPickle("repostudents")
        repoDicipline = RepoDisciplinesPickle("repodisciplines")
        repoGrade = RepoGradesPickle("repogrades")
    elif repo_type == "text":
        repoStudent = RepoStudentsText("repostudents_t")
        repoDicipline = RepoDisciplinesText("repodiscipline_t")
        repoGrade = RepoGradesText("repogrades_t")
    else:
        raise BaseException("invalid config file")
    srvStudent = ServiceStudent(validStudent, repoStudent,srvUndo)
    srvDiscipline = ServiceDiscipline(validDiscipline, repoDicipline,srvUndo)
    '''srvStudent.add_student(1,"Diana")
    srvStudent.add_student(2,"Joe")
    srvStudent.add_student(3,"Adam")
    srvStudent.add_student(4,"John")
    srvStudent.add_student(5,"Adolf")
    srvStudent.add_student(6,"Mike")
    srvStudent.add_student(7,"Mike")
    srvStudent.add_student(8,"Mary")
    srvStudent.add_student(9,"Paul")
    srvStudent.add_student(10,"Radu")
    srvDiscipline.add_discipline(1,"CS history")
    srvDiscipline.add_discipline(2,"CSA")
    srvDiscipline.add_discipline(3,"FP")
    srvDiscipline.add_discipline(4,"CL")
    srvDiscipline.add_discipline(5,"Sports")
    srvDiscipline.add_discipline(6,"E")
    srvDiscipline.add_discipline(7,"F")
    srvDiscipline.add_discipline(8,"R")
    srvDiscipline.add_discipline(9,"Science")
    srvDiscipline.add_discipline(10,"Optional")'''
    srvGrade = ServiceGrade(validGrade, repoStudent,repoDicipline,repoGrade,srvUndo)
    '''srvGrade.add_grade(1, 1, 2, 10)
    srvGrade.add_grade(2, 1, 1, 8)
    srvGrade.add_grade(3, 1, 6, 9)
    srvGrade.add_grade(4, 2, 2, 2)
    srvGrade.add_grade(9, 3, 2, 2)
    srvGrade.add_grade(5, 2, 3, 4)
    srvGrade.add_grade(6, 3, 6, 5)
    srvGrade.add_grade(7, 3, 7, 7)
    srvGrade.add_grade(8, 3, 8, 8)'''
    cons=UI(srvStudent,srvDiscipline,srvGrade,srvUndo)
    cons.run()
       
