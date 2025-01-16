#!usr/bin/python3

import importlib.util

if __name__ == "__main__":
    module_path = "/tmp/hidden_4.pyc"

    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importliv.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    all_names = dir(hidden_4)

    valid_names = sorted(name for name in all_names if not name.startswith("__"))
    for name in valid_names:
        print(name)
