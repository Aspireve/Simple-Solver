# Basic Simplex 
# Note x1, x2, ... xn, s1, s2, .... sn >= 0

import numpy as np

def simplex() :
    # Take Inputs

    # Check Inputs

    # Initialize Inputs
    headers = ["Cb", "Basis", "b", "x1", "x2", "x3", "s1", "s2", "s3", "ratio" ]
    no_of_eq = 3
    obj_coe = {"x1" : 3.0, 
            "x2" : 2.0, 
            "x3" : 5.0,
            "s1" : 0.0, 
            "s2" : 0.0,
            "s3" : 0.0}
    st_coe = [[1.0, 2.0, 1.0, 1.0, 0.0, 0.0 ],
            [3.0, 0.0, 2.0, 0.0, 1.0, 0.0],
            [1.0, 4.0, 0.0, 0.0, 0.0, 1.0]]
    st_val = [430.0, 460.0, 420]
    basis = ["s1", "s2", "s3" ]
    all_basis = ["x1", "x2", "x3", "s1", "s2", "s3"]
    itr = 10
    zj = []
    while itr:
        if(itr > 0):
            pass
        zj = calculateZj(st_coe, obj_coe, no_of_eq, basis, st_val)
        zjmcj = calculateZjmCj(zj, obj_coe,st_coe, all_basis)
        key_col = calculateKeyCol(zjmcj)
        [ratio, key_row] = calculateKeyRow(no_of_eq,st_val, st_coe, key_col)
        
        print(f"\n------ Iteration {itr} ------")

        printTable(headers, obj_coe, basis, st_val, st_coe, key_col, zj, zjmcj, no_of_eq, ratio)
        if (key_col == -1):
            break
        itr -= 1
        mul = st_coe[key_row][key_col]
        for i in range(len(st_coe[0])):
            st_coe[key_row][i] = round(st_coe[key_row][i]/mul,2)
        st_val[key_row] = round(st_val[key_row]/mul, 2)
        for i in range(len(st_coe)):
            if( i != key_row):
                factor = st_coe[i][key_col]
                for j in range(len(st_coe[0])):
                    st_coe[i][j] = round(st_coe[i][j] - (factor * st_coe[key_row][j]), 2)
                st_val[i] = round(st_val[i] - (factor*st_val[key_row]))
        
        # st_val[key_row] = round(st_val[key_row]/mul,2) 
        basis[key_row] = all_basis[key_col]
    print("Maxima Occurs at ")
    for i in range(len(basis)):
        print(basis[i], " : ", st_val[i])
    print (f"Maximum Value is : {zj[0]}")


# Calculates Zj properly
def calculateZj(st_coe, obj_coe, no_of_eq, basis, st_val):
    zj = [0.0 for i in range(len(st_coe[0])+1)]
    for i in range(1,len(st_coe[0])+1):
        z = 0
        for j in range(no_of_eq):
            z = round(z + obj_coe[basis[j]] * st_coe[j][i-1], 2)
        zj[i] = z
    for j in range (no_of_eq):
        zj[0] = round(zj[0] +  obj_coe[basis[j]] * st_val[j], 2)
    return zj

# Calculates Key Column Correctly
def calculateKeyCol(zjmcj):
    mi = zjmcj[0]
    index = 0
    for i in range(len(zjmcj)):
        if(zjmcj[i] < mi):
            mi = zjmcj[i]
            index = i
    return index if mi<0 else -1
    
# Calculates Key Row Correctly 
def calculateKeyRow(no_of_eq, st_val, st_coe, key_col):
    ratio = [0.0 for i in range(len(st_coe))]
    for i in range(no_of_eq):
        if(st_coe[i][key_col] == 0):
            ratio[i] = round(float('inf'),2)
        else:
            ratio[i] = round(st_val[i]/ st_coe[i][key_col],2)
    
    mi = ratio[0]
    index = 0
    for i in range(len(ratio)):
        if(ratio[i] < mi):
            mi = ratio[i]
            index = i
    return [ratio, index]

# Prints zjmcj correctly
def calculateZjmCj(zj, obj_coe,st_coe, all_basis):
    zjmcj = [0.0 for i in range(len(st_coe[0]))]
    for i in range(len(zj)-1):
        zjmcj[i] = round(zj[i+1] - obj_coe[all_basis[i]],2)
    return zjmcj

def printTable(headers, obj_coe, basis, st_val, st_coe, key_col, zj, zjmcj, no_of_eq, key_row):

    #Prints Headers of the Table
    for i in headers:
        print(i, end="\t")
    print("", end = "\n")

    for i in range (no_of_eq):

        """"
        Prints the basis section
        Prints the Value od the middle matrix
        """
        
        print(obj_coe[basis[i]], end= "\t")
        print(basis[i], end = "\t")
        print(st_val[i], end = "\t")
        for j in st_coe[i]:
            print(j, end="\t")

        # Prints the ratio section
        print(key_row[i], end = "\n")

    # Prints the Zj row
    print("\t", "Zj", end="\t")
    for i in zj:
        print(i, end="\t")

    # Prints the Cj row
    print("\n\t", "Cj", end="\t\t")
    for i in obj_coe.values():
        print(i, end="\t")

    # Prints the Zj-Cj row
    print("\n\t", "Zj - Cj", end="\t")
    for i in (zjmcj):
        print(i, end="\t")

    print("\n\n")

if __name__ == "__main__":
    simplex()


