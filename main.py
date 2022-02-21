from pm4py.objects.log.importer.xes import importer as xes_importer

log_data = xes_importer.apply('data/BPI_Challenge_2017.xes')

for trace in log_data:
    print(trace)
    for event in trace:
        eventId = event["EventID"]
        user = event["org:resource"]
        time = event["time:timestamp"]
        action = event["Action"]
        name = trace.__dict__["_attributes"]["concept:name"]

#log1 = log[0]
#log2 = log[1]
#log3 = log[2]
#log4 = log[3]
#log5 = log[4]

#print(f"Log 1: {log1}")
#print(f"Log 2: {log2}")
#print(f"Log 3: {log3}")
#print(f"Log 4: {log4}")
#print(f"Log 5: {log5}")
