s1 = int(input("enter first person's score: "))
s2 = int(input("enter second person's score: "))
s3 = int(input("enter third person's score: "))
def get_grade(s1, s2, s3):
    s = (s1+s2+s3)/3
    if s >=90 and s<=100:
        return 'A'
    if s >=80 and s<=90:
        return 'B'
    if s >=70 and s<=80:
        return 'C'
    if s >=60 and s<=70:
        return 'D'
    else:
        return 'F'
print(get_grade(s1,s2,s3))