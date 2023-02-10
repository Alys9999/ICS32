import ds_messenger as dsm



#168.235.86.101
#'Mark','why do we need a Direct Message class?'

m=dsm.DirectMessage('Mark', 'Hello!')


mer=dsm.DirectMessenger('168.235.86.101','user888','pw')

mer.join()
mer.send('???????','test_user999')

r=mer.retrieve_all()
#mer.p_obj

mer.retrieve_new()
mer.make_pair()

print(r)



'''
dic={'s':[{'sender':3, 'entry':4}],'b':[{'sender':5, 'entry':6}]}

k=dic.values()
print(k[0])

'''



