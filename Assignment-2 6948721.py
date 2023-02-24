#List of cars and their prices
cars={"Mazda 6":58000,
      "Maclaren":63000,
      "Land Cruiser":75000,
      "Mercedes Benz C63":58500, 
      "Toyota Rush":61000,
      "Bugatti Veyron":78000,
      "Prado V8":52000,
      "Koenigsegg Trevita":380000,
      "Tesla Model 4":62000,
      "Ford 150":75600,
      "Chevrolet Camaro":25950,
      "Citroen C5X":57670,
      "Kia Sportage":70000,
      "Honda Accord":85600,
      "Honda Civic":79900,
      "Mercedes EQE":75950,
      "Lincoln":39000,
      "Jeep Wrangler":69800,
      "lotus Emira":93000000,
      "Hyundai Sonata":86000,
      "Honda Pilot":85000,
      "BMW M4":60975,
      "Highlander":55600,
      "Porche":82200,
      "Rolls Royce":100250,
      "Bugatti Chiron":95000,
      "Lamboghini":84000,
      "Ineos Grenadier":11905, 
      "Hyundai Ioniq 6":41600,
      "VW Jetta":35600,
      "Toyota Hilux":55000,
      "Range Rover Velar":63600,
      "Aston Martin DBR22":75000,
      "Hummer EV":108700,
      "Tundra":45220,
      "G Wagon":89632,
      "Benz S550":85500,
      "Dacia Jogger":25500,
      "Golf 2022":42500}
#Get user input for car name
car_name=input("Enter the car you want")
#Check if car name is in the list of cars available
if car_name in cars:
    #If car name is present,get its price
    car_price=cars[car_name]
    print(f"Tthe price of {car_name}is${car_price}")
else:
    #If car name is not present,inform the user
    print(f"Sorry,{car_name}is not available at the moment")

#https://github.com/cntakyidanquah