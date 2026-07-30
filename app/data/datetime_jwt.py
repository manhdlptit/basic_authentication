from datetime import datetime, timedelta

now = datetime.now()

target_time = datetime(2026,12,31,23,59,59)

expires_delta_refresh = target_time - now

expires_delta_access = timedelta(minutes=5)
# expires_delta_access = timedelta(seconds=25)