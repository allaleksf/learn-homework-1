import ephem
from datetime import date, datetime

grocery = '/planet Mars'
a=(grocery.split(' ',2))
print(a[1])

today = str(date.today())
today = datetime.strptime(str(date.today()), "%Y-%m-%d").strftime('%Y/%m/%d')
print(today)

ans1= "Mars"
planet = ephem.Mars(today)
constellation = str(ephem.constellation(planet))
ans = (ans1 +"//"+ constellation)
print(ans)