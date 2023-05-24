'''6 Degrees of Kevin Bacon command line app'''

import sys
from bs4 import BeautifulSoup  # noqa: E501 F401 pylint: disable=unused-import, import-error,line-too-long
sys.path.insert(0, "..")
from six_degrees_of_kevin_bacon import KevinBacon    # noqa: 501 pylint: disable=wrong-import-position,import-error,line-too-long


def main(argv):  # pylint: disable=unused-argument
    """main for Kevin Bacon"""
    my_sd = KevinBacon('/wiki/Six_Degrees_of_Kevin_Bacon')
    my_sd.six_degrees()

    print("As JSON")
    print(my_sd.as_json())

    print("As a List")
    for list_item in my_sd.as_list():
        print(list_item)


if __name__ == "__main__":
    main(sys.argv[1:])
