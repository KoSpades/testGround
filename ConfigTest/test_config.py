import sys
import yaml

def init(path_to_config):
    with open(path_to_config) as config_file:
        total_config = yaml.load(config_file, Loader=yaml.FullLoader)
    return total_config


res = init(sys.argv[1])
print(res["front_end"])
