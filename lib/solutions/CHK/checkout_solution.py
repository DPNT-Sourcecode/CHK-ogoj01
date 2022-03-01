# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    Input: string of goods to checkout. Example: 'ABCADAZ'
    Output: total checkout value (attention to special offers)
    '''

    price_rules = Constant.PRICE_RULES
    offer_rules = Constant.OFFER_RULES

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
    sorted_skus = ''
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

    sorted_skus = ''
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
                    for idx in range(1, repetitions+1):
                        shop_list = list(sorted_skus)
                        product = shop_list.index(value)
                        del(shop_list[product])
                    print('Offers applied to shop list!')
            else:
                print('No offer available for current shop list...')
                shop_list = list(sorted_skus)

    shop_list_with_offer = ''.join(shop_list)    
    return shop_list_with_offer

class Constant:

    PRICE_RULES = [(5, {'A': 200}), (3, {'A': 130}), (2, {'B': 45}), (2, {'E': 80}), (1, {'A': 50}), (1, {'B': 30}), (1, {'C': 20}), (1, {'D': 15}), (1, {'E': 40})]
    OFFER_RULES = [(2, {'E': 'B'})]                

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
    print(200)
    '''
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
    print(200+50+45+45+3*20+15+40+40)
    
    print('Test14...')
    purchase = 'EEB'
    print(checkout(purchase))
    print(40+40+0)
    '''
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
