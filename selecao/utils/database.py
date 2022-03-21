from typing import Dict

from django.db.models import QuerySet


def queryset_to_dict(query_set: QuerySet, key: str, value: str) -> Dict:

    return {
        row.get(key): row.get(value)
        for row in query_set
    }
