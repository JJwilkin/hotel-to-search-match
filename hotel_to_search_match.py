#Variable Declaration
num_suppliers = ""
num_queries = ""
hotels= []
e = 0
queries=[]
price = 0
price_arr = []

input = """7
Toronto,A,100.00
North York,B,250
Waterloo,C,19.99
Toronto,D,100.00
Kitchener,F,25
Kitchener,F,24
Kitchener,F,25
4
Toronto,1
North York,2
Waterloo,8
Kitchener,10
"""

#Seperate Input into respective lines
entries = input.splitlines()

#Finds number of suppliers and queries for any input
for x in entries:
  if len(x) == 1:
    if num_suppliers == "":
      num_suppliers = int(x)
    else:
      num_queries = int(x)

#Stores all given hotel suppliers
for i in range(0,num_suppliers+1):
  if len(entries[i]) > 1:
    hotels.append(entries[i].split(','))

#Stores all give queries
for i in range(num_suppliers+1,num_suppliers+num_queries+2):
  if len(entries[i]) > 1:
    queries.append(entries[i].split(','))

#Matching Queries to Suppliers
for i in range(0, num_queries):
  empty = False
  price_arr.clear()
  #Goes through each hotel supplier
  for x in range(0, num_suppliers):
    #If the city of query matches city of supplier
    if queries[i][0] == hotels[x-1][0]:
      #If type of query matches type of differnet suppliers
        if hotels[x-1][1]== 'A':
          if int(queries[i][1]) == 1:
            price = float(hotels[x-1][2])*1.5
            price_arr.append(round(price,2))

          elif int(queries[i][1]) > 1:
            price = float(hotels[x-1][2])
            price_arr.append(round(price,2))

        elif hotels[x-1][1]== 'B':
          if int(queries[i][1]) < 3:
            print("NONE")
            empty = True

        elif hotels[x-1][1]== 'C':
          if int(queries[i][1]) >=7:
            price = float(hotels[x-1][2])*0.9
            price_arr.append(round(price,2))

        elif int(queries[i][1]) <7:
            price = float(hotels[x-1][2])
            price_arr.append(round(price,2))

        elif hotels[x-1][1]== 'D':
          if int(queries[i][1]) >=7:
            price = float(hotels[x-1][2])
            price_arr.append(round(price,2))

        elif int(queries[i][1]) <7:
          price = float(hotels[x-1][2])*1.1
          price_arr.append(round(price,2))

        else:
          price = float(hotels[x-1][2])
          price_arr.append(round(price,2))
  #If NONE is result, this section is skipped
  if not empty:
    price_arr.sort() #sort array from least to greatest
    x=''
    #print outcome with commas, except on last element
    for i in range(0,len(price_arr)):
      x += str(price_arr[i])
      if i != len(price_arr)-1:
        x += ', '
    print(x)

  
