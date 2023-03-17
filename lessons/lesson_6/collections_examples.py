from collections import defaultdict

# collections.defaultdict

d = {
    "красные утята": 0,
    "зеленые утята": 0,
    "желтые утята": 0
}

d["красные утята"] += 1

d = defaultdict(int)

d["какой-то неизвестный утенок"] += 1

print(d)

d = defaultdict(list)

d["key"].append(123)

print(d)




# collections.namedtuple

from collections import namedtuple
from dataclasses import dataclass

region_city_pair = namedtuple("region_city_pair", ["region", "city"])

ekb = region_city_pair(region=66, city="Екатеринбург")
print(tuple(ekb))


@dataclass
# @dataclass(frozen=True)  # in case we want to use such tuple as a key for dict (keys should be unmutable)
class RegionCityPair:
    region: int
    city: str


ekb = RegionCityPair(region=66, city="екатеринбург")

print(f'dataclass:{ekb}')
print(f'dataclass city: {ekb.city}')
print(f'dataclass region: {ekb.region}')

# collections.OrderedDict

from collections import OrderedDict

d = dict(namedkey=123)
d["key"] = "value"
d["other"] = "123"


# неизменяемые типы данных в качестве ключей словаря

# изменяемые:
# - dict, list, set
# неизменяемые:
# frozenset, tuple, str


d = {
    "key": "value",
    1234: "another",
    (66, "Екатеринбург"): "value",
    frozenset([1, 2, 3]): 123
}

regions = [123, 456, 789]
cities = ["abc", "def", "xyz"]
