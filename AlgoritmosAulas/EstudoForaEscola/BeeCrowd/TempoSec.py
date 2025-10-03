TempoT = int(input())

hora= TempoT//3600
min= (TempoT%3600)//60
sec=   ((TempoT%3600)%60)

print("{}:{}:{}".format(hora,min,sec))