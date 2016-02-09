#JORGE VICENTE VIOLA
import random

rest={'p1':0,'p2':0,'p3':0 }
N=10000
for i in range(N):
	exp=['cabra','cabra','cabra']
	coche=random.randrange(3)
	exp[coche]='coche'
	
	player=random.randrange(3)
	select=[x for x in range(3) if exp[x] is not 'coche' and x is not player][0] #presentador
	
	if exp[player]=='coche':
		rest['p1']+=1

	otra=[x for x in range(3) if x  not in(player, select) ][0]
	
	if random.randrange(2)==0:
		r=player
	else:
		r=otra
	if exp[r]=='coche':
		rest['p2']+=1

	if exp[otra]=='coche':
		rest['p3']+=1

for n,r in rest.iteritems():
	print n, (r*100)/N, '%'

