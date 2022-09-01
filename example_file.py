import pandas as pd

arrays = [["Bear", "Bear", "Canary", "Canary"], ["Captive", "Wild", "Captive", "Wild"]]
index = pd.MultiIndex.from_arrays(arrays, names=("Animal", "Type"))
df = pd.DataFrame({"Max Speed": [490.0, 450.0, 50.0, 40.0]}, index=index)
