import sqlite3
import math
from datetime import datetime, timedelta
def bookshelf():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    n=int(input("Enter Bookshelf Number "))
    code="bookshelf"+str(n)
    c.execute('''CREATE TABLE IF NOT EXISTS {}
             (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Author TEXT, Year INTEGER, Pages INTEGER, Quantity INTEGER, Price INTEGER)'''.format(code))
    conn.commit()
    conn.close()
    librarysettings()
def addbooks():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    name = input("Enter the name of the book: ")
    author = input("Enter the name of the author: ")
    year = input("Enter the year of publishing: ")
    pages = input("Enter the number of pages: ")
    quantity=input("Enter the number of books: ")
    price = input("Enter the price of the book: ")
    n=int(input("Enter Bookshelf Number "))
    code="bookshelf"+str(n)
    c.execute("INSERT INTO {} (Name, Author, Year, Pages, Quantity, Price) VALUES (?, ?, ?, ?, ?, ?)".format(code), (name, author, year, pages, quantity, price))
    conn.commit()
    conn.close()
    librarysettings()
def displayshelf():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    n=int(input("Enter Bookshelf Number "))
    code="bookshelf"+str(n)
    c.execute("SELECT * FROM {}".format(code))
    for row in c:
        print(row)
    c.close()
    conn.close()
    librarysettings()
def deletebooks():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    n=int(input("Enter Bookshelf Number "))
    code="bookshelf"+str(n)
    c.execute("SELECT * FROM {}".format(code))
    for row in c:
        print(row)
    id=int(input("Enter the id of the book you want to delete: "))
    c.execute("DELETE FROM {} WHERE id = ?".format(code), (id,))
    conn.commit()
    conn.close()
    librarysettings()
def displayall():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    n=1
    try:
        while True:
         code="bookshelf"+str(n)
         c.execute("SELECT * FROM {}".format(code))
         for row in c:
            print(row)
         n=n+1
    except sqlite3.OperationalError:
        c.close()
        conn.close()
    librarysettings()
def searchid():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    n=int(input("Enter Bookshelf Number "))
    code="bookshelf"+str(n)
    id=int(input("Enter the id of the book you want to search: "))
    c.execute("SELECT * FROM {} WHERE id = ?".format(code), (id,))
    for row in c:
        print(row)
    c.close()
    conn.close()
    librarysettings()
def searchname():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    n=1
    name=input("Enter the name of the book you want to search: ")
    while True:
        try:
            f='%'+name+'%'
            code="bookshelf"+str(n)
            c.execute("SELECT * FROM {} WHERE Name LIKE ?".format(code),(f,))
            for row in c:
                print(row)
            n=n+1
        except sqlite3.OperationalError:
            c.close()
            conn.close()
            break
    librarysettings()
def searchauthor():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    n=1
    name=input("Enter the name of the Author you want to search: ")
    while True:
         try:
            f='%'+name+'%'
            code="bookshelf"+str(n)
            c.execute("SELECT * FROM {} WHERE Author LIKE ?".format(code),(f,))
            for row in c:
                print(row)
            n=n+1
         except sqlite3.OperationalError:
            c.close()
            conn.close()
            break 
    librarysettings() 
def updatebook():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    n=int(input("Enter Bookshelf Number "))
    code="bookshelf"+str(n)
    c.execute("SELECT * FROM {}".format(code))
    for row in c:
        print(row)
    id=int(input("Enter the id of the book you want to update: "))
    name = input("Enter the name of the book: ")
    author = input("Enter the name of the author: ")
    year = input("Enter the year of publishing: ")
    pages = input("Enter the number of pages: ")
    quantity=input("Enter the number of books: ")
    price = input("Enter the price of the book: ")
    c.execute("UPDATE {} SET Name = ?, Author = ?, Year = ?, Pages = ?, Quantity = ?, Price = ? WHERE id = ?".format(code), (name, author, year, pages, quantity, price, id))
    c.execute("SELECT * FROM {}".format(code))
    for row in c:
        print(row)
    print("Update Succesful")
    conn.commit()
    conn.close()
    librarysettings()
