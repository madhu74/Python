from __future__ import division


# Newtons method to find root
def sqtr_n(n):
    root= n/2
    for _ in range(20):
        root=1/2 *((root)+ (n/root))
    return root
print sqtr_n(4)