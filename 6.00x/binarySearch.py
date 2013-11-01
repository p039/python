def biSearch(L, e):

    def wrapperS(L, e, low, high):
        if low == high:
            return L[low] == e
        else:
            mid = low + (low + high)/2
            if e < L[mid]:
                return wrapperS(L, e, 0, mid-1)
            else:
                return wrapperS(L, e, mid+1, high)

    if len(L) == 0:
        return False
    elif e == '':
        return False
    else:

        return wrapperS(L, e, 0, len(L)-1)
