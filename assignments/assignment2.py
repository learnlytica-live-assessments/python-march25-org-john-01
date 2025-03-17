import pandas as pd

def read_data(file_path):
    """
    Reads the CSV file from the given file path and returns a DataFrame.
    """
    # Using pandas to read the CSV file
    df = pd.read_csv(file_path)
    return df

def get_average_salary(df):
    """
    Returns the average salary of the employees.
    """
    # Calculate the mean of the 'Salary' column
    return df['Salary'].mean()

def get_department_counts(df):
    """
    Returns a dictionary with the count of employees per department.
    """
    # Use value_counts to count the number of employees per department
    return df['Department'].value_counts().to_dict()

def get_top_earners(df, n):
    """
    Returns a DataFrame of the top n earners, sorted by salary in descending order.
    """
    # Sort the DataFrame by 'Salary' in descending order and return the top n rows
    return df.sort_values(by='Salary', ascending=False).head(n)

if __name__ == "__main__":
    # For quick testing, read employees.csv from the repository root.
    # This block is only executed when running the file directly.
    df = read_data("employees.csv")
    print("Data from CSV:")
    print(df)
    print("\nAverage Salary:", get_average_salary(df))
    print("\nDepartment Counts:", get_department_counts(df))
    print("\nTop 2 Earners:")
    print(get_top_earners(df, 2))
