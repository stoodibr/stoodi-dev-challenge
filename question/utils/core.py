from typing import Any, Dict


def sort_dict_by_keys(unsorted_dict: Dict[str, Any]) -> Dict[str, Any]:
    return {key: unsorted_dict[key] for key in sorted(unsorted_dict)}
