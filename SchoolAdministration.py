import csv
def write_into_csv(std_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Phone Number","E-mail ID"])
        writer.writerow(std_list)


if __name__=='__main__':
    i=1
    while True:
        std_info=input("Enter student #{} information in the format (Name Age Phone Number E-mail ID):".format(i))
        std_info_list=std_info.split(' ')

        print("The entered student details is:\nName:",std_info_list[0],"\nAge:",std_info_list[1],"\nPhone Number:",std_info_list[2],"\nE-mail ID:",std_info_list[3])
        check_correct=input("Enter (yes/no) if the entered input is right:")

        if check_correct.lower()=="yes":
            write_into_csv(std_info_list)
            check_next=input("Enter (yes/no) if you want to enter next student information:")
            if check_next.lower()=="yes":
                i+=1
                continue
            elif check_next.lower()=="no":
                break
        elif check_correct.lower()=="no":
            print("Please re-enter the values.")