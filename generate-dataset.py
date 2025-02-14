from faker import Faker
import numpy as np
import pandas as pd

fake = Faker()
data = {
    "name": [fake.name() for _ in range(1000)],
    "age": np.random.randint(20, 60, 1000),
    "salary": np.random.randint(30000, 120000, 1000),
    "city": [fake.city() for _ in range(1000)],
}
df = pd.DataFrame(data)
df.to_csv("mock_data.csv", index=False)
