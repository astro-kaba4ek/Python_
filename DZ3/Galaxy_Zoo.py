# coding: utf-8

from urllib.request import urlretrieve
from multiprocessing import Pool


def func(lst):

	coords = lst[0]
	k = lst[1]
	n = lst[2]

	M = [i for i in range(len(coords))]

	for i in M[k::n]:
		pic = f"http://skyservice.pha.jhu.edu/DR12/ImgCutout/getjpeg.aspx?ra={coords[i][1]}&dec={coords[i][2]}&scale=0.2&width=600&height=600&opt=G" 
		urlretrieve(pic, f"GZ_pic/{coords[i][0]}.jpeg")

		if i > 30: break



if __name__ == '__main__':

	# Выбираем тип:
	# GType = 4 # P_EL
	# GType = 5 # P_CW
	# GType = 6 # P_ACW
	GType = 7 # P_EDGE


	# Читаем таблицу
	table = open("GalaxyZoo1_DR_table2.csv")

	lst = table.readlines()
	table.close()

	lst = lst[1:]

	coords = []

	# Собираем coords[Name, RA, DEC] из галактик только нужного типа 
	for i, s in enumerate(lst):

		lst[i] = s.split(",")[:8]

		if lst[i].index(max(lst[i][4:])) == GType:
			coords.append(lst[i][0:3])



	# Параллелим
	n = 5

	array = []

	for i in range(n):
		array.append([coords, i, n])

	pool = Pool(n)
	
	pool.map(func, array)

