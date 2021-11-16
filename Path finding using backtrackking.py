def find_dest(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if(l[i][j]==9):
               return (i,j)
    return (0,0)


def is_valid(l,x,y,m,n):
    if(x>=0 and x<m and y>=0 and y<n and l[x][y]==1):
        return True
    return False


def solve(l,a,b,sol,x,y,m,n):
    if(x==a and y==b and l[x][y]==9):
        sol[x][y]=1
        return True
    if(is_valid(l,x,y,m,n)):
        if(sol[x][y]==1):
            return False
        sol[x][y]=1
        if(solve(l,a,b,sol,x+1,y,m,n)==True):
            return True
        if(solve(l,a,b,sol,x,y+1,m,n)==True):
            return True
        if(solve(l,a,b,sol,x-1,y,m,n)==True):
            return True
        if(solve(l,a,b,sol,x,y-1,m,n)==True):
            return True
        sol[x][y]=0
        return False


def solve_mat(l,m,n,a,b):
    x=0;y=0;
    sol=[[0 for i in range(n)]for j in range(m)]
    print(sol)
    if(solve(l,a,b,sol,x,y,m,n)==False):
        return -1
    return sol
               


def main():
    m=5
    n=5
    mat=[[1,1,1,0,0],
         [0,1,1,0,0],
         [0,1,0,9,0],
         [0,1,1,1,0],
         [0,0,1,1,0]]
    a,b=find_dest(mat)
    start=(0,0); end=(a,b)
    print(*solve_mat(mat,m,n,a,b),sep='\n')


main()

        
