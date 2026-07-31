from functools import wraps

def report_style(style):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            report = func(*args, **kwargs)

            if style == "star":
                border = "*" * 50
            elif style == "dash":
                border = "-" * 50
            elif style == "hash":
                border = "#" * 50
            else:
                border = "=" * 50

            return f"{border}\n{report}\n{border}"
        return wrapper
    return decorator


class Report:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.sections = []

    def __str__(self):
        return self.generate()

    def __len__(self):
        return len(self.sections)

    def __add__(self, other):
        new_report = Report(
            f"{self.title} + {other.title}",
            self.author
        )
        new_report.sections = self.sections + other.sections
        return new_report

    def add_section(self, heading, content):
        self.sections.append((heading, content))

    @report_style("star")
    def generate(self):
        report = f"Title : {self.title}\n"
        report += f"Author: {self.author}\n\n"

        for heading, content in self.sections:
            report += f"{heading}\n"
            report += f"{'-'*len(heading)}\n"
            report += content + "\n\n"

        return report

    @classmethod
    def business_template(cls, author):
        report = cls("Business Report", author)
        report.add_section("Executive Summary", "Write summary here...")
        report.add_section("Financial Analysis", "Enter financial data...")
        return report

    @classmethod
    def academic_template(cls, author):
        report = cls("Academic Report", author)
        report.add_section("Introduction", "Write introduction...")
        report.add_section("Methodology", "Describe methodology...")
        report.add_section("Conclusion", "Write conclusion...")
        return report


business = Report.business_template("Alice")
academic = Report.academic_template("Bob")

business.add_section("Recommendations", "Increase online marketing.")

print(business)

print("Sections:", len(business))

combined = business + academic

print("\nCombined Report:\n")
print(combined)
