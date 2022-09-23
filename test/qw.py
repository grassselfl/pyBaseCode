import datetime
import decimal

now = datetime.datetime.now()
if now.hour < 15:
    reject_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")



print("{:.2f}".format(1313131553.321515))
print("{:,}".format(decimal.Decimal("{:.2f}".format(1))))
print("{:,}".format(decimal.Decimal("{:.2f}".format(decimal.Decimal("1231231.3232")))))