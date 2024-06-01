def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee,
        how = "left",
        left_on = "managerId",
        right_on = "id")
    df = df.query("salary_x > salary_y").rename({"name_x":"Employee"}, axis = 1)
    return df[["Employee"]]