from typing import List

def display_results(results: List[str]) -> None:
    """
    Used to display evaluation results.

    Args:
        results: A list of evaluation results.

    Returns:
        None
    """
    for result in results:
        print(result)

def generate_report(results: List[str]) -> str:
    """
    Used to generate evaluation reports.

    Args:
        results: A list of evaluation results.

    Returns:
        report: A string containing the evaluation reports.
    """
    report = "\n".join([f"Result: {result}" for result in results])
    return report
