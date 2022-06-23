
import os


def jumping_on_clouds(c):
    i=0
    steps=0
    while i<len(c):
        if c[0]!=0:
            return
        if i+2<len(c) and c[i+2]==0:
            i+=2
            steps+=1
        elif i+1<len(c):
            i += 1
            steps += 1
        else:
            i+=1
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
