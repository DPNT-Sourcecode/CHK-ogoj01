# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    Input: string of goods to checkout. Example: 'ABCADAZ'
    Output: total checkout value (attention to special offers)
    '''

    price_rules = Constant.PRICE_RULES 
    price_rules.sort(key = lambda x:x[0], reverse = True)
       
    offer_rules = Constant.OFFER_RULES
    offer_rules.sort(key = lambda x:x[0], reverse = True)

    group_rules = Constant.GROUP_RULES
    group_rules.sort(key = lambda x:x[0], reverse = True)

    if is_invalid(skus, price_rules) is True: return -1
    skus_with_offers = calculate_offer_policy(skus, offer_rules)
    total = min(calculate_price(skus, price_rules), calculate_price(skus_with_offers, price_rules))

    return total  


def is_invalid(skus: str, price_rules: list) -> bool:

    products_map_list = list(zip(*price_rules))[1]
    items_in_store = list(set().union(*(item.keys() for item in products_map_list)))  

    for item in skus:
        if item not in items_in_store:
            return True
    return False 


def calculate_price(skus: str, price_rules: list) -> int:
    
    total = 0
    #sorted_skus = ''
    sorted_skus = ''.join(sorted(skus))

    for quantity, item_map in price_rules:
        for item, price in item_map.items():
            
            price_rule = quantity * item
            
            if price_rule in sorted_skus:  
                #print('Applying discount...') 
                repetitions = sorted_skus.count(price_rule)       
                total += repetitions * price                
                sorted_skus = sorted_skus.replace(price_rule, '')

    return total

def calculate_offer_policy(skus: str, offer_rules: list) -> str:

    #sorted_skus = ''
    sorted_skus = ''.join(sorted(skus))

    print(skus)

    for quantity, item_map in offer_rules:
        for item, value in item_map.items():

            offer_rule = quantity * item

            if offer_rule in sorted_skus:
                repetitions = sorted_skus.count(offer_rule)
                
                if value not in sorted_skus:
                    print('No offer available for current shop list...')                    
                    return sorted_skus

                else:
                    print('Calculating offers...')
                    max_offer = sorted_skus.count(value)
                    iterator = min(repetitions, max_offer)

                    for _ in range(1, iterator+1): 
                        shop_list = list(sorted_skus)                        
                        shop_list.pop(shop_list.index(value))                        
                        sorted_skus = ''.join(shop_list)
                    print('Offers applied to shop list!')
            else:
                print('No offer available for current shop list...')
                shop_list = list(sorted_skus)

    shop_list_with_offer = ''.join(shop_list)
    return shop_list_with_offer

def calculate_group_policy(skus: str, group_rules: list):

    sorted_skus = ''.join(sorted(skus))
    save_indexes = []
    count_group_disc = 0
    group_discount_total = 0

    print(skus)    

    for quantity, item_map in group_rules:
        for item, price in item_map.items():

            group_rule = quantity * item

            if group_rule in sorted_skus:
                starting_index = sorted_skus.index(group_rule)
                save_indexes.append(starting_index)

                repetitions = sorted_skus.count(group_rule)

                for idx in range(1, repetitions+1):
                    save_indexes.append(starting_index+idx)

                count_group_disc += repetitions
                if count_group_disc == Constant.GROUP_SIZE:
                    print('Removing...')
                    shop_list = ''.join([char for idx, char in enumerate(sorted_skus) if idx not in set(save_indexes)])
                    group_discount_total += count_group_disc * price




                    

                

class Constant:

    PRICE_RULES = [
        (1, {'A': 50}),
        (3, {'A': 130}),
        (5, {'A': 200}),
        (1, {'B': 30}),
        (2, {'B': 45}),
        (1, {'C': 20}), 
        (1, {'D': 15}),
        (1, {'E': 40}),
        (1, {'F': 10}),
        (1, {'G': 20}),
        (1, {'H': 10}),
        (5, {'H': 45}),
        (10, {'H': 80}), 
        (1, {'I': 35}),
        (1, {'J': 60}),
        (1, {'K': 80}),
        (2, {'K': 150}),
        (1, {'L': 90}),
        (1, {'M': 15}),
        (1, {'N': 40}),
        (1, {'O': 10}),
        (1, {'P': 50}),
        (5, {'P': 200}),
        (1, {'Q': 30}),
        (3, {'Q': 80}),
        (1, {'R': 50}),
        (1, {'S': 30}),
        (1, {'T': 20}),
        (1, {'U': 40}),
        (1, {'V': 50}),
        (2, {'V': 90}),
        (3, {'V': 130}),
        (1, {'W': 20}),
        (1, {'X': 90}),
        (1, {'Y': 10}),
        (1, {'Z': 50})      
    ]
    
    OFFER_RULES = [
        (2, {'E': 'B'}),
        (3, {'F': 'F'}),
        (3, {'N': 'M'}),
        (3, {'R': 'Q'}),
        (4, {'U': 'U'})
    ]

    GROUP_SIZE = 3

    GROUP_RULES = [
        (1, {'S': 15}),
        (1, {'T': 15}),
        (1, {'X': 15}),
        (1, {'Y': 15}),
        (1, {'Z': 15})
    ]


if __name__ == '__main__':

    print('Test23...')
    purchase = 'SSSS'
    print(checkout(purchase))
    print(45+30)     
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
    print(200)
    
    print('Test9...')
    purchase = 'AAAAABBBCCCD'
    print(checkout(purchase))
    print(200+45+30+20+20+20+15)
    
    print('Test10...')
    purchase = 'ABCDA'
    print(checkout(purchase))
    print(50+30+20+15+50)


    print('Test11...')
    purchase = 'ABCDABCD'
    print(checkout(purchase))
    print(215)  
   
    print('Test13...')
    purchase = 'AAAAAABBBBBCCCDEE'
    print(checkout(purchase))
    print(200+50+45+45+0+3*20+15+40+40)
    
    print('Test14...')
    purchase = 'EEB'
    print(checkout(purchase))
    print(40+40+0)
    
    print('Test15...')
    purchase = 'ABCEEE'
    print(checkout(purchase))
    print(50+20+40*3)
    
    print('Test16...')
    purchase = 'EEBB'
    print(checkout(purchase))
    print(40+40+0+30)
    
    print('Test17...')
    purchase = 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEBBBBBBBB'
    print(checkout(purchase))
    print(28*40 +0)
    
    print('Test13...')
    purchase = 'AAAAAABBBBBCCCDEE'
    print(checkout(purchase))
    print(200+50+45+45+0+3*20+15+40+40)

    print('Test16...')
    purchase = 'EEBB'
    print(checkout(purchase))
    print(40+40+0+30)

    print('Test18...')
    purchase = 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEDEEEEEEEEEEEEEEEEEEEEBBBBBBBBBBBBBBBBABBBBB'
    print(checkout(purchase))
    print(67*40+50+15)
    
    print('Test19...')
    purchase = 'FF'
    print(checkout(purchase))
    print(10+10)

    print('Test20...')
    purchase = 'FFF'
    print(checkout(purchase))
    print(10+10)

    print('Test21...')
    purchase = 'FAFAAAAFFFF'
    print(checkout(purchase))
    print(200+10+10+10+10)

    print('Test22...')
    purchase = 'FFFHHHHHUUUU'
    print(checkout(purchase))
    print(10+10+45+40+40+40)
'''

    



