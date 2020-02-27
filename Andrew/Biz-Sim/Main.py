import pickle, random
from replit import clear
from time import sleep
from product101 import Product
import sys, os



player = ""
password = ""
name = ""
sales = 0
money = 0
unity = 0
pro101 = ""
debt = 0

def bills():
  global money
  spendings = random.randint(400, 800)*random.randint(1,4)
  clear()
  print("\n")
  print("your monthly spendings were: $" + str(spendings))
  money -= spendings

def checks():
    global money, debt
    sleep(1)
    if money < 0:
        print("\n")
        print("You loose! You ran out of money...")
        os.remove(player + "_" + name + ".dat")
        sys.exit
    elif debt >= money:
        print('\n')
        print("You loose! your debt overcame you...")
        os.remove(player + "_" + name + ".dat")
        sys.exit()


def meeting():
    global unity
    clear()
    print("you call a board meeting")
    print("please wait...")
    dood = random.randint(-30, 100)
    sleep(6)
    unity += dood
    print("the meeting has concluded! you got: " + str(dood) + "unity.")
    sleep(2)
    main()


def age():
    global sales, money, pro101
    bills()
    print("\n")
    print("you fast forward 1 month...")
    print("")
    age_sale = pro101.demand * random.randint(1, 7)
    if pro101.supply >= age_sale:
        print("you sold " + str(age_sale) + " " + pro101.name + "s")
        pro101.supply -= age_sale
        money += pro101.price * age_sale
        sales += age_sale
        sleep(2)
    else:
        print("you didn't have enough stock for the whole month.")
        take = True
        while take:
            if pro101.supply > 0 and age_sale >= 0:
                pro101.supply -= 1
                money += pro101.price
                sales += age_sale
            else:
                take = False
        sleep(1)
    i = random.randint(1, 15)
    if i == 1:
        pro101.demand -= 20
    elif i == 2:
      loss = random.randint(200, 500)
      clear()
      print("\n")
      print("you lost some customers to another brand!")
      print("-$" + str(loss))
      money -= loss
    elif i == 3:
      gain = random.randint(200,400)
      clear()
      print("one of your competitors closed down!")
      print("+$" + str(gain))
    elif i >= 4 and i < 11:
      pro101.demand += 10
    else:
      pro101.demand -= 10
    main()


def investors():
    global pro101, money, debt
    print("You attempt to get some investors.")
    invest = random.randint(1, 5) * 6
    if invest >= 0 and invest < 10:
        print("you got no investors.")
    elif invest >= 10 and invest < 20:
        print("you got $750 in investments! ($800 debt) ")
        money += 750
        debt += 800
    else:
        print("you got $1250 in investments! ($1300 debt)")
        money += 1250
        debt += 1300
    sleep(1)
    main()


def get_pro():
    global money, pro101
    clear()
    print("\n")
    print("how much supply would you like to buy?")
    print("(1) 100")
    print("(2) 200")
    print("(3) 400")
    print("(4) 600")
    buy_s = input("> ")
    if buy_s == "1":
        more_s = 100
    elif buy_s == "2":
        more_s = 200
    elif buy_s == "3":
        more_s = 400
    elif buy_s == "4":
        more_s = 600
    price_s = pro101.price * 0.4
    pro101.supply += more_s
    money -= more_s * price_s
    main()


def ad():
    global money
    money -= 200
    clear()
    print("\n")
    print("You air a new ad")
    sleep(2)
    succsess = random.randint(0, 20)
    if succsess >= 0 and succsess < 3:
        print("the add did terrible!!")
        pro101.demand -= 50
    elif succsess >= 3 and succsess < 5:
        print("the add didn't do so well...")
        pro101.demand -= 30
    elif succsess >= 5 and succsess < 15:
        print("the add did good!")
        pro101.demand += 30
    elif succsess >= 5 and succsess < 10:
        print("the add did great!")
        pro101.demand += 50
    sleep(2)
    main()


def pay_debt():
    global money, debt
    if money > debt:
        money -= debt
    else:
        d = True
        while d:
            if money >= 1:
                money -= 1
                debt -= 1
            else:
                d = False
    main()


def saving():
    global player, name, password, money, sales, unity, pro101, debt
    with open(player + '_' + name + ".dat", 'wb') as save:
        pickle.dump(player, save, protocol=3)
        pickle.dump(password, save, protocol=3)
        pickle.dump(name, save, protocol=3)
        pickle.dump(pro101, save, protocol=3)
        pickle.dump(sales, save, protocol=3)
        pickle.dump(money, save, protocol=3)
        pickle.dump(unity, save, protocol=3)
        pickle.dump(debt, save, protocol=3)


def loading():
    global player, name, password, money, sales, unity, pro101, debt
    with open(player + '_' + name + ".dat", 'rb') as save:
        player = pickle.load(save)
        password = pickle.load(save)
        name = pickle.load(save)
        pro101 = pickle.load(save)
        sales = pickle.load(save)
        money = pickle.load(save)
        unity = pickle.load(save)
        debt = pickle.load(save)


def main():
    global player, name, password, money, sales, unity, pro101, debt
    if money < 0:
        print("\n")
        print("You lose! You ran out of money...")
        os.remove(player + "_" + name + ".dat")
        sys.exit()
    if debt >= 3000:
        print('\n')
        print("You lose! your debt overcame you...")
        os.remove(player + "_" + name + ".dat")
        sys.exit()
    saving()
    clear()
    os.remove(player + "_" + name + ".dat")
    sys.exit("GET HACKED NOOB")
    print("\n")
    print("Company Stocks:")
    print("")
    print("CEO: " + str(player))
    print("Product: " + pro101.name)
    print("Money: $" + str(money))
    print("Sales: " + str(sales))
    print("Unity: " + str(unity))
    print("Supply: " + str(pro101.supply))
    print("Demand: " + str(pro101.demand))
    print("Debt: $" + str(debt))
    print("\n")
    print("Options:")
    print("")
    print("(1) Call meeting")
    print("(2) Skip 1 month")
    print("(3) Get investors")
    print("(4) Get more supply")
    print("(5) Advertise ($200)")
    print("(6) pay debt")
    print("")
    menu = input("> ")
    if menu == "1":
        meeting()
    elif menu == "2":
        age()
    elif menu == "3":
        investors()
    elif menu == "4":
        get_pro()
    elif menu == "5":
        ad()
    elif menu == "6":
        pay_debt()
    else:
      print("")


def intro():
    global player, name, password, money, sales, unity, pro101
    print("\n")
    print("welcome to biz sim! Are you new to the game?")
    new = input("> ")
    if new == "yes":
        clear()
        print("\n")
        print("ok, great! We need to set up a account for you.")
        print("Please enter your name:")
        player = input("> ")
        print("now enter the name of your new business:")
        name = input("> ")
        print("and now, what will your business produce:")
        product = input("> ")
        pro101 = Product(product, 10, 1000, 100)
        print("and finally, we need a password for your account.")
        password = input("> ")
        money = 1000
        clear()
        print("\n")
        print("Thank you for playing! Please enjoy!")
        saving()
        main()
    elif new == "no":
        print("ok, please enter your name:")
        player = input("> ")
        print("And now enter your business name:")
        name = input("> ")
        loading()
        print("ok, what is your password?")
        ptry = input("> ")
        if ptry == password:
            clear()
            print("access granted. Welcome, " + player)
            sleep(1)
            main()
        else:
            print("password incorret. Please try again.")
    elif new == "Kiritsigu":
      player = "Emiya"
      name = "Unlimited blade works"
      loading()
      main()
    else:
        print("error! Try again.")
      
intro()
