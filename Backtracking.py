def is_valid(maze,x,y,m,n):
    if(x>=0 and x<m and y>=0 and y<n and maze[x][y]==1):
        return True
    return False


def s_maze(maze,m,n):
    x=0;y=0
    sol=[[0 for x in range(5)] for y in range(4)]
    if(solve(maze,x,y,sol,m,n)== False):
        print('there is no feasible path')
        return False
    print(*sol,sep='\n')
    return True


def solve(maze,x,y,sol,m,n):
    if(x==m-1 and y==n-1 and maze[x][y]==1):
        sol[x][y]=1
        return True
    if(is_valid(maze,x,y,m,n)):
        if(sol[x][y]==1):
            return False
        sol[x][y]=1
        if solve(maze,x+1,y,sol,m,n)==True:
            return True
        if solve(maze,x,y+1,sol,m,n)==True:
            return True
        if solve(maze,x-1,y,sol,m,n)==True:
            return True
        if solve(maze,x,y-1,sol,m,n)==True:
            return True
        sol[x][y]=0
        return False

        
def main():
    m=int(input())
    n=int(input())
    l=[[1,0,1,0,1],
       [1,1,0,1,1],
       [0,1,0,1,1],
       [1,1,1,1,1]]
    print(*l,sep='\n')
    s_maze(l,m,n)


main()

        
