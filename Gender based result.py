import csv
import numpy as np
from matplotlib import pyplot as plt
def passed(row):
    if(int(row[5])+int(row[6])+int(row[7])<150) or ((int(row[5])<50) or (int(row[6])<50) or (int(row[7])<50)):
        return False 
    return True
def Group_check(row):
        if(row[1]=="group A"):
            group_A.append(row[1])
            if(passed(row)):
                A_passed.append(row[1])
        elif(row[1]=="group B"):
            group_B.append(row[1])
            if(passed(row)):
                B_passed.append(row[1])
        elif(row[1]=="group C"):
            group_C.append(row[1])
            if(passed(row)):
                C_passed.append(row[1])
        elif(row[1]=="group D"):
            group_D.append(row[1])        
            if(passed(row)):
                D_passed.append(row[1])
        elif(row[1]=="group E"):
            group_E.append(row[1])
            if(passed(row)):
                E_passed.append(row[1])
        else:
            pass
def Parental_Education(row):
    pass
filename = 'D:\VS code\.py code\Data Visulization of Students\'s marks based on various factors\kaggle student\'s data\StudentsPerformance.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    male,male_passed=[],[]
    female,female_passed=[],[]
    group_A,group_B,group_C,group_D,group_E=[],[],[],[],[] 
    A_passed,B_passed,C_passed,D_passed,E_passed=[],[],[],[],[]   
    bacholers,college,high_school,masters,associate=[],[],[],[],[]
    for row in reader:
        #print(row[0])   
        Group_check(row)
        if(row[0]=="male"):
            male.append(row[0])
            if passed(row):
                male_passed.append(row[0])
                pass
        elif(row[0]=="female"):
            female.append(row[0])
            if passed(row):
                female_passed.append(row[0])
                pass
def Gender_Based_Result():
        #Bar chart of Students Result based on Data
    barWidth = 0.25
    fig = plt.figure(figsize = (10, 5))
    Total_Students=[len(male),len(female)]
    passed_students=[len(male_passed),len(female_passed)]
    failed_Students=[(len(male)-len(male_passed)),(len(female)-len(female_passed))]
    #X_axis=["Total Male Sutdents","Passed","Failed"]
    #Values=[len(male),len(male_passed),(len(male)-len(male_passed))]

    br1 = np.arange(len(Total_Students))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]

    plt.bar(br1, Total_Students, color ='darkslategrey', width = barWidth,
            edgecolor ='grey', label ='Total Students')
    plt.bar(br2, passed_students, color ='teal', width = barWidth,
            edgecolor ='grey', label ='Passed')
    plt.bar(br3, failed_Students, color ='Aqua', width = barWidth,
            edgecolor ='grey', label ='Failed')

    plt.ylabel("Maximum no. of students")
    plt.xlabel("Gender")

    plt.xticks([r + barWidth for r in range(len(Total_Students))],
            ['Male','Female'])
    plt.title("Comparison of Passed and Failed Students")
    plt.legend()
    plt.show()
################################################################
def Gender_Ratio():
    #PIE CHART of Gender Share

    data=[len(male),len(female)]
    label=["Male","Female"]
    fig = plt.figure(figsize =(10, 7))
    explode = [0, 0.09]

    plt.pie(data,labels=label,explode=explode,shadow=True,autopct='%1.1f%%',
            wedgeprops={'edgecolor': 'grey'})
    plt.title("Ratio of Gender")
    plt.legend()
    plt.show()
#######################################################################
def Group_Ratio():
    data=[len(group_A),len(group_B),len(group_C),len(group_D),len(group_E)]
    label=["Group A","Group B","Group C","Group D","Group E"]
    fig = plt.figure(figsize =(10, 7))
    explode = [0, 0.09,0.09,0.09,0.09]

    plt.pie(data,labels=label,explode=explode,shadow=True,autopct='%1.1f%%',
            wedgeprops={'edgecolor': 'grey'})
    plt.title("Group Ratio")
    plt.legend(bbox_to_anchor=(1, 1))
    plt.show()
####################################################################### 
def Group_Based_Result():
    
    barWidth = 0.25
    fig = plt.figure(figsize = (10, 5))
    Total_Students=[len(group_A),len(group_B),len(group_C),len(group_D),len(group_E)]
    passed_students=[len(A_passed),len(B_passed),len(C_passed),len(D_passed),len(E_passed)]
    failed_Students=[(len(group_A)-len(A_passed)),(len(group_B)-len(B_passed)),(len(group_C)-len(C_passed)),(len(group_D)-len(D_passed)),(len(group_E)-len(E_passed))]
    #X_axis=["Total Male Sutdents","Passed","Failed"]
    #Values=[len(male),len(male_passed),(len(male)-len(male_passed))]

    br1 = np.arange(len(Total_Students))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]

    plt.bar(br1, Total_Students, color ='darkslategrey', width = barWidth,
            edgecolor ='grey', label ='Total Students')
    plt.bar(br2, passed_students, color ='teal', width = barWidth,
            edgecolor ='grey', label ='Passed')
    plt.bar(br3, failed_Students, color ='Aqua', width = barWidth,
            edgecolor ='grey', label ='Failed')

    plt.ylabel("Maximum no. of students")
    plt.xlabel("Group")

    plt.xticks([r + barWidth for r in range(len(Total_Students))],
            ['Group A','Group B','Group C','Group D','Group E'])
    plt.title("Comparison of Passed and Failed Students on Group Basis")
    plt.legend()
    plt.show()
########################################################################
Gender_Ratio()
Gender_Based_Result()
Group_Ratio()
Group_Based_Result()