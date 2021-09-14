print("****************🚗🚗🚗🚗🚗welcome Meru Cab Booking🚗🚗🚗🚗🚗************************")
def Vehicles():
    # took a vehicle named Vrubel
    vehicle=["Bike🚴 ","Auto🛺 ","Car mini🚗","Car Prime🚓"]
    print("vehicles: ")
    # used for loop
    for i in range(len(vehicle)):
        print(i+1," ", vehicle[i])
        # took a user
    select_vehicles=int(input("Select vehicle option🧭: "))
    return select_vehicles
def Drivers():
    Name=["Aman","Rajesh","Chetan","Bhavesh"]
    Phone=[9878127656,8798657687,8798656754,7685323120]
    Rating=[7,8,7,9]

    for i in range(len(Name)):
       print( i+1,"Driver name: ", Name[i])
       print("   Phone number: ",Phone[i])
       print("   Rating of Driver: ",Rating[i])
    select_driver=input("   Enter driver option: ")
    
    
def fare(km,vehicle_option):
    Rate=[8,10,11,15]
    fare=km*Rate[vehicle_option-1]

    print("Your total fare is: ", fare)
    Earning=[0,0,0,0]
    Earning.insert(vehicle_option,fare)


def payment():
    payment=["cash","UPI"]
    print("Payment modes: ")
    for i in range(len(payment)):
        print(i+1," ",payment[i]) 
    option=int(input("Enter payment option: "))
    payment_mode=payment[option-1]
    return payment_mode

   
current_location=input("enter your current location🌍: ")
dropping_point=input("enter your dropping point📍: ")
vehicle_option=Vehicles()
print(vehicle_option)
Drivers()


import random
km=random.randint(1,50)
print("Your location distance is: " ,km)
fare(km,vehicle_option)

confirmation=input("Confirm your booking enter y or n : ")
if confirmation=="y":
    import random
    otp=random.randint(1000,2000)
    print("Your otp is: ",otp)
    print("share it with Driver")
    cancellation=input("Do you want to cancel ride enter y or n: ")
    if cancellation=="n":
        payment_mode=payment()
        print("Your payment mode is: ", payment_mode)
        transaction=input("Transaction done? Enter y or n : ")
        if transaction=="y":
            print("Ok done!!")
            
            feedback=int(input("enter rating from 1 to 10: "))
            Rating=[7,8,7,9]
            New_rating=(Rating[vehicle_option-1]+feedback)/2
            
            Rating.insert(Rating[vehicle_option-1],New_rating)
            print("Drivers new Rating is: ",New_rating)
            print("Thank you, visit again")

        
        else:
            print("Not done, try again🥴.")
    else:
        print("Thank you for visiting our app🙏")

else:
    print("Thank you for visiting our app🙏")