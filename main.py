from replit import clear
from art import logo
print(logo)

bid_max = {}

bid_start = True
while bid_start:
  
   name= input("What's your name? ")
   bid_price = int(input("What's your Bid Price? \n $"))


   bid_max[name] = bid_price
   

   other_bid = input("Are they other users who want to bid? Type 'Yes' to contunie or 'No' to exit ")
   if other_bid == "Yes":
        clear()

   else:
     max = 0
     winner = ''
     for  value in bid_max :
         bidder_amount = bid_max[value]
         if bidder_amount > max :
          max= bidder_amount
          winner = value
    
     print(f" The winner is {winner} with a bid of ${max}")
     bid_start = False
          

    


