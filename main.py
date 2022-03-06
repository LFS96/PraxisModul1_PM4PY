a = 6


def get_mysql_connector():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pm4py"
    )


if a == 6: #Similar Activities
    from pm4py.objects.log.importer.xes import importer as xes_importer
    from pm4py.algo.organizational_mining.sna import algorithm as sna
    from pm4py.visualization.sna import visualizer as sna_visualizer
    log = xes_importer.apply('data/BPI_Challenge_2017.xes')
    ja_values = sna.apply(log, variant=sna.Variants.JOINTACTIVITIES_LOG)
    gviz_ja_py = sna_visualizer.apply(ja_values, variant=sna_visualizer.Variants.PYVIS)
    sna_visualizer.view(gviz_ja_py, variant=sna_visualizer.Variants.PYVIS)

if a == 5: #Roles Discovery
    from pm4py.objects.log.importer.xes import importer as xes_importer
    from pm4py.algo.organizational_mining.roles import algorithm as roles_discovery
    log = xes_importer.apply('data/BPI_Challenge_2017.xes')
    roles = roles_discovery.apply(log)
    print([x for x in roles])
if a == 4:# Handover of Work
    from pm4py.algo.organizational_mining.sna import algorithm as sna
    from pm4py.visualization.sna import visualizer as sna_visualizer
    from pm4py.objects.log.importer.xes import importer as xes_importer

    log = xes_importer.apply('data/BPI_Challenge_2017.xes')
    hw_values = sna.apply(log, variant=sna.Variants.HANDOVER_LOG)
    gviz_hw_py = sna_visualizer.apply(hw_values, variant=sna_visualizer.Variants.PYVIS)
    sna_visualizer.view(gviz_hw_py, variant=sna_visualizer.Variants.PYVIS)

if a == 3:
    import pm4py
    import mysql.connector
    from pm4py.objects.log.importer.xes import importer as xes_importer

    mydb = get_mysql_connector()
    log = xes_importer.apply('data/BPI_Challenge_2017.xes')
    for trace in log:
        print(trace)
        for event in trace:
            eventId = event["EventID"]
            user = event["org:resource"]
            time = event["time:timestamp"]
            action = event["Action"]
            name = trace.__dict__["_attributes"]["concept:name"]
            my_cursor = mydb.cursor()
            sql = "INSERT IGNORE INTO pm4py.log VALUES (%s, %s, %s,%s, %s)"
            val = (eventId, user, time, action, name)
            my_cursor.execute(sql, val)
            mydb.commit()

if a == 2:
    import pm4py
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

    log1 = log[0][0]
    log2 = log[1][0]
    log3 = log[2][0]
    log4 = log[3][0]
    log5 = log[4][0]
    print(f"Log 1: {log1}")
    print(f"Log 2: {log2}")
    print(f"Log 3: {log3}")
    print(f"Log 4: {log4}")
    print(f"Log 5: {log5}")

    log = pm4py.read_xes('data/BPI_Challenge_2017.xes')
    process_tree = pm4py.discover_process_tree_inductive(log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)

if a == 1:
    # https://pm4py.fit.fraunhofer.de/documentation#discovery Directly-Follows Graph

    import os
    from pm4py.objects.log.importer.xes import importer as xes_importer

    from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
    from pm4py.visualization.dfg import visualizer as dfg_visualization

    os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'
    log = xes_importer.apply('data/BPI_Challenge_2017.xes')
    dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)
    parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "svg"}
    gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.PERFORMANCE, parameters=parameters)
    dfg_visualization.save(gviz, "dfg.svg")

    log = xes_importer.apply('data/BPI_Challenge_2017_Offer_log.xes')
    dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)
    parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "svg"}
    gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.PERFORMANCE, parameters=parameters)
    dfg_visualization.save(gviz, "dfg_offer.svg")

print("FERTIG")
