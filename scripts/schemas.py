"""
Request/response models for api.py. No logic here, just the API contract.
"""

from typing import Any, Dict, Optional

from pydantic import BaseModel


class LineItem(BaseModel):
    id: int
    description: str
    note: Optional[str] = ""
    amount: Optional[str] = ""


class ClassifyRequest(BaseModel):
    companyName: Optional[str] = None
    items: list[LineItem]


class ExtractionRequest(BaseModel):
    companyName: Optional[str] = None
    extraction: Dict[str, Any]


class GicsResult(BaseModel):
    code: str
    name: str
    level: str
    confidence: float
    path: list[str]


class MappingResult(BaseModel):
    id: int
    description: str
    amount: str
    tag: Optional[str]
    tagLabel: Optional[str]
    distance: Optional[float]


class KnowledgeResponse(BaseModel):
    """UC2, Knowledge Layer: GICS identification + pruned candidate tags, no per-item assignment."""
    gics: GicsResult
    candidateTags: list[str]


class TaorStepOut(BaseModel):
    step: str
    content: str


class ReasonedMappingResult(BaseModel):
    id: int
    description: str
    amount: str
    tag: Optional[str]
    tagLabel: Optional[str]
    distance: Optional[float]
    resolvedBy: str
    confidence: str
    reactTrace: list[TaorStepOut]


class ReasoningResponse(BaseModel):
    gics: GicsResult
    mappings: list[ReasonedMappingResult]


class StructuralIssue(BaseModel):
    id: int
    tag: str
    issue: str


class SummationIssue(BaseModel):
    parentTag: str
    reportedAmount: float
    computedAmount: float
    difference: float
    childIds: list[int]


class LedgerResponse(BaseModel):
    """UC4, Validation Layer output. The report calls this the 'Ledger'."""
    passed: bool
    gics: GicsResult
    mappings: list[ReasonedMappingResult]
    structuralIssues: list[StructuralIssue]
    summationIssues: list[SummationIssue]
