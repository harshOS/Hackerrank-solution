def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_dist = 0 # apple distance from home
    o_dist = 0 # oranges distance from home
    a_count = 0
    o_count = 0
    for i in range(m):
        a_dist = a + apples[i]
        if a_dist >= s and a_dist <= t:
            a_count += 1
    print(a_count)
    for i in range(n):
        o_dist = b + oranges[i]
        if o_dist >= s and o_dist <= t:
            o_count += 1
    print(o_count)
