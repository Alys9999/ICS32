import ds_messenger as dsm



#168.235.86.101
#'Mark','why do we need a Direct Message class?'

#m=dsm.DirectMessage('Mark', 'Hello!')


mer=dsm.DirectMessenger('168.235.86.101','test_user999','pw')

mer.join()
r=mer.send('','')


a=mer.retrieve_new()
b=mer.retrieve_all()
'''
mer.make_pair()
b=mer.all_list
for x in b:
    print(x)

'''

print(r)
