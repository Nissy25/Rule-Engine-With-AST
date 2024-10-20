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
def combine_rules_endpoint(request: CombineRulesRequest):
    try:
        asts = [create_rule(rule) for rule in request.rules]
        combined_rule = combine_rules(asts)
        return {"combined_AST": combined_rule}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while combining rules.")

@router.post("/evaluate_rule")
def evaluate_rule_endpoint(data: dict, rule_string: str):
    rule = create_rule(rule_string)
    result = evaluate_rule(rule, data)
    return {"result": result}

