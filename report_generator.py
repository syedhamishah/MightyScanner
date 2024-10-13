import json
import pandas as pd

class ReportGenerator:
    def __init__(self, scan_results, vulnerabilities, report_format):
        self.scan_results = scan_results
        self.vulnerabilities = vulnerabilities
        self.report_format = report_format

    def generate_report(self):
        if self.report_format == 'json':
            self._generate_json_report()
        else:
            self._generate_html_report()

    def _generate_json_report(self):
        report = {
            'scan_results': self.scan_results,
            'vulnerabilities': self.vulnerabilities
        }
        with open('report.json', 'w') as f:
            json.dump(report, f, indent=4)
        print("Report generated: report.json")

    def _generate_html_report(self):
        df = pd.DataFrame(self.scan_results)
        df.to_html('report.html')
        print("Report generated: report.html")
