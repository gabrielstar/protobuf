import pandas as pd
import requests

df = pd.read_csv("creditcard-test.csv", dtype=str)
score = df.drop(columns=["ID", "default payment next month", "PAY_6"], axis=1)
columns = list(score.columns)
request_json = {"fields": columns, "rows": score.values.tolist()}
response = requests.post(
    # headers={"Authorization": "Bearer iufdUSjYfjyKosId37UDj7Qz5Cb9zK5qLVxZ4ljDmeM"},
    url="https://model.cloud-internal.h2o.ai/01309ad2-98b7-433a-b22b-339648686702/model/score",
    json=request_json,
)

print(response.status_code)
response_json = response.json()

print(response_json)
