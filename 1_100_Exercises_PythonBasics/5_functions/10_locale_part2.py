'''Similar to the previous exercise, write a function that extracts the region code from a locale. For example:

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR
'''

def extract_region(locale):
    return locale [3:5]

print(extract_region('en_US.UTF-8'))    
print(extract_region('en_GB.UTF-8'))    
print(extract_region('ko_KR.UTF-16'))

'''launch school solution with split:'

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]'''