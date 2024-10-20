from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rule_engine import create_rule, combine_rules, evaluate_rule

router = APIRouter()

# Define a Pydantic model for the create_rule input
class CreateRuleRequest(BaseModel):
    rule_string: str

@router.post("/create_rule")
def create_rule_endpoint(request: CreateRuleRequest):
    rule = create_rule(request.rule_string)
    return {"AST": rule}

class CombineRulesRequest(BaseModel):
    rules: list[str]

@router.post("/combine_rules")
def combine_rules_endpoint(request: CombineRulesRequest):
    try:
        combined_rule = combine_rules(request.rules)
        return {"combined_rule": combined_rule}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Define a Pydantic model for evaluating rules input
class EvaluateRuleRequest(BaseModel):
    data: dict  # Expecting a dictionary for the data input
    rule_string: str

@router.post("/evaluate_rule")
def evaluate_rule_endpoint(request: EvaluateRuleRequest):
    rule = create_rule(request.rule_string)
    result = evaluate_rule(rule, request.data)
    return {"result": result}


