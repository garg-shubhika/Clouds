# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from collections import defaultdict
import logging

def main(name: tuple[str, int]) -> tuple[str, int]:
  res = defaultdict(list)
  dataitems = []
  key_shuffler = []
  for i in name:
    keys = i.keys()
    values = i.values()
    for j,k in zip(keys,values):
      dataitems.append((j, k))
  return dataitems
