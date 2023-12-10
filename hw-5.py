from datetime import date

date = date(2002, 10, 2)
moscow_times = date.strftime('%A %B, %e, %Y')
guardian = date.strftime('%A, %d.%m.%y')
daily_news = date.strftime('%A, %d %B %Y')
