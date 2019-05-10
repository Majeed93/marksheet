Islamiat = int(print("Enter your Islamiat marks"))
Urdu = int(print("Enter your Urdu marks"))
Mathematics = int(print("Enter your Mathematics marks"))
Physics = int(print("Enter your Physics marks"))
English = int(print("Enter your English marks"))
marks = (Islamiat+Urdu+Mathematics+Physics+English)/5
if(marks>=80):
    print("Grade:A1")

elif(marks>=70):
    print("Grade:A")

elif(marks>=60):
    print("Grade:B")

elif(marks>=50):
    print("Grade:C")

elif(marks>=40):
    print("Grade:D")   

else:
    print("Fail")             

