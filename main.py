import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import w
import seaborn as sns
warnings.filterwarnings('ignore')

df=pd.read_csv('3. ciclismo.csv')

df.describe()

sns.pairplot(df)
