import json
import pickle

def save_index(index, filename):
    """ Save positional index to a file in data directory
    Example: save_index(positional_index, 'positional_index.pkl')
    """
    with open(filename, 'wb') as file:
        pickle.dump(index, file)


def load_index(filename):
    """ Load positional index from a file in data directory
    Example: loaded_positional_index = load_index('positional_index.pkl')
    """
    with open(filename, 'rb') as file:
        index = pickle.load(file)
    return index


def ind2json(pickle_file_name):
    """ Convert pickle-format serialized output of index to json human-readable format
    """
    with open(f"data/{pickle_file_name}", 'rb') as file:
        serialized_dict = pickle.load(file)

    # Convert the dictionary to JSON format
    json_data = json.dumps(serialized_dict, indent=2)

    # Write the JSON data to the output file
    with open(f"data/{pickle_file_name}-converted.json", 'w') as json_file:
        json_file.write(json_data)