def students():
    names = ["Dave", "Jazper",  "Andy", "Corey", "Samuel", "Cesar", "Darius", "Demetri", "Janaye", "Donald", "Marco"]
    print(names)
    
    names.append("Sergio")
    
    for name in names:
        print(name)
    
    
    
    print(len(names))

def products():
    prices = [23, 234, 34, 672, 77, 214, 756, 76, 500, 479, 629, 325, 389, 29, 101, 50, 67, 800, 54]
    total = 0
    count = 0
    expensive = 0
    for price in prices:
        print(price)
        if price<500:
            count += 1
            #* count = count + 1
        listed = sorted(prices, reverse=True)
        
        if price >= 500:
            expensive += 1
            
        
    print(total)
    print(count)
    print(listed)
    print (expensive)
        
    
    
    
students()
products()


def art():
    colors = ["red", "blue", "pink", "blue", "white", "blak", "green", "black", "red", "white", "blue", "yellow"]
    
    amount = 0 
    blue_color = 0
    white_black = 0
    for color in colors:
        amount += 1
        if color=="blue":
            blue_color += 1
        if color == "black" or color == "white":
            white_black += 1
    print ("blues " + str(blue_color))
    print('wANDb ' + str(white_black))
        
    
    
    
art()

