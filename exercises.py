def elementos_distintos(numeros):
    diff_num = set()
    
    for num in numeros:
        # we return false in case of the set already contains the current element
        if num in diff_num:
            return False
        diff_num.add(num)
        
    return True