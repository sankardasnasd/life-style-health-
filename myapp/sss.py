
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

print("Yesterday was:", yesterday)