def deletebookshelf():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    n=int(input("Enter Bookshelf Number "))
    code="bookshelf"+str(n)
    c.execute("DROP TABLE {}".format(code))
    conn.commit()
    conn.close()
    print("Table Deleted")
    librarysettings()
def movebooks():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    n=int(input("Enter Bookshelf Number "))
    code="bookshelf"+str(n)
    c.execute("SELECT * FROM {}".format(code))
    for row in c:
        print(row)
    id=int(input("Enter the id of the book you want to move: "))
    m=int(input("Enter the Bookshelf Number you want to move the book to: "))
    code1="bookshelf"+str(m)
    c.execute("INSERT INTO {} (Name, Author, Year, Pages, Quantity, Price) SELECT Name, Author, Year, Pages, Quantity, Price FROM {} WHERE id=?".format(code1,code),(id,))
    c.execute("DELETE FROM {} WHERE id = ?".format(code), (id,))   
    conn.commit()
    conn.close()
    print("Book Moved")
    librarysettings()
conn=sqlite3.connect('Library.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS customerlst
         (uid INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Address TEXT, Phone INTEGER, Email TEXT)''')
conn.commit()
conn.close()
def addcustomer():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    nam = input("Enter the name of the customer: ")
    address = input("Enter the address of the customer: ")
    phone = input("Enter the phone number of the customer: ")
    email = input("Enter the email of the customer: ")
    c.execute("INSERT INTO customerlst (Name, Address, Phone, Email) VALUES (?, ?, ?, ?)", (nam, address, phone, email))
    c.execute("SELECT * FROM customerlst WHERE (Name,Address,Phone,Email)=(?,?,?,?)", (nam, address, phone, email))
    for row in c:
        uid=row[0]
    print("Your UID is ",uid)
    conn.commit()
    conn.close()
    customersettings()
def addcustomer1():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    name = input("Enter the name of the customer: ")
    address = input("Enter the address of the customer: ")
    phone = input("Enter the phone number of the customer: ")
    email = input("Enter the email of the customer: ")
    c.execute("INSERT INTO customerlst (Name, Address, Phone, Email) VALUES (?, ?, ?, ?)", (name, address, phone, email))
    c.execute("SELECT * FROM customerlst WHERE (Name,Address,Phone,Email)=(?,?,?,?)", (name, address, phone, email))
    for row in c:
        uid=row[0]
    print("Your UID is ",uid)
    conn.commit()
    conn.close()
def displaycustomer():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT * FROM customerlst")
    for row in c:
        print(row)
    conn.close()
    customersettings()
def searchuid():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    uid=input("Enter UID: ")
    c.execute("SELECT * FROM customerlst WHERE uid = ?",(uid,))
    for row in c:
        print(row)
        if row==():
            print("UID not found")
            addcustomer()
        else:
            name=row[1]
            print("UID found")
    conn.close()
    customersettings()
def searchuid1(uid):
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT * FROM customerlst WHERE uid = ?",(uid,))
    for row in c:
        print(row)
        if row==():
            print("UID not found")
            addcustomer()
        else:
            name=row[1]
            print("UID found")
    conn.close()
def searchcustomer():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    name=input("Enter the name of the customer you want to search: ")
    c.execute("SELECT * FROM customerlst WHERE Name = ?",(name,))
    for row in c:
        print(row)
    conn.close()
    customersettings()
def updatecustomer():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT * FROM customerlst")
    for row in c:
        print(row)
    id=int(input("Enter the uid of the customer you want to update: "))
    name = input("Enter the name of the customer: ")
    address = input("Enter the address of the customer: ")
    phone = input("Enter the phone number of the customer: ")
    email = input("Enter the email of the customer: ")
    c.execute("UPDATE customerlst SET Name = ?, Address = ?, Phone = ?, Email = ? WHERE uid = ?", (name, address, phone, email, id))
    c.execute("SELECT * FROM customerlst")
    for row in c:
        print(row)
    print("Update Succesful")
    conn.commit()
    conn.close()
    customersettings()
def deletecustomer():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT * FROM customerlst")
    for row in c:
        print(row)
    id=int(input("Enter the uid of the customer you want to delete: "))
    c.execute("DELETE FROM customerlst WHERE uid = ?", (id,))
    conn.commit()
    conn.close()
    print("Customer Deleted")
    customersettings()
def issuebooks():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    n=int(input("Enter Bookshelf Number "))
    code="bookshelf"+str(n)
    c.execute("SELECT * FROM {}".format(code))
    for row in c:
        print(row)
    id=int(input("Enter the id of the book you want to issue: "))
    uid=input("Enter your UID: ")
    if uid == "":
        addcustomer1()
    else:
        searchuid1(uid)
    c.execute('SELECT Quantity FROM {}'.format(code))
    for row in c:
        q=row[0]
    if q==0:
        print("Book not available")
        booksettings()
    c.execute("SELECT Name FROM customerlst WHERE uid=?",(uid,))
    for row in c:
        nam=row[0]
    date=datetime.now().date()
    date1=date+timedelta(days=7)
    q=date.strftime('%Y-%m-%d')
    q1=date1.strftime('%Y-%m-%d')
    c.execute("SELECT * FROM {} WHERE id=?".format(code),(id,))
    for row in c:
        bookname=row[1]
        bookaut=row[2]
    c.execute("UPDATE {} SET Quantity = Quantity-1 WHERE id = ?".format(code), (id,))
    c.execute("INSERT INTO Borrowedbooks (uid, Name, Bookshelf, Bookid, Book, Author, DateOfIssue, LastDateToReturn) VALUES (?,?,?,?,?,?,?,?)",(uid,nam,code,id,bookname,bookaut,q,q1))
    c.execute("SELECT * FROM Borrowedbooks")
    for row in c:
        r=row[8]
    conn.commit()
    conn.close()
    print("Book Issued")
    print("Receipt No. ",r)
    booksettings()
conn=sqlite3.connect('Library.db')
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS history (ReceiptNo INTEGER PRIMARY KEY, uid INTEGER, CustomerName TEXT, Bookid INTEGER, BookIssued TEXT, BookAuthor TEXT, DateOfIssue DATE, DateOfReturn DATE)")
c.execute("CREATE TABLE IF NOT EXISTS Borrowedbooks (uid INTEGER, Name TEXT, Bookshelf INTEGER, Bookid INTEGER, Book TEXT, Author TEXT, DateOfIssue DATE, LastDateToReturn DATE, ReceiptNo INTEGER PRIMARY KEY AUTOINCREMENT)")
conn.commit()
conn.close()
def viewborrowed():
    conn = sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT * FROM Borrowedbooks")
    for row in c:
        print(row)
    c.close()
    conn.close()
    booksettings()
def fine(o):
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT DateOfIssue FROM Borrowedbooks WHERE ReceiptNo = ?",(o,))
    for row in c:
        d1=row[0]
    n=datetime.strptime(d1,"%Y-%m-%d").date()
    d2=datetime.now().date()
    d=math.fabs((d2-n).days)
    if d>14:
        f=(d-14)*10
        print("Fine is ",f)
    else:
        print("No fine")
        conn.close()
def returnbook():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    o=int(input("Enter the Receipt no. of the book you borrowed: "))
    c.execute("SELECT * FROM Borrowedbooks")
    for row in c:
        if row[8]==o:
            id=row[3]
            uid=row[0]
            name=row[1]
            n=row[2]
            code=str(n)
            book=row[4]
            author=row[5]
            doi=row[6]
            dor=datetime.now().date()
            c.execute("INSERT INTO history (ReceiptNo, uid, CustomerName, Bookid, BookIssued, BookAuthor, DateOfIssue, DateOfReturn) VALUES (?,?,?,?,?,?,?,?)",(o,uid,name,id,book,author,doi,dor))
            c.execute("DELETE FROM Borrowedbooks WHERE ReceiptNo = ?", (o,))
            c.execute("UPDATE {} SET Quantity = Quantity+1 WHERE id = ?".format(code), (id,))
            fine(o)
            print("Book Returned")
        else:
            print("Book not found")
    conn.commit()
    conn.close()
    booksettings()
def searchborroweduid():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    uid=int(input('Enter uid :'))
    c.execute("SELECT * FROM Borrowedbooks WHERE uid = ?",(uid,))
    for row in c:
        print(row)
    conn.close()
    booksettings()
def searchborrowedname():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    name=input("Enter the name of the customer you want to search: ")
    c.execute("SELECT * FROM Borrowedbooks WHERE Name = ?",(name,))
    for row in c:
        print(row)
    conn.close()
    booksettings()
def searchborrowedid():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    id=int(input("Enter the id of the book you want to search: "))
    c.execute("SELECT * FROM Borrowedbooks WHERE Bookid = ?",(id,))
    for row in c:
        print(row)
    conn.close()
    booksettings()
def searchborrowedreturn():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    date=input("Enter the date of return(YYYY-MM-DD) :")
    n=strptime(date,"%Y-%m-%d").date()
    c.execute("SELECT * FROM Borrowedbooks WHERE LastDateToReturn = ?",(date,))
    for row in c:
        print(row)
    conn.close()
    booksettings()
def searchhistory1(uid,date):
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    n=strptime(date,"%Y-%m-%d").date()
    c.execute("SELECT * FROM history WHERE uid = ? AND DateOfIssue = ?",(uid,date))
    for row in c:
        print(row)
    conn.close()
def searchhistory2(uid):
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT * FROM history WHERE uid = ?",(uid,))
    for row in c:
        print(row)
    conn.close()
def searchhistory3(date):
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    n=strptime(date,"%Y-%m-%d").date()
    c.execute("SELECT * FROM history WHERE DateOfIssue = ?",(date,))
    for row in c:
        print(row)
    conn.close()
def searchhistory4(name):
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT * FROM history WHERE CustomerName = ?",(name,))
    for row in c:
        print(row)
    conn.close()
def searchhistory5(name,date):
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    n=strptime(date,"%Y-%m-%d").date()
    c.execute("SELECT * FROM history WHERE CustomerName = ? AND DateOfIssue = ?",(name,date))
    for row in c:
        print(row)
    conn.close()
def searchhistory6(ReceiptNo):
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT * FROM history WHERE ReceiptNo = ?",(ReceiptNo,))
    for row in c:
        print(row)
    conn.close()
def searchhistory():
    o=input('Enter ReceiptNo :')
    uid=input('Enter uid :')
    name=input('Enter name :')
    date=input('Enter date of issue(YYYY-MM-DD) :')
    if len(o)==0:
        if len(uid)!=0 and len(name)==0 and len(date)!=0:
            searchhistory1(uid,date)
        elif len(uid)!=0 and len(name)==0 and len(date)==0:
            searchhistory2(uid)
        elif len(uid)==0 and len(name)==0 and len(date)!=0:
            searchhistory3(date)
        elif len(uid)==0 and len(name)!=0 and len(date)==0:
            searchhistory4(name)
        elif len(uid)==0 and len(name)!=0 and len(date)!=0:
            searchhistory5(name,date)
        if len(uid)!=0 and len(name)!=0 and len(date)==0:
            searchhistory2(uid)
        elif len(uid)!=0 and len(name)!=0 and len(date)!=0:
            searchhistory1(uid,name)
    elif len(o)!=0:
        searchhistory6(o)
    booksettings()
def viewhistory():
    conn=sqlite3.connect('Library.db')
    c=conn.cursor()
    c.execute("SELECT * FROM history")
    for row in c:
        print(row)
    conn.close()
    booksettings()
def booksettings():
    print("\n\n\t1) ISSUE BOOKS")
    print("\t2) RETURN BOOKS")
    print("\t3) VIEW BORROWED BOOKS")
    print("\t4) SEARCH BORROWED LIST")
    print("\t5) VIEW HISTORY")
    print("\t6) SEARCH HISTORY")
    print("\t7) EXIT")
    b=int(input("\tENTER CHOICE: "))
    if b==1:
        issuebooks()
    elif b==2:
        returnbook()
    elif b==3:
        viewborrowed()
    elif b==4:
        print("\n\t1) SEARCH BY UID")
        print("\t2) SEARCH BY NAME")
        print("\t3) SEARCH BY BOOK ID")
        print("\t4) SEARCH BY RETURN DATE")
        q=int(input("\tENTER CHOICE: "))
        if q==1:
            searchborroweduid()
        elif q==2:
            searchborrowedname()
        elif q==3:
            searchborrowedid()
        elif q==4:
            searchborrowedreturn()
    elif b==5:
        viewhistory()
    elif b==6:
        searchhistory()
    elif b==7:
        menu()
def librarysettings():
    print("\n\n\t1) ADD BOOKSHELF")
    print("\t2) DELETE BOOKSHELF")
    print("\t3) ADD BOOKS")
    print("\t4) DISPLAY BOOKS")
    print("\t5) REMOVE BOOKS")
    print("\t6) MODIFY BOOKS")
    print("\t7) SEARCH BOOKS")
    print("\t8) MOVE BOOKS")
    print("\t9) EXIT")
    w=int(input("\tENTER CHOICE: "))  
    if w==1:
        bookshelf()
    elif w==2:
        deletebookshelf()
    elif w==3:
        addbooks()
    elif w==4:
        e=input("\n\tDO YOU WANT ME TO DISPLAY ALL THE BOOKS?(Y/N) ")
        if e=="Y":
            displayall()
        elif e=="N":
            displayshelf()
    elif w==5:
        deletebooks()
    elif w==6:
        updatebook()
    elif w==7:
        print("\n\t1) SEARCH BY ID")
        print("\t2) SEARCH BY NAME")
        print("\t3) SEARCH BY AUTHOR")
        q=int(input("\tENTER CHOICE: "))
        if q==1:
            searchid()
        elif q==2:
            searchname()
        elif q==3:
            searchauthor()
    elif w==8:
        movebooks()
    elif w==9:
        menu()
def customersettings():
    print("\n\n\t1) ADD CUSTOMER")
    print("\t2) DISPLAY CUSTOMER DATABSE")
    print("\t3) SEARCH CUSTOMER")
    print("\t4) UPDATE CUSTOMER DATABASE")
    print("\t5) REMOVE CUSTOMER")
    print("\t6) EXIT")
    r=int(input("\tENTER CHOICE: "))
    if r==1:
        addcustomer()
    elif r==2:
        displaycustomer()
    elif r==3:
        print("\n\t1) SEARCH BY UID")
        print("\t2) SEARCH BY NAME")
        t=int(input("\tENTER CHOICE: "))
        if t==1:
            searchuid()
        elif t==2:
            searchcustomer()
    elif r==4:
        updatecustomer()
    elif r==5:
        deletecustomer()
    elif r==6:
        menu()

def menu():
    print("________________________________________________________________________")
    print("                          ABC SCHOOL LIBRARY                           ")
    print("________________________________________________________________________")
    print("\n\n\t\t\t  HOW CAN I HELP YOU?")
    print("\t\t1) BOOK SETTINGS")
    print("\t\t2) LIBRARY SETTINGS")
    print("\t\t3) CUSTOMER SETTINGS")
    print("\t\t4) EXIT THE PROGRAM")
    a=int(input("\n\t\tENTER CHOICE: "))
    if a==1:
        booksettings()
    elif a==2:
        librarysettings()
    elif a==3:
        customersettings()
    elif a==4:
        exit()
menu()
