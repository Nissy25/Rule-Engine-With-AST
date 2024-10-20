from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rule_engine import create_rule, combine_rules, evaluate_rule

router = APIRouter()

# Define the input models
class RuleRequest(BaseModel):
    rule_string: str

class CombineRulesRequest(BaseModel):
    rules: list[str]

class EvaluateRuleRequest(BaseModel):
    data: dict
    rule_string: str

# Create rule endpoint
@router.post("/create_rule")
def create_rule_endpoint(rule_request: RuleRequest):
    try:
        rule = create_rule(rule_request.rule_string)
        return {"AST": rule}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Combine rules endpoint
@router.post("/combine_rules")
def combine_rules_endpoint(combine_rules_request: CombineRulesRequest):
    try:
        combined_rule = combine_rules([create_rule(rule) for rule in combine_rules_request.rules])
        return {"combined_AST": combined_rule}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Evaluate rule endpoint
@router.post("/evaluate_rule")
def evaluate_rule_endpoint(evaluate_rule_request: EvaluateRuleRequest):
    try:
        rule = create_rule(evaluate_rule_request.rule_string)
        result = evaluate_rule(rule, evaluate_rule_request.data)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
