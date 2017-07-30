import time
from string_literals import e18_triangle_string

def e18():
    lines = e18_triangle_string.strip().split('\n')
    numbers, max_path_sums = [], []
    for l in lines:
        numbers.append( [int(s) for s in l.strip().split(' ') ] )
        max_path_sums.append( [ 0 for _ in l.strip().split(' ') ] )

    for i in xrange( len(numbers) ):
        if i == 0:
            max_path_sums[i][i] = numbers[i][i]
        else:
            for j in xrange(i+1):
                if j == 0:
                    max_path_sums[i][j] = max_path_sums[i-1][j] + numbers[i][j]
                if j == i:
                    max_path_sums[i][j] = max_path_sums[i-1][j-1] + numbers[i][j]
                if j > 0 and j < i:
                    max_path_sums[i][j] = max( max_path_sums[i-1][j-1], max_path_sums[i-1][j] ) + numbers[i][j]

    return max( max_path_sums[ len(numbers) - 1 ]) 

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 18 solution is:",  e18()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
