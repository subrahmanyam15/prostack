# employees = [
#     {"eid": 1, "ename": "John Smith", "gender": "M"},
#     {"eid": 2, "ename": "Sarah Johnson", "gender": "F"},
#     {"eid": 3, "ename": "Michael Brown", "gender": "M"},
#     {"eid": 4, "ename": "Emily Davis", "gender": "F"},
#     {"eid": 5, "ename": "David Wilson", "gender": "M"},
#     {"eid": 6, "ename": "Jessica Martinez", "gender": "F"},
#     {"eid": 7, "ename": "James Anderson", "gender": "M"},
#     {"eid": 8, "ename": "Lisa Taylor", "gender": "F"},
#     {"eid": 9, "ename": "Robert Thomas", "gender": "M"},
#     {"eid": 10, "ename": "Mary Garcia", "gender": "F"},
#     {"eid": 11, "ename": "William Lee", "gender": "M"},
#     {"eid": 12, "ename": "Patricia Rodriguez", "gender": "F"},
#     {"eid": 13, "ename": "Richard Jones", "gender": "M"},
#     {"eid": 14, "ename": "Jennifer White", "gender": "F"},
#     {"eid": 15, "ename": "Joseph Harris", "gender": "M"},
#     {"eid": 16, "ename": "Linda Clark", "gender": "F"},
#     {"eid": 17, "ename": "Charles Lewis", "gender": "M"},
#     {"eid": 18, "ename": "Barbara Walker", "gender": "F"},  
#     {"eid": 19, "ename": "Christopher Hall", "gender": "M"},
#     {"eid": 20, "ename": "Nancy Allen", "gender": "F"}
# ]


# for i in employees:
#     print(i['ename'])

# i=0
# while i<=len(employees)-1:
#     print(employees[i]['ename'])
#     i=i+1










cars=[
 { "brand": "Maruti Suzuki", "model": "Swift", "price": 650000, "color": "Red" },
 { "brand": "Maruti Suzuki", "model": "Baleno", "price": 800000, "color": "Blue" },
 { "brand": "Hyundai", "model": "i20", "price": 900000, "color": "White" },
 { "brand": "Hyundai", "model": "Venue", "price": 1100000, "color": "Black" },
 { "brand": "Tata", "model": "Nexon", "price": 1200000, "color": "Grey" },
 { "brand": "Tata", "model": "Punch", "price": 700000, "color": "Orange" },
 { "brand": "Mahindra", "model": "XUV300", "price": 1300000, "color": "Silver" },
 { "brand": "Mahindra", "model": "Thar", "price": 1600000, "color": "Black" },
 { "brand": "Honda", "model": "Amaze", "price": 850000, "color": "White" },
 { "brand": "Honda", "model": "City", "price": 1400000, "color": "Red" },
 { "brand": "Toyota", "model": "Glanza", "price": 900000, "color": "Blue" },
 { "brand": "Toyota", "model": "Innova Crysta", "price": 2200000, "color": "Silver" },
 { "brand": "Kia", "model": "Seltos", "price": 1500000, "color": "Black" },
 { "brand": "Kia", "model": "Sonet", "price": 1100000, "color": "Grey" },
 { "brand": "Renault", "model": "Kwid", "price": 550000, "color": "Yellow" },
 { "brand": "Renault", "model": "Triber", "price": 800000, "color": "White" },
 { "brand": "Skoda", "model": "Slavia", "price": 1400000, "color": "Blue" },
 { "brand": "Volkswagen", "model": "Virtus", "price": 1500000, "color": "Red" },
 { "brand": "MG", "model": "Hector", "price": 1800000, "color": "White" },
 { "brand": "Nissan", "model": "Magnite", "price": 900000, "color": "Silver" }
]


#collect all white color cars
#collect all cars price below 20,00000
#collect all Maruthi cars
#update all car price by adding 10000/-


# new_cars=list(filter(lambda car:car ["color"]=="white",cars))

# new_cars=list(filter(lambda car:car['color']=='White',cars))

# print(list(filter(lambda car:car['price']<2000000,cars )))
print(list(filter(lambda car:car['color']=='white',cars)))
print(list(filter(lambda car:car['color']=='White',cars)))




