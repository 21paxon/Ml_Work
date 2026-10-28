import pandas as pd
import numpy as np

data = {
    "Student ID": [
        "ST001", "ST002", "ST003", "ST004", "ST005",
        "ST006", "ST007", "ST008", "ST009", "ST010"
    ],
    "Attendance (%)": [
        85, 60, 92, np.nan, 110, 75, 60, 48, 88, 70
    ],
    "Study hours/week": [
        12, 5, 18, 8, 15, np.nan, 5, 3, 14, 9
    ],
    "Previous score": [
        72, 45, 88, 55, 78, 65, 45, 35, 82, 60
    ],
    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Female", "Male", "Female", "M"
    ],
    "Programme": [
        "IT", "Business", "IT", "Business", "IT",
        "IT", "Business", "Business", "IT", "IT"
    ],
    "Final result": [
        "Pass", "Fail", "Pass", "Fail", "Pass",
        "Pass", "Fail", "Fail", "Pass", "Pass"
    ]
}

df = pd.DataFrame(data)
df.to_csv("student.csv", index=False)