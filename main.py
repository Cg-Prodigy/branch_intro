from datetime import date, datetime

t_now = datetime.now().time()
d_now = datetime.now().date()

combined = datetime.combine(d_now, t_now)
