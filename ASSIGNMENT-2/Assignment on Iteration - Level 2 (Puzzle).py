def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if (heads>=legs or legs%2!=0 or heads==0):
        print(error_msg)
    else:
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))
solve(4,19)