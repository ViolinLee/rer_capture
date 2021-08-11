"""
am6:00-pm8:00,每隔1小时录制30分钟
pm10:00, 录制15分钟
am2:00, 录制15分钟
"""

minute_segments = []
record_hours = [2] + list(range(6, 21+1)) + [22]
record_span_minutes = [15] + [30]*(len(record_hours)-2) + [15]
for i, record_hour in enumerate(record_hours):
    minute_segments.append(list(range(record_hour*60, record_hour*60+(record_span_minutes[i]+1))))

# For Debug
from datetime import datetime
time_now = datetime.now()

for i in range(24):
    time_span = list(range(int(time_now.hour*60+time_now.minute+i*30), int(time_now.hour*60+time_now.minute+i*30+20)))
    minute_segments.append(time_span)
    # print(time_span)