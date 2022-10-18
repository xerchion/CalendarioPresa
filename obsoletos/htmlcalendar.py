import calendar


calendario_HTML = calendar.HTMLCalendar(calendar.MONDAY)
tablaHTML = calendario_HTML.formatmonth(2020, 2)
print(tablaHTML)