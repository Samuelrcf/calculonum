MAX = 100 

def luDecomposition(mat, n):

 

    lower = [[0 for x in range(n)]

             for y in range(n)]

    upper = [[0 for x in range(n)]

             for y in range(n)]

 

    # Decomposing matrix into Upper

    # and Lower triangular matrix

    for i in range(n): 

        # Upper Triangular

        for k in range(i, n): 

            # Summation of L(i, j) * U(j, k)

            sum1 = 0

            for j in range(i):

                sum1 += (lower[i][j] * upper[j][k]) 

            # Evaluating U(i, k)

            upper[i][k] = mat[i][k] - sum1

 

        # Lower Triangular

        for k in range(i, n):

            if (i == k):

                lower[i][i] = 1  # Diagonal as 1

            else: 

                # Summation of L(k, j) * U(j, i)

                sum2 = 0

                for j in range(i):

                    sum2 += (lower[k][j] * upper[j][i]) 

                # Evaluating L(k, i)

                lower[k][i] = ((mat[k][i] - sum2)/(upper[i][i]))

 

    # setw is for displaying nicely

    print("Lower Triangular\t\tUpper Triangular")

 

    # Displaying the result :

    for i in range(n): 

        # Lower

        for j in range(n):

            print(lower[i][j], end="\t")

        print("", end="\t")

 

        # Upper

        for j in range(n):

            print(upper[i][j], end="\t")

        print("")

 

 

# Driver code

mat = [[2, 3, 1],[1, 2, 3],[3, 1, 2]]                  #ESTE CÓDIGO ESTÁ CORRETO!!!!!!!!!!!!

 

luDecomposition(mat, 3)