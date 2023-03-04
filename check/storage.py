import psutil 

store = psutil.disk_usage('/')

#RAM
mem_info = psutil.virtual_memory()
ram_size_in_gb = round(mem_info.total / (1024 ** 3), 2)


#hdd or ssd
total= store.total / (2**30)
used = store.used / (2**30)
free = store.free / (2**30)

