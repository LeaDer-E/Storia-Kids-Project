
# config.py
'''
PAS_List = [
]


Cst_No_Answer_List = [
    
    ]



# Open PCC.txt and read the data
with open('PCC.txt', 'r') as file:
    data = file.read().split()

# Convert the data to integers
PCC_List = list(map(int, data))


STD_List = [

]



DW_List = [
 
]
'''

def read_file_to_list(filename):
    with open(filename, 'r') as file:
        return list(map(int, file.read().split()))

# Read data from each text file into respective lists
PCC_List = read_file_to_list('PCC.txt')
PAS_List = read_file_to_list('PAS.txt')
Cst_No_Answer_List = read_file_to_list('NoRes.txt')
STD_List = read_file_to_list('STD.txt')
DW_List = read_file_to_list('DW.txt')




