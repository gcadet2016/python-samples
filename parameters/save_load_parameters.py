# This code provides functions to save and load parameters using configparser.
# configparser is part of Python's standard library
# Documentation: https://docs.python.org/3/library/configparser.html

import configparser

def save_parameters(file_path, params):
    config = configparser.ConfigParser()
    config['DEFAULT'] = params
    with open(file_path, 'w') as configfile:
        config.write(configfile)

def load_parameters(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config['DEFAULT']

# Example usage:
if __name__ == "__main__":
    parameters = {
        'learning_rate': '0.01',
        'batch_size': '32',
        'num_epochs': '10'
    }
    
    # Save parameters to ini file
    save_parameters('settings.conf', parameters)
    
    # Load parameters from ini file
    loaded_params = load_parameters('settings.conf')
    print(dict(loaded_params))
    print(f"Learning Rate: {loaded_params['learning_rate']}")