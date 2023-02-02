try:
    import random
    import datetime
    import smtplib


    class cafe():

        def cream_shakes(self):
            bill_no = random.randint(999,9999)      #creating bill no
            time = datetime.datetime.now()          #print live time
            print("you select cream shakes")
            print("List of cream shakes and price\n1) vanilla\t\tRS:- 50\n2) pista\t\tRS:- 50\n3) dry fruit shake\tRS:- 100\n4) return on main manu")
            choice = int(input("enter your choice sir [1/2/3/4]:- "))
            if choice == 1 :
                vanilla = 50
                order =("your order is vanilla shake")
                print(order)
                print("your order ready in 20 min")
                quntity = int(input("enter your quntity[1/2/3/4..etc]:- "))
                bill = quntity*vanilla
                print(f"your bill is :- {bill}")
                file = open(f"{bill_no}.txt",mode="w",encoding="utf-8")
                file.write(f"\nEAT MORE\ntime = {time}\nyour order is :- {order}\nquntity :- {quntity}\ntotal bill :- {bill}\n Thank to visit us ('~')")
            elif choice == 2 :
                pista = 50
                order =("your order is pista shake")
                print(order)
                print("your order ready in 20 min")
                quntity = int(input("enter your quntity[1/2/3/4..etc]:- "))
                bill = quntity*pista
                print(f"your bill is :- {bill}")
                file = open(f"{bill_no}.txt",mode="w",encoding="utf-8")
                file.write(f"\nEAT MORE\ntime = {time}\nyour order is :- {order}\nquntity :- {quntity}\ntotal bill :- {bill}\n Thank to visit us ('~')")
            elif choice == 3 :
                dry_fruit_shake = 100
                order =("your order is dry fruit shake")
                print(order)
                print("your order ready in 20 min")
                quntity = int(input("enter your quntity[1/2/3/4..etc]:- "))
                bill = quntity*dry_fruit_shake
                print(f"your bill is :- {bill}")
                file = open(f"{bill_no}.txt",mode="w",encoding="utf-8")
                file.write(f"\nEAT MORE\ntime = {time}\nyour order is :- {order}\nquntity :- {quntity}\ntotal bill :- {bill}\n Thank to visit us ('~')")   

        def pizzs(self):
            bill_no = random.randint(999,9999)
            time = datetime.datetime.now()
            print("you select pizzs ")
            print("List of pizzs and price\n1) chocolate pizza\t\tRS:- 130\n2) veg. cheese pizza\t\tRS:- 150\n3) paneer pizza\t\t\tRS:- 150\n4) return on main manu")
            choice = int(input("enter your choice sir [1/2/3/4] :- "))
            if choice == 1 :
                chocolate_pizza = 130
                order = ("your order is chocolate pizza")
                print(order)
                print("your order ready in 30 min")
                quntity = int(input("enter your quntity[1/2/3/4..etc]:- "))
                bill = quntity*chocolate_pizza
                print(f"your bill is :- {bill}")
                file = open(f"{bill_no}.txt",mode="w",encoding="utf-8")
                file.write(f"\nEAT MORE\ntime = {time}\nyour order is :- {order}\nquntity :- {quntity}\ntotal bill :- {bill}\n Thank to visit us ('~')")
            elif choice == 2 :
                veg_cheese_pizza = 150
                order = ("your order is veg. cheese pizza")
                print(order)
                print("your order ready in 35 min")
                quntity = int(input("enter your quntity[1/2/3/4..etc]:- "))
                bill = quntity*veg_cheese_pizza
                print(f"your bill is :- {bill}")
                file = open(f"{bill_no}.txt",mode="w",encoding="utf-8")
                file.write(f"\nEAT MORE\ntime = {time}\nyour order is :- {order}\nquntity :- {quntity}\ntotal bill :- {bill}\n Thank to visit us ('~')")
            elif choice == 3 :
                paneer_pizza = 150
                order = ("your order is paneer pizza")
                print(order)
                print("your order ready in 25 min")
                quntity = int(input("enter your quntity[1/2/3/4..etc]:- "))
                bill = quntity*paneer_pizza
                print(f"your bill is :- {bill}")
                file = open(f"{bill_no}.txt",mode="w",encoding="utf-8")
                file.write(f"\nEAT MORE\ntime = {time}\nyour order is :- {order}\nquntity :- {quntity}\ntotal bill :- {bill}\n Thank to visit us ('~')")
            
        def exit(self):
            print("thank you sir/mam visit us")
            print("see soon ('~')")       

    while (True):

        cafe_name = "Eat more"
        cafe_name.capitalize()
        print(cafe_name.center(50))
        print("welcome our cafe place your order sir/mam we proved 100% veg food and deliver food accurate time")
        print("1) shakes")
        print("2) pizzs")
        print("3) exit")


        choice = int(input("Enter your choice [1/2/3] :- "))
        if choice == 1 :
            cafe.cream_shakes(cafe)
        elif choice == 2 :
            cafe.pizzs(cafe)
        elif choice == 3 :
            cafe.exit(cafe)
            break

        #sent bill costmer mail

        c_mailID = str(input("enter your mail ID :- "))
        bill_no = int(input("enter your bill no :- "))
        
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()

        server.login("MAILID","PASSWOLRD")      #enter your cafe mail id and passwolrd
        subject = "EAT MORE CAFE Bill"
        body = f"{bill_no}.txt"
        msg = f"subject:{subject}\n\n{body}"
        server.sendmail("SENDER MAILID",f"{c_mailID}",msg)
        print("bill send on your mail id !!!!!! thank you ('~')")
except BaseException as ex:
    print(ex)
    print("Author :- shubham mane , contact:- maneshubham4033@gmail.com")

finally:
    print("Thank you")    