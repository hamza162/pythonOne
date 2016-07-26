    
def wutfunc(array):
    for x in array:
        if x%2 == 0 or x ==1:
            print "yeah evens"
        else:
            print "yeah odds"

ar = [1,8,3,2,4,5,6,4]
ab = [5,3,5,56,7,43,7]
hah = ar + ab
print hah
wutfunc(hah)

