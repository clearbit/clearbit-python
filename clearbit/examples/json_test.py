import clearbit
import json

combined = clearbit.Enrichment.find(email='alex@clearbit.com',stream=True)

print(json.dumps(combined))
