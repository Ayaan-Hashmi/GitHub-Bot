import os

def makeCommits(days: int) -> int:
    if days < 1:
        os.system('git push')
        return 1  # Base case should return an integer
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!!\n')

        # staging
        os.system('git add data.txt')

        # commit
        os.system(f'git commit --date="{dates}" -m "First commit for the day!"')

        return makeCommits(days - 1)  # Recursive case should return the result of the next call

# Call the function
makeCommits(365)
