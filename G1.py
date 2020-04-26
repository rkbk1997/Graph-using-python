import xlrd 
import matplotlib.pyplot as plt 
loc = ('Data.xlsx') 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
 
sheet.cell_value(0, 0) 
pt=[]
for i in range(1,sheet.nrows): 
	pt.append(sheet.cell_value(i,0)) 

thal=[]
for i in range(1,sheet.nrows): 
	thal.append(sheet.cell_value(i,1))

plt.plot(pt, thal) 
  

plt.xlabel('Patients') 

plt.ylabel('Absence Of Thal') 
  
 
plt.title('Evaluation in absence of Thal, Slope and CA') 
  

plt.show() 
