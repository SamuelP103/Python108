def about_me():
    me = {
        'first': 'billy',
        'last': 'bob',
        'age': 54,
        'address':{
            'street': 'Evergreen',
            'number': 42,
            'city': 'springfield',
            'zip': '12345'
            
        }
    }
    
    
    print(me)
    
    print(me['first'] + ' ' + me['last'])
    
    #print('I am ' + str(me['age'])+ ' years old')
    print(f"I'm {me['age']} years old ")
    # f is for f string which allows contactination of strings and int
    
    #print (me['address']['street'])
    

    
    address = me["address"]
    street = address["street"]
    num = address['number']
    city = address['city']
    zip = address['zip']
    print(street)
    

    print(f'Return to: {street}, #{num}, {city}, {zip}')
    
    
about_me()