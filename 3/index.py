import requests
import json
url = 'https://shop123z.myshopify.com'
customer_url = url + "/admin/api/2020-10/customers.json"

response = requests.get(url=customer_url,
                        headers={'X-Shopify-Access-Token': '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'})
print(response.json()["customers"])

header = [key for key in response.json()["customers"][0] if key != 'addresses']

data = ' | '.join(header)
for customer in response.json()["customers"]:
    row = []
    for value in header:
        row.append(str(customer[value]))
    data+= "\n" + " | ".join(row)
with open(file="customer.csv", mode='w') as input_file:
    input_file.write(data)