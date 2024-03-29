# hotel-to-search-match
## Context
Written as part of a SnapTravel's technical coding challenges. 
Any language of choice, Python was selected.

## Challenge 
Timeframe: This Challenge should take approx. 30 minutes.

At SnapTravel, we sift through millions of unique hotel rates to help our users get the best possible pricing. This challenge will give you an idea of what this process looks like, and help us to better understand your logical approach to solving a problem.

For this coding challenge, your task is to process through a list of hotel rates, and when the user queries for a city, print out the prices from lowest to highest. You can write your solution in the language of your choice.

We source our hotel rates from different suppliers. Each supplier has different rules associated with them.

For this coding challenge, we will have the following rules for each supplier:

For Supplier A, if the days until check-in is 1, then the price increases by 50%.
For Supplier B, if the days until check-in is less than 3, then they are unable to book the hotel.
For Supplier C, if the days until check-in is 7 days or more, then the listing price decreases by 10%
For Supplier D, if the days until check-in is less than 7 days, then the listing price increases by 10%
For all other suppliers, the price stays consistent.
 

Your input is of the following format:

N: the number of supplier rates (1 < N < 1,000,000)
The next N lines will contain the city, supplier, and price separated by a comma (no space between words)

Q: The number of user queries (1 < Q < 100)
The next Q lines will contain a city and days until check-in separated by a comma (assume days until check-in, D  is 1<=D<=20) 


Your output will be Q lines, with each line printing all available hotel prices sorted from lowest to highest with 2 decimals, separated by a comma. If there are no hotels available, print out None.

 

# Sample input:

### 7
### Toronto,A,100.00
### North York,B,250
### Waterloo,C,19.99
### Toronto,D,100.00
### Kitchener,F,25
### Kitchener,F,24
### Kitchener,F,25
### 4
### Toronto,1
### North York,2
### Waterloo,8
### Kitchener,10


# Desired Output:

### 110.00,150.00
### None
### 17.99
### 24.00,25.00,25.00

# CODED SOLUTION: 
https://codeinterview.io/UKQNWNWSJE or check .py file.
