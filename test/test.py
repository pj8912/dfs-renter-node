import psutil 
#RAM
mem_info = psutil.virtual_memory()

ram_name =  mem_info._asdict().get('total')

print(ram_name)


size_in_gb = round(mem_info.total / (1024 ** 3), 2)
print(f"Total Memory: {size_in_gb} GB")


def get_storage_type():
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        if partition.fstype != '':
            usage = psutil.disk_usage(partition.mountpoint)
            if usage.percent < 90:
                if 'ssd' in partition.opts.lower():
                    return 'SSD'
                else:
                    return 'HDD'
    return 'Unknown'

# print(get_storage_type())


def is_ssd():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'sd' in partition.device:
            usage = psutil.disk_usage(partition.mountpoint)
            if usage.percent < 10 and 'ssd' in partition.opts:
                return True
    return False

# if is_ssd():
#     print("Storage device is an SSD")
# else:
#     print("Storage device is an HDD")


#*******************************************************************************************************

import subprocess

def get_storage_type():
    output = subprocess.check_output("lsblk -o NAME,MODEL | grep -v loop", shell=True)
    lines = output.decode().strip().split('\n')
    for line in lines:
        columns = line.strip().split()
        if len(columns) > 1:
            model = ' '.join(columns[1:])
            if 'SSD' in model:
                return 'SSD'
            elif 'HDD' in model:
                return 'HDD'
    return 'Unknown'

print(get_storage_type())

