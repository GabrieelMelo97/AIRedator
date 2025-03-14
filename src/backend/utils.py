import re
from typing import Dict, Any

def extract_score(content: str) -> float:
    """
    Extracts the numerical score from the response text.
    Expected format in text: 'Pontuação: 0.75'.
    """
    match = re.search(r'Pontuação:\s*(\d+(\.\d+)?)', content)
    if match:
        return float(match.group(1))
    raise ValueError(f"Não foi possível extrair a pontuação de: {content}")

def create_initial_state(essay: str) -> Dict[str, Any]:
    """
    Creates the initial state for the evaluation workflow.
    """
    return {
        "essay": essay,
        "relevance_score": 0.0,
        "grammar_score": 0.0,
        "structure_score": 0.0,
        "depth_score": 0.0,
        "final_score": 0.0
    } 