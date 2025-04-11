from datetime import datetime
print(datetime.strptime(input(), "%Y-%m-%d").strftime("%A"))
