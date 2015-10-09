from datetime import datetime
import pytz # $ pip install pytz

current_time = datetime.now(pytz.timezone('Asia/Shanghai'))
print(current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))