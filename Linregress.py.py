import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

df = pd.read_csv("C:/Users/chiar/Downloads/Study_vs_Score_data.csv")

x_data = df["Attendance_Hours"]
y_data = df["Final_Marks"]

A, B , r, p, re = stats.linregress(x_data, y_data)

formula = f"y = {A:.2f}x + {B:.2f}"
correlacao = f"Coeficiente de correlação (r): {r:.4f}"

x=[]
y=[]

for i in range(90):
    x.append(i)
    y.append(A*i + B)
    
plt.figure(figsize=(8,6), dpi=100)
plt.scatter(x_data, y_data)
plt.plot(x, y, color="red")
plt.text(5, max(y_data)-5, formula, fontsize=10, color='blue') 
plt.show()