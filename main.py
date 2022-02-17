from pm4py.objects.log.importer.xes import importer as xes_importer

log = xes_importer.apply('data/BPI_Challenge_2017.xes')

log1 = log[0]
log2 = log[1]
log3 = log[2]
log4 = log[3]
log5 = log[4]

print(f"Log 1: {log1}")
print(f"Log 2: {log2}")
print(f"Log 3: {log3}")
print(f"Log 4: {log4}")
print(f"Log 5: {log5}")
