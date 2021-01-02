
from errors.exception import ValidError



class ValidatorDiscipline(object):
    
    
    def __init__(self):
        pass
    
    def validateDiscipline(self,discipline):
        errors=""
        if discipline.get_idd() < 0:
            errors+="invalid  id\n"
        if discipline.get_name()=="":
            errors += "invalid name!\n"
        if len(errors)>0 :
            raise ValidError(errors)

class ValidatorGrade(object):
    
    
    def __init__(self):
        pass
    
    
    def validateGrade(self,grade):
        errors = ""
        if grade.get_idg()<0:
            errors+="invalid  id\n"
        if grade.get_grade()<0:
            errors+="invalid grade\n"
        if len(errors)>0 :
            raise ValidError(errors)
    
                


class ValidatorStudent(object):
    
    
    def __init__(self):
        pass
    
    def validateStudent(self,st):
        errors=""
        if st.getIds() < 0:
            errors+="invalid  id\n"
        if st.getName()=="":
            errors += "invalid name!\n"
        if len(errors)>0 :
            raise ValidError(errors)
        
        
   
 
    
    
    
    




