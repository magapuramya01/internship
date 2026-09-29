class InvalidMarksError(Exception):
      pass
def validate_marks(marks):
      if marks<0 or marks>100:
            raise InvalidMarksError("marks must be blw 0 to 100")
      return True
try:
      student_Marks=float(input("Enter marks:"))
      validate_marks(student_Marks)
except ValueError:
      print("enter marks numerical format")
except InvalidMarksError as error:
      print("invalid marks:",error)
else:
      print("marks saved successully")
    