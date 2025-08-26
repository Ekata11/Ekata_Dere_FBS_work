## 5sub marks and display grade.. 1st class,2nd clas..

m1 = int(input("Enter Marks of subject 1 :"))
m2 = int(input("Enter Marks of subject 2 :"))
m3 = int(input("Enter Marks of subject 3 :"))
m4 = int(input("Enter Marks of subject 4 :"))
m5 = int(input("Enter Marks of subject 5 :"))
total_marks = (m1+m2+m3 +m4+m5)/ 500 *100

if(total_marks>=75):
    print("Grade:First class")
elif(total_marks>=65):
    print("Grade:Second class")
elif(total_marks>=36):
        print("Grade : Pass")
else:
     print("Fail")
