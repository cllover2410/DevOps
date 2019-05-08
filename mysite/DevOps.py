#%%
import psutil

mem = psutil.virtual_memory()

print(mem.total,mem.used)
