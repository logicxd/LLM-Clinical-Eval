from dataclasses import dataclass
from typing import List, Dict

# DM: usually the classes/objects should live on their own file but these are pretty small so it's fine. As things grow larger, you'll probalby have to move it around so the file keeps single responsibility. 

@dataclass
class Item:
    id: str
    topic: str
    criteria: dict[int, str]

@dataclass
class Domain:
    name: str
    max_points: int
    items: List[Item]

@dataclass
class Rubric:
    rubric_name: str
    total_points: int
    domains: List[Domain]
    flags: Dict[str, bool]

# DM: I'm not too familiar with python but are these methods outside of the dataclass's defined above? An alternative is that they can be defined within the class themselves so they live together.
def build_items(item_dicts):
    items = []
    for item_dict in item_dicts:
        curr_item = Item(item_dict["id"], item_dict["topic"], item_dict["criteria"])
        items.append(curr_item)
    return items

def build_domains(domain_dicts):
    domains = []
    for domain_dict in domain_dicts:
        items = build_items(domain_dict["items"])
        curr_domain = Domain(domain_dict["name"], domain_dict["max_points"], items)
        domains.append(curr_domain)
    return domains

def build_rubric(rubric_dict):
    domains = build_domains(rubric_dict["domains"])
    rubric = Rubric(rubric_dict["rubric_name"], rubric_dict["total_points"], domains, rubric_dict["flags"])
    return rubric