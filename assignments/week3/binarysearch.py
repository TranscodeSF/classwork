def search(lst, elt):
    """Return the index of elt in the sorted list lst, or None if the
    given element is not in the list.

    Parameters:
    lst - a sorted list in which to look up the element
    elt - the element to look up
    """
    
    center = len(lst)/2
    if lst[center] == elt:
        return center
    elif lst[center] > elt:
        #must be in the first half
        return search(lst[0:center], elt)
    else:
        #must be in the second half
        return center + search(lst[center:], elt)
    
