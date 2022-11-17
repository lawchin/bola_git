import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("img/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

def get_login():
	doc = db.collection('agent').document('login').get()
	kira = 0
	if doc.exists:
		x = (doc.to_dict())
		ll = sorted([(k,v) for k,v in x.items()])
		for k,v in ll:
			v = v.split(',')
			cd,rn,hn,li,lp,cr,ab,cm,tn = v
			print(li,lp)
	else:
	    print(u'No such document!')
def get_sales():
	doc = db.collection('agent').document('sales').get()
	kira = 0
	if doc.exists:
	    x = (doc.to_dict())
	    ll = sorted([(k,v) for k,v in x.items()])
	    for k,v in ll:
	    	v = v.split(',')
	    	cd,agn,day,dat,tme,tno,avb,sco,pay,bet = v
	    	kira += int(sk)
	    print(kira)
	else:
	    print(u'No such document!')
# RETRIEVE DATE BY KEY (have to download all data first)
def get_key():
	doc = db.collection('agent').document('sales').get()
	if doc.exists:
	    x = (doc.to_dict())
	    ll = sorted([(k,v) for k,v in x.items()])
	    for k,v in ll:
	    	print(k)
	else:
	    print(u'No such document!')
# RETRIEVE DATE BY VALUE (have to download all data first)
def get_val():
	doc = db.collection('agent').document('sales').get()
	if doc.exists:
	    x = (doc.to_dict())
	    ll = sorted([(k,v) for k,v in x.items()])
	    for k,v in ll:
	    	print(v)
	    	v = v.split(',')

	else:
	    print(u'No such document!')	    
#RETRIEVE DATE BY KEY and update to the largest(have to download all data first)
def markup():
	doc = db.collection('agent').document('sales').get()
	kira,lst,agn = 0,list(),'law'
	x = (doc.to_dict())
	ll = sorted([(k,v) for k,v in x.items()])
	if len(ll) == 0:
		det = f'{agn}-1'
		data = {f'{det}':f'cd,123,016-5858696,123,123,{det}'}
		db.collection('agent').document('sales').set(data, merge=True)
	else:
		doc = db.collection('agent').document('sales').get()
		x = (doc.to_dict())
		ll = sorted([(k,v) for k,v in x.items()])
		for k,v in ll:
			k = k.split('-')
			agent = k[0]
			num = k[1]
			if agn == agent:
				lst.append(k)
				for k,v in lst:
					biggest = max(v)		
				add = int(biggest) + 1
				det = f'{agn}-{add}'
				data = {f'{det}':f'cd,123,016-5858696,123,123,{det}'}
				db.collection('agent').document('sales').set(data, merge=True)			
				doc = db.collection('agent').document('sales').get()
				x = (doc.to_dict())
				ll = sorted([(k,v) for k,v in x.items()])
			elif agn != agent:
				det = f'{agn}-1'
				data = {f'{det}':f'cd,123,016-5858696,123,123,{det}'}
				db.collection('agent').document('sales').set(data, merge=True)
	doc = db.collection('agent').document('sales').get()
	x = (doc.to_dict())
	ll = sorted([(k,v) for k,v in x.items()])
	for k,v in ll:
		if k.startswith('ch'):
			print(k)
def markup2(): # UNDER CONSTRUCTION

	doc = db.collection('agent').document('account').get()
	x = (doc.to_dict())
	ll = sorted([(k,v) for k,v in x.items()])
	for k,v in ll:
		v = v.split(',')
		li,lp,cr,ab,tn,ni,nm,pn = v # retrieving current number increment
def update_ni():
	agn = 'law'
	doc = db.collection('agent').document('account').get()
	x = (doc.to_dict())
	ll = sorted([(k,v) for k,v in x.items()])
	for k,v in ll:
		if agn == k:
			v = v.split(',')
			cd,rn,hn,li,lp,ni,cr,ab,cm,tn = v
	nni = int(ni)+1
	data = f'{li},{lp},{cr},{ab},{tn},{nni},{nm},{pn}'
	doc = db.collection('agent').document('account').update({f'{agn}':f'{data}'})
# ADD BY LOOP ()
def add_loop():
	x = 99
	for i in range(1,6):
		data1 = i+int(x) 
		data = {f'{data1}':f'cd,123,016-5858696,123,123,{data1}'}
		db.collection('agent').document('sales').set(data, merge=True)
# ADD DEFAULT
def default():
	data1 = f'law'
	data = {f'{data1}':f'nil,lawrence,0165858696,law,321,20,1000,0,cm,0,0'}
	db.collection('agent').document('account').set(data, merge=True)
# ADD AGENT 
# cd,rn,hn,li,lp,cr,ab,cp,ni,tn
# (code,runner/agent name,handphone number,login id,login password,currency,account balance,commission percentage,number increment,ticket number)
def a321(): # in = SALES STATUS (indicate for purchase increment number)
	data1 = '321' 
	data = {f'{data1}':f'nil,james,016,{data1},321,MYR,1000.00,20,0,0'}
	db.collection('agent').document('account').set(data, merge=True)
a321()
def law(): # in = SALES STATUS (indicate for purchase increment number)
	data1 = 'law' 
	data = {f'{data1}':f'nil,lawrence,0165858696,{data1},321,MYR,10000.00,25,0,0'}
	db.collection('agent').document('account').set(data, merge=True)

# RETRIEVE DATA
def get():
	doc = db.collection('host').document('game').get()

	if doc.exists:
	    x = (doc.to_dict())
	    ll = sorted([(k,v) for k,v in x.items()])
	    for k,v in ll:
	    	v = v.split(',')
	    	sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
	    	if cd == 'm01':
	    		print(f'{la} vs {lb}')
	else:
	    print(u'No such document!')
# RETRIEVE DATA (by startwith) (but have to download all data first)
def get2():
	doc = db.collection('host').document('game').get()

	if doc.exists:
	    x = (doc.to_dict())
	    ll = sorted([(k,v) for k,v in x.items()])
	    for k,v in ll:
	    	v = v.split(',')
	    	sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
	    	if cd.startswith('m1'):
	    		print(v)
	else:
	    print(u'No such document!')
# DELETE ONLY SELECTED FIELD
def delete():

	db.collection('agent').document('sales').update({'bom-1':firestore.DELETE_FIELD})
# DELETE DOCUMENT
def d_doc():

	db.collection('agent').document('sales').delete()
# ADD GAME (DETAILS BUT LARGE FILE) NOT RECOMENDED
def add_game():
	data = {'sk':0,\
			'dk':0,\
			'ds':0,\
			'tk':0,\
			'ts':0,\
			'td':0,\
			'ek':0,\
			'es':0,\
			'ed':0,\
			'et':0,\

			'kk':0,\
			'ss':0,\
			'dd':0,\
			'tt':0,\
			'ee':0,\
			'au':0,\
			's0':0,\
			'd0':0,\
			'd1':0,\
			't0':0,\

			't1':0,\
			't2':0,\
			'e0':0,\
			'e1':0,\
			'e2':0,\
			'e3':0,\
			'bu':0,\
			'la':'NIL',\
			'lb':'NIL',\
			'sa':'NIL',\

			'sb':'NIL',\
			'dy':'day',\
			'dt':'date',\
			'tm':'time',\
			'sh':'T',\
			'de':'T',\
			'fx':'',\
			'ab':0,\
			'st':'',\
			'at':''}
	db.collection('games').document('m01').set(data, merge=True)
# ADD GAME
#sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd
def game():
	data = {'m20':f'0,0,0,0,0,0,0,0,0,0,0,\
					0,0,0,0,0,\
					0,0,0,0,0,0,0,0,0,0,0,\
					x,x,x,x,\
					F,F,F,F,T,F,F,F,m20'}
	db.collection('host').document('game').set(data, merge=True)
# THIS WILL DELETE THE DOCUMENT AND ITS ENTIRE FIELD
def del1():

	db.collection('host').document('game').delete()
# THIS WILL DELETE ONLY THE SELECTED FIELD
def del2():

	db.collection('agent').document('sales').update({'chin(1)':firestore.DELETE_FIELD})
# UPDATE/EDIT SELECTED FIELD
def update():
	data = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Germany,Japan,GER,JPN,Wednesday,23 November 2022,9:00 pm,T,F,x,x,x,m10'
	db.collection('host').document('game').update({'m10':data})
def subsub():

	db.collection('agent').document('sales').collection('belian').add({'anjing':'bullshit'})
def sales1():
	data = {'law_100':'a,b,c,d,e,f,g,h,i,j'}
	db.collection('agent').document('sales').set(data, merge=True)
def sales2():
	data = 'A,B,C,D,E,F,G,H,I,J'
	db.collection('agent').document('sales').update({'law_100':data})
# ARRAY IS NOT RECOMMEND BECAUSE YOU CAN'T ADD TWO SAME OJBECT
def tambah():




	db.collection('agent').document('runner').update({'law': firestore.ArrayUnion(['bullshits'])})
# ADD RUNNER TO FIREBASE FIRESTORE
# cd,rn,hn,li,lp,cr,ab,cm,ni,tn
def cnr(): # CREATE NEW RUNNER
	user = 'bob'
	name = 'unknown'

	set1 = f'nil,{name},hp,{user},321,cr,1000.00,cm,0,0'
	data1 = {f'{user}':f'{set1}'}

	set2 = f'cd,{name},hn,{user},lp,cr,ab,cm,ni,tn'
	data2 = {f'{user}':f'{set2}'}

	db.collection('agent').document('account').set(data1, merge=True)
	db.collection('sales').document(f'{user}').set(data2, merge=True)
	db.collection('sales').document(f'{user}').update({f'{user}':firestore.DELETE_FIELD})
#cnr()
