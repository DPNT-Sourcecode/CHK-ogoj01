# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    input: string of goods to checkout. example: 'ABCADAZ'
    output: total checkout value (attention to special offers)
    '''

    price_rules = [(1, {'A': 50})]
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

            item_rule = quantity * item
            print(f"item_rule {item_rule}")

            if item_rule in skus:
                total += quantity * price

    return total

if __name__ == '__main__':
    #purchase = 'ABCFF'
    #print(checkout(purchase))

    #purchase = 'A'
    #print(checkout(purchase))

    purchase = 'AA'
    print(checkout(purchase))



    

    




