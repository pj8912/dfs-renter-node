import check


print('*'*20,'Total Storage','*'*20)
print(check.storage.total, "Gib")


print('\n','*'*20, 'Used Storage','*'*20)
print("Free: ",check.storage.used, "GiB")

print(
    
    "\n", " RAM name:" , check.storage.ram_name
)