from collections import OrderedDict
rivers=OrderedDict()
rivers['nile'] = 'egypt'
rivers['dnepr'] = 'ukrain'
rivers['volga'] = 'russia'
rivers['berezino'] = 'belarus'
for key,value in rivers.items():
    print ('river {} in {}'.format(key.title(), value.title()))