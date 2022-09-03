#Funcion que agarra una lista y un objetivo.
#Variables: Medio, comienzo, final, pasos.
#Recursión o while loop.
#Seguimiento de las variables y, principalmente, los pasos/
def binarySearch(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("Paso: ", steps, "\n", str(list[start:end+1]))
        steps = steps + 1
        middle = (start+end) // 2  #Entire division

        if target == list[middle]:
            print("The value ", list[middle], "is in position ", middle)
            return middle
        if target < list[middle]:
            end = middle-1
        else:
            start = middle+1
    
    return (print("Sorry, not found!"))

list1 = [1,2,3,4,5,6,7,8,10,11,12,13,14]
target1 = 9
binarySearch(list1, target1)