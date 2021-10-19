from tkinter import *
from tkinter import ttk 
from PIL import ImageTk, Image
import sqlite3

root=Tk()
root.geometry('1024x768')
root.configure(bg='#0623ab')
root.iconbitmap('D:\docs\Sjcjcpic.ico')
root.resizable(False,False)
# Title of App 
root.title("SJC APP")
# Header of the Application 
label=Label(root, text="APPLICATION INFO", font=('arial', 20,'bold'),bg="blue",fg="white")
label.pack(side=TOP,fill=X)
label=Label(root, text=" ", font=('arial', 15,'bold'),bg="blue",fg="white")
label.pack(side=BOTTOM,fill=X)
# Image of the sign
image1 = Image.open("D:\docs\Slide2.jpg")
test = ImageTk.PhotoImage(image1)
label1 =Label(image=test)
label1.image = test
# Position image
label1.place(x=0, y=700)


# Connects to the database
conn= sqlite3.connect('dadabase.db')

c=conn.cursor()
'''
# created the table for the database
c.execute("""CREATE TABLE student(
   First_name varchar(50) not null ,
   Middle_name varchar(50) not null,
   Last_name varchar(50) not null,
   Street varchar(50) not null,
   City varchar(50) not null,
   District varchar(50) not null,
   Gender char(1),
   Marital_status varchar(50) not null,
   Date_of_birth Date not null,
   Occupation varchar(50) not null,
   Ethnicity varchar(50) not null,
   Nationality varchar(50) not null,
   Cell_number int(7) not null,
   Email varchar(50) not null   

)""")

c.execute("""CREATE TABLE educationalinfo(
    High_school varchar(50) not null,
    Address varchar(50) not null,
    District varchar(25) not null,
    Department varchar(50) not null

)""")
'''
conn.commit()

conn.close()



