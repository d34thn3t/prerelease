dailytotal=0
while 1:

    hour=0
    day=str(input("Enter day of arrival:"))

    while day not in ["Sunday","Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday"]:

        day=str(input("Invalid day!\nEnter valid day:"))

    while hour>23 or hour<8:
    
        print("Disclaimer: No parking is allowed between Midnight and 08:00.")
    
        hour=int(input("Enter hour of arrival(excluding minutes):"))
    
    hours=int(input("Enter number of hours to leave your car:"))

    if day=="Sunday" and hour<16:

        while hours>8:

            print("You have exceeded maximum stay of 8 hours.")

            hours=int(input("Re-enter number of hours to leave your car:"))

    elif day=="Saturday" and hour<16:

        while hours>8:

            print("You have exceeded maximum stay of 8 hours.")

            hours=int(input("Re-enter number of hours to leave your car:"))

    elif hour>=16:

        while hour+hours>24:

            print("You have exceeded maximum stay of until midnight.")

            hours=int(input("Re-enter number of hours to leave your car:"))

    else:

        while hours>2:

            print("You have exceeded maximum stay of 2 hours.")

            hours=int(input("Re-enter number of hours to leave your car:"))
        

    is_fp_number=" "
    evening_hours=0

    while not(is_fp_number=="yes" or is_fp_number=="no"):

        is_fp_number=str(input("Do you have a frequent parking number:"))

    if is_fp_number=="yes":

        fp_dig1=int(input("Enter first digit:"))

        fp_dig2=int(input("Enter second digit:"))

        fp_dig3=int(input("Enter third digit:"))

        fp_dig4=int(input("Enter fourth digit:"))

        check_digit=input("Enter fifth digit:")

        if check_digit=="X":

            check_digit=10

        elif check_digit==0:

            check_digit=11

        dig_sum=int(check_digit)+(fp_dig4*2)+(fp_dig3*3)+(fp_dig2*4)+(fp_dig1*5)

        if dig_sum%11==0:

            print("Frequent parking number is valid.")

            is_fp_number="valid"

        else:

            print("Invalid frequent parking number.")

            is_fp_number="invalid"

    if hour>=16:

        parking_price=hours*2

        if is_fp_number=="valid":

            discount=parking_price/2

            parking_price=parking_price-discount

        print("Price to park is "+str(parking_price))

    elif day=="Sunday":


        if hour+hours>16:

            hours=16-hour

            parking_price=(hours*2)+2

        else:

            parking_price=hours*2

        if is_fp_number=="valid":

            discount=parking_price/10

            parking_price=parking_price-discount

        print("Price to park is "+str(parking_price))

    elif day=="Saturday":

        if hour+hours>16:

            hours=16-hour

            parking_price=(hours*3)+2

        else:

            parking_price=hours*3
            
        if is_fp_number=="valid":

            discount=parking_price/10

            parking_price=parking_price-discount

        print("Price to park is "+str(parking_price))

    else:

        if hour+hours>16:

            hours=16-hour

            parking_price=(hours*10)+2

        else:

            parking_price=hours*10
            
        if is_fp_number=="valid":

            discount=parking_price/10

            parking_price=parking_price-discount

        print("Price to park is "+str(parking_price))

    payment=int(input("Enter amount to pay:"))

    while payment<parking_price:

        payment=int(input("You cannot pay less than the price stated\nPlease enter valid payment:"))

    dailytotal+=payment



        
        

    
    

    
