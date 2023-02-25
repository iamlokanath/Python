# write a pyhon program to find out wheather a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

sub1 = input("Enter the marks of the suject 1: ")
sub2 = input("Enter the marks of the suject 2: ")
sub3 = input("Enter the marks of the suject 3: ")
total = input("Enter the total marks: ")
sub1 = int(sub1)
sub2 = int(sub2)
sub3 = int(sub3)
total = int(total)
Tmark = sub1 + sub2 + sub3
# print(Tmark)
avg = Tmark / total
# print(avg)
Tper = avg * 100
per1 = (sub1 / 100 ) * 100
per2 = (sub2 / 100 ) * 100
per3 = (sub3 / 100 ) * 100
print(Tper)
if (Tper < 40):
    print("Fail")
if (per1 < 33):
    print("Fail in subject1")
if (per2 < 33):
    print("Fail in subject2")
if (per3 < 33):
    print("Fail in subject3")
if(Tper > 40):
    print("Pass")
