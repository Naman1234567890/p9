import pandas as pd
import plotly.express as pe
import statistics
data=pd.read_csv("numbers.csv")
marks = list(data['numbers'])
print(marks)
num_of_elements=len(marks)
sum=0
for i in marks:
    sum=sum+i
mean=sum/num_of_elements
sd=statistics.stdev(marks)
print(sd)