class Report:
    def __init__(self):
        self.header = ""
        self.content = ""
        self.footer = ""

    def show(self):
        print(self.header)
        print(self.content)
        print(self.footer)


class IReportBuilder:
    def set_header(self, header): pass
    def set_content(self, content): pass
    def set_footer(self, footer): pass
    def get_report(self): pass


class TextReportBuilder(IReportBuilder):
    def __init__(self):
        self.report = Report()

    def set_header(self, header):
        self.report.header = f"=== {header} ==="

    def set_content(self, content):
        self.report.content = content

    def set_footer(self, footer):
        self.report.footer = f"--- {footer} ---"

    def get_report(self):
        return self.report


class HtmlReportBuilder(IReportBuilder):
    def __init__(self):
        self.report = Report()

    def set_header(self, header):
        self.report.header = f"<h1>{header}</h1>"

    def set_content(self, content):
        self.report.content = f"<p>{content}</p>"

    def set_footer(self, footer):
        self.report.footer = f"<footer>{footer}</footer>"

    def get_report(self):
        return self.report


class ReportDirector:
    def construct_report(self, builder, title, content, footer):
        builder.set_header(title)
        builder.set_content(content)
        builder.set_footer(footer)


if __name__ == "__main__":
    director = ReportDirector()

    text_builder = TextReportBuilder()
    director.construct_report(
        text_builder,
        "Контрольный отчёт",
        "Этот отчёт содержит информацию о выполненной студентом работе.",
        "Отчёт завершён."
    )
    text_report = text_builder.get_report()
    print("=== ТЕКСТОВЫЙ ОТЧЁТ ===")
    text_report.show()

    html_builder = HtmlReportBuilder()
    director.construct_report(
        html_builder,
        "Контрольный отчёт (HTML)",
        "Этот отчёт содержит информацию о выполненной студентом работе.",
        "Отчёт завершён."
    )
    html_report = html_builder.get_report()

    html_code = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Отчёт</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f3f3f3;
                color: #222;
                padding: 20px;
            }}
            h1 {{
                color: #007BFF;
            }}
            footer {{
                margin-top: 20px;
                font-size: 12px;
                color: gray;
            }}
            .container {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                width: 600px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {html_report.header}
            {html_report.content}
            {html_report.footer}
        </div>
    </body>
    </html>
    """

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html_code)


