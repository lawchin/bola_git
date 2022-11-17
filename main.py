from kivy.config import Config
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 539)
Config.set('graphics', 'top', 30)

import time
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("img/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()

#requests, openssl, urllib3, chardet, idna, jwt, cryptography, pyparsing, firebase_admin, PIL, google-auth, cachetools, pyasn1, pyasn1_modules, rsa, google-api-python-client, google-cloud-storage, google-cloud-firestore, google-api-core,  protobuf, cachecontrol, gcloud, google-cloud, httplib2

# to avoid android keyboard from popping up.. 
# kindly use label as text input (do not use text field, text field cause focus)

#Window.size = (563, 1000)

class Login(Screen):
	def log_in(self):
	# LOGIN SESSION	
		#try:
		a,b,d = self.ids,self.manager.get_screen('m_p').ids,self.manager.get_screen('p_a').ids
		with open('img/temp.txt', 'w') as f:
			f.write('')
		self.manager.get_screen('p_a').ids.ttv.text = ''
		user = a.user.text
		pasw = a.password.text
		a.user.helper_text = ''
		a.password.helper_text = ''
		if user == '':
			a.user.helper_text = 'Username cannot be blank'
			a.password.helper_text = ''
		elif pasw == '':
			a.password.helper_text = 'Password cannot be blank'
			a.user.helper_text = ''
		else:
			ll = list()
			ti_user = a.user.text
			ti_pswd = a.password.text

			doc = db.collection('agent').document('account').get()
			x = (doc.to_dict())
			lst = sorted([(k,v) for k,v in x.items()])
			for k,v in lst:
				v = v.split(',')
				cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
				ll.append(li)
				if ti_user in ll:
					if ti_pswd != lp:
						a.user.helper_text = ''
						a.password.helper_text = 'Password not match'
						ll = []
					else:
						d.agent_log.text = user
						self.parent.current = "m_p"
						a.user.helper_text = ''
						a.password.helper_text = ''
						# a.lp_label.color = 1,1,1,1
						# a.lp_label.font_size = 40
						# a.lp_label.text = 'WELCOME'
						data = rn.title()
						welcome_user = f'Welcome Agent {data}'
						b.welcome.text = welcome_user
						ll = []
						#Clock.schedule_interval(self.runrun, 60.0)
					
					# m01
						doc = db.collection('host').document('game').get()
						x = (doc.to_dict())
						ll = sorted([(k,v) for k,v in x.items()])
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm01':
								b.m01_tal.source = f'img/{sa}.png'
								d.m01_alogo.source = f'img/{sa}.png' ###
								b.m01_tbl.source = f'img/{sb}.png'
								d.m01_blogo.source = f'img/{sb}.png' ###
								b.m01_aln.text = la
								b.m01_bln.text = lb
								d.m01_asn.text = sa ###
								d.m01_bsn.text = sb ###
								b.m01_dt.text = f'{dy}, {dt}\n{tm}'
								d.m01_t.text = f'{dy}, {dt}\n{tm}'###
								cm01 = b.m01_mb.active
								if sh == 'T':
									if cm01 == True:
										if de == 'T':
											b.m01_mb.disabled = False																				
										elif de == 'F':
											b.m01_mb.disabled = True
											d.bl.remove_widget(d.m01_bb) ###
									elif cm01 == False:
										b.ml.add_widget(b.m01_mb)
										d.bl.add_widget(d.m01_bb) ###
										b.m01_mb.active = True
										if de == 'T':
											b.m01_mb.disabled = False
										elif de == 'F':
											b.m01_mb.disabled = True
								elif sh == 'F':
									if cm01 == True:
										b.ml.remove_widget(b.m01_mb)
										d.bl.remove_widget(d.m01_bb) ###
										b.m01_mb.active = False
									elif cm01 == False:
											pass
					# m02
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm02':
								b.m02_tal.source = f'img/{sa}.png'
								d.m02_alogo.source = f'img/{sa}.png' ###
								b.m02_tbl.source = f'img/{sb}.png'
								d.m02_blogo.source = f'img/{sb}.png' ###
								b.m02_aln.text = la
								b.m02_bln.text = lb
								d.m02_asn.text = sa ###
								d.m02_bsn.text = sb ###
								b.m02_dt.text = f'{dy}, {dt}\n{tm}'
								d.m02_t.text = f'{dy}, {dt}\n{tm}'###
								cm02 = b.m02_mb.active
								if sh == 'T':
									if cm02 == True:
										if de == 'T':
											b.m02_mb.disabled = False																				
										elif de == 'F':
											b.m02_mb.disabled = True
											d.bl.remove_widget(d.m02_bb) ###
									elif cm02 == False:
										b.ml.add_widget(b.m02_mb)
										d.bl.add_widget(d.m02_bb) ###
										b.m02_mb.active = True
										if de == 'T':
											b.m02_mb.disabled = False
										elif de == 'F':
											b.m02_mb.disabled = True
								elif sh == 'F':
									if cm02 == True:
										b.ml.remove_widget(b.m02_mb)
										d.bl.remove_widget(d.m02_bb) ###
										b.m02_mb.active = False
									elif cm02 == False:
											pass
					# m03
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm03':
								b.m03_tal.source = f'img/{sa}.png'
								d.m03_alogo.source = f'img/{sa}.png' ###
								b.m03_tbl.source = f'img/{sb}.png'
								d.m03_blogo.source = f'img/{sb}.png' ###
								b.m03_aln.text = la
								b.m03_bln.text = lb
								d.m03_asn.text = sa ###
								d.m03_bsn.text = sb ###
								b.m03_dt.text = f'{dy}, {dt}\n{tm}'
								d.m03_t.text = f'{dy}, {dt}\n{tm}'###
								cm03 = b.m03_mb.active
								if sh == 'T':
									if cm03 == True:
										if de == 'T':
											b.m03_mb.disabled = False																				
										elif de == 'F':
											b.m03_mb.disabled = True
											d.bl.remove_widget(d.m03_bb) ###
									elif cm03 == False:
										b.ml.add_widget(b.m03_mb)
										d.bl.add_widget(d.m03_bb) ###
										b.m03_mb.active = True
										if de == 'T':
											b.m03_mb.disabled = False
										elif de == 'F':
											b.m03_mb.disabled = True
								elif sh == 'F':
									if cm03 == True:
										b.ml.remove_widget(b.m03_mb)
										d.bl.remove_widget(d.m03_bb) ###
										b.m03_mb.active = False
									elif cm03 == False:
											pass
					# m04
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm04':
								b.m04_tal.source = f'img/{sa}.png'
								d.m04_alogo.source = f'img/{sa}.png' ###
								b.m04_tbl.source = f'img/{sb}.png'
								d.m04_blogo.source = f'img/{sb}.png' ###
								b.m04_aln.text = la
								b.m04_bln.text = lb
								d.m04_asn.text = sa ###
								d.m04_bsn.text = sb ###
								b.m04_dt.text = f'{dy}, {dt}\n{tm}'
								d.m04_t.text = f'{dy}, {dt}\n{tm}'###
								cm04 = b.m04_mb.active
								if sh == 'T':
									if cm04 == True:
										if de == 'T':
											b.m04_mb.disabled = False																				
										elif de == 'F':
											b.m04_mb.disabled = True
											d.bl.remove_widget(d.m04_bb) ###
									elif cm04 == False:
										b.ml.add_widget(b.m04_mb)
										d.bl.add_widget(d.m04_bb) ###
										b.m04_mb.active = True
										if de == 'T':
											b.m04_mb.disabled = False
										elif de == 'F':
											b.m04_mb.disabled = True
								elif sh == 'F':
									if cm04 == True:
										b.ml.remove_widget(b.m04_mb)
										d.bl.remove_widget(d.m04_bb) ###
										b.m04_mb.active = False
									elif cm04 == False:
											pass
					# m05
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm05':
								b.m05_tal.source = f'img/{sa}.png'
								d.m05_alogo.source = f'img/{sa}.png' ###
								b.m05_tbl.source = f'img/{sb}.png'
								d.m05_blogo.source = f'img/{sb}.png' ###
								b.m05_aln.text = la
								b.m05_bln.text = lb
								d.m05_asn.text = sa ###
								d.m05_bsn.text = sb ###
								b.m05_dt.text = f'{dy}, {dt}\n{tm}'
								d.m05_t.text = f'{dy}, {dt}\n{tm}'###
								cm05 = b.m05_mb.active
								if sh == 'T':
									if cm05 == True:
										if de == 'T':
											b.m05_mb.disabled = False																				
										elif de == 'F':
											b.m05_mb.disabled = True
											d.bl.remove_widget(d.m05_bb) ###
									elif cm05 == False:
										b.ml.add_widget(b.m05_mb)
										d.bl.add_widget(d.m05_bb) ###
										b.m05_mb.active = True
										if de == 'T':
											b.m05_mb.disabled = False
										elif de == 'F':
											b.m05_mb.disabled = True
								elif sh == 'F':
									if cm05 == True:
										b.ml.remove_widget(b.m05_mb)
										d.bl.remove_widget(d.m05_bb) ###
										b.m05_mb.active = False
									elif cm05 == False:
											pass
					# m06
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm06':
								b.m06_tal.source = f'img/{sa}.png'
								d.m06_alogo.source = f'img/{sa}.png' ###
								b.m06_tbl.source = f'img/{sb}.png'
								d.m06_blogo.source = f'img/{sb}.png' ###
								b.m06_aln.text = la
								b.m06_bln.text = lb
								d.m06_asn.text = sa ###
								d.m06_bsn.text = sb ###
								b.m06_dt.text = f'{dy}, {dt}\n{tm}'
								d.m06_t.text = f'{dy}, {dt}\n{tm}'###
								cm06 = b.m06_mb.active
								if sh == 'T':
									if cm06 == True:
										if de == 'T':
											b.m06_mb.disabled = False																				
										elif de == 'F':
											b.m06_mb.disabled = True
											d.bl.remove_widget(d.m06_bb) ###
									elif cm06 == False:
										b.ml.add_widget(b.m06_mb)
										d.bl.add_widget(d.m06_bb) ###
										b.m06_mb.active = True
										if de == 'T':
											b.m06_mb.disabled = False
										elif de == 'F':
											b.m06_mb.disabled = True
								elif sh == 'F':
									if cm06 == True:
										b.ml.remove_widget(b.m06_mb)
										d.bl.remove_widget(d.m06_bb) ###
										b.m06_mb.active = False
									elif cm06 == False:
											pass
					# m07
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm07':
								b.m07_tal.source = f'img/{sa}.png'
								d.m07_alogo.source = f'img/{sa}.png' ###
								b.m07_tbl.source = f'img/{sb}.png'
								d.m07_blogo.source = f'img/{sb}.png' ###
								b.m07_aln.text = la
								b.m07_bln.text = lb
								d.m07_asn.text = sa ###
								d.m07_bsn.text = sb ###
								b.m07_dt.text = f'{dy}, {dt}\n{tm}'
								d.m07_t.text = f'{dy}, {dt}\n{tm}'###
								cm07 = b.m07_mb.active
								if sh == 'T':
									if cm07 == True:
										if de == 'T':
											b.m07_mb.disabled = False																				
										elif de == 'F':
											b.m07_mb.disabled = True
											d.bl.remove_widget(d.m07_bb) ###
									elif cm07 == False:
										b.ml.add_widget(b.m07_mb)
										d.bl.add_widget(d.m07_bb) ###
										b.m07_mb.active = True
										if de == 'T':
											b.m07_mb.disabled = False
										elif de == 'F':
											b.m07_mb.disabled = True
								elif sh == 'F':
									if cm07 == True:
										b.ml.remove_widget(b.m07_mb)
										d.bl.remove_widget(d.m07_bb) ###
										b.m07_mb.active = False
									elif cm07 == False:
											pass
					# m08
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm08':
								b.m08_tal.source = f'img/{sa}.png'
								d.m08_alogo.source = f'img/{sa}.png' ###
								b.m08_tbl.source = f'img/{sb}.png'
								d.m08_blogo.source = f'img/{sb}.png' ###
								b.m08_aln.text = la
								b.m08_bln.text = lb
								d.m08_asn.text = sa ###
								d.m08_bsn.text = sb ###
								b.m08_dt.text = f'{dy}, {dt}\n{tm}'
								d.m08_t.text = f'{dy}, {dt}\n{tm}'###
								cm08 = b.m08_mb.active
								if sh == 'T':
									if cm08 == True:
										if de == 'T':
											b.m08_mb.disabled = False																				
										elif de == 'F':
											b.m08_mb.disabled = True
											d.bl.remove_widget(d.m08_bb) ###
									elif cm08 == False:
										b.ml.add_widget(b.m08_mb)
										d.bl.add_widget(d.m08_bb) ###
										b.m08_mb.active = True
										if de == 'T':
											b.m08_mb.disabled = False
										elif de == 'F':
											b.m08_mb.disabled = True
								elif sh == 'F':
									if cm08 == True:
										b.ml.remove_widget(b.m08_mb)
										d.bl.remove_widget(d.m08_bb) ###
										b.m08_mb.active = False
									elif cm08 == False:
											pass
					# m09
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm09':
								b.m09_tal.source = f'img/{sa}.png'
								d.m09_alogo.source = f'img/{sa}.png' ###
								b.m09_tbl.source = f'img/{sb}.png'
								d.m09_blogo.source = f'img/{sb}.png' ###
								b.m09_aln.text = la
								b.m09_bln.text = lb
								d.m09_asn.text = sa ###
								d.m09_bsn.text = sb ###
								b.m09_dt.text = f'{dy}, {dt}\n{tm}'
								d.m09_t.text = f'{dy}, {dt}\n{tm}'###
								cm09 = b.m09_mb.active
								if sh == 'T':
									if cm09 == True:
										if de == 'T':
											b.m09_mb.disabled = False																				
										elif de == 'F':
											b.m09_mb.disabled = True
											d.bl.remove_widget(d.m09_bb) ###
									elif cm09 == False:
										b.ml.add_widget(b.m09_mb)
										d.bl.add_widget(d.m09_bb) ###
										b.m09_mb.active = True
										if de == 'T':
											b.m09_mb.disabled = False
										elif de == 'F':
											b.m09_mb.disabled = True
								elif sh == 'F':
									if cm09 == True:
										b.ml.remove_widget(b.m09_mb)
										d.bl.remove_widget(d.m09_bb) ###
										b.m09_mb.active = False
									elif cm09 == False:
											pass
					# m10
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm10':
								b.m10_tal.source = f'img/{sa}.png'
								d.m10_alogo.source = f'img/{sa}.png' ###
								b.m10_tbl.source = f'img/{sb}.png'
								d.m10_blogo.source = f'img/{sb}.png' ###
								b.m10_aln.text = la
								b.m10_bln.text = lb
								d.m10_asn.text = sa ###
								d.m10_bsn.text = sb ###
								b.m10_dt.text = f'{dy}, {dt}\n{tm}'
								d.m10_t.text = f'{dy}, {dt}\n{tm}'###
								cm10 = b.m10_mb.active
								if sh == 'T':
									if cm10 == True:
										if de == 'T':
											b.m10_mb.disabled = False																				
										elif de == 'F':
											b.m10_mb.disabled = True
											d.bl.remove_widget(d.m10_bb) ###
									elif cm10 == False:
										b.ml.add_widget(b.m10_mb)
										d.bl.add_widget(d.m10_bb) ###
										b.m10_mb.active = True
										if de == 'T':
											b.m10_mb.disabled = False
										elif de == 'F':
											b.m10_mb.disabled = True
								elif sh == 'F':
									if cm10 == True:
										b.ml.remove_widget(b.m10_mb)
										d.bl.remove_widget(d.m10_bb) ###
										b.m10_mb.active = False
									elif cm10 == False:
											pass
					# m11
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm11':
								b.m11_tal.source = f'img/{sa}.png'
								d.m11_alogo.source = f'img/{sa}.png' ###
								b.m11_tbl.source = f'img/{sb}.png'
								d.m11_blogo.source = f'img/{sb}.png' ###
								b.m11_aln.text = la
								b.m11_bln.text = lb
								d.m11_asn.text = sa ###
								d.m11_bsn.text = sb ###
								b.m11_dt.text = f'{dy}, {dt}\n{tm}'
								d.m11_t.text = f'{dy}, {dt}\n{tm}'###
								cm11 = b.m11_mb.active
								if sh == 'T':
									if cm11 == True:
										if de == 'T':
											b.m11_mb.disabled = False																				
										elif de == 'F':
											b.m11_mb.disabled = True
											d.bl.remove_widget(d.m11_bb) ###
									elif cm11 == False:
										b.ml.add_widget(b.m11_mb)
										d.bl.add_widget(d.m11_bb) ###
										b.m11_mb.active = True
										if de == 'T':
											b.m11_mb.disabled = False
										elif de == 'F':
											b.m11_mb.disabled = True
								elif sh == 'F':
									if cm11 == True:
										b.ml.remove_widget(b.m11_mb)
										d.bl.remove_widget(d.m11_bb) ###
										b.m11_mb.active = False
									elif cm11 == False:
											pass
					# m12
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm12':
								b.m12_tal.source = f'img/{sa}.png'
								d.m12_alogo.source = f'img/{sa}.png' ###
								b.m12_tbl.source = f'img/{sb}.png'
								d.m12_blogo.source = f'img/{sb}.png' ###
								b.m12_aln.text = la
								b.m12_bln.text = lb
								d.m12_asn.text = sa ###
								d.m12_bsn.text = sb ###
								b.m12_dt.text = f'{dy}, {dt}\n{tm}'
								d.m12_t.text = f'{dy}, {dt}\n{tm}'###
								cm12 = b.m12_mb.active
								if sh == 'T':
									if cm12 == True:
										if de == 'T':
											b.m12_mb.disabled = False																				
										elif de == 'F':
											b.m12_mb.disabled = True
											d.bl.remove_widget(d.m12_bb) ###
									elif cm12 == False:
										b.ml.add_widget(b.m12_mb)
										d.bl.add_widget(d.m12_bb) ###
										b.m12_mb.active = True
										if de == 'T':
											b.m12_mb.disabled = False
										elif de == 'F':
											b.m12_mb.disabled = True
								elif sh == 'F':
									if cm12 == True:
										b.ml.remove_widget(b.m12_mb)
										d.bl.remove_widget(d.m12_bb) ###
										b.m12_mb.active = False
									elif cm12 == False:
											pass
					# m13
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm13':
								b.m13_tal.source = f'img/{sa}.png'
								d.m13_alogo.source = f'img/{sa}.png' ###
								b.m13_tbl.source = f'img/{sb}.png'
								d.m13_blogo.source = f'img/{sb}.png' ###
								b.m13_aln.text = la
								b.m13_bln.text = lb
								d.m13_asn.text = sa ###
								d.m13_bsn.text = sb ###
								b.m13_dt.text = f'{dy}, {dt}\n{tm}'
								d.m13_t.text = f'{dy}, {dt}\n{tm}'###
								cm13 = b.m13_mb.active
								if sh == 'T':
									if cm13 == True:
										if de == 'T':
											b.m13_mb.disabled = False																				
										elif de == 'F':
											b.m13_mb.disabled = True
											d.bl.remove_widget(d.m13_bb) ###
									elif cm13 == False:
										b.ml.add_widget(b.m13_mb)
										d.bl.add_widget(d.m13_bb) ###
										b.m13_mb.active = True
										if de == 'T':
											b.m13_mb.disabled = False
										elif de == 'F':
											b.m13_mb.disabled = True
								elif sh == 'F':
									if cm13 == True:
										b.ml.remove_widget(b.m13_mb)
										d.bl.remove_widget(d.m13_bb) ###
										b.m13_mb.active = False
									elif cm13 == False:
											pass
					# m14
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm14':
								b.m14_tal.source = f'img/{sa}.png'
								d.m14_alogo.source = f'img/{sa}.png' ###
								b.m14_tbl.source = f'img/{sb}.png'
								d.m14_blogo.source = f'img/{sb}.png' ###
								b.m14_aln.text = la
								b.m14_bln.text = lb
								d.m14_asn.text = sa ###
								d.m14_bsn.text = sb ###
								b.m14_dt.text = f'{dy}, {dt}\n{tm}'
								d.m14_t.text = f'{dy}, {dt}\n{tm}'###
								cm14 = b.m14_mb.active
								if sh == 'T':
									if cm14 == True:
										if de == 'T':
											b.m14_mb.disabled = False																				
										elif de == 'F':
											b.m14_mb.disabled = True
											d.bl.remove_widget(d.m14_bb) ###
									elif cm14 == False:
										b.ml.add_widget(b.m14_mb)
										d.bl.add_widget(d.m14_bb) ###
										b.m14_mb.active = True
										if de == 'T':
											b.m14_mb.disabled = False
										elif de == 'F':
											b.m14_mb.disabled = True
								elif sh == 'F':
									if cm14 == True:
										b.ml.remove_widget(b.m14_mb)
										d.bl.remove_widget(d.m14_bb) ###
										b.m14_mb.active = False
									elif cm14 == False:
											pass
					# m15
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm15':
								b.m15_tal.source = f'img/{sa}.png'
								d.m15_alogo.source = f'img/{sa}.png' ###
								b.m15_tbl.source = f'img/{sb}.png'
								d.m15_blogo.source = f'img/{sb}.png' ###
								b.m15_aln.text = la
								b.m15_bln.text = lb
								d.m15_asn.text = sa ###
								d.m15_bsn.text = sb ###
								b.m15_dt.text = f'{dy}, {dt}\n{tm}'
								d.m15_t.text = f'{dy}, {dt}\n{tm}'###
								cm15 = b.m15_mb.active
								if sh == 'T':
									if cm15 == True:
										if de == 'T':
											b.m15_mb.disabled = False																				
										elif de == 'F':
											b.m15_mb.disabled = True
											d.bl.remove_widget(d.m15_bb) ###
									elif cm15 == False:
										b.ml.add_widget(b.m15_mb)
										d.bl.add_widget(d.m15_bb) ###
										b.m15_mb.active = True
										if de == 'T':
											b.m15_mb.disabled = False
										elif de == 'F':
											b.m15_mb.disabled = True
								elif sh == 'F':
									if cm15 == True:
										b.ml.remove_widget(b.m15_mb)
										d.bl.remove_widget(d.m15_bb) ###
										b.m15_mb.active = False
									elif cm15 == False:
											pass
					# m16
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm16':
								b.m16_tal.source = f'img/{sa}.png'
								d.m16_alogo.source = f'img/{sa}.png' ###
								b.m16_tbl.source = f'img/{sb}.png'
								d.m16_blogo.source = f'img/{sb}.png' ###
								b.m16_aln.text = la
								b.m16_bln.text = lb
								d.m16_asn.text = sa ###
								d.m16_bsn.text = sb ###
								b.m16_dt.text = f'{dy}, {dt}\n{tm}'
								d.m16_t.text = f'{dy}, {dt}\n{tm}'###
								cm16 = b.m16_mb.active
								if sh == 'T':
									if cm16 == True:
										if de == 'T':
											b.m16_mb.disabled = False																				
										elif de == 'F':
											b.m16_mb.disabled = True
											d.bl.remove_widget(d.m16_bb) ###
									elif cm16 == False:
										b.ml.add_widget(b.m16_mb)
										d.bl.add_widget(d.m16_bb) ###
										b.m16_mb.active = True
										if de == 'T':
											b.m16_mb.disabled = False
										elif de == 'F':
											b.m16_mb.disabled = True
								elif sh == 'F':
									if cm16 == True:
										b.ml.remove_widget(b.m16_mb)
										d.bl.remove_widget(d.m16_bb) ###
										b.m16_mb.active = False
									elif cm16 == False:
											pass
					# m17
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm17':
								b.m17_tal.source = f'img/{sa}.png'
								d.m17_alogo.source = f'img/{sa}.png' ###
								b.m17_tbl.source = f'img/{sb}.png'
								d.m17_blogo.source = f'img/{sb}.png' ###
								b.m17_aln.text = la
								b.m17_bln.text = lb
								d.m17_asn.text = sa ###
								d.m17_bsn.text = sb ###
								b.m17_dt.text = f'{dy}, {dt}\n{tm}'
								d.m17_t.text = f'{dy}, {dt}\n{tm}'###
								cm17 = b.m17_mb.active
								if sh == 'T':
									if cm17 == True:
										if de == 'T':
											b.m17_mb.disabled = False																				
										elif de == 'F':
											b.m17_mb.disabled = True
											d.bl.remove_widget(d.m17_bb) ###
									elif cm17 == False:
										b.ml.add_widget(b.m17_mb)
										d.bl.add_widget(d.m17_bb) ###
										b.m17_mb.active = True
										if de == 'T':
											b.m17_mb.disabled = False
										elif de == 'F':
											b.m17_mb.disabled = True
								elif sh == 'F':
									if cm17 == True:
										b.ml.remove_widget(b.m17_mb)
										d.bl.remove_widget(d.m17_bb) ###
										b.m17_mb.active = False
									elif cm17 == False:
											pass
					# m18
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm18':
								b.m18_tal.source = f'img/{sa}.png'
								d.m18_alogo.source = f'img/{sa}.png' ###
								b.m18_tbl.source = f'img/{sb}.png'
								d.m18_blogo.source = f'img/{sb}.png' ###
								b.m18_aln.text = la
								b.m18_bln.text = lb
								d.m18_asn.text = sa ###
								d.m18_bsn.text = sb ###
								b.m18_dt.text = f'{dy}, {dt}\n{tm}'
								d.m18_t.text = f'{dy}, {dt}\n{tm}'###
								cm18 = b.m18_mb.active
								if sh == 'T':
									if cm18 == True:
										if de == 'T':
											b.m18_mb.disabled = False																				
										elif de == 'F':
											b.m18_mb.disabled = True
											d.bl.remove_widget(d.m18_bb) ###
									elif cm18 == False:
										b.ml.add_widget(b.m18_mb)
										d.bl.add_widget(d.m18_bb) ###
										b.m18_mb.active = True
										if de == 'T':
											b.m18_mb.disabled = False
										elif de == 'F':
											b.m18_mb.disabled = True
								elif sh == 'F':
									if cm18 == True:
										b.ml.remove_widget(b.m18_mb)
										d.bl.remove_widget(d.m18_bb) ###
										b.m18_mb.active = False
									elif cm18 == False:
											pass
					# m19
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm19':
								b.m19_tal.source = f'img/{sa}.png'
								d.m19_alogo.source = f'img/{sa}.png' ###
								b.m19_tbl.source = f'img/{sb}.png'
								d.m19_blogo.source = f'img/{sb}.png' ###
								b.m19_aln.text = la
								b.m19_bln.text = lb
								d.m19_asn.text = sa ###
								d.m19_bsn.text = sb ###
								b.m19_dt.text = f'{dy}, {dt}\n{tm}'
								d.m19_t.text = f'{dy}, {dt}\n{tm}'###
								cm19 = b.m19_mb.active
								if sh == 'T':
									if cm19 == True:
										if de == 'T':
											b.m19_mb.disabled = False																				
										elif de == 'F':
											b.m19_mb.disabled = True
											d.bl.remove_widget(d.m19_bb) ###
									elif cm19 == False:
										b.ml.add_widget(b.m19_mb)
										d.bl.add_widget(d.m19_bb) ###
										b.m19_mb.active = True
										if de == 'T':
											b.m19_mb.disabled = False
										elif de == 'F':
											b.m19_mb.disabled = True
								elif sh == 'F':
									if cm19 == True:
										b.ml.remove_widget(b.m19_mb)
										d.bl.remove_widget(d.m19_bb) ###
										b.m19_mb.active = False
									elif cm19 == False:
											pass
					# m20
						for k,v in ll:
							v = v.split(',')
							sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = v
							if cd == 'm20':
								b.m20_tal.source = f'img/{sa}.png'
								d.m20_alogo.source = f'img/{sa}.png' ###
								b.m20_tbl.source = f'img/{sb}.png'
								d.m20_blogo.source = f'img/{sb}.png' ###
								b.m20_aln.text = la
								b.m20_bln.text = lb
								d.m20_asn.text = sa ###
								d.m20_bsn.text = sb ###
								b.m20_dt.text = f'{dy}, {dt}\n{tm}'
								d.m20_t.text = f'{dy}, {dt}\n{tm}'###
								cm20 = b.m20_mb.active
								if sh == 'T':
									if cm20 == True:
										if de == 'T':
											b.m20_mb.disabled = False																				
										elif de == 'F':
											b.m20_mb.disabled = True
											d.bl.remove_widget(d.m20_bb) ###
									elif cm20 == False:
										b.ml.add_widget(b.m20_mb)
										d.bl.add_widget(d.m20_bb) ###
										b.m20_mb.active = True
										if de == 'T':
											b.m20_mb.disabled = False
										elif de == 'F':
											b.m20_mb.disabled = True
								elif sh == 'F':
									if cm20 == True:
										b.ml.remove_widget(b.m20_mb)
										d.bl.remove_widget(d.m20_bb) ###
										b.m20_mb.active = False
									elif cm20 == False:
											pass
				else:
					a.user.helper_text = 'Username is not found'
					a.password.helper_text = ''
class Signup(Screen):
	def submit(self):
		try:
			fname = self.ids.su_fname.text
			lname = self.ids.su_lname.text
			hp = self.ids.su_hp.text
			email = self.ids.su_email.text
			pasw1 = self.ids.su_pasw1.text
			pasw2 = self.ids.su_pasw2.text
			semua = (fname, lname, str(hp), email, pasw1, pasw2)


			if not fname.isalpha():
				self.ids.submit_error.color = 1,0,0,1
				self.ids.submit_error.text = 'First Name must contain Alphabets only'

			else:
				if not lname.isalpha():
					self.ids.submit_error.color = 1,0,0,1
					self.ids.submit_error.text = 'Last Name must contain Alphabets only'
				else: 
					if not hp.isnumeric():
						self.ids.submit_error.color = 1,0,0,1
						self.ids.submit_error.text = 'HP No required numbers only no dash(-) or spacing'				
					else:
						if '@' not in email:
							self.ids.submit_error.color = 1,0,0,1
							self.ids.submit_error.text = 'Invalid Email'
						else:
							if pasw1 != pasw2:
								self.ids.submit_error.color = 1,0,0,1
								self.ids.submit_error.text = 'Password Not Match'
							else:
								cn = psycopg2.connect(
									host = 'ec2-18-215-44-132.compute-1.amazonaws.com',
									database = 'dfutejkpibjm8k',
									user = 'kzgcizenodmacc',
									password = '5a8190e2cd110c90a9f4c35b8d5cfb84a44e2953ce583148ff789ebbb6f82338',
									port = '5432',)
								c = cn.cursor()
								
								c.execute('''CREATE TABLE if not exists dm_cust (								
										   	first_name VARCHAR (30) NOT NULL,
											last_name VARCHAR (30) NOT NULL,
											hp_number NUMERIC (11) NOT NULL,
											email VARCHAR (50) NOT NULL,
											password1 VARCHAR (20) NOT NULL,
											password2 VARCHAR (20) NOT NULL);
											''')

								arahan = '''INSERT INTO dm_cust (
											first_name,
											last_name,
											hp_number,
											email,
											password1,
											password2) 
											VALUES (%s,%s,%s,%s,%s,%s)'''
								nilai = (semua)
								c.execute(arahan, nilai)
								cn.commit()
								cn.close()
								
								self.ids.su_fname.text = ''
								self.ids.su_lname.text = ''
								self.ids.su_hp.text = ''
								self.ids.su_email.text = ''
								self.ids.su_pasw1.text = ''
								self.ids.su_pasw2.text = ''
								# self.ids.submit_error.color = 0,1,0,1
								# self.ids.submit_error.text = 'SIGNUP SUCCESSFULLY'
								self.manager.get_screen('login_page').ids.lp_label.color = 0,1,0,1
								self.manager.get_screen('login_page').ids.lp_label.font_size = 20
								self.manager.get_screen('login_page').ids.lp_label.text = 'Register Successfully\nYou may login now'
								self.parent.current = "login_page"

		except (Exception, psycopg2.Error) as error:
			print("Failed inserting record into mobile table {}".format(error))
			self.ids.submit_error.text = 'SOMETHING IS WRONG! check your internet connection!'
	def clear_form(self):
		try:			
			self.ids.su_fname.text = ''
			self.ids.su_lname.text = ''
			self.ids.su_hp.text = ''
			self.ids.su_email.text = ''
			self.ids.su_pasw1.text = ''
			self.ids.su_pasw2.text = ''
			self.ids.submit_error.text = ''
		except (Exception, psycopg2.Error) as error:
			print("Failed inserting record into mobile table {}".format(error))
			self.ids.submit_error.text = 'SOMETHING IS WRONG! check your internet connection!'
class Main(Screen):
	pass
	def on_enter(self):
		try:	
			a,b = self.ids, self.manager.get_screen('p_a').ids
			c = self.manager.get_screen('login_page').ids 
			d = self.manager.get_screen('a_t').ids 
			with open('img/temp.txt', 'w') as f:
				f.write('')
			with open('img/express.txt', 'w') as f:
				f.write('')
			c.user.text = ''
			c.password.text = ''
			agn = b.agent_log.text
			doc = db.collection('agent').document('account').get()
			x = (doc.to_dict())
			agn_list = sorted([(k,v) for k,v in x.items()])
			for k,v in agn_list:
				v = v.split(',')
				cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
				if agn == li:
					b.cr_l.text = ab
					b.ttl.text = ''
					d.cr_l2.text = ab
					b.ttv.text = ''
					b.curr_display.text = cr
					b.curr_flg.source = f'img/{cr}.png'
					if cr == 'MYR':
						b.curr_txt.text = 'rm'
					else:
						b.curr_txt.text = cr

			doc = db.collection('host').document('game').get()
			x = (doc.to_dict())
			lst = sorted([(k,v) for k,v in x.items()])
			#Clock.schedule_interval(self.end_it, 300.0)
		# append data to m01 to m20
			for k,v in lst:
				v = v.split(',')
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
				kk,ss,dd,tt,ee,\
				s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
				la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,st,cd = v
				if cd == 'm01':
					m01.append(v)
				if cd == 'm02':
					m02.append(v)
				if cd == 'm03':
					m03.append(v)
				if cd == 'm04':
					m04.append(v)
				if cd == 'm05':
					m05.append(v)
				if cd == 'm06':
					m06.append(v)
				if cd == 'm07':
					m07.append(v)
				if cd == 'm08':
					m08.append(v)
				if cd == 'm09':
					m09.append(v)
				if cd == 'm10':
					m10.append(v)
				if cd == 'm11':
					m11.append(v)
				if cd == 'm12':
					m12.append(v)
				if cd == 'm13':
					m13.append(v)
				if cd == 'm14':
					m14.append(v)
				if cd == 'm15':
					m15.append(v)
				if cd == 'm16':
					m16.append(v)
				if cd == 'm17':
					m17.append(v)
				if cd == 'm18':
					m18.append(v)
				if cd == 'm19':
					m19.append(v)
				if cd == 'm20':
					m20.append(v)
		except:
			 self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	# def end_it(self, *arg): # THIS WILL STOP AND DISABLE BETTING MATCH
	# 		doc = db.collection('host').document('game').get()
	# 		x = (doc.to_dict())
	# 		lst = sorted([(k,v) for k,v in x.items()])
	# 		for k,v in lst:
	# 			v = v.split(',')
	# 			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
	# 			kk,ss,dd,tt,ee,\
	# 			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
	# 			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,st,cd = v
	def close_smenu(self):
		try:
			self.ids.small_m.pos_hint = {'x':1,'y':.0}
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def show_smenu(self):
		try:
			self.ids.small_m.pos_hint = {'x':0,'y':.0}
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}

	def m_p_alert_out(self):

		self.ids.m_p_alert.pos_hint = {'x':-1, 'y':-1}
	def m01_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m01
			for l in m01:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m01_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m02_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m02
			for l in m02:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m02_bb.disabled = True
			b.m01_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m03_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m03
			for l in m03:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m03_bb.disabled = True
			b.m02_bb.disabled = False
			b.m01_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m04_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m04
			for l in m04:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m04_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m01_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m05_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m05
			for l in m05:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m05_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m01_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m06_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m06
			for l in m06:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m06_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m01_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m07_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m07
			for l in m07:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m07_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m01_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m08_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m08
			for l in m08:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m08_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m01_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m09_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m09
			for l in m09:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m09_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m01_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m10_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m10
			for l in m10:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m10_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m01_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m11_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m11
			for l in m11:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m11_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m01_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m12_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m12
			for l in m12:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m12_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m01_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m13_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m13
			for l in m13:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m13_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m01_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m14_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m14
			for l in m14:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m14_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m01_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m15_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m15
			for l in m15:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m15_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m01_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m16_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m16
			for l in m16:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m16_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m01_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m17_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m17
			for l in m17:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m17_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m01_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m18_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m18
			for l in m18:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m18_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m01_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m19_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m19
			for l in m19:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m19_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m01_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def m20_call(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			self.parent.current = "p_a"
			global m20
			for l in m20:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m20_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m01_bb.disabled = False
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
# TRY AND EXCEPT POPUP ALERT FOR INTERNET SLOW/ERROR ie_pop()
	ippop = None # EMPTY TEXT INPUT INDICATOR POPUP
	def ie_pop(self): # EMPTY TEXT INPUT ALERT / INTERNET ERROR
		try:
			if not self.ippop:
				self.ippop = MDDialog(
					text = 'Internet too slow, please try again',
					buttons = [
					MDRectangleFlatButton(
					text = 'I Understand',text_color=(1,1,1,1),on_release = self.i_und)],) # POPUP DISMISS
			self.ippop.open()
		except:
			self.ie_pop()
	def i_und(self, obj): # UNDERSTAND POPUP DISMISS
		try:
			self.ippop.dismiss()
		except:
			self.ie_pop()			
# BACK TO MAIN (WITH WARNING OF COINTAIN BET)
	log_out_warning = None # EMPTY TEXT INPUT INDICATOR POPUP
	def low(self): # log out warning
		try:
			try:
				if not self.log_out_warning:
					self.log_out_warning = MDDialog(
						title = 'ARE YOU SURE?',
						text = 'You want to log out?',
						buttons = [
						MDRectangleFlatButton(
						text = 'NO',text_color=(1,1,1,1),on_release = self.dont_logout),
						MDRectangleFlatButton(
						text = 'YES',text_color=(1,1,1,1),on_release = self.yes_logout)],)
				self.log_out_warning.open()
			except:
				self.force_close_low()
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def dont_logout(self, obj):
		try:
			self.log_out_warning.dismiss()
		except:
			self.force_close_bm()
	def force_close_low(self,obj):
		try:
			self.log_out_warning.dismiss()
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
	def yes_logout(self,obj):
		try:
			self.log_out_warning.dismiss()
			self.parent.current = 'login_page'
		except:
			self.ids.m_p_alert.pos_hint = {'x':0, 'y':0}
m01,m02,m03,m04,m05 = list(),list(),list(),list(),list()
m06,m07,m08,m09,m10 = list(),list(),list(),list(),list()
m11,m12,m13,m14,m15 = list(),list(),list(),list(),list()
m16,m17,m18,m19,m20 = list(),list(),list(),list(),list()	
class Play(Screen):
	con_prob = None # EMPTY TEXT INPUT INDICATOR POPUP
# CALCULATOR AND BACK_MAIN AND OTHER BUTTONS
	def back_main(self):
		a = self.ids
		self.parent.current = "m_p"
		a.ab.text = ''
		a.basb.pos_hint = {'x':0, 'y':0}
		a.calc.pos_hint = {'x':1, 'y':0}
		a.m01_bb.disabled = False
		a.m02_bb.disabled = False
		a.m03_bb.disabled = False
		a.m04_bb.disabled = False
		a.m05_bb.disabled = False
		a.m06_bb.disabled = False
		a.m07_bb.disabled = False
		a.m08_bb.disabled = False
		a.m09_bb.disabled = False
		a.m10_bb.disabled = False
		a.m11_bb.disabled = False
		a.m12_bb.disabled = False
		a.m13_bb.disabled = False
		a.m14_bb.disabled = False
		a.m15_bb.disabled = False
		a.m16_bb.disabled = False
		a.m17_bb.disabled = False
		a.m18_bb.disabled = False
		a.m19_bb.disabled = False
		a.m20_bb.disabled = False
		a.calc.pos_hint = {'x':-1, 'y':0}
	def button_press(self, button):
		prior = self.ids.ab.text
		if prior == "0":
			self.ids.ab.text = ""
			self.ids.ab.text = f'{button}'
		else:
			self.ids.ab.text = f'{prior}{button}'									
	def back(self):
		a = self.ids
		a.ab.text = '' # AMOUNT BET
		a.stas.text = ''
		a.basb.pos_hint = {'x':0, 'y':0}
		a.calc.pos_hint = {'x':1, 'y':0}
		a.ne_cr.text = ''
	def padam(self):
		prior = self.ids.ab.text
		prior = prior[:-1]
		prior = self.ids.ab.text = prior
# TEAM A
	def ask(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bask = a.pask.text
		a.stas.text = f'{ta}-{tb} 1-0 ({bask}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def adk(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		badk = a.padk.text
		a.stas.text = f'{ta}-{tb} 2-0 ({badk}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def ads(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bads = a.pads.text
		a.stas.text = f'{ta}-{tb} 2-1 ({bads}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def atk(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		batk = a.patk.text
		a.stas.text = f'{ta}-{tb} 3-0 ({batk}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def ats(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bats = a.pats.text
		a.stas.text = f'{ta}-{tb} 3-1 ({bats}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def atd(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		batd = a.patd.text
		a.stas.text = f'{ta}-{tb} 3-2 ({batd}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def aek(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		baek = a.paek.text
		a.stas.text = f'{ta}-{tb} 4-0 ({baek}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def aes(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		baes = a.paes.text
		a.stas.text = f'{ta}-{tb} 4-1 ({baes}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def aed(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		baed = a.paed.text
		a.stas.text = f'{ta}-{tb} 4-2 ({baed}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def aet(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		baet = a.paet.text
		a.stas.text = f'{ta}-{tb} 4-3 ({baet}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def a5u(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		ba5u = a.pa5u.text
		a.stas.text = f'{ta}-{tb} 5up ({ba5u}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
# DRAW
	def dkk(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bdkk = a.pdkk.text
		a.stas.text = f'{ta}-{tb} 0-0 ({bdkk}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def dss(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bdss = a.pdss.text
		a.stas.text = f'{ta}-{tb} 1-1 ({bdss}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def ddd(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bddd = a.pddd.text
		a.stas.text = f'{ta}-{tb} 2-2 ({bddd}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def dtt(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bdtt = a.pdtt.text
		a.stas.text = f'{ta}-{tb} 3-3 ({bdtt}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def dee(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bdee = a.pdee.text
		a.stas.text = f'{ta}-{tb} 4-4 ({bdee}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
# TEAM B
	def bsk(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbsk = a.pbsk.text
		a.stas.text = f'{tb}-{ta} 1-0 ({bbsk}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def bdk(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbdk = a.pbdk.text
		a.stas.text = f'{tb}-{ta} 2-0 ({bbdk}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def bds(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbds = a.pbds.text
		a.stas.text = f'{tb}-{ta} 2-1 ({bbds}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def btk(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbtk = a.pbtk.text
		a.stas.text = f'{tb}-{ta} 3-0 ({bbtk}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def bts(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbts = a.pbts.text
		a.stas.text = f'{tb}-{ta} 3-1 ({bbts}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def btd(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbtd = a.pbtd.text
		a.stas.text = f'{tb}-{ta} 3-2 ({bbtd}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def bek(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbek = a.pbek.text
		a.stas.text = f'{tb}-{ta} 4-0 ({bbek}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def bes(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbes = a.pbes.text
		a.stas.text = f'{tb}-{ta} 4-1 ({bbes}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def bed(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbed = a.pbed.text
		a.stas.text = f'{tb}-{ta} 4-2 ({bbed}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def b43(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bbet = a.pbet.text
		a.stas.text = f'{tb}-{ta} 4-3 ({bbet}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
	def b5u(self):
		a = self.ids
		crcy = a.curr_txt.text
		ta = a.sf_a.text 
		tb = a.sf_b.text 
		bb5u = a.pb5u.text
		a.stas.text = f'{tb}-{ta} 5up ({bb5u}) {crcy}'
		a.basb.pos_hint = {'x':1, 'y':0}
		a.calc.pos_hint = {'x':0, 'y':0}
# ERASE
	def erase(self):
		try:
			ll,kk,a,b= list(),0,self.ids,self.manager.get_screen('a_t').ids
			htn = self.manager.get_screen('m_p').ids.hid_tn.text
			crcy = a.curr_txt.text 
			cr = a.cr_l.text
			with open('img/express.txt', 'r') as f:
				for l in f:
					ll.append(l)
			with open('img/express.txt', 'w') as fh:
				fh.write('')
			with open('img/express.txt', 'a') as fhd:
				lll = ll[:-1]

				for x in lll:
					fhd.write(x)
			with open('img/express.txt', 'r') as fhd:
				fh = fhd.read()
			a.ttv.text = fh
			check = a.ttv.text

			last = ll[-1:]
			if check != '':
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				for l in last:
					l = l.split()
					avb,sco,pay,bet = l
					bet = bet.split(f'{crcy}')
					l = bet[1]
					prcd = float(cr)+float(l)
					prcd = format(float(prcd),'.2f')
					a.cr_l.text = str(prcd)
					b.cr_l2.text = str(prcd)
					a.ne_cr.text = ''
			else:
				a.ttl.text = ''	
				for l in last:
					l = l.split()
					avb,sco,pay,bet = l
					bet = bet.split(f'{crcy}')
					l = bet[1]
					prcd = float(cr)+float(l)
					prcd = format(float(prcd),'.2f')
					a.cr_l.text = str(prcd)
					a.ne_cr.text = ''

			if htn == '0' or htn == '' and len(check) == 0:
				a.curr_txt.pos_hint = {'x':.57,'y':.935}
				a.curr_lbl.text = ''
			else:
				pass
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
# BUY
	# def alert_in(self):
	# 	a = self.ids
	# 	a.blocker.pos_hint = {'x':0,'y':0}
	# 	a.alert.pos_hint = {'x':.1,'y':.5}
	def buy(self):
		try:
			a,b = self.ids,self.manager.get_screen('t_p').ids
			dd,kk,kr = self.manager.get_screen('m_p').ids,0,0
			check = a.ttv.text 
			agn = self.ids.agent_log.text
		
			doc = db.collection('agent').document('account').get()
			x = (doc.to_dict())
			agl = sorted([(k,v) for k,v in x.items()])
			for k,v in agl:
				v = v.split(',')
				cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
				if agn == li:
					cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
					a.hid_ni.text = ni
			ini = a.hid_ni.text
			ini = int(ini)
			ttl = a.ttl.text
			ttl = ttl.split()
			tl = ttl[1]
			tl = tl.split('rm')
			t = tl[1]
			ttl = format(float(t),'.2f')

			if check == '':
				pass
			elif agn == '':
				a.ttv.text = 'user admin required'
			else:
				self.parent.current = "t_p"
				masa = time.strftime('%a %d'+'/'+'%m'+'/'+'%y %X')
				t_t = a.ttv.text
				#new
				doc = db.collection('agent').document('account').get()
				x = doc.to_dict()
				ll = sorted([(k,v) for k,v in x.items()])
				for k,v in ll:
					v = v.split(',')
					cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
					if agn == li:
						cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
		
						a.hid_tn.text = str(tn)			
				tkt_num = a.hid_tn.text
				ntn = int(tkt_num) + 1
				a.hid_tn.text = str(ntn)

				# ADDING 1 TO THE OLD TICKET NUMBER AND UPDATE THE hid_tn LABEL
				prcd = float(ab)-float(ttl)	
				ttl = format(float(prcd),'.2f')

				ttl = a.ttl.text 
				final_t = f'({agn}) {masa} ({ntn})\n{t_t}{ttl}\n'
				b.tkt.text = final_t 
				a.ttv.text = ''
				a.ttl.text = ''
				with open('img/temp.txt', 'w') as f:
					f.write('')
				tkt = b.tkt.text
				with open('img/comp_ticket.txt', 'w') as f:
					f.write(tkt)
				with open('img/all_ticket.txt', 'a') as f:
					f.write(tkt+'\n')

				ll,gl,kk = list(),list(),0 # (otl = only top line) (wtb = without top and bottom)
				with open('img/comp_ticket.txt', 'r') as f:
					for l in f:
						l = l.rstrip()
						ll.append(l)
				otl = ll[:1]
				for l in otl:
					l = l.split()
					agn,day,dat,tme,tno = l
					agn = agn[1:-1]
					#addtt = f'{cd} {cm} {agn} {day} {dat} {tme} {tno}'
					addtt = f'{cd} {agn} {day} {dat} {tme} {ntn}'
				wtb = ll[1:-1]
				for l in wtb:
					l = l.split()
					avb,sco,pay,bet = l
					rm = bet.split('rm')
					bet = rm[1]
					pay = pay[1:-1]
					aspb = f'{avb} {sco} {pay} {bet}'
					new = f'{addtt} {aspb}'
					gl.append(new)
				for l in gl:
					kk += 1
					ini += 1
					a.hid_ni.text = str(ini)

					l = l.split()
					data2 = f'{agn}_{ini}'
					cd,agn,day,dat,tme,tno,avb,sco,pay,bet = l
					data = {f'{data2}':f'{cd},{agn},{day},{dat},{tme},{ntn},{avb},{sco},{pay},{bet}'}
					db.collection('sales').document(f'{agn}').set(data, merge=True)

			agn = self.ids.agent_log.text
		
			doc = db.collection('agent').document('account').get()
			x = (doc.to_dict())
			agl = sorted([(k,v) for k,v in x.items()])
			for k,v in agl:
				v = v.split(',')
				cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
				if agn == li:
					cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
					ttl = ttl.split()
					ttl = ttl[1]
					ttl = ttl.split('rm')
					ttl = ttl[1]
					nab = float(ab)-float(ttl)
					nab = format(float(nab),'.2f')
					a.cr_l.text = str(f'rm{nab}')
					cd,rn,hn,li,lp,cr,ab,cm,ni,tn
					data = {f'{agn}':f'{cd},{rn},{hn},{li},{lp},{cr},{nab},{cm},{ini},{ntn}'}
					db.collection('agent').document('account').update(data)

			with open('img/comp_ticket.txt', 'w') as f:
				f.write('')
			with open('img/express.txt', 'w') as f:
				f.write('')
		except:
			#self.alert_in()
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def small_menu(self):
		try:
			a = self.ids
			a.small_m.pos_hint = {'x':0,'y':.0}
			#self.parent.current = "m_p"
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def close_smenu(self,*args):
		try:
			a = self.ids
			a.small_m.pos_hint = {'x':1,'y':.0}
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	# def alert_out(self):
	# 	a = self.ids
	# 	a.blocker.pos_hint = {'x':.1,'y':1}
	# 	a.alert.pos_hint = {'x': 1, 'y': 1}
	# 	self.parent.current = "login_page"
	def go_all_tickets(self):
		try:
			self.parent.current = "a_t"
			a,b = self.ids,self.manager.get_screen('p_a').ids
			a.small_m.pos_hint = {'x':1,'y':.0}
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def sac(self): # SALES & COMMISSIONS
		pass
# BACK TO MAIN (WITH WARNING OF COINTAIN BET)
	data_loss_warning = None # EMPTY TEXT INPUT INDICATOR POPUP
	def back_main(self):
		try:
			a = self.ids  
			cie = a.ttv.text # CHECK IF EMPTY
			if cie == '':

				self.parent.current = "m_p"
			else:
				try:
					if not self.data_loss_warning:
						self.data_loss_warning = MDDialog(
							title = 'ARE YOU SURE?',
							text = 'If you leave now it will clear the Bet',
							buttons = [
							MDRectangleFlatButton(
							text = 'NO',text_color=(1,1,1,1),on_release = self.close_bm),
							MDRectangleFlatButton(
							text = 'YES',text_color=(1,1,1,1),on_release = self.yesgo_m_p)],)
					self.data_loss_warning.open()
				except:
					self.force_close_bm()
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def close_bm(self, obj):
		try:
			self.data_loss_warning.dismiss()
		except:
			self.force_close_bm()
	def force_close_bm(self,obj):
		try:
			self.data_loss_warning.dismiss()
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def yesgo_m_p(self,obj):
		try:
			a = self.ids  
			a.ttv.text = ''
			self.data_loss_warning.dismiss()
			self.parent.current = "m_p"
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
# CANCEL ALL BET
	ippop = None # EMPTY TEXT INPUT INDICATOR POPUP
	def cancel_all(self): # EMPTY TEXT INPUT ALERT / INTERNET ERROR
		try:
			a = self.ids  
			cie = a.ttv.text # CHECK IF EMPTY
			if cie == '':
				pass  
			else:
				try:
					if not self.ippop:
						self.ippop = MDDialog(
							title = 'ARE YOU SURE?',
							text = 'You want to CANCEL ALL?',
							buttons = [
							MDRectangleFlatButton(
							text = 'NO',text_color=(1,1,1,1),on_release = self.close_dialog),
							MDRectangleFlatButton(
							text = 'YES',text_color=(1,1,1,1),on_release = self.yes_cancel_all)],)
					self.ippop.open()
				except:
					self.get_off()
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def close_dialog(self, obj):
		try:
			self.ippop.dismiss()
		except:
			self.get_off()
	def yes_cancel_all(self, obj): # UNDERSTAND POPUP DISMISS
		try:
			a,b = self.ids,self.manager.get_screen('a_t').ids
			htn = self.manager.get_screen('m_p').ids.hid_tn.text
			crcy = a.curr_txt.text 
			cl = a.cr_l.text
			ttl = a.ttl.text
			ttl = ttl.split()
			tl = ttl[1]
			tl = tl.split(f'{crcy}')
			t = tl[1]
			ttl = float(t)
			cl = float(cl)
			if htn == '0' or htn == '':
				a.curr_txt.pos_hint = {'x':.57,'y':.935}
				a.curr_lbl.text = ''
			else:
				pass
			try:
				self.ids.ttv.text = ''
				with open('img/express.txt', 'w') as f:
					f.write('')
				a.ttl.text = ''
				self.ippop.dismiss()
				prcd = cl+ttl
				prcd = format(float(prcd),'.2f')
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
			except:
				self.get_off()
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def get_off(self):
		self.ippop.dismiss()
		self.ids.ttl.text = ''
# EXPRESS BET
	def ten(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text
			ep10 = a.exp_10.text
			pick = a.stas.text
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass		
			ptt = f'{pick}{ep10}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep10):
				prcd = float(cr)-float(ep10)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 5)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def twenty(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text 
			ep20 = a.exp_20.text
			pick = a.stas.text
			
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass							
			ptt = f'{pick}{ep20}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep20):
				prcd = float(cr)-float(ep20)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def twentyfive(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text 
			ep25 = a.exp_25.text
			pick = a.stas.text
			
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass							
			ptt = f'{pick}{ep25}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep25):
				prcd = float(cr)-float(ep25)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def fifty(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text 
			ep50 = a.exp_50.text
			pick = a.stas.text
			
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass							
			ptt = f'{pick}{ep50}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep50):
				prcd = float(cr)-float(ep50)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def hundred(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text 
			ep100 = a.exp_100.text
			pick = a.stas.text
			
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass							
			ptt = f'{pick}{ep100}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep100):
				prcd = float(cr)-float(ep100)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def fifteen(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text			
			ep15 = a.exp_15.text
			pick = a.stas.text
			
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass							
			ptt = f'{pick}{ep15}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep15):
				prcd = float(cr)-float(ep15)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def thirty(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text 
			ep30 = a.exp_30.text
			pick = a.stas.text
			
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass							
			ptt = f'{pick}{ep30}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep30):
				prcd = float(cr)-float(ep30)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def eighty(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text 
			ep80 = a.exp_80.text
			pick = a.stas.text
			
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass							
			ptt = f'{pick}{ep80}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep80):
				prcd = float(cr)-float(ep80)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def hundredfifty(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text 
			ep150 = a.exp_150.text
			pick = a.stas.text
			
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass						
			ptt = f'{pick}{ep150}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep150):
				prcd = float(cr)-float(ep150)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def twohundred(self):
		try:
			kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
			crcy = a.curr_txt.text 
			ep200 = a.exp_200.text
			pick = a.stas.text
			
			cr = a.cr_l.text
			if 'rm' in cr:
				cr = cr.split('rm')
				cr = cr[1]
			else:
				pass						
			ptt = f'{pick}{ep200}'+'\n' # PUT TO TEMPORARY TICKET
			
			a.curr_txt.pos_hint = {'x':1,'y':1}
			a.curr_lbl.color = 0,0,0,1
			a.curr_lbl.text = crcy
			if float(cr) >= float(ep200):
				prcd = float(cr)-float(ep200)
				a.ne_cr.text = ''
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				with open('img/express.txt', 'a') as f:
					f.write(ptt)
				with open('img/express.txt', 'r') as fhd:
					for l in fhd:
						l = l.split()
						aa = l[3]
						bb = aa.split(f'{crcy}')
						cc = bb[1]
						kk += int(cc)
				a.ttl.text = f'Total {crcy}{kk}'
				with open('img/express.txt', 'r') as f:
					fh = f.read()
				a.ttv.text = fh
				a.basb.pos_hint = {'x':0, 'y':0}
				a.calc.pos_hint = {'x':-1, 'y':-1}
				a.stas.text = ''
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}		
# BET
	def bet(self):
		kk,a,b = 0,self.ids,self.manager.get_screen('a_t').ids
		crcy = a.curr_txt.text
		k1 = a.stas.text
		k2 = a.ab.text
		cr = a.cr_l.text
		a.curr_txt.pos_hint = {'x':1,'y':1}
		a.curr_lbl.color = 0,0,0,1
		a.curr_lbl.text = crcy
		if not k2.isnumeric() or k2 == '':
			pass
		else:
			if float(cr) >= float(k2):
				prcd = float(cr) - float(k2)
				prcd = format(float(prcd),'.2f')
				a.cr_l.text = str(prcd)
				b.cr_l2.text = str(prcd)
				a.ne_cr.text = ''
				if k2 == '':
					pass
				elif k2 == '0':
					a.ab.text = ''
				else:
					with open('img/temp.txt', 'a') as f:
						f.write(f'{k1}{k2}\n')
					with open('img/temp.txt', 'r') as fh:
						fhd = fh.read()
					a.ttv.text = fhd
					a.ab.text = ''
					a.basb.pos_hint = {'x':0, 'y':0}
					a.calc.pos_hint = {'x':1, 'y':0}
					with open('img/temp.txt', 'r') as fhd:
						for l in fhd:
							l = l.split()
							aa = l[3]
							bb = aa.split(f'{crcy}')
							cc = bb[1]
							kk += int(cc)
					a.ttl.text = f'Total {crcy}{kk}'
			else:
				a.ne_cr.text = 'NOT ENOUGH CREDIT'
				Clock.schedule_once(self.negone, 3)
# NEGONE
	def negone(self,dt):
		try:
			self.ids.ne_cr.text = ''
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
# BOTTOM BUTTONS
	def m01_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m01
			for l in m01:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m01_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m02_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m02
			for l in m02:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m02_bb.disabled = True
			b.m01_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False	
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m03_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m03
			for l in m03:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m03_bb.disabled = True
			b.m02_bb.disabled = False
			b.m01_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m04_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m04
			for l in m04:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m04_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m01_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m05_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m05
			for l in m05:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m05_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m01_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m06_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m06
			for l in m06:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m06_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m01_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m07_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m07
			for l in m07:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m07_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m01_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m08_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m08
			for l in m08:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m08_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m01_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m09_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m09
			for l in m09:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m09_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m01_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m10_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m10
			for l in m10:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m10_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m01_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m11_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m11
			for l in m11:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m11_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m01_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m12_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m12
			for l in m12:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m12_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m01_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m13_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m13
			for l in m13:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m13_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m01_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m14_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m14
			for l in m14:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m14_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m01_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m15_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m15
			for l in m15:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m15_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m01_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m16_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m16
			for l in m16:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m16_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m01_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m17_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m17
			for l in m17:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m17_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m01_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m18_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m18
			for l in m18:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m18_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m01_bb.disabled = False
			b.m19_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m19_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m19
			for l in m19:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m19_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m01_bb.disabled = False
			b.m20_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
	def m20_bbc(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			global m20
			for l in m20:
				sk,dk,ds,tk,ts,td,ek,es,ed,et,au,kk,ss,dd,tt,ee,s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,sc,at = l
			b.pask.text = sk
			b.padk.text = dk
			b.pads.text = ds
			b.patk.text = tk
			b.pats.text = ts
			b.patd.text = td
			b.paek.text = ek
			b.paes.text = es
			b.paed.text = ed
			b.paet.text = et
			b.pa5u.text = au
			b.pdkk.text = kk
			b.pdss.text = ss
			b.pddd.text = dd
			b.pdtt.text = tt
			b.pdee.text = ee
			b.pbsk.text = s0
			b.pbdk.text = d0
			b.pbds.text = d1
			b.pbtk.text = t0
			b.pbts.text = t1
			b.pbtd.text = t2
			b.pbek.text = e0
			b.pbes.text = e1
			b.pbed.text = e2
			b.pbet.text = e3
			b.pb5u.text = bu
			Clock.schedule_once(self.cind, 1/2)
			a.ta_tb.text = f'{la}\nvs\n{lb}'
			ca,cb,cd = (.2,.8,.2,1),(.2,.2,.8,1),(.75,.5,0,1)
			b.pask.background_color = ca
			b.padk.background_color = ca
			b.pads.background_color = ca
			b.patk.background_color = ca
			b.pats.background_color = ca
			b.patd.background_color = ca
			b.paek.background_color = ca
			b.paes.background_color = ca
			b.paed.background_color = ca
			b.paet.background_color = ca
			b.pa5u.background_color = ca		
			b.pdkk.background_color = cd
			b.pdss.background_color = cd
			b.pddd.background_color = cd
			b.pdtt.background_color = cd
			b.pdee.background_color = cd
			b.pbsk.background_color = cb
			b.pbdk.background_color = cb
			b.pbds.background_color = cb
			b.pbtk.background_color = cb
			b.pbts.background_color = cb
			b.pbtd.background_color = cb
			b.pbek.background_color = cb
			b.pbes.background_color = cb
			b.pbed.background_color = cb
			b.pbet.background_color = cb
			b.pb5u.background_color = cb
			b.tal.color = ca 
			b.tbl.color = cb
			b.sf_a.text = sa
			b.sf_b.text = sb
			b.tal.text = la 
			b.tbl.text = lb
			b.alogo.source = f'img/{sa}.png'
			b.jam.text = f'{dy}, {dt}\n{tm}'
			b.blogo.source = f'img/{sb}.png'
			b.m20_bb.disabled = True
			b.m02_bb.disabled = False
			b.m03_bb.disabled = False
			b.m04_bb.disabled = False
			b.m05_bb.disabled = False
			b.m06_bb.disabled = False
			b.m07_bb.disabled = False
			b.m08_bb.disabled = False
			b.m09_bb.disabled = False
			b.m10_bb.disabled = False
			b.m11_bb.disabled = False
			b.m12_bb.disabled = False
			b.m13_bb.disabled = False
			b.m14_bb.disabled = False
			b.m15_bb.disabled = False
			b.m16_bb.disabled = False
			b.m17_bb.disabled = False
			b.m18_bb.disabled = False
			b.m19_bb.disabled = False
			b.m01_bb.disabled = False
		except:
			self.ids.p_a_alert.pos_hint = {'x':0, 'y':0}
# CHANGE INDICATOR
	def cind(self, dt): # CHANGE INDICATOR
		self.ids.ta_tb.text = ''
	def p_a_alert_out(self):
		self.ids.p_a_alert.pos_hint = {'x':-1, 'y':-1}
# GO TO ALL TOTAL
	def gtattl(self):
		# try:	
		a,b = self.ids, self.manager.get_screen('ttl_p').ids
		c,ll = self.manager.get_screen('p_a').ids,list()
		agn = a.agent_log.text
		crcy = a.curr_txt.text
		if crcy == 'MYR':
			crcy = 'rm'
		self.parent.current = "ttl_p"
		Clock.schedule_once(self.close_smenu)
		with open('img/temp.txt', 'w') as f:
			f.write('')

		doc = db.collection('host').document('game').get()
		x = (doc.to_dict())
		game = sorted([(k,v) for k,v in x.items()])

		doc = db.collection('sales').document(f'{agn}').get()
		x = (doc.to_dict())
		asfa = sorted([(k,v) for k,v in x.items()])

		for k,val in game:
			if k == 'mm01':
				mm01.append(val)
			if k == 'mm02':
				mm02.append(val)
			if k == 'mm03':
				mm03.append(val)
			if k == 'mm04':
				mm04.append(val)
			if k == 'mm05':
				mm05.append(val)
			if k == 'mm06':
				mm06.append(val)
			if k == 'mm07':
				mm07.append(val)
			if k == 'mm08':
				mm08.append(val)
			if k == 'mm09':
				mm09.append(val)
			if k == 'mm10':
				mm10.append(val)
			if k == 'mm11':
				mm11.append(val)
			if k == 'mm12':
				mm12.append(val)
			if k == 'mm13':
				mm13.append(val)
			if k == 'mm14':
				mm14.append(val)
			if k == 'mm15':
				mm15.append(val)
			if k == 'mm16':
				mm16.append(val)
			if k == 'mm17':
				mm17.append(val)
			if k == 'mm18':
				mm18.append(val)
			if k == 'mm19':
				mm19.append(val)
			if k == 'mm20':
				mm20.append(val)
	# m01
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m01[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m01_ab = f'{sa}-{sb}'
		m01_ba = f'{sb}-{sa}'
		m01_avb = f'{la} vs {lb}\n\n'
		ll.append(m01_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m01_ab or avb == m01_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m01[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m01_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m01_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m01_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m02
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m02[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m02_ab = f'{sa}-{sb}'
		m02_ba = f'{sb}-{sa}'
		m02_avb = f'{la} vs {lb}\n\n'
		ll.append(m02_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m02_ab or avb == m02_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m02[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m02_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m02_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m02_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m03
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m03[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m03_ab = f'{sa}-{sb}'
		m03_ba = f'{sb}-{sa}'
		m03_avb = f'{la} vs {lb}\n\n'
		ll.append(m03_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m03_ab or avb == m03_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m03[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m03_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m03_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m03_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m04
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m04[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m04_ab = f'{sa}-{sb}'
		m04_ba = f'{sb}-{sa}'
		m04_avb = f'{la} vs {lb}\n\n'
		ll.append(m04_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m04_ab or avb == m04_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m04[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m04_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m04_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m04_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m05
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m05[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m05_ab = f'{sa}-{sb}'
		m05_ba = f'{sb}-{sa}'
		m05_avb = f'{la} vs {lb}\n\n'
		ll.append(m05_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m05_ab or avb == m05_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m05[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m05_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m05_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m05_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m06
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m06[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m06_ab = f'{sa}-{sb}'
		m06_ba = f'{sb}-{sa}'
		m06_avb = f'{la} vs {lb}\n\n'
		ll.append(m06_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m06_ab or avb == m06_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m06[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m06_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m06_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m06_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m07
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m07[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m07_ab = f'{sa}-{sb}'
		m07_ba = f'{sb}-{sa}'
		m07_avb = f'{la} vs {lb}\n\n'
		ll.append(m07_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m07_ab or avb == m07_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m07[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m07_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m07_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m07_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m08
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m08[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m08_ab = f'{sa}-{sb}'
		m08_ba = f'{sb}-{sa}'
		m08_avb = f'{la} vs {lb}\n\n'
		ll.append(m08_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m08_ab or avb == m08_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m08[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m08_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m08_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m08_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m09
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m09[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m09_ab = f'{sa}-{sb}'
		m09_ba = f'{sb}-{sa}'
		m09_avb = f'{la} vs {lb}\n\n'
		ll.append(m09_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m09_ab or avb == m09_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m09[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m09_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m09_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m09_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m10
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m10[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m10_ab = f'{sa}-{sb}'
		m10_ba = f'{sb}-{sa}'
		m10_avb = f'{la} vs {lb}\n\n'
		ll.append(m10_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m10_ab or avb == m10_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m10[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m10_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m10_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m10_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m11
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m11[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m11_ab = f'{sa}-{sb}'
		m11_ba = f'{sb}-{sa}'
		m11_avb = f'{la} vs {lb}\n\n'
		ll.append(m11_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m11_ab or avb == m11_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m11[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m11_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m11_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m11_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m12
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m12[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m12_ab = f'{sa}-{sb}'
		m12_ba = f'{sb}-{sa}'
		m12_avb = f'{la} vs {lb}\n\n'
		ll.append(m12_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m12_ab or avb == m12_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m12[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m12_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m12_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m12_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m13
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m13[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m13_ab = f'{sa}-{sb}'
		m13_ba = f'{sb}-{sa}'
		m13_avb = f'{la} vs {lb}\n\n'
		ll.append(m13_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m13_ab or avb == m13_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m13[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m13_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m13_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m13_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m14
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m14[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m14_ab = f'{sa}-{sb}'
		m14_ba = f'{sb}-{sa}'
		m14_avb = f'{la} vs {lb}\n\n'
		ll.append(m14_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m14_ab or avb == m14_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m14[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m14_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m14_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m14_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m15
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m15[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m15_ab = f'{sa}-{sb}'
		m15_ba = f'{sb}-{sa}'
		m15_avb = f'{la} vs {lb}\n\n'
		ll.append(m15_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m15_ab or avb == m15_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m15[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m15_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m15_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m15_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m16
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m16[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m16_ab = f'{sa}-{sb}'
		m16_ba = f'{sb}-{sa}'
		m16_avb = f'{la} vs {lb}\n\n'
		ll.append(m16_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m16_ab or avb == m16_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m16[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m16_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m16_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m16_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m17
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m17[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m17_ab = f'{sa}-{sb}'
		m17_ba = f'{sb}-{sa}'
		m17_avb = f'{la} vs {lb}\n\n'
		ll.append(m17_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m17_ab or avb == m17_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m17[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m17_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m17_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m17_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m18
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m18[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m18_ab = f'{sa}-{sb}'
		m18_ba = f'{sb}-{sa}'
		m18_avb = f'{la} vs {lb}\n\n'
		ll.append(m18_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m18_ab or avb == m18_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m18[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m18_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m18_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m18_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m19
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m19[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m19_ab = f'{sa}-{sb}'
		m19_ba = f'{sb}-{sa}'
		m19_avb = f'{la} vs {lb}\n\n'
		ll.append(m19_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m19_ab or avb == m19_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m19[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m19_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m19_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m19_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
	# m20
		jum_ke,kira,ll,asm = 0,0,[],[]
		for l in m20[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
		m20_ab = f'{sa}-{sb}'
		m20_ba = f'{sb}-{sa}'
		m20_avb = f'{la} vs {lb}\n\n'
		ll.append(m20_avb)

		for k,v in asfa:
			val = v.split(',')			
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = val			
			data = f'{cd},{rn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
			if agn == rn: # APPEND ONLY NAME THAT NOT STARTSWITH -
				asm.append(data)
		
		for l in asm:
			l = l.split(',')
			cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
			if avb == m20_ab or avb == m20_ba:
				jum_ke += int(bet)
		total = format(float(jum_ke),'.2f')
		for l in m20[-1:]:
			#xx = l.split(',')
			sk,dk,ds,tk,ts,td,ek,es,ed,et,au,\
			kk,ss,dd,tt,ee,\
			s0,d0,d1,t0,t1,t2,e0,e1,e2,e3,bu,\
			la,lb,sa,sb,dy,dt,tm,sh,de,fx,ab,at,cd = l
			if sh != 'T' or de != 'T':
				b.tvp.remove_widget(b.m20_mtv)
			else:
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '1-0':
						kira += int(bet)
						ask = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ask)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '2-0':
						kira += int(bet)
						adk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(adk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '2-1':
						kira += int(bet)
						ads = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ads)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '3-0':
						kira += int(bet)
						atk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '3-1':
						kira += int(bet)
						ats = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ats)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '3-2':
						kira += int(bet)
						atd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(atd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '4-0':
						kira += int(bet)
						aek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '4-1':
						kira += int(bet)
						aes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '4-2':
						kira += int(bet)
						aed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '4-3':
						kira += int(bet)
						aet = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(aet)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '5up':
						kira += int(bet)
						alu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(alu)
				kira = 0
				blank = f'\n'
				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '0-0':
						kira += int(bet)
						dkk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dkk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '1-1':
						kira += int(bet)
						dss = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dss)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '2-2':
						kira += int(bet)
						ddd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(ddd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '3-3':
						kira += int(bet)
						dtt = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dtt)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ab and sco == '4-4':
						kira += int(bet)
						dee = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(dee)
				kira = 0

				ll.append(blank)


				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '1-0':
						kira += int(bet)
						bsk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bsk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '2-0':
						kira += int(bet)
						bdk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bdk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '2-1':
						kira += int(bet)
						bds = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bds)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '3-0':
						kira += int(bet)
						btk = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btk)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '3-1':
						kira += int(bet)
						bts = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bts)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '3-2':
						kira += int(bet)
						btd = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(btd)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '4-0':
						kira += int(bet)
						bek = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bek)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '4-1':
						kira += int(bet)
						bes = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bes)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '4-2':
						kira += int(bet)
						bed = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bed)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '4-3':
						kira += int(bet)
						bets = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(bets)
				kira = 0
				for l in asm:
					l = l.split(',')
					cd,rn,day,dat,tme,tno,avb,sco,pay,bet = l
					if avb == m20_ba and sco == '5up':
						kira += int(bet)
						blu = f'{avb} {sco} ({pay}) {crcy}{kira}\n'
				ll.append(blu)
				ll.append(f'\nTotal sales {crcy}{total}\n')
			for l in ll:
				with open('img/temp.txt', 'a') as f:
					f.write(l)
			with open('img/temp.txt', 'r') as f:
				fh = f.read()
			self.manager.get_screen('ttl_p').ids.m20_l.text = fh
			with open('img/temp.txt', 'w') as f:
				f.write('')
m01,m02,m03,m04,m05 = list(),list(),list(),list(),list()
m06,m07,m08,m09,m10 = list(),list(),list(),list(),list()
m11,m12,m13,m14,m15 = list(),list(),list(),list(),list()
m16,m17,m18,m19,m20 = list(),list(),list(),list(),list()
ask,adk,ads,atk,ats,atd,aek,aes,aed,aet,alu = '','','','','','','','','','',''
dkk,dss,ddd,dtt,dee = '','','','',''
bsk,bdk,bds,btk,bts,btd,bek,bes,bed,bets,blu = '','','','','','','','','','',''
mm01,mm02,mm03,mm04,mm05 = list(),list(),list(),list(),list()
mm06,mm07,mm08,mm09,mm10 = list(),list(),list(),list(),list()
mm11,mm12,mm13,mm14,mm15 = list(),list(),list(),list(),list()
mm16,mm17,mm18,mm19,mm20 = list(),list(),list(),list(),list()
class Ticket(Screen):
	pass
class All_Tickets(Screen):	
	def on_enter(self,*arg):
		try:
			kr,kk,ll,dtl,lst,dlst = 1,0,[],[],[],[]
			with open('img/temp.txt', 'w') as f:
				f.write('')
			a,b = self.ids,self.manager.get_screen('p_a').ids
			agn = b.agent_log.text
			doc = db.collection('sales').document(f'{agn}').get()
			x = (doc.to_dict())
			zz = sorted([(k,v) for k,v in x.items()])
			for k,val in zz:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				value = f'{cod},{nme},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
				if not nme.startswith('-'):
					lst.append((k,value))
				else:
					dlst.append((k,value))
			# GETTING LATEST TICKET NUMBER FOR i count
			doc = db.collection('agent').document('account').get()
			x = (doc.to_dict())
			xx = sorted([(k,v) for k,v in x.items()])
			for k,v in xx:
				v = v.split(',')
				cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
				if agn == li:
					cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v

					# DISPLAY ALL PURCHASED TICKET ON at
					for i in range(int(tn)+1):
						for k,v in lst:
							v = v.split(',')
							cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
							info = f'({nme}) {day} {dat} {tme} ({tno})\n'
							if int(tno) == i:				
								kk += int(bet)
								ll.append(info)
								ll = ll[-1:]
						for k,v in lst:
							v = v.split(',')
							cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
							ticket = f'{avb} {sco} ({pay}) rm{bet}\n'
							if int(tno) == i:
								ll.append(ticket)
						tl1 = f'Total rm{kk}\n\n'
						tl2 = f'Ticket no {i} has been Canceled\n\n'
						if i == 0:
							pass
						else:
							if kk == 0:
								ll.append(tl2)
							else:
								ll.append(tl1)
						for l in ll:
							with open('img/temp.txt', 'a') as f:
								f.write(l)
						with open('img/temp.txt', 'r') as f:
							fh = f.read()
							a.at.text = fh
						ll,kk = [], 0
			Clock.schedule_once(self.dtl)
		except:
			self.ids.a_t_alert.pos_hint = {'x':0, 'y':0}
	def dtl(self, *arg): # THIS WILL DISPLAY ALL DELETED TICKET FROM LIST
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			agn = b.agent_log.text
			#a.dtl.text = "shit"
			#DISPLAY ALL PURCHASED TICKET ON dtl
			kr,kk,ll,dtl,lst,dlst = 1,0,[],[],[],[]
			with open('img/temp.txt', 'w') as f:
				f.write('')
			doc = db.collection('sales').document(f'{agn}').get()
			x = (doc.to_dict())
			zz = sorted([(k,v) for k,v in x.items()])
			for k,val in zz:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				value = f'{cod},{nme},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
				if nme.startswith('-'):
					lst.append((k,value))
			# GETTING LATEST TICKET NUMBER FOR i count
			doc = db.collection('agent').document('account').get()
			x = (doc.to_dict())
			xx = sorted([(k,v) for k,v in x.items()])
			for k,v in xx:
				v = v.split(',')
				cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
				if agn == li:
					# DISPLAY ALL PURCHASED TICKET ON at
					for i in range(int(tn)+1):
						for k,v in lst:
							v = v.split(',')
							cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
							if int(tno) == i:
								head = f'******Ticket ({i}) NOT VALID******\n({nme}) {day} {dat} {tme} ({tno})\n'			
								kk += int(bet)
								ll.append(head)
								ll = ll[-1:]
						for k,v in lst:
							v = v.split(',')
							cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
							ticket = f'{avb} {sco} ({pay}) rm{bet}\n'
							if int(tno) == i:
								ll.append(ticket)
						tl1 = f'Total rm{kk}\n************CANCELED************\n\n'
						tl2 = f'Ticket no {i} has been Deleted\n\n'
						if i == 0:
							pass
						else:
							if kk == 0:
								pass
							else:
								ll.append(tl1)
						for l in ll:
							with open('img/temp.txt', 'a') as f:
								f.write(l)
						with open('img/temp.txt', 'r') as f:
							fh = f.read()
							a.dtl.text = fh				
						ll,kk = [], 0
		except:
			self.ids.a_t_alert.pos_hint = {'x':0, 'y':0}
	def clear_tsv(self):
		try:
			a,b, = self.ids,self.manager.get_screen('a_t').ids
			a.tsv.text = ''
		except:
			self.ids.a_t_alert.pos_hint = {'x':0, 'y':0}
	def cancel_ticket(self):
		try:
			# 1st ALL TICKER (at), 2nd TEMPORARY SCREEN VIEW (tsv), 3rd DELETED TIKET LIST (dtl)
			a,b,kk,kr,agn_ab = self.ids,self.manager.get_screen('p_a').ids,0,0,0
			agn = b.agent_log.text
			with open('img/temp.txt', 'w') as f:
				f.write('')
			top,mid,check,tnum,tsv = list(),list(),list(),list(),list()
			gn = a.gtn.text # GET NUMBER FROM TEXT INPUT

			# GET TOTAL BET
			doc = db.collection('sales').document(f'{agn}').get()
			x = (doc.to_dict())
			atfa = sorted([(k,v) for k,v in x.items()])
			for k,val in atfa:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				if tno == gn and agn == nme:
					kk += int(bet)
			# GET ACCOUNT BALANCE - TOTAL BET (nab)
			doc = db.collection('agent').document('account').get()
			x = (doc.to_dict())
			agac = sorted([(k,v) for k,v in x.items()])
			for k,v in agac:
				v = v.split(',')
				cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
				if agn == li:
					agn_ab = ab
			nab = kk+float(agn_ab)
			nab = format(float(nab),'.2f')
			# DISPLAY A DELETED TICKET ON THE TSV
			dtop = f'***** Ticket no {gn} is INVALID *****\n'
			dbot = f'*********** CANCELED ************\n\n'
			tsv.append(dtop)
			for k,v in atfa:
				v = v.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				title = f'({nme}) {day} {dat} {tme} ({tno})\n' # TOP LINE ONLY
				body = f'{avb} {sco} ({pay}) rm{bet}\n'	
				if tno == gn:
					kr += int(bet)
				if tno == gn and title not in tsv:
					tsv.append(title)
				if tno == gn:
					tsv.append(body)
			total = f'Total rm{kr}\n'
			for k,v in atfa:
				v = v.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				title = f'({nme}) {day} {dat} {tme} ({tno})\n' # TOP LINE ONLY
				body = f'{avb} {sco} ({pay}) rm{bet}\n'
			if total not in tsv:
				tsv.append(total)
			if dbot not in tsv:
				tsv.append(dbot)
			for l in tsv:
				with open('img/temp.txt', 'a') as f:
					fh = f.write(l)
			if len(tnum) == 0:
				a.tsv.text = f'TICKET {gn} NOT FOUND'
				a.gtn.text = ''
			# ALL TICKET FROM AGENT
			for k,val in atfa:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				tnum.append(tno)
				if not gn.isnumeric() or gn == '':
					a.gtn.text = ''
				elif gn not in tnum:
					a.tsv.text = f'Ticket {gn} not exist'
					a.gtn.text = ''
				elif tno == gn and nme.startswith('-'):
					a.tsv.text = f'Ticket {gn} already canceled'
					a.gtn.text = ''
				elif gn == tno and not nme.startswith('-'):
					a.ne_cr2.text = ''
			# ADD (-) TO AGENT NAME
					for k,val in atfa:
						v = val.split(',')
						cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v				
						if tno == gn and not nme.startswith('-'):
							d2 = f'{cod},-{nme},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
							db.collection('sales').document(f'{agn}').update({f'{k}':f'{d2}'})
			# UPDATE THE ACCOUNT BALANCE BY ADDING BACK THE TOTAL BET AMOUNT
					for k,v in agac:
						v = v.split(',')
						cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
						if agn == li:
							cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
							data = {f'{agn}':f'{cd},{rn},{hn},{li},{lp},{cr},{nab},{cp},{ni},{tn}'}
					db.collection('agent').document('account').update(data)
					b.cr_l.text = str(nab)
					a.cr_l2.text = str(nab)
					for k,v in atfa:
						v = v.split(',')
						cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
						if gn == tno:
							with open('img/temp.txt', 'r') as f:
								fh = f.read()
								a.tsv.text = fh
					Clock.schedule_once(self.on_enter)
					a.gtn.text = ''
		except:
			self.ids.a_t_alert.pos_hint = {'x':0, 'y':0}
	def rebuy_tn(self):
		try:
			a,b = self.ids,self.manager.get_screen('p_a').ids
			rby,tnum,kk = list(),list(),0
			a.tsv.text = ''
			with open('img/temp.txt', 'w') as f:
				f.write('')

			rb = a.gdtn.text # THIS IS RE-BUY TICKET NUMBER
			agn = b.agent_log.text
			abal = a.cr_l2.text
			dtl = a.dtl.text
			
			# GETTING ALL SALES FROM AGENT	
			doc = db.collection('sales').document(f'{agn}').get()
			x = (doc.to_dict())
			sales = sorted([(k,v) for k,v in x.items()])

			for k,val in sales:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				if nme.startswith('-'):
					if not tno in tnum:
						tnum.append(tno)
			# GET HEAD
			for k,val in sales:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				head = f'<<<<<<Ticket {rb} is now Valid>>>>>\n({agn}) {day} {dat} {tme} ({tno})\n'
				if tno == rb and nme.startswith('-'):
					if not head in rby:
						rby.append(head)
			# GET BODY
			for k,val in sales:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				body = f'{avb} {sco} ({pay}) rm{bet}\n'
				if tno == rb and nme.startswith('-'):
					rby.append(body)
			# GET TOTAL
			for k,val in sales:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				if tno == rb and nme.startswith('-'):
					kk += int(bet)

			# GET TAIL
			for k,val in sales:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
				tail = f'Total rm{kk}\n<<<<<REBUY SUCCESSFULLY>>>>>\n\n'
				if not tail in rby:
					rby.append(tail)
			# CALCULATING FOR LATEST AGENT ACCOUNT BALANCE
			doc = db.collection('agent').document('account').get()
			x = (doc.to_dict())
			aa = sorted([(k,v) for k,v in x.items()])
			for k,v in aa:
				v = v.split(',')
				if agn == k:
					cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v
			nab = float(ab)-float(kk)
			nab = format(float(nab), '.2f')

			# UPDATING AGENT ACCOUNT BALANCE
			for k,v in aa:
				v = v.split(',')
				cd,rn,hn,li,lp,cr,ab,cp,ni,tn = v

				if agn == li and kk < float(abal):
					data = {f'{agn}':f'{cd},{rn},{hn},{li},{lp},{cr},{nab},{cp},{ni},{tn}'}
					db.collection('agent').document('account').update(data)
					b.cr_l.text = str(nab)
					a.cr_l2.text = str(nab)

			# TRANSFER FROM LIST TO TXT		
			for l in rby:
				with open('img/temp.txt', 'a') as f:
					fh = f.write(l)

			if len(tnum) == 0:
				a.tsv.text = f'REBUY list is empty\nNothing to rebuy'
				a.gdtn.text = ''

			for k,val in sales:
				v = val.split(',')
				cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v

				if not rb.isnumeric() or rb == '':
					a.gdtn.text = ''

				if kk > float(abal):
					a.tsv.text = 'You have reach your credit limit'
					a.gdtn.text = ''				

				elif rb not in tnum:
					a.tsv.text = f'Ticket {rb} not it REBUY list'
					a.gdtn.text = ''
				elif tno == rb and not nme.startswith('-'):
						a.tsv.text = f'Ticket {rb} not it REBUY list'
						a.gdtn.text = ''
				elif tno == rb and nme.startswith('-'):
					for k,val in sales:
						v = val.split(',')
						cod,nme,day,dat,tme,tno,avb,sco,pay,bet = v
						if int(tno) == int(rb):
							d2 = f'{cod},{agn},{day},{dat},{tme},{tno},{avb},{sco},{pay},{bet}'
							db.collection('sales').document(f'{agn}').update({f'{k}':f'{d2}'})
					# DISPLAY TICKET TO TSV
					with open('img/temp.txt', 'r') as f:
						fh = f.read()
						a.tsv.text = fh				
						Clock.schedule_once(self.on_enter)
						a.gdtn.text = ''
		except:
			self.ids.a_t_alert.pos_hint = {'x':0, 'y':0}
	def negone(self,dt):
		try:
			self.ids.ne_cr2.text = ''
		except:
			self.ids.a_t_alert.pos_hint = {'x':0, 'y':0}
	def a_t_alert_out(self):
		
		self.ids.a_t_alert.pos_hint = {'x':-1, 'y':-1}
class Total(Screen):
	pass
class Report(Screen):
	pass
class WindowManager(ScreenManager):
	pass
kv = Builder.load_file('bb_client.kv')
class Bb_cApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = 'BlueGray'

		window_sizes = Window.size
		return WindowManager()
		return Label(text="screen sizes= "+str(window_sizes))
if __name__ == '__main__':
    Bb_cApp().run()