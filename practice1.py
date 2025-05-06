# # def adj(n, edges, matrix):
# #     # adj = {i:{"neighbors": [], "degree": 0} for i in range(1,n+1)}
# #     visited_matrix = [ [ 0 for i in range(len(matrix)) ] for j in range(len(matrix[0])) ]
# #     print(visited_matrix)

# #     nodes = len(matrix) * len(matrix[0]) # No +1 is needed because len() give you 1 indexed value
# #     adj_list = {i: [] for i in range(1, nodes)}
# #     print(adj_list)

# #     # for u, v in edges:
# #     #     adj[u].get("neighbors").append(v)
# #     #     adj[v].get("neighbors").append(u) # If we comment this line the graph become directed from bidirectional or undirected
# #     #     adj[u].update(degree = adj[u].get("degree") + 1)
# #     #     adj[v].update(degree = adj[v].get("degree") + 1) # If we comment this line the graph become directed from bidirectional or undirected
       
# #     # return adj


# def dfs(r,c):
#     stack = [(r,c)] # We initialize the stack with the first_node 
#                 visited_matrix[r][c] = 1 # We visit the node as it has been appended to the stack
#                 area = 0
#                 while stack: # while len(stack) > 0
#                     cn = stack.pop() # LIFO for DFS

#                     row = cn[0]
#                     col = cn[1]
#                     if matrix[row][col] == 1:
#                         # Are the neighbors valid first
#                         # We can have 4
#                         # right = cn[cn[0]+0][cn[1]+1]
#                         if col+1 < len(matrix[0]): # We can't reach it
#                             if matrix[row][col+1] == 1:
#                                 area = area + 1
#                                 visited_matrix[row][col+1] = 1
#                                 stack.append((row, col+1))
#                             else:
                                
#                         else:
#                             pass

                            
#                         if col-1 >= 0 and matrix[row][col-1] == 1:
#                             visited_matrix[row][col-1] = 1
#                             stack.append((row, col-1))
#                         if row+1 < len(matrix) and matrix[row+1][col] == 1:
#                             visited_matrix[row+1][col] = 1
#                             stack.append(row+1, col)
#                         if row-1 >= 0 and matrix[row-1][col] == 1:
#                             visited_matrix[row-1][col] = 1
#                             stack.append(row-1, col)


#                     else:
#                         # If there is water and no land , we dont need to check for neighbours
#                         visited_matrix[row][col] = 1




# def adj(n, edges, matrix):
#     # adj = {i:{"neighbors": [], "degree": 0} for i in range(1,n+1)}
#     visited_matrix = [ [ 0 for i in range(len(matrix)) ] for j in range(len(matrix[0])) ]
#     print(visited_matrix)

#     nodes = len(matrix) * len(matrix[0]) # No +1 is needed because len() give you 1 indexed value
#     adj_list = {i: [] for i in range(1, nodes)}
#     print(adj_list)

    
#     visited_matrix[0][0] = 1 # We visited the node as soon as we append it to the stack

#     # We can go    Right  down    up     left
#     directions = [(0,1), (1,0), (-1,0), (0,-1)]

#     for r in range(len(matrix)):
#         for c in range(len(matrix[0])):
           
#            if visited_matrix[r][c] == 0: # We treat each element in the matrix as the starting node, iff it has not been visited
                
            
#            else:
#                continue


def arraySum(nums):
    def listsum(index, nums):
        n = len(nums)
        if index >= n:
            return 0

        final_sum = nums[index] + listsum(index + 1 , nums)
        print(f"The nums[index] was :{nums[index]} and final_sum is : {final_sum}")

        return final_sum

    final = listsum(0,nums)
    return final

def reverse_a_string(str1):
    def reverse(index, str1):
        if index < 0:
            return ""
        
        reversed1 = str1[index] + reverse(index-1, str1)
        return reversed1
    
    final = reverse(len(str1)-1, str1)
    return final

def howSum(targetSum, nums, memo):
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    if targetSum in memo:
        return memo[targetSum]
    
    for i in range(len(nums)):
        remainder = targetSum - nums[i]
        remainderResult = howSum(remainder, nums, memo)
        if remainderResult is not None:
            remainderResult.append(nums[i])
            memo[targetSum] = remainderResult
            return remainderResult
    
    memo[targetSum] = None
    return None

