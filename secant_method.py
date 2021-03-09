import math

def fungsi(x):
    y = (x*x)-(7*x)-7
    return y

def main():
    xn1 = 1
    xn2 = 2
    x = 9999
    selisih = x-xn1
    error = 0
    print(" x | Selisih ")
    print('------------')

    print(xn2, " | ", 0)
    print(xn1, " | ", selisih)
    
    while(abs(selisih)>error):
        
        x = xn1 - ((fungsi(xn1)*(xn1-xn2)) / (fungsi(xn1)-fungsi(xn2)))
        selisih = x-xn1
        print(x, " | ", selisih)
                   
        xn2 = xn1
        xn1 = x
        
    print("\nAkar Persamaan = ", x, "\t|\t", "Error = ", abs(selisih))
    
main()
