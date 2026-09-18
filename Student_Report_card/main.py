student ={}

def get_student_info():
    try:
        try:
            student_ID = input("Enter Student ID:")
            if not student_ID.isnumeric():
                raise Exception ("StudentId must be numeric.") 
        except Exception as e:
            print(e)
            return
        try:
            student_name = input("Enter Student Name:")
            if not student_name.isalpha():
                raise Exception ("Student name must be string.")
        except Exception as e:
            print(e)
            return
        

        print("Please Enter Marks of the below subjects")
        
    
        Python = int(input("Python: "))
        Mathematics = int(input("Mathematics: "))
        English = int(input("English: "))
        Science = int(input("Science: "))
        Computer_Science = int(input("Computer Science: "))
    
        student[student_ID] = {
        "student_ID" : student_ID,
        "student_name": student_name,
        
        "Marks":{
             "math": Mathematics,
             "Python": Python,
             "English": English,
             "science": Science,
             "csc"   : Computer_Science
            }
    }
    
    except ValueError:
        print("Value Error")
    
  
    
    total = get_total(student[student_ID]["Marks"])
    student[student_ID]["total"] = total
    
    average = total/len(student[student_ID]["Marks"])
   
    student[student_ID]["average"] = average
    
    grade = get_grade(average)
    
    student[student_ID]["grade"] = grade
    print(student)
    pass


def get_total(marks):
    total = 0
    for subjects in marks:
        total += (marks.get(subjects))
    
    return total 

def get_grade(average):
    if average in range(90,100):
        return "A"
    elif average in range(80,89):
        return "B"
    elif average in range(70,79):
        return "C"
    elif average in range(60,69):
        return "D"
    else:
        return "F"


def main():
    print("Welcome")
    print("Please Enter the student details")
    get_student_info()
    pass
    

main()