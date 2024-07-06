
#importing modules

import mysql.connector
from tabulate import tabulate

#password
def pswd():
    ps=input("enter password")
    while ps!="1234":
        pswd()
    
pswd()

#create database and tables

db=input("enter name of your database :")

#connecting to sql
mydb=mysql.connector.connect(host='localhost',user="root",passwd='QWErty')
mycursor=mydb.cursor()

sql="create database if not exists %s"%(db,)
mycursor.execute(sql)
print("Database created...")
mycursor=mydb.cursor()
mycursor.execute("use "+db)
TableName=input("Name of table to be created:")
query="create table if not exists "+TableName+"\
(itemcode int primary key,\
itemname varchar(15) not null,\
itemnos int,\
itemprice int)"
print("table "+TableName+" created successfully...")
mycursor.execute(query)
#menu of program
while True:
    print(75*'*')
    print('\t\t\t\t\tMAIN MENU')
    print('\t\t\t\t\t1. Adding records')
    print('\t\t\t\t\t2.Display record of all items')
    print('\t\t\t\t\t3.Display record of particular item')
    print('\t\t\t\t\t4.Delete record of all items')
    print('\t\t\t\t\t5.Delete record of particular item')
    print('\t\t\t\t\t6.Modification in a record')
    print('\t\t\t\t\t7.Exit')
    print(75*"*")
    print('-----Enter choice: ')
    choice=int(input())

#Adding records
    if choice==1:
        try:
            print('enter item info')
            itemcode=int(input('enter item code'))
            itemname=input('enter item name')
            itemnos=int(input('enter number of item:'))
            itemprice=int(input('item price:'))
            rec=(itemcode,itemname,itemnos,itemprice)
            query="insert into "+TableName+" values(%s,%s,%s,%s)"
            mycursor.execute(query,rec)
            mydb.commit()
            print('record added successfully...')
        except Exception as e:
            print('something went wrong',e)

#display all records
    elif choice==2:
        try:
            query='select* from '+TableName
            mycursor.execute(query)
            print(tabulate(mycursor, headers=['itemcode','name','nos','price'],tablefmt='psql'))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
                print(rec)'''
        except:
            print('something went wrong')

#display particular record
    elif choice==3:
        try:
            en=input('Enter item code of the record to be displayed')
            query="select * from "+TableName+" where itemcode="+en
            print(query)
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\nrecord of item no.:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==1:
                print:('nothing to display')
        except:
            print('something went wrong')

#delete all records
    elif choice==4:
        try:
            ch=input('do you want to delete all records? This can not be undone..(y/n)')
            if ch.upper()=='Y':
                mycursor.execute('delete from '+TableName)
                mydb.commit()
                print('all the records are deleted...')
        except:
            print('Something went wrong')

#delete particular record
    elif choice==5:
        try:
            en=input('enter item no.of the record to be deleted...')
            query='delete from '+TableName+' where itemcode='+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print('deletion done')
            else:
                print('item no: ',en,' not found')
        except:
            print('something went wrong')

#modify record
    elif choice==6:
        try:
            en=input('enter item no. of the record to be modified')
            query='select * from '+TableName+' where itemcode='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print('item no '+en+' does not exist')
            else:
                iname=myrecord[1]
                print('code :',myrecord[0])
                print('name :',myrecord[1])
                print('nos :',myrecord[2])
                print('price :',myrecord[3])
                print('-----------------------')
                print('type value to modify below or just press enter for no change')
                x=input('enter name:')
                if len(x)>0:
                    mname=x
                x=input('enter nos:')
                if len(x)>0:
                    mnos=x
                x=input("enter price:")
                if len(x)>0:
                    mprice=(x)
                query='update '+TableName+' set itemname='+"'"+mname+"'"+','+'itemnos='+"'"+mnos+"'"+','+'itemprice='\
                +mprice+' where itemcode='+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print('record modified')
        except:
            print("something went wrong")

#exit from program
    elif choice==7:
        break
    else:
        print('Wrong choice')
