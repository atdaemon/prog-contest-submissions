"""
https://www.hackerrank.com/contests/zenhacks/challenges/pairing
"""
N = int(raw_input().strip())
store = {}
count = 0
for _ in xrange(N) :
	company,color,size,typ = map(str,raw_input().split())
	#print "process",company,color,size,typ
	typ2 = 'R' if typ=='L' else 'L'
	if size in store and company in store[size] and color in store[size][company] and store[size][company][color][typ2] > 0: 
		count+=1
		store[size][company][color][typ2]-=1
		#print "found_in_store",company,color,size,typ2
	else :
		if size not in store :
			store[size] = {}
		_size = store[size]
		if company not in _size :
			_size[company] = {}
		_company = _size[company]
		if color not in _company :
			_company[color] = {typ:0,typ2:0}
		_color = _company[color]
		_color[typ]+=1
		#print "added_to_store" , company,color,size,_company[color]
print count