#New window
def firstWindow():
    firstWin = Toplevel(root)
    firstWin.title("Student Information")
    firstWin.geometry('900x900')
    firstWin.configure(bg='#0623ab')

    # lable widgets
    fname_label=Label(firstWin, text="First Name",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    fname_label.place(x=30,y=60)

    mname_label=Label(firstWin, text="Middle Name",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    mname_label.place(x=280,y=60)

    lname_label=Label(firstWin, text="Last Name",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    lname_label.place(x=550,y=60)

    street_label=Label(firstWin, text="Street Name",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    street_label.place(x=30,y=100)

    city_label=Label(firstWin, text="City/Town",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    city_label.place(x=280,y=100)

    district_label=Label(firstWin, text="District",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    district_label.place(x=550,y=100)

    '''gender_label=Label(firstWin, text="Gender",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    gender_label.place(x=30,y=140)'''

    clicked = StringVar()
    clicked.set('M')

    drop= OptionMenu(firstWin, clicked, "M", "F")
    drop.place(x=30, y=140)




    marital_label=Label(firstWin, text="Marital Status",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    marital_label.place(x=280,y=140)

    birth_label=Label(firstWin, text="Date of birth",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    birth_label.place(x=30,y=180)

    job_label=Label(firstWin, text="Occupation",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    job_label.place(x=280,y=180)

    ethnicity_label=Label(firstWin, text="Ethnicity",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    ethnicity_label.place(x=30,y=220)

    nationality_label=Label(firstWin, text="Nationality",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    nationality_label.place(x=280,y=220)

    cellNum_label=Label(firstWin, text="Cell Number",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    cellNum_label.place(x=30,y=260)

    email_label=Label(firstWin, text="Email",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    email_label.place(x=280,y=260)

    delete_label=Label(firstWin, text="Delete ID ", font=('arial',13,'bold'), bg='#0623ab', fg='white')
    delete_label.place(x=160, y=340)



    # entry widgets 
    first_name=Entry(firstWin, borderwidth=1, relief="solid")
    first_name.place(x=133,y=60)
    first_name.focus()

    middle_name=Entry(firstWin, borderwidth=1, relief="solid")
    middle_name.place(x=394,y=60)

    last_name=Entry(firstWin, borderwidth=1, relief="solid")
    last_name.place(x=645,y=60)

    street_name=Entry(firstWin, borderwidth=1, relief="solid")
    street_name.place(x=133,y=100)

    city=Entry(firstWin, borderwidth=1, relief="solid")
    city.place(x=394,y=100)

    district=Entry(firstWin, borderwidth=1, relief="solid")
    district.place(x=645,y=100)

    '''gender=Entry(firstWin, borderwidth=1, relief="solid")
    gender.place(x=133,y=140)'''

    marital=Entry(firstWin, borderwidth=1, relief="solid")
    marital.place(x=394,y=140)

    birthday=Entry(firstWin, borderwidth=1, relief="solid")
    birthday.place(x=133,y=180)

    job=Entry(firstWin, borderwidth=1, relief="solid")
    job.place(x=394,y=180)

    ethnicity=Entry(firstWin, borderwidth=1, relief='solid')
    ethnicity.place(x=133,y=220)

    nationality=Entry(firstWin, borderwidth=1, relief="solid")
    nationality.place(x=394,y=220)

    cellNum=Entry(firstWin, borderwidth=1, relief="solid")
    cellNum.place(x=133,y=260)

    email=Entry(firstWin, borderwidth=1, relief="solid")
    email.place(x=394,y=260)

    delete=Entry(firstWin, borderwidth=1, relief="solid")
    delete.place(x=290, y=340)


    # shows the info in the database
    def query():
        conn= sqlite3.connect('dadabase.db')

        c=conn.cursor()
        c.execute("SELECT *, oid FROM student")
        records = c.fetchall()
        print_records=''

        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[6])+ " " + "\t "+ str(record[14])+ "\n"

        query_label = Label(firstWin, text=print_records, borderwidth=1, relief="solid", bg='#0623ab', fg='white')
        query_label.place(x=340, y=380)
        conn.commit()
        conn.close()

    def savedata():
        conn= sqlite3.connect('dadabase.db')

        c=conn.cursor()
        #inserts the data into the database
        c.execute("INSERT INTO student VALUES (:First_name,:Middle_name, :Last_name, :Street_name, :City, :District, :Gender, :Date_of_birth, :Job, :Marital_status, :Ethnicity, :Nationality, :Cell_number, :Email) ",
            {
                'First_name' : first_name.get(),
                'Middle_name' : middle_name.get(),
                'Last_name' : last_name.get(),
                'Street_name' : street_name.get(),
                'City' : city.get(),
                'District' : district.get(),
                'Gender' : clicked.get(),
                'Date_of_birth' : birthday.get(),
                'Job' : job.get(),
                'Marital_status' : marital.get(),
                'Ethnicity' : ethnicity.get(),
                'Nationality' : nationality.get(),
                'Cell_number' : cellNum.get(),
                'Email' : email.get()

            })
        #clear the text Boxes
        first_name.delete(0,END) 
        middle_name.delete(0, END)
        last_name.delete(0, END)
        street_name.delete(0, END)
        city.delete(0, END)
        district.delete(0, END)
        birthday.delete(0, END)
        job.delete(0, END)
        marital.delete(0, END)
        ethnicity.delete(0, END)
        nationality.delete(0, END)
        cellNum.delete(0, END)
        email.delete(0, END)
        
        conn.commit()

        conn.close()

    # create funtion to delete 
    def id_delete():
        conn= sqlite3.connect('dadabase.db')

        c=conn.cursor()
        
        c.execute("DELETE from student WHERE oid = " + delete.get())

        delete.delete(0, END)
        

        conn.commit()

        conn.close()



    # Buttons for saving and seeing records 
    btn=Button(firstWin, text='Save Data',font=('arial',13,'bold'), borderwidth=1, relief="raised", activebackground="blue", command=savedata)
    btn.place(x=30,y=300, width=120, height=20)

    btn2=Button(firstWin, text="Show Records", font=('arial',13,'bold'), borderwidth=1, relief="raised", activebackground="red", command=query)
    btn2.place(x=160, y=300, width=120, height=20)

    # Delete button
    btn3=Button(firstWin, text="Delete Record", font=('arial',13,'bold'), borderwidth=1, relief="raised", activebackground="red", command=id_delete)
    btn3.place(x=290, y=300, width=120, height=20)

    conn.commit()


    conn.close()


#button for First New Window
but = Button(root, text ="Student Informtion", font=('arial',15,'bold'), command=firstWindow)
but.place(x=60, y=60, width=200, height=40)


#New window
def secondWindow():
    secWin = Toplevel(root)
    secWin.title("Student Information")
    secWin.geometry('900x900')
    secWin.configure(bg='#0623ab')

    # lable widgets
    highs_label=Label(secWin, text="High School",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    highs_label.place(x=30,y=60)

    address_label=Label(secWin, text="Address",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    address_label.place(x=350,y=60)

    dist=Label(secWin, text="District",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    dist.place(x=580,y=60)

    dept=Label(secWin, text="Choose your preferred Department",font=('arial',13,'bold'), bg='#0623ab', fg='white')
    dept.place(x=30,y=100)

    delete_label=Label(secWin, text="Delete ID ", font=('arial',13,'bold'), bg='#0623ab', fg='white')
    delete_label.place(x=160, y=330)

    # entry widgets 
    highs_name=Entry(secWin, borderwidth=1, relief="solid", width=33)
    highs_name.place(x=130,y=60)
    highs_name.focus()

    address_name=Entry(secWin, borderwidth=1, relief="solid")
    address_name.place(x=425,y=60)

    dist_name=Entry(secWin, borderwidth=1, relief="solid")
    dist_name.place(x=645,y=60)

    dept=Entry(secWin, borderwidth=1, relief="solid")
    dept.place(x=335,y=100)

    delete=Entry(secWin, borderwidth=1, relief="solid")
    delete.place(x=290, y=330)


    # shows the info in the database
    def query():
        conn= sqlite3.connect('dadabase.db')

        c=conn.cursor()
        c.execute("SELECT *, oid FROM educationalinfo")
        records = c.fetchall()
        print_records=''

        for record in records:
            print_records += str(record[0]) + " " + str(record[2]) + " " + "\t "+ str(record[3])+ "\n"

        query_label = Label(secWin, text=print_records, borderwidth=1, relief="solid", bg='#0623ab', fg='white')
        query_label.place(x=290, y=380)
        conn.commit()
        conn.close()

    def savedata():
        conn= sqlite3.connect('dadabase.db')

        c=conn.cursor()
        #inserts the data into the database
        c.execute("INSERT INTO educationalinfo VALUES (:High_school, :Address, :District, :Department) ",
            {
                'High_school' : highs_name.get(),
                'Address' : address_name.get(),
                'District' : dist_name.get(),
                'Department' : dept.get()
                
            })
        #clear the text Boxes
        highs_name.delete(0,END) 
        address_name.delete(0, END)
        dist_name.delete(0, END)
        dept.delete(0, END)
        
        
        conn.commit()

        conn.close()

    # create funtion to delete 
    def id_delete():
        conn= sqlite3.connect('dadabase.db')

        c=conn.cursor()
        
        c.execute("DELETE from educationalinfo WHERE oid = " + delete.get())

        delete.delete(0, END)
        

        conn.commit()

        conn.close()



    # Buttons for saving and seeing records 
    btn=Button(secWin, text='Save Data',font=('arial',13,'bold'), borderwidth=1, relief="raised", activebackground="blue", command=savedata)
    btn.place(x=30,y=300, width=120, height=20)

    btn2=Button(secWin, text="Show Records", font=('arial',13,'bold'), borderwidth=1, relief="raised", activebackground="red", command=query)
    btn2.place(x=160, y=300, width=120, height=20)

    # Delete button
    btn3=Button(secWin, text="Delete Record", font=('arial',13,'bold'), borderwidth=1, relief="raised", activebackground="red", command=id_delete)
    btn3.place(x=290, y=300, width=120, height=20)

    conn.commit()


    conn.close()


#button for First New Window
but = Button(root, text ="Educational Informtion", font=('arial',15,'bold'), command=secondWindow)
but.place(x=300, y=60, width=230, height=40)





root.mainloop()
