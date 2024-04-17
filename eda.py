import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

# df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])
df = pd.read_csv('./data/house.csv', encoding='cp949')

profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("your_report.html")