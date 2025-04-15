1. Design DynamoDB Table Structure

DynamoDB is NoSQL, so we need a Partition Key and (optionally) a Sort Key. Based on the table:

Partition Key (PK): stock — groups all entries by stock symbol.

Sort Key (SK): time — allows you to store time-series entries for each stock and retrieve them in order.

2. Export Data from SQLite

Extracting data from sqlite example:

```
import sqlite3
import json

conn = sqlite3.connect("requests.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM requests")
rows = cursor.fetchall()

columns = [column[0] for column in cursor.description]

data = [dict(zip(columns, row)) for row in rows]

with open("requests_data.json", "w") as f:
    json.dump(data, f, indent=4)
```

3. Transform for DynamoDB Format

DynamoDB expects data in a slightly specific format, especially for batch writes. Each item should include the primary keys.

Example Python script to generate DynamoDB PutRequest objects:

```
import json

with open("requests_data.json") as f:
    data = json.load(f)

dynamodb_items = []
for item in data:
    dynamodb_items.append({
        "PutRequest": {
            "Item": {
                "stock": {"S": item["stock"]},
                "time": {"N": str(item["time"])},
                "price": {"N": str(item["price"])},
                "av_7": {"N": str(item["av_7"])},
                "av_14": {"N": str(item["av_14"])},
                "av_21": {"N": str(item["av_21"])},
                "daily_price": {"N": str(item["daily_price"])},
                "month_price": {"N": str(item["month_price"])}
            }
        }
    })

with open("batch_write_requests.json", "w") as f:
    json.dump({"requests": dynamodb_items}, f, indent=2)

```
DynamoDB only allows 25 items per batch, so if you're planning to use AWS CLI, you’ll need to chunk this into 25-item batches.

4. Create DynamoDB Table

You can create the table using AWS Console or the CLI:

```
aws dynamodb create-table \
    --table-name requests \
    --attribute-definitions \
        AttributeName=stock,AttributeType=S \
        AttributeName=time,AttributeType=N \
    --key-schema \
        AttributeName=stock,KeyType=HASH \
        AttributeName=time,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST
```

5. Load Data into DynamoDB

You can now write a Python script using boto3 to insert data, or use the AWS CLI.

```
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("requests")

with open("requests_data.json") as f:
    data = json.load(f)

for item in data:
    table.put_item(Item=item)
```

6. Update Application Logic

Wherever you had something like:

```
SELECT * FROM requests WHERE time = 11111111;
```

You would now use:
```
response = table.query(
    KeyConditionExpression=Key('time').eq('11111111')
)
```
