
import time
from string_literals import e11_raw_grid_string

def e11():
    num_lines = e11_raw_grid_string.strip().split('\n')
    numbers = []
    for l in num_lines:
        numbers.append( [int(s) for s in l.strip().split() ] )

    square_side, adjacency_length, max_prod = 20, 4, 0

    for i in xrange(square_side):
        for j in xrange(square_side):
            down_product, right_product, r_diag_product, l_diag_product = 1, 1,1, 1
            for k in xrange(adjacency_length):
                if j + k < square_side:
                    right_product *= numbers[i][j+k]
                if i + k < square_side:
                    down_product *= numbers[i+k][j]
                if i + k < square_side and j + k < square_side:
                    r_diag_product *= numbers[i+k][j+k]
                if i + k < square_side and j - k >= 0:
                    l_diag_product *= numbers[i+k][j-k]

            max_prod = max( max_prod, right_product, down_product, r_diag_product, l_diag_product )

    return max_prod


if __name__ == '__main__':
    start = time.time()
    print 
    print "Euler 11 solution is:", e11()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % ( 1000 * (end-start ))


