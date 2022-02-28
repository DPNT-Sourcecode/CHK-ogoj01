# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    input: string of goods to checkout. example: 'ABCADAZ'
    output: total checkout value (attention to special offers)
    '''

    price_rules = [(3, {'A': 130}), (2, {'B': 45}), (1, {'A': 50}), (1, {'B': 30}), (1, {'C': 20}), (1, {'D': 15})]
    items_in_store = ['A', 'B', 'C', 'D']
    total = 0

    for item in skus:
        if item not in items_in_store:
            return -1


    for quantity, item_map in price_rules:
        for item, price in item_map.items():
            print('quantity: ', quantity)
            print('item_map: ', item_map)
            print('item: ', item)
            print('price: ', price)

            price_rule = quantity * item
            print(f"item_rule {price_rule}")

            if price_rule in skus:
                total += quantity * price
                
            else:
                print('not found')

    return total

if __name__ == '__main__':
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



    

    







