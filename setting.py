"""
am5:00-pm9:00,每1小时录制25分钟
pm11:00, 录制15分钟
am2:00, 录制15分钟
"""

"""
minute_segments = []
record_hours = [2] + list(range(5, 21+1)) + [23]
record_span_minutes = [15] + [25]*(len(record_hours)-2) + [15]
for i, record_hour in enumerate(record_hours):
    minute_segments.append(list(range(record_hour*60, record_hour*60+(record_span_minutes[i]+1))))
"""

"""
# For Debug
from datetime import datetime
time_now = datetime.now()

minute_segments = []
for i in range(24):
    time_span = list(range(int(time_now.hour*60+time_now.minute+i*60), int(time_now.hour*60+time_now.minute+i*60+30)))
    minute_segments.append(time_span)
"""

minute_segments = []
for i in range(24):
    time_span = list(range(int(i*60), int(i*60+31)))
    minute_segments.append(time_span)


print(len(minute_segments))
for segment in minute_segments:
    print(segment)
