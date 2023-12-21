import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('salary_dataset.csv')

# Filter the DataFrame for rows where the 'age' column is equal to 26
filtered_data = data[data['age'] == 26]

# Print the rows where 'age' is 26
print(filtered_data)
def love_na_jubjub(n):
    m = n + 1

    # loops for upper part
    for i in range(n // 2 - 1):
        for j in range(m):

            # condition for printing stars to GFG upper line
            if i == n // 2 - 2 and (j == 0 or j == m - 1):
                print("*", end=" ")

            # condition for printing stars to left upper
            elif j <= m // 2 and ((i + j == n // 2 - 3 and j <= m // 4) \
                                  or (j - i == m // 2 - n // 2 + 3 and j > m // 4)):
                print("*", end=" ")

            # condition for printing stars to right upper
            elif j > m // 2 and ((i + j == n // 2 - 3 + m // 2 and j < 3 * m // 4) \
                                 or (j - i == m // 2 - n // 2 + 3 + m // 2 and j >= 3 * m // 4)):
                print("*", end=" ")

            # condition for printing spaces
            else:
                print(" ", end=" ")
        print()

    # loops for lower part
    for i in range(n // 2 - 1, n):
        for j in range(m):

            # condition for printing stars
            if (i - j == n // 2 - 1) or (i + j == n - 1 + m // 2):
                print('*', end=" ")

            # condition for printing GFG
            elif i == n // 2 - 1:

                if j == m // 2 - 1 or j == m // 2 + 1:
                    print(' ', end=" ")
                elif j == m // 2:
                    print(' ', end=" ")
                else:
                    print(' ', end=" ")

            # condition for printing spaces
            else:
                print(' ', end=" ")

        print()

# Set the desired height of the heart (change this value as needed)
n = 10

love_na_jubjub(n)