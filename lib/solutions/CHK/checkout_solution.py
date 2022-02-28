# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    Input: string of goods to checkout. Example: 'ABCADAZ'
    Output: total checkout value (attention to special offers)
    '''

    price_rules = [(5, {'A': 200}), (3, {'A': 130}), (2, {'B': 45}), (2, {'E': 80}), (1, {'A': 50}), (1, {'B': 30}), (1, {'C': 20}), (1, {'D': 15}), (1, {'E': 40})]
    items_in_store = ['A', 'B', 'C', 'D', 'E']
    total = 0
    sorted_skus = ''

    for item in skus:
        if item not in items_in_store:
            return -1

    sorted_skus = ''.join(sorted(skus))

    deleted_rules = {}

    for quantity, item_map in price_rules:
        for item, price in item_map.items():
            
            price_rule = quantity * item
            
            if price_rule in sorted_skus:   
                nr_present_price_rules = sorted_skus.count(price_rule)       
                total += nr_present_price_rules * price
                deleted_rules[f"{price_rule}"]=  nr_present_price_rules
                sorted_skus = sorted_skus.replace(price_rule, '')

    
    if {'EE', 'B'} <= set(deleted_rules):
        nr_EE = deleted_rules['EE']
        nr_B = deleted_rules['B']
        deduct = 0

        for i in range(nr_EE):
            for j in range(nr_B):
                nr_B -=1
                deduct += 40

        print(deduct)


                 



    return total


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
    '''
    print('Test14...')
    purchase = 'EEB'
    print(checkout(purchase))
    print(40+40+0)
    
    print('Test15...')
    purchase = 'ABCEEE'
    print(checkout(purchase))
    print(40+40+0)
    '''
    print('Test16...')
    purchase = 'EEBB'
    print(checkout(purchase))
    print(40+40+0+45)

    print('Test17...')
    purchase = 'EE EE EE EE BB'
    print(checkout(purchase))
    print(40+40+0+45)
    '''


 








