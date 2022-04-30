#dictionary.py

friend = {'somchai':'สมชาย ดีมาก','somsak':'สมศักดิ์ เก่งมาก','somsri':'สมศรี เยี่ยมมาก'}
friend_list = ['somchai','somsak','somsri']
x = [1,2,3,4]
print(friend['somsri'])
print(friend_list[2])

#เพิ่มข้อมูลใน dict
friend['somkiat'] = 'สมเกียรติ ยอดเยี่ยม'
friend['somchai-1'] = 'สมชาย สุดยอด'

del friend['somchai']
print(friend)


print('-------item-------')

for k,v in friend.items():
	print(k,v)
print('-------keys-------')

for k in friend.keys():
	print(k)	

print('-------values-------')

for v in friend.values():
	print(v)