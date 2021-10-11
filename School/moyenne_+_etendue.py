import statistics as s

while True:
	list1 = input("list : ")
	list2 = []
	list1 = list1.split(";")

	for x in list1:
		x = x.replace('$', '')
		x = x.replace('\qquad', '')
		list2.append(float(x))


	def moyenne(nb_point_virgule):
		print("moyenne : {}".format(s.mean(nb_point_virgule)))


	def etendue(listnb):
		etendue = max(listnb) - min(listnb)
		print("etendue : {0}".format(etendue))


	etendue(list2)
	moyenne(list2)
