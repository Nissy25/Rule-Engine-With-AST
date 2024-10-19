from fastapi import APIRouter
from app.services.rule_engine import create_rule, combine_rules, evaluate_rule

router = APIRouter()

@router.post("/create_rule")
def create_rule_endpoint(rule_string: str):
    rule = create_rule(rule_string)
    return {"AST": rule}

@router.post("/combine_rules")
def combine_rules_endpoint(rules: list):
    combined_rule = combine_rules([create_rule(rule) for rule in rules])
    return {"combined_AST": combined_rule}

@router.post("/evaluate_rule")
def evaluate_rule_endpoint(data: dict, rule_string: str):
    rule = create_rule(rule_string)
    result = evaluate_rule(rule, data)
    return {"result": result}
