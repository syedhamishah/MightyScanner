class RemediationSuggestions:
    def suggest_fix(self, vulnerability):
        if "CVE-2020-0601" in vulnerability:
            return "Run the following PowerShell script to apply the necessary patch."
        return "No fix available."
