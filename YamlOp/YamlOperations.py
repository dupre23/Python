import yaml

class YamlOperations:
    def __init__(self, path_to_file, type):
        self.yaml_dict = {}
        with open(path_to_file, "r") as file:
            try:
                content = yaml.safe_load(file)
            except yaml.YAMLError as e:
                print("Error when loading 'yaml' file", "\n", e)
            else:
                if type == "network_config":
                    self.yaml_dict["network_config"] = content

    def listNetworkConfig(self):
        print(yaml.dump(self.yaml_dict["network_config"]["network"]["ethernets"]))

