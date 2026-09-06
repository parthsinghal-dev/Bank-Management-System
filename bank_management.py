from datetime import datetime
while True:
    choice=input("admin/user/exit")
    if choice.lower()=="admin":
        #admin panel
        print("1.remove user")
        print("2.add user")
        print("3.add admin")
        print("4.remove admin")
        print("5.update user")
        print("6.transaction")
        print("7.see details")
        print("8.menu")
        ch=int(input("enter your choice"))
        n1=int(input("enter admin id"))
        password=input("enter admin password")
        if n1 in data and data[n1]["password"]== password:
            if ch==1:
                rem=int(input("enter id  to remove"))
                if rem in data1:
                    data1.pop(rem)
                    print("successfully removed")
                else:
                    print("invalid data")
            elif ch==2:
                transaction=[]
                user_id= max(data1) + 1
                name=input("enter name")
                address=input("enter address")
                ph_no=input("enter ph no")
                initial_balance=int(input("enter balace commence"))
                password=input("enter password for future login")
                data1[user_id]={"name":name,"address":address,"ph_no":ph_no,"balance":initial_balance,"password":password,"transaction":transaction}
                print("user successfylly added")
            elif ch==3:
                name=input("enter name admin")
                address=input("enter address")
                ph_no=input("enter ph no")
                password=input("enter password for future login")
                admin_id= max(data) + 1
                data[admin_id]={"name":name,"address":address,"ph_no":ph_no,"password":password}
                print("admin successfylly added")
            elif ch==4:
                n=int(input("enter admin id to remove"))
                if n in data:
                    data.pop(n)
                    print("admin successfylly removed")
                else:
                    print("please enter valid data")
            elif ch==5:
                n=int(input("enter user id to update"))
                if n in data1:
                    print("what you want to update!")
                    print("1 name")
                    print("2 address")
                    print("3 ph no")
                    choose=int(input("enter your choice"))
                    if choose==1:
                        name=input("new name")
                        data1[n]["name"]= name
                        print("user name successfylly updated")
                    elif choose==2:
                        address=input("new address")
                        data1[n]["address"]= address
                        print("user address successfylly updated")
                    elif choose==3:
                        ph_no= input("new ph no.")
                        data1[n]["ph_no"]= ph_no
                        print("user phone no. successfylly updated")
                    else:
                        print("please enter valid data!")
                else:
                    print("please enter valid data!")
            elif ch==6:
                n=int(input("enter user id to see transaction"))
                if n in data1:
                    print("transaction: ",data1[n]["transaction"])
                else:
                    print("please enter valid data")
            elif ch==7:
                n=int(input("enter user id to see details"))
                if n in data1:
                    print("details: ",data1[n])
                else:
                    print('please enter valid data')
            elif ch==8:
                continue
            else:
                print("invalid data found")
        else:
            print("invalid data")
    elif choice.lower()=="user":
        n=int(input("enter user id"))
        password=input("enter password")
        if n in data1 and data1[n]["password"]== password:
            #user panel
            print("1.withdraw")
            print("2.deposit")
            print("3.transaction")
            print("4.details")
            print("5.balance")
            print("6.transfer")
            print("7.change password")
            print("8.menu")
            ch=int(input("enter your choice"))
            if ch==1:
                amt=int(input("amount to withdraw"))
                if data1[n]["balance"] >= amt and amt>0:
                    data1[n]["balance"]= data1[n]["balance"] - amt
                    transaction_record= {"type":"withdraw", "amount":amt, "balance":data1[n]["balance"], "date_time": datetime.now().strftime("%D %H:%M:%S")}
                    data1[n]["transaction"].append(transaction_record)
                    print("amount successfuly withdrawed")
                    print("remaining balance: ",data1[n]["balance"])
                else:
                    print("balance can't be negative")
            elif ch==2:
                amt=int(input("amount to deposit"))
                if amt>0:
                    data1[n]["balance"]= data1[n]["balance"] + amt
                    transaction_record= {"type":"deposit", "amount":amt, "balance":data1[n]["balance"], "date_time": datetime.now().strftime("%D %H:%M:%S")}
                    data1[n]["transaction"].append(transaction_record)
                    print("amount successfuly deposit")
                    print("balance: ",data1[n]["balance"])
                else:
                    print("make positive value")
            elif ch==3:
                print("transaction ",data1[n]["transaction"])
            elif ch==4:
                print("details ",data1[n])
            elif ch==5:
                print("balance: ",data1[n]["balance"])
            elif ch==6:
                amt1= int(input("enter amounnt to transfer"))
                n1=int(input("enter id to which you want to transfer"))
                if n1 in data1 and data1[n]["balance"] >= amt1 and n1 != n and amt1>0:
                    data1[n1]["balance"]= data1[n1]["balance"] + amt1
                    transaction_record= {"type":"deposit", "amount":amt1, "balance":data1[n1]["balance"], "date_time": datetime.now().strftime("%D %H:%M:%S")}
                    data1[n1]["transaction"].append(transaction_record)
                    data1[n]["balance"]= data1[n]["balance"] -  amt1
                    transaction_record= {"type":"withdraw", "amount":amt1, "balance":data1[n]["balance"], "date_time": datetime.now().strftime("%D %H:%M:%S")}
                    data1[n]["transaction"].append(transaction_record)
                    print("balance: ",data1[n]["balance"])
                    print("balance: ",data1[n1]["balance"])
                else:
                    print("invalid data")
            elif ch==7:
                p=input("enter new password")
                data1[n]["password"]= p
                print("password successfully changed")
            elif ch==8:
                continue
            else:
                print("invalid data found")
        else:
            print("either pass/id invalid")
    elif choice.lower()=="exit":
        print("thanks for visiting!")
        exit()
    else:
        print("please enter valid data.")