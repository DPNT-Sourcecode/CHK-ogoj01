# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    Input: string of goods to checkout. Example: 'ABCADAZ'
    Output: total checkout value (attention to special offers)
    '''

    price_rules = [(5, {'A': 200}), (3, {'A': 130}), (2, {'B': 45}), (2, {'E': 80}), (1, {'A': 50}), (1, {'B': 30}), (1, {'C': 20}), (1, {'D': 15}), (1, {'E': 40})]
    
    

    if is_invalid(skus, price_rules) is True:
        return -1  


    total = 0
    sorted_skus = ''
    sorted_skus = ''.join(sorted(skus))

    for quantity, item_map in price_rules:
        for item, price in item_map.items():
            
            price_rule = quantity * item
            
            if price_rule in sorted_skus:   
                nr_present_price_rules = sorted_skus.count(price_rule)       
                total += nr_present_price_rules * price                
                sorted_skus = sorted_skus.replace(price_rule, '')

    return total

def is_invalid(skus: str, price_rules: list) -> bool:

    products_map_list = list(zip(*price_rules))[1]
    items_in_store = list(set().union(*(item.keys() for item in products_map_list)))  

    for item in skus:
        if item not in items_in_store:
            return True
    return False 

def calculate_price(skus, price_rules):


if __name__ == '__main__':
    '''
    print('Test1...')
    purchase = 'ABCFF'
    print(checkout(purchase))

    print('Test2...')
    purchase = 'A'
    print(checkout(purchase))
    print(50)

    print('Test3...')
    purchase = 'AB'
    print(checkout(purchase))
    print(50+30)

    print('Test4...')
    purchase = 'ABCD'
    print(checkout(purchase))
    print(50+30+20+15)
    
    print('Test5...')
    purchase = 'AA'
    print(checkout(purchase))
    print(50+50)
    
    print('Test6...')
    purchase = 'AAA'
    print(checkout(purchase))
    print(130)
    
    print('Test7...')
    purchase = 'AAAA'
    print(checkout(purchase))
    print(130+50)
    
    print('Test8...')
    purchase = 'AAAAA'
    print(checkout(purchase))
    print(130+50+50)
    
    print('Test9...')
    purchase = 'AAAAABBBCCCD'
    print(checkout(purchase))
    print(130+50+50+45+30+20+20+20+15)
    
    print('Test10...')
    purchase = 'ABCDA'
    print(checkout(purchase))
    print(50+30+20+15+50)

  
    print('Test11...')
    purchase = 'ABCDABCD'
    print(checkout(purchase))
    print(215)   

    print('Test12...')
    purchase = 'ABCDCBAABCABBAAA'
    print(checkout(purchase))
    print(505) 
    
    print('Test13...')
    purchase = 'AAAAAABBBBBCCCDEE'
    print(checkout(purchase))
    print(200+50+45+45+30+20+20+20+15+40+40)
    
    print('Test14...')
    purchase = 'EEB'
    print(checkout(purchase))
    print(40+40+0)
    
    print('Test15...')
    purchase = 'ABCEEE'
    print(checkout(purchase))
    print(40+40+0)
    
    print('Test16...')
    purchase = 'EEBB'
    print(checkout(purchase))
    print(40+40+0+45)

    print('Test17...')
    purchase = 'EE EE EE EE BB'
    print(checkout(purchase))
    print(40+40+0+45)
    '''



 


