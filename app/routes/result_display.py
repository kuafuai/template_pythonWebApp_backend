def display_results(results):
    # Display evaluation results
    for result in results:
        print(result)

def generate_report(results):
    # Generate evaluation reports
    report = ""
    for result in results:
        report += f"Result: {result}\n"
    return report