def bestSum(targetSum, nums, memo):
    if targetSum == 0:
        return [[]]
    
    if targetSum < 0:
        return None
    
    if targetSum in memo:
        return memo[targetSum]
    
    all_combinations = [] 
    for elem in nums:
        print(f"Target Sum is {targetSum} and elem is {elem}")
        remainder = targetSum - elem

        
        remainderResult = bestSum(remainder, nums, memo)
        print(f"Remainder Result is : {remainderResult}")
        memo[targetSum] = remainderResult

        if remainderResult is not None:
            for combo in remainderResult:
                print(f"combo is : {combo} in remainderResult: {remainderResult}")
                new_combo = combo + [elem]
                print(f"new_combo is  : {new_combo}")
                all_combinations.append(new_combo)
                print(f"All_combinations updated : {all_combinations}")
            
            
    if not all_combinations:
        return None
    
    ans = {}
    for combo in all_combinations:
        if combo not in ans:
            ans[combo] = 0
        else:
            ans[combo] = len(combo)

    min = float("inf")
    for val in ans.values():
        if val < min:
            min = val
    
    for key, val in ans.items():
        if val == min:
            print(key, val)


    return all_combinations

def gridTraveler(m,n):

    grid = [[0 for j in range(n+1)] for i in range(m+1) ]
    
    # Just like we used to return the value for the base cases , now we set the values of the base cases.
    grid[1][1] = 1

    print("Before grid : ", grid)
    
    for r in range(m+1):
        for c in range(n+1):
            # First op we go right i.e. column ++ 
            if c+1 <= n:
                grid[r][c+1] += grid[r][c]

            # Second Op we go down i.e. row ++
            if r+1 <= m:
                grid[r+1][c] += grid[r][c]
            
            
    return grid[m][n]


def canSumTabu(targetSum, nums):
    table = [False] * (targetSum + 1)
    table[0] = True

    for i in range(len(table)):
        if table[i] == True:
            for j in range(len(nums)):
                if i+nums[j] < len(table):
                    table[i+nums[j]] = True
    
    print(table)
    return table[targetSum]

def howSumTabu(targetSum, nums):
    table = [None] * (targetSum + 1)
    table[0] = []
    print("The table is: ", table)

    for i in range(len(table)):
        print("Iteration : ", i)
        if table[i] != None:
            for j in range(len(nums)):
                print("i+nums[j]", i+nums[j])
                if i+nums[j] < len(table):
                    table[i+nums[j]] = [] + table[i]
                    table[i+nums[j]].append(nums[j])
                    print(table)
    
    print(table)
    return table[targetSum]


def bestSumTabu(targetSum, nums):
    table = [None] * (targetSum + 1)
    table[0] = []
    print("The table is: ", table)

    for i in range(len(table)):
        print("Iteration : ", i)
        if table[i] != None:
            for j in range(len(nums)):
                print("i+nums[j]", i+nums[j])
                if i+nums[j] < len(table):
                    table[i+nums[j]] = [] + table[i]
                    table[i+nums[j]].append(nums[j])
                    print(table)
    
    print(table)
    return table[targetSum]


def kadanes(nums):
    maxSum = 0

    for i in range(len(nums)):
        currentSum = max(0, currentSum)
        currentSum = abs(currentSum) + nums[i]
        maxSum = max(currentSum, maxSum)
    return maxSum

    


if __name__ == "__main__":
    n = 5
    edges = [
        (1, 2),  # Group 1
        (1, 5),  # Group 1
        (1, 3),  # Group 2
        (2, 4),  # Group 1
        (3, 4)   # Group 2
    ]

    matrix = [
        [1,0],
        [0,1]
    ]

    nums = [2,3,4,5]
    str1 = "abcd"

    # result2 = reverse_a_string(str1)
    # print(result2)

    nums = [7,30]
    targetSum = 300
    memo = {}
    print(bestSum(targetSum, nums, memo))

    # print(howSumTabu(7,[5,3,4]))

    # no of nodes = number of rows * number of columns
    
    # result = arraySum(nums)
    # print(result)