lis = [5,1,3,6,10,1,5,2,3,4,8]
target = 11
pair=[]
for i in range(0, len(lis)):
    for j in range(i+1, len(lis)):
        if target-lis[i] == lis[j]:
            ele = (min(lis[i], lis[j]), max(lis[i], lis[j]))
            if ele not in pair:
                pair.append(ele)        # to avoid duplicates in the pair- (5,6) and (6,5)
# print(pair)
# for i in pair:
#     print("{} and {}".format(i[0],i[1]))
for i in pair:
    print(i)