def likes(names):
    rtext = f"like{'s'*(len(names)<2)} them" #right part of text
    print(rtext)
    print(names.pop(0), 'and', names.pop(0))





print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
# print(likes(['Alex', 'Jacob', 'Mark']))
# print(likes(['Alex', 'Jacob']))
# print(likes(['Alex']))
# print(likes([]))

