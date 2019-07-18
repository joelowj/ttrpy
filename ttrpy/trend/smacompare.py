from ttrpy.trend.sma import sma  

#compares 2 smas
def smacompare(df,price,sma1,sma2,n1,n2):
	df = sma(df,price,sma1,n1)  
	df = sma(df,price,sma2,n2)
	df[sma1+'/'+sma2] = df[sma1]/df[sma2]
	return df     

#compares 3 smas
def smacompare3(df,price,sma1,sma2,sma3,n1,n2,n3):
	df = sma(df,price,sma1,n1)  
	df = sma(df,price,sma2,n2)
	df = sma(df,price,sma3,n3)
	df[sma1+'/'+sma2] = df[sma1]/df[sma2]
	df[sma2+'/'+sma3] = df[sma2]/df[sma3]
	df[sma1+'/'+sma3] = df[sma1]/df[sma3]
	return df     
