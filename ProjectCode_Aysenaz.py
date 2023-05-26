import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import findspark
findspark.init()
import pyspark
from pyspark.sql import *
from pyspark."sql.types import *
from pyspark.sql.functions import *
spark = SparkSession.builder.master("local[1]") \
    .appName('Aysenaz_Project') \
    .getOrCreate()
sc = spark.sparkContext

schema = StructType() \
    .add("Year", IntegerType(), True) \
    .add("Production", FloatType(), True) \
    .add("Price", FloatType(), True)\
    .add("Area", FloatType(), True) \
    .add("Import", FloatType(), True) \
    .add("Inflation", FloatType(), True)\
    .add("Population", FloatType(), True)\
    .add("Temperature", FloatType(), True)\
    .add("Yield", FloatType(), True)

dataFile="ProjectData_Ayşenaz_Yedekçioğlu.csv"
df_Wheat_Data = spark.read.option("header", True).schema(schema).csv(dataFile)
df_Wheat_Data.printSchema()
df_Wheat_Data.show()
fig1=plt.figure(figsize=(6,6))
#--------------------------Obtain correlation matrix--------------
df_Wheat_Pandas=df_Wheat_Data.toPandas()
df_Corr=df_Wheat_Pandas.dropna()[["Production","Price","Area","Import","Inflation","Population","Temperature"]].corr()
#--------------  Now Over the years

df_Wheat_Data = df_Wheat_Data.sort("Year")
Year_Values=[val.Year for val in df_Wheat_Data.select('Year').collect()]
Production_Values=[val.Production for val in df_Wheat_Data.select('Production').collect()]
Price_Values=[val.Price for val in df_Wheat_Data.select('Price').collect()]
Area_Values=[val.Area for val in df_Wheat_Data.select('Area').collect()]
Import_Values=[val.Import for val in df_Wheat_Data.select('Import').collect()]
Inflation_Values=[val.Inflation for val in df_Wheat_Data.select('Inflation').collect()]
Population_Values=[val.Population for val in df_Wheat_Data.select('Population').collect()]
Temperature_Values=[val.Temperature for val in df_Wheat_Data.select('Temperature').collect()]

#Now cultivation area over the years line chart
plt.ylabel("Cultivation Area (Million Hectares)")
plt.xlabel("Years")
plt.title("Cultivation Area Over the Years")
plt.plot(Year_Values,Area_Values, linewidth='4')
plt.show()

#Now production over the years
plt.title("Wheat Production Over the Years")
plt.ylabel("Wheat Production (Million Tons)")
plt.plot(Year_Values,Production_Values, linewidth='4')
plt.show()

#Now Inflation over the years
plt.ylabel("Inflation Index")
plt.xlabel("Years")
plt.title("Inflation Index Over the Years")
plt.plot(Year_Values,Inflation_Values, linewidth='4')
plt.show()

#Now Imports over the years line chart
plt.ylabel("Wheat Imports")
plt.xlabel("Years")
plt.title("Wheat Imports Over the Years")
plt.plot(Year_Values,Import_Values, linewidth='4')
plt.show()

#Now Price over the years line chart
plt.ylabel("Wheat Price (TL)")
plt.xlabel("Years")
plt.title("Wheat Prices Over the Years")
plt.plot(Year_Values,Price_Values, linewidth='4')
plt.show()

#Now cultivation area and production over the years with twin axes

plt.ylabel("Cultivation Area (Million Hectares)")
plt.xlabel("Years")
plt.title("Cultivation Area and Production Over the Years")
plt.plot(Year_Values,Area_Values, label="Cultivation Area (Million Hectares)", color='blue',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Production (Million Tons)")
plt2.plot(Year_Values,Production_Values, label="Wheat Production Million (Tons)", color='orange',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Production']['Area'],2)), xy=(0.5, 0.1), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Now cultivation area and price over the years with twin axes
plt.ylabel("Cultivation Area (Million Hectares)")
plt.xlabel("Years")
plt.title("Wheat Cultivation Area and Price Over the Years")
plt.plot(Year_Values,Area_Values, label="Cultivation Area (Million Hectares)", color='blue',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Price (TL)")
plt2.plot(Year_Values,Price_Values, label="Wheat Price (TL)", color='orange',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Price']['Area'],2)), xy=(0.5, 0.1), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Now cultivation area and Inflation over the years with twin axes
plt.ylabel("Wheat Cultivation Area (Million Hectares)")
plt.xlabel("Years")
plt.title("Wheat Cultivation Area and Inflation Index Over the Years")
plt.plot(Year_Values,Area_Values, label="Cultivation Area (Million Hectares)", color='blue',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Inflation Index")
plt2.plot(Year_Values,Inflation_Values, label="Inflation Index", color='orange',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Inflation']['Area'],2)), xy=(0.5, 0.1), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Now cultivation area and Imports over the years with twin axes
plt.ylabel("Wheat Cultivation Area (Million Hectares)")
plt.xlabel("Years")
plt.title("Wheat Cultivation Area and Imports Over the Years")
plt.plot(Year_Values,Area_Values, label="Cultivation Area (Million Hectares)", color='blue',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Wheat Imports (Million Tons)")
plt2.plot(Year_Values,Import_Values, label="Wheat Imports (Million Tons)", color='orange',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Import']['Area'],2)), xy=(0.5, 0.1), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Now production and price over the years with twin axes
plt.ylabel("Wheat Production (Million Tons")
plt.xlabel("Years")
plt.title("Wheat Production and Price Over the Years")
plt.plot(Year_Values,Production_Values, label="Production (Million Tons)", color='blue',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Price (TL)")
plt2.plot(Year_Values,Price_Values, label="Wheat Price (TL)", color='orange',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Production']['Price'],2)), xy=(0.5, 0.1), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Now production and Inflation over the years with twin axes
plt.ylabel("Wheat Production (Million Tons")
plt.xlabel("Years")
plt.title("Wheat Production and Inflation Index Over the Years")
plt.plot(Year_Values,Production_Values, label="Production (Million Tons)", color='blue',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Inflation Index")
plt2.plot(Year_Values,Inflation_Values, label="Inflation Index", color='orange',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Production']['Inflation'],2)), xy=(0.5, 0.1), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Now production and Imports over the years with twin axes
plt.ylabel("Wheat Production (Million Tons")
plt.xlabel("Years")
plt.title("Wheat Production and Imports Over the Years")
plt.plot(Year_Values,Production_Values, label="Production (Million Tons)", color='blue',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Wheat Imports (Million Tons)")
plt2.plot(Year_Values,Import_Values, label="Wheat Imports (Million Tons)", color='orange',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Production']['Import'],2)), xy=(0.5, 0.1), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Now Inflation and price and  over the years with twin axes
plt.ylabel("Inflation Index")
plt.xlabel("Years")
plt.title("Inflation Index and Price Over the Years")
plt.plot(Year_Values,Inflation_Values, label="Inflation Index", color='blue',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Wheat Price (TL)")
plt2.plot(Year_Values,Price_Values, label="Wheat Price (TL)", color='orange',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Inflation']['Price'],2)), xy=(0.5, 0.3), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Now Import and price over the years with twin axes
plt.ylabel("Wheat Price (TL)")
plt.xlabel("Years")
plt.title("Wheat Price and Imports Over the Years")
plt.plot(Year_Values,Price_Values, label="Wheat Price (TL)", color='orange',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Imports (Million Tons)")
plt2.plot(Year_Values,Import_Values, label="Wheat Import (Million Tons)", color='blue',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Import']['Price'],2)), xy=(0.5, 0.1), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Now inflation and Import over the years with twin axes
plt.ylabel("Inflation Index")
plt.xlabel("Years")
plt.title("Inflation Index and Imports Over the Years")
plt.plot(Year_Values,Inflation_Values, label="Inflation Index", color='blue',linewidth = '4')
plt.legend(loc='upper left', fontsize=8)
plt2=plt.twinx()
plt2.set_ylabel("Import (Million Tons)")
plt2.plot(Year_Values,Import_Values, label="Wheat Import (Million Tons)", color='orange',linewidth = '4')
plt.legend(loc='upper right', fontsize=8)
plt.annotate('Correlation Coefficient= '+str(np.round(df_Corr['Inflation']['Import'],2)), xy=(0.5, 0.3), xycoords='axes fraction', fontsize=10, style='italic', horizontalalignment='right',verticalalignment='bottom')
plt.grid()
plt.show()

#Finally correlation matrix, seaborn heatmap
fig1=plt.figure(figsize=(7,7))
sns.set(style='white',font_scale=1)
sns.heatmap(df_Corr,fmt='.2f',annot=True,linewidth=2)
plt.yticks(rotation=0)
plt.show()