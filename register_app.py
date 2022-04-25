import sys
import yaml

from dsapplicationregistration.dsar_core import register_connectors, __test_registration

def parse_config(path_to_config):
    with open(path_to_config) as config_file:
        res_config = yaml.load(config_file, Loader=yaml.FullLoader)
    return res_config


if __name__ == "__main__":

    # take path to connector from command line
    # FIXME: use argparse and do this properly
    app_config = parse_config(sys.argv[1])
    connector_name = app_config["connector_name"]
    connector_module_path = app_config["connector_module_path"]
    print("connector name: " + str(connector_name))
    print("connector module path: " + str(connector_module_path))

    # and register that module
    register_connectors(connector_name, connector_module_path)

    print("Testing registration")
    __test_registration()

    app_config = parse_config(sys.argv[2])
    connector_name = app_config["connector_name"]
    connector_module_path = app_config["connector_module_path"]
    print("connector name: " + str(connector_name))
    print("connector module path: " + str(connector_module_path))

    # and register that module
    register_connectors(connector_name, connector_module_path)

    print("Testing registration")
    __test_registration()
