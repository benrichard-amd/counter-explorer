import yaml
import json
import sys

counters_file = sys.argv[1]

with open(counters_file, 'r') as f:
    data = yaml.safe_load(f)


del data['schema-version']


new_data = []
for counter in data:
  
  ctr = {}
  ctr['name'] = counter
  ctr['description'] = data[counter]['description']
  
  archs = data[counter]['architectures']
  arch_list = []   
  for arch in archs.keys():
    #print(arch)
    #print(data[counter]['architectures'])
    ar = {}
    ar['architectures'] = arch.split('/')
    if 'block' in data[counter]['architectures'][arch]:
      ar['block'] = data[counter]['architectures'][arch]['block']
    if 'event' in data[counter]['architectures'][arch]:
      ar['event'] = data[counter]['architectures'][arch]['event']

    arch_list.append(ar)

  ctr['arch'] = arch_list 
  #ctr['arch'] = data[counter]['architectures'].split('/')

  new_data.append(ctr)

with open('counter_defs.json', 'w') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
  
