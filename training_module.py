class TrainingModule:
    def display_tutorial(self, topic):
        tutorials = {
            "SQL Injection": "Learn how to prevent SQL injection attacks by using prepared statements.",
            "XSS": "Understand Cross-Site Scripting and its mitigation techniques."
        }
        return tutorials.get(topic, "No tutorial available.")
