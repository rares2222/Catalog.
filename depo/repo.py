from errors.exception import RepoError



class RepoStudents(object):
    def __init__(self):
        self.__students = []
     

    def add(self,std):
        if std in self.__students:
            raise RepoError("student already exist")
            #return
        self.__students.append(std)
        return std
  
    def update(self,name,ids):
        for i in range(len(self.__students)):
            if self.__students[i].getIds()==ids: 
                x=self.__students[i].getName()
                self.__students[i].setName(name)
                stud=self.__students[i]
                return stud,x
              
             
    def remove(self,ids):
        i=0
        while i<len(self.__students):
            if self.__students[i].getIds()==ids:
                stud=self.__students[i]

                self.__students.remove(self.__students[i])
                i-=1
                return stud
            i+=1
        return self.__students

   
    
    def get_all(self):
        return self.__students[:]
    
    def __len__(self):
        return len(self.__students)
    
    def get_std_by_id(self,ids):
        for std in self.__students:
            if std.getIds()==ids:
                return std           



class RepoDisciplines(object):
    
    
    def __init__(self):
        self.__disciplines=[]
        
    def add(self,discipline):
        if discipline in self.__disciplines:
            raise RepoError("discipline already exist")
            #return
        self.__disciplines.append(discipline)
        return discipline
            
    def get_all(self):
        return self.__disciplines[:]

    def __len__(self):
        return len(self.__disciplines)

    def update(self,name,idd):
        for i in range(len(self.__disciplines)):
            if self.__disciplines[i].get_idd()==idd: 
                x=self.__disciplines[i].get_name()
                self.__disciplines[i].set_name(name)
                dis=self.__disciplines[i]
                return dis,x

    def remove(self,idd):
        i=0
        while i<len(self.__disciplines):
            if self.__disciplines[i].get_idd()==idd:
                dis=self.__disciplines[i]
                self.__disciplines.remove(self.__disciplines[i])
                i-=1
                return dis
            i+=1
        return self.__disciplines
    
    def get_dis_by_id(self,idd):
        for dis in self.__disciplines:
            if dis.get_idd()==idd:
                return dis           
        raise RepoError("elem inexistent")  
    
    
class RepoGrades(object):
    
    def __init__(self):
        self.__grades=[]

    def add(self,grade):
        if grade in self.__grades:
            raise RepoError("grade already exist")
        self.__grades.append(grade)
         
    def get_all(self):
        return self.__grades[:]
                
    def remove_grade(self,idg):
        i=0
        while i<len(self.__grades):
            if self.__grades[i].get_idg()==idg:
                self.__grades.remove(self.__grades[i])
                i-=1
                
            i+=1
        return self.__grades     


