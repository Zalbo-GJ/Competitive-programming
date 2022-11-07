def minimumBuckets(self, street):
    """
    :type street: str
    :rtype: int
    """
    block = list(street)
    buckets = 0
    for i in range(len(block)):
        if block[i] == 'H':
            if i > 0 and block[i-1] == 'B':
                continue
            if i < len(block)-1 and block[i+1] == '.':
                block[i+1] = "B"
                buckets += 1
                continue
            if i > 0 and block[i-1] == '.':
                block[i-1] = 'B'
                buckets += 1
                continue
            return -1
    return buckets
