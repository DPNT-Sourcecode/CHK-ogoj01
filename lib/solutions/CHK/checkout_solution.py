# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    '''
    input: string of goods to checkout. example: 'ABCADAZ'
    output: total checkout value (attention to special offers)
    '''

    price_rules = []
    items_in_store = ['A', 'B', 'C', 'D']
    items = ''
    total = 0

    for item in skus:
        if item not in items_in_store:
            return -1

    

    return 'OK'

if __name__ == '__main__':
    purchase = 'ABCFF'
    print(checkout(purchase))

    purchase = 'ABCD'
    print(checkout(purchase))



    

    







