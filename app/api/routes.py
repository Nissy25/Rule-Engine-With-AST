from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.rule_engine import create_rule, combine_rules, evaluate_rule

# Define the CombineRulesRequest model
class CombineRulesRequest(BaseModel):
    rules: List[str]  # List of rule strings

router = APIRouter()

@router.post("/create_rule")
def create_rule_endpoint(rule_string: str):
    rule = create_rule(rule_string)
    return {"AST": rule}

@router.post("/combine_rules")
def combine_rules_endpoint(rules: List[str]):  # Ensure you're using List[str]
    try:
        combined_rule = combine_rules(rules)
        return {"combined_AST": combined_rule}
    except Exception as e:
        return {"detail": str(e)}, 500  # Return the error message

@router.post("/evaluate_rule")
def evaluate_rule_endpoint(data: dict, rule_string: str):
    rule = create_rule(rule_string)
    result = evaluate_rule(rule, data)
    return {"result": result}

