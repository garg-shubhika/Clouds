# This function is not intended to be invoked directly. Instead it will be triggered by an HTTP starter function.
# Before running this sample, please add azure-functions-durable to requirements.txt
# Run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df
from collections import Counter

def orchestrator_function(context: df.DurableOrchestrationContext):
    temp = []
    input = yield context.call_activity('GetInputDataFn', None)
    Mapper = []
    for file in input:
        Mapper.append(context.call_activity('Mapperfunction', file))
    shuffler_results= yield context.task_all(Mapper)
    result_a = yield context.call_activity('shuffler', shuffler_results)
    reducer = []
    for file2 in result_a:
        reducer.append(context.call_activity('reducer', file2))
    results2 = yield context.task_all(reducer)
    val = Counter(results2)
    print(val)
    return val
main = df.Orchestrator.create(orchestrator_function)