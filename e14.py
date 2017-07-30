

import time

collatz_chain_dict = { 1:1, 2:2, 4:3 }

def e14():
    def collatz_chain_length(n):
        if n in collatz_chain_dict:
            return collatz_chain_dict[n]

        if n%2 == 0:
            new_length = collatz_chain_length( n/2 ) + 1
            collatz_chain_dict[n] = new_length
            return new_length
        else:
            new_length = collatz_chain_length( 3*n + 1 )
            collatz_chain_dict[n] = new_length
            return new_length

    max_chain_length, max_chain_index = 0,0
    for i in xrange(1, 10** 6):
        if collatz_chain_length(i) > max_chain_length:
            max_chain_length, max_chain_index = collatz_chain_dict[i], i

    return max_chain_index



if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 14 solution is:",  e14()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
