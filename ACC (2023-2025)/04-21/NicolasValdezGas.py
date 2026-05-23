# Nicolas Valdez Fri Apr 18 15:18:38 2025
# NicolasValdezGas
# Analyzes the gas prices over time and aggregates the data
# Input(s)
# Provided text file
# Output
# Saved as file:
# Average price of gas per year
# Average price of gas per month
# Highest and lowest prices of gas per year
# Gas prices sorted lowest to highest
# Gas prices sorted highest to lowest

import pyinputplus as pyip
import pandas as pd

# Welcoming Statement
print("Analyzes the gas prices over time and aggregates the data.")

# Import file Name
fileName="GasPrices.txt"


def isFileEmpty(fileName):
    data=[]
    with open(fileName) as infile:
        for line in infile:
            data.append(line)
    infile.close()
    length=len(data)
    1/length

def validate(fileName):
    # Exception List
    fileNotFound="File not found"
    divisionByZero="File is empty"
    errors=(fileNotFound,divisionByZero)
    
    try:    
        error=False
        isFileEmpty(fileName)
    except FileNotFoundError:
        print(errors[0])
        error=True
    except ZeroDivisionError:
        print(errors[1])
        error=True
    else:
        pass
    return(error)

def meanMinMaxYear(df):
    """Group dataframe by year to get aggregate data
    on the mean, minimum, and maximum of price for that year."""
    g=df.copy()
    g["year"]=g["date"].dt.year
    g=g.groupby("year")["price"].agg(["mean","min","max"])
    return(g)

def meanMinMaxMonth(df):
    """Group dataframe by month to get aggregate data
    on the mean, minimum, and maximum of price for that month."""
    g=df.copy()
    g["year"]=g["date"].dt.year
    g["month"]=g["date"].dt.month
    g["month"]=pd.to_datetime(g["month"],format="%m").dt.strftime("%B")
    g=g.groupby(["year","month"])["price"].agg(["mean","min","max"])
    return(g)

def dfAsc():
    """Sort dataframe rows from lowest to highest price."""
    df=pd.read_csv(fileName,sep=":",header=None,names=["date","price"],parse_dates=["date"],index_col="date")
    df=df.sort_values("price")
    return(df)

def dfDes():
    """Sort dataframe rows from highest to lowest price."""
    df=pd.read_csv(fileName,sep=":",header=None,names=["date","price"],parse_dates=["date"],index_col="date")
    df=df.sort_values("price",ascending=False)
    return(df)

def main():
    # Input prompts
    choices1=["See minimum, maximum, and average price of gas","See gas prices sorted"]
    choices2=["Group by year","Group by month"]
    choices3=["Sort by lowest to highest price","Sort by highest to lowest price"]
    choices4=["See another table","Exit program"]
    
    # Export file names
    outFiles=["MeanMinMaxYear.txt","MeanMinMaxMonth.txt","GasPricesAscending.txt","GasPricesDescending.txt"]
    
    # Menu selection
    choice1=pyip.inputMenu(choices1,numbered=True)
    if choice1==choices1[0]:
        choice2=pyip.inputMenu(choices2,numbered=True)
        
        if choice2==choices2[0]:
            print(gYear)
            print(f"\nTable saved to {outFiles[0]}\n")
            gYear.to_csv(outFiles[0],sep=":",header=False)
        else:
            print(gMonth)
            print(f"\nTable saved to {outFiles[1]}\n")
            gMonth.to_csv(outFiles[1],sep=":",header=False)
    else:
        choice3=pyip.inputMenu(choices3,numbered=True)
        
        if choice3==choices3[0]:
            print(gAsc)
            print(f"\nFull table saved to {outFiles[2]}\n")
            gAsc.to_csv(outFiles[2],sep=":",header=False)
        else:
            print(gDes)
            print(f"\nFull table saved to {outFiles[3]}\n")
            gAsc.to_csv(outFiles[3],sep=":",header=False)
            
    choice4=pyip.inputMenu(choices4,numbered=True)
    return(choice4,choices4)


# Make dateframes
data=validate(fileName)
if data==False:
    df=pd.read_csv(fileName,sep=":",header=None,names=["date","price"],parse_dates=["date"])
    gYear=meanMinMaxYear(df)
    gMonth=meanMinMaxMonth(df)
    gAsc=dfAsc()
    gDes=dfDes()
    
    # Loop program
    restart=main()
    while restart[0]==restart[1][0]:
        restart=main()
    
# Ending Note
print("Program Ends")