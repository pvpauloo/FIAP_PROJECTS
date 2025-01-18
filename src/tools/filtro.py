
from typing import Optional, List, Dict, Any

def filtro(query,data):
    conditions = query.split("&")
    for cond in conditions:
        cond = cond.strip() 
        operator = None
        for op in ["!=", ">=", "<=", "=", ">", "<"]:
            if op in cond:
                operator = op
                break

        if not operator:
            continue

        field, value = cond.split(operator)
        field = field.strip()
        value = value.strip().strip('"').strip("'")


        numeric_value: Any = value
        try:
            if "." in value:
                numeric_value = float(value)  
            else:
                numeric_value = int(value)  
        except ValueError:
            numeric_value = value
        if operator == "=":
            data = [
                item for item in data
                if item[field] == numeric_value
            ]
        elif operator == "!=":
            data = [
                item for item in data
                if item[field] != numeric_value
            ]
        elif operator == ">":
            data = [
                item for item in data
                if item[field] > numeric_value
            ]
        elif operator == "<":
            data = [
                item for item in data
                if item[field] < numeric_value
            ]
        elif operator == ">=":
            data = [
                item for item in data
                if item[field] >= numeric_value
            ]
        elif operator == "<=":
            data = [
                item for item in data
                if item[field] <= numeric_value
            ]
    return data
            