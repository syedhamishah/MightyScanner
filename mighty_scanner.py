import argparse
from scanner import NetworkScanner
from vulnerability_checker import VulnerabilityChecker
from report_generator import ReportGenerator
from training_module import TrainingModule
from best_practices import BestPractices
from remediation_suggestions import RemediationSuggestions
from compliance_checker import ComplianceChecker
from threat_intelligence import ThreatIntelligence
from user_management import UserManagement
from feedback_system import FeedbackSystem

def main():
    parser = argparse.ArgumentParser(description="MightyScanner - Network and Vulnerability Scanner")
    parser.add_argument('--target', required=True, help='Target IP or subnet (e.g., 192.168.1.0/24)')
    parser.add_argument('--ports', default='1-1024', help='Port range to scan (default: 1-1024)')
    parser.add_argument('--vuln-check', action='store_true', help='Perform vulnerability checks')
    parser.add_argument('--report-format', choices=['json', 'html'], default='html', help='Report format')
    
    args = parser.parse_args()
    
    # Initialize components
    scanner = NetworkScanner(args.target, args.ports)
    vulnerabilities = []
    
    # Perform scanning
    scan_results = scanner.scan_network()
    
    if args.vuln_check:
        checker = VulnerabilityChecker(scan_results)
        vulnerabilities = checker.check_vulnerabilities()
        
        remediation = RemediationSuggestions()
        for vuln in vulnerabilities:
            print(remediation.suggest_fix(vuln))
    
    # Generate report
    report = ReportGenerator(scan_results, vulnerabilities, args.report_format)
    report.generate_report()

    # User education
    training = TrainingModule()
    print(training.display_tutorial("SQL Injection"))

    # Best practices
    best_practices = BestPractices()
    recommendations = best_practices.get_recommendations(vulnerabilities)
    for rec in recommendations:
        print(rec)

if __name__ == "__main__":
    main()
