# python3
# Makars Sinakovs 221RDB519
def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m//n):
        for j in range(n):
            output.append((j,i))
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    # TODO: create the function
    result=parallel_processing(n,m,data)
    x=len(result)
    # TODO: print out the results, each pair in it's own line
    for i in range(x):
        print(result[i])

if __name__ == "__main__":
    main()
