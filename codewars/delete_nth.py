def delete_nth(order,max_e):
    # code here
    order_d = {}
    for e in set(order):
        order_d[e] = 0
    print(order_d)
    for i in range(0, len(order)):
        if order_d[order[i]] >= max_e:
            order.pop(i)
        else:
            order_d[order[i]] += 1
            print(order_d[order[i]])

    return order

print(delete_nth([20,37,20,21], 1))