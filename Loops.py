for i in range(0,10):
    print(i+1)
    
    



L1 = [100,200,300,500,800,900]
watchlist = ["acc","gail","cipla","bhel","ntpc","zeel"]

watchlist.append("hdfc")

watchlist.remove("acc")


watchlist1 = ["naturalgas", "nickel", "crudeoil"]
watchlist2 = ["nifty","banknifty"]
watchlist3 = ["acc","gail","cipla","bhel","ntpc","zeel"]
watchlist = [watchlist1,watchlist2,watchlist3]


for i in watchlist:
    index = watchlist.index(i)
    
    
    if index == 0:
        print("trade only rsi for", i)
    
    if index == 1:
        print("trade only trend following for", i) 
        
    if index == 2: 
        print("trade moving average for", i)
