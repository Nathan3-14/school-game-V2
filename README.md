# School Game V2
## World Schema
```json
{
    "sections": [
        {
            "map": [
            ],
            "tl_bound": [<x: int>, <y: int>],
            "br_bound": [<x: int>, <y: int>]
        },
        {
            "map": [
            ],
            "tl_bound": [<x: int>, <y: int>],
            "br_bound": [<x: int>, <y: int>]
        },
        {
            "map": [
            ],
            "tl_bound": [<x: int>, <y: int>],
            "br_bound": [<x: int>, <y: int>]
        }
    ],
    "loot_tables": {
        "<table_name>": {
            "items": {
                "<item1_name: str>": {
                    "min": <int>,
                    "max": <int>,
                    "weight": <int>
                },
                "<item1_name: str>": {
                    "min": <int>,
                    "max": <int>,
                    "weight": <int>
                }
            },
            "rolls": <int>
        }
    }
}
```