from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rule_engine import create_rule, combine_rules, evaluate_rule

router = APIRouter()

# Pydantic model for rule input
class RuleInput(BaseModel):
    rule_string: str

# Pydantic model for combining rules
class CombineRulesInput(BaseModel):
    rules: list

# Pydantic model for evaluation input
class EvaluateRuleInput(BaseModel):
    data: dict
    rule_string: str

@router.post("/create_rule")
def create_rule_endpoint(input_data: RuleInput):
    rule = create_rule(input_data.rule_string)
    return {"AST": rule}

@router.post("/combine_rules")
def combine_rules_endpoint(input_data: CombineRulesInput):
    combined_rule = combine_rules([create_rule(rule) for rule in input_data.rules])
    return {"combined_AST": combined_rule}

@router.post("/evaluate_rule")
def evaluate_rule_endpoint(input_data: EvaluateRuleInput):
    rule = create_rule(input_data.rule_string)
    result = evaluate_rule(rule, input_data.data)
    return {"result": result}


