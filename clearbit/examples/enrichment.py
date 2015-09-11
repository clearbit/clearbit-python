import clearbit

combined = clearbit.Enrichment.find(email='alex@clearbit.com',stream=True)

print(combined)
