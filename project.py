import smtplib
import  mysql.connector
#default configuration
mydb=mysql.connector.connect(
user="root",
host="localhost",
password="12345",
database="hospital")
 #connection
connection=mydb.cursor()
#view ()
def view():
    connection.execute("select * from patient")
    myresult=connection.fetchall()
    for i in myresult:
        print(f"patients data{i}")
 #update()       
def update():
    try:
        
        id=input("Enter Id U Want To Update:")
        q="select * from patient where id='{}'".format(id)
        connection.execute(q)

        row=connection.fetchone()
                    
        if(row==None):
            print("Not Found")
        else:
            print("id:",row[0])
            print("1]name:", row[1])
            print("2]age:", row[2])
            print("3]dob:", row[3])
            print("4]phno:", row[4])
            print("5]adharno:", row[5])
            print("6]mail:", row[6])
            print("7]dose1:", row[7])
            print("8]dose2:", row[8])
            print("9]Exit")
        ch=input("Which Field U Want to Edit?")
        pat=""
        if(ch=="1"):
            nn=input("Enter New Name:")
            pat="fname='{}'".format(nn)
        elif(ch=="2"):
            na=input("Enter New age:")
            pat="age='{}'".format(na)
        elif (ch == "3"):
            ndo = input("Enter New dob:")
            pat = "dob='{}'".format(ndo)
        elif (ch == "4"):
            np = input("Enter New phno:")
            pat = "phno='{}'".format(np)
        elif (ch == "5"):
            nad = input("Enter New adharno:")
            pat = "adharno='{}'".format(nad)
        elif (ch == "6"):
            nm = input("Enter New mail:")
            pat = "mail='{}'".format(nm)
        elif (ch == "7"):
            fc =input("Enter completed or not:")
            pat = "dose1='{}'".format(fc)
        elif (ch == "8"):
            sc = input("Enter completed or not:")
            pat = "dose2='{}'".format(sc)
        elif(ch=='9'):
            print("Exit")
        else:
            print("Invalid Option")
        if(not pat==''):
                q="update patient set {} where id='{}'".format(pat,id)
                print(q)
                connection.execute(q)
                mydb.commit()
                print("Record Updated")
                update()
        connection.close()
    except Exception as e:
        print("Error:",e)
update()
def delete():
    print("which data u want to delete")
        
def admin():
    print("*********welcome to admin portal")
    print("press 1 for view data:")
    print("press 2 for update data:")
    print("press 3 for delete the data:")
    operation=int(input("enter any one operation:"))
    if operation==1:
            view()
    if operation==2:
            update()
    else:
        print("enter the correct option")       

    def user():
        sql="insert into patient(id,name,age,dob,adharno,phno,mail,dose1,dose2) value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print("*********register your data*******")
        id=int(input("enter your id:"))
        name=(input("enter your name:"))
        age=int(input("enter your age:"))
        dob=(input("enter your date of birth:"))
        adharno=(input("enter your adharno:"))
        phno=int(input("enter your phone number:"))
        mail=(input("enter your  mail:"))
        dose1=(input("enter completed if u complete dose1 :"))
        dose2=(input("enter completed if u complete dose2 :"))
        value=(id,name,age,dob,adharno,phno,mail,dose1,dose2)
        connection.execute(sql,value)
        mydb.commit()#save the data
        print("your data has been saved in the database")
        #************send mail************
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com',587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login("k.soodappancse2002@gmail.com", "jghvkphbpqurhmny")
        # message to be sent
        message =(f"greetings mr/mrs{name},your vaccination datails are updated successfully.")
        # sending the mail
        s.sendmail(f"k.soodappancse2002@gmail.com",{mail},message)
        print("your mail is sent")
        # terminating the session
        s.quit()
        print("your data hasbeen inserted")
        reenter=(input(" do u want to entry another data press yes:"))
        if reenter=="yes":
            user()
        else:
            print("thank you")    
    
    
      
def again():
    print("*****welcome to COVID-19 database******")
    print("1.user")
    print("2.admin")
    choose=int(input("enter the option:"))
    if choose==1:
        print("*********welcome to admin portal")
        print("press 1 for view data:")
        print("press 2 for update data:")
        print("press 3 for delete the data:")
        operation=int(input("enter any one operation:"))
        if operation==1:
            connection.execute("select * from patient")
            myresult=connection.fetchall()
        for i in myresult:
            print(f"patients data{i}")
        if operation==2:
            update()
        else:
            print("enter the correct option")
