import xlrd

arquivo = xlrd.open_workbook('projetos.xls')
planilha = arquivo.sheet_by_index(0)
    
lista_final = []
for i in range(planilha.nrows):
	#col1 = planilha.row_values(i)[0]
	col2 = planilha.row_values(i)[planilha.ncols - 1]
	temp = (col2,i)
	lista_final.append(temp)
	#print i
lista_final.sort()
lista_final.reverse()
for i in range(planilha.nrows):
	print planilha.row_values(lista_final[i][1])[0]
#print lista_final