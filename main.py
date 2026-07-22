def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

from fasthtml.common import *
from database import (
    search_name, search_case, duplicate_cases, missing_values,
    crime_types, case_status, open_cases, officer_workload,
    average_age, evidence
)

app, rt = fast_app(
    hdrs=(
        Style("""
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    background-image: linear-gradient(to right top, #18030f, #241421, #302134, #3a2f48, #403e5e, #445177, #436690, #3d7ca7, #329bc2, #2bbbd8, #3adbe8, #5ffbf1);
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Header & Navigation */
header {
    background: linear-gradient(135deg, #18030F 0%, #000000 100%);
    color: white;
    padding: 25px 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 30px;
}

header h1 {
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.5px;
}

.nav-tabs {
    display: flex;
    gap: 10px;
    margin-top: 20px;
    flex-wrap: wrap;
}

.nav-tabs a, .nav-tabs button {
    padding: 10px 16px;
    background: rgba(255,255,255,0.15);
    color: white;
    border: 2px solid transparent;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.nav-tabs button {
    background: none;
    border: none;
    padding: 10px 16px;
}

.nav-tabs a:hover, .nav-tabs button:hover {
    background: rgba(255,255,255,0.25);
    border-color: rgba(255,255,255,0.5);
}

/* Dashboard Cards */
.dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}

.card-title {
    font-size: 14px;
    font-weight: 600;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
}

.card-value {
    font-size: 32px;
    font-weight: 700;
    color: #2c1270;
    line-height: 1;
}

.card-meta {
    font-size: 12px;
    color: #999;
    margin-top: 8px;
}

/* Forms */
.form-section {
    background: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.form-section h2 {
    font-size: 18px;
    margin-bottom: 20px;
    color: #2c3e50;
    font-weight: 600;
}

.form-group {
    display: flex;
    gap: 10px;
    margin-bottom: 16px;
    align-items: center;
}

input[type="text"], input[type="search"] {
    flex: 1;
    min-width: 0;
    padding: 12px 14px;
    border: 2px solid #e0e0e0;
    border-radius: 30px;
    font-size: 14px;
    transition: border-color 0.3s ease;
    font-family: helvetica, sans-serif;
    background: white;
    color: #2c3e50;
}

input[type="text"]::placeholder, input[type="search"]::placeholder {
    color: #999;
}

input[type="text"]:focus, input[type="search"]:focus {
    outline: none;
    border-color: #b289f6;
    box-shadow: 0 0 0 3px rgba(178, 137, 246, 0.1);
}

button[type="submit"], .form-group button {
    padding: 12px 24px;
    background: #8345ff;
    color: black;
    border: none;
    border-radius: 30px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: inherit;
    white-space: nowrap;
    flex-shrink: 5;
}

button {
    padding: 12px 24px;
    background: #b289f6;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: inherit;
}

button:hover {
    background: #6336bf;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(30, 64, 175, 0.25);
}

button:active {
    transform: translateY(0);
}

.btn-secondary {
    background: #6b7280;
}

.btn-secondary:hover {
    background: #6336bf;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

thead {
    background: #f9fafb;
    border-bottom: 2px solid #e0e0e0;
}

th {
    padding: 12px 16px;
    text-align: left;
    font-weight: 600;
    color: #666;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

td {
    padding: 12px 16px;
    border-bottom: 1px solid #f0f0f0;
    font-size: 14px;
}

tbody tr:hover {
    background: #f9fafb;
}

tbody tr:last-child td {
    border-bottom: none;
}

/* Status Badges */
.badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
}

.badge-open {
    background: #fee2e2;
    color: #991b1b;
}

.badge-closed {
    background: #dcfce7;
    color: #166534;
}

.badge-pending {
    background: #fef3c7;
    color: #92400e;
}

/* Results Section */
.results-section {
    background: white;
    padding: 24px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.results-section h2 {
    font-size: 18px;
    margin-bottom: 20px;
    color: #2c3e50;
    font-weight: 600;
}

/* Back Link */
.back-link {
    display: inline-block;
    padding: 10px 16px;
    color: #b289f6;
    text-decoration: none;
    font-weight: 500;
    margin-top: 20px;
    border-radius: 6px;
    transition: all 0.3s ease;
}

.back-link:hover {
    background: #f0f4ff;
    padding-left: 12px;
}

/* Loading & Empty States */
.empty-state {
    text-align: center;
    padding: 40px 20px;
    color: #999;
}

.empty-state h3 {
    color: #666;
    margin-bottom: 10px;
    font-size: 18px;
}

/* Pre/Code Blocks */
pre {
    background: #f5f7fa;
    padding: 16px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 12px;
    line-height: 1.5;
    color: #2c3e50;
    border-left: 4px solid #b289f6;
}

/* Responsive */
@media (max-width: 768px) {
    .nav-tabs {
        flex-direction: column;
    }

    .nav-tabs a, .nav-tabs button {
        width: 100%;
        text-align: center;
    }

    .form-group {
        flex-direction: column;
    }

    .dashboard {
        grid-template-columns: 1fr;
    }

    header h1 {
        font-size: 22px;
    }

    table {
        font-size: 12px;
    }

    th, td {
        padding: 8px 12px;
    }
}
"""),
    )
)

def header_nav():
    """Reusable header without navigation"""
    return Header(
        Div(
            cls="container",
            style="color: white;"
        )(
            H1("🔍 Criminal Database Analyzer")
        )
    )

def format_status(status):
    """Format case status with badge"""
    status_lower = str(status).lower()
    if "open" in status_lower:
        return Span(status, cls="badge badge-open")
    elif "closed" in status_lower:
        return Span(status, cls="badge badge-closed")
    else:
        return Span(status, cls="badge badge-pending")

@rt("/")
def home():
    """Dashboard home page"""
    try:
        open_count = len(open_cases())
        crime_types_df = crime_types()
        total_crimes = len(crime_types_df)
        avg_age_val = f"{average_age():.2f}"
        evidence_df = evidence()
        evidence_count = len(evidence_df)
    except Exception as e:
        open_count = total_crimes = evidence_count = 0
        avg_age_val = "N/A"

    return Div(
        header_nav(),
        Div(
            cls="container"
        )(
            # Dashboard Cards
            Div(
                cls="dashboard"
            )(
                Div(
                    cls="card"
                )(
                    Div(cls="card-title")("Open Cases"),
                    Div(cls="card-value")(str(open_count)),
                    Div(cls="card-meta")("Active investigations")
                ),
                Div(
                    cls="card"
                )(
                    Div(cls="card-title")("Crime Types"),
                    Div(cls="card-value")(str(total_crimes)),
                    Div(cls="card-meta")("In database")
                ),
                Div(
                    cls="card"
                )(
                    Div(cls="card-title")("Avg. Age"),
                    Div(cls="card-value")(str(avg_age_val)),
                    Div(cls="card-meta")("Of subjects")
                ),
                Div(
                    cls="card"
                )(
                    Div(cls="card-title")("Evidence Items"),
                    Div(cls="card-value")(str(evidence_count)),
                    Div(cls="card-meta")("Top suspects tracked")
                ),
            ),

            # Search by Name
            Div(
                id="search-name",
                cls="form-section"
            )(
                H2("Search by Name"),
                Form(
                    Div(
                        cls="form-group"
                    )(
                        Input(
                            name="name",
                            typ="text",
                            placeholder="Enter first or last name",
                            required=True
                        ),
                        Button("🔍", type="submit")
                    ),
                    action="/search",
                    method="get"
                )
            ),

            # Search by Case
            Div(
                id="search-case",
                cls="form-section"
            )(
                H2("Search by Case ID"),
                Form(
                    Div(
                        cls="form-group"
                    )(
                        Input(
                            name="case_id",
                            typ="text",
                            placeholder="Enter case ID",
                            required=True
                        ),
                        Button("🔍", type="submit")
                    ),
                    action="/search-case",
                    method="get"
                )
            ),

            # Quick Actions
            Div(
                id="stats",
                cls="form-section"
            )(
                H2("Quick Analytics"),
                Div(
                    cls="form-group",
                    style="flex-wrap: wrap;"
                )(
                    Button(
                        "View Duplicates",
                        hx_get="/duplicates",
                        hx_target="#result"
                    ),
                    Button(
                        "Missing Values",
                        hx_get="/missing",
                        hx_target="#result",
                        cls="btn-secondary"
                    ),
                    Button(
                        "Officer Workload",
                        hx_get="/workload",
                        hx_target="#result",
                        cls="btn-secondary"
                    ),
                ),
                Div(id="result", style="margin-top: 20px;")
            ),
        )
    )

@rt("/search")
def search(name: str):
    """Search results by name"""
    results = search_name(name)

    if results.empty:
        rows_content = [Tr(
            Td("No results found", colspan="5", style="text-align: center; padding: 40px;")
        )]
    else:
        rows = []
        for _, row in results.iterrows():
            rows.append(
                Tr(
                    Td(str(row["Case_ID"])),
                    Td(str(row["First_Name"])),
                    Td(str(row["Last_Name"])),
                    Td(str(row["Crime_Type"])),
                    Td(format_status(row["Case_Status"]))
                )
            )
        rows_content = rows

    return Div(
        header_nav(),
        Div(
            cls="container"
        )(
            Div(
                cls="results-section"
            )(
                H2(f"Search Results for '{name}'"),
                Table(
                    Thead(
                        Tr(
                            Th("Case ID"),
                            Th("First Name"),
                            Th("Last Name"),
                            Th("Crime"),
                            Th("Status")
                        )
                    ),
                    Tbody(*rows_content)
                )
            ),
            A("← Back to Dashboard", href="/", cls="back-link")
        )
    )

@rt("/search-case")
def search_case_route(case_id: str):
    """Search by case ID"""
    results = search_case(case_id)

    if results.empty:
        rows_content = [Tr(
            Td("No results found", colspan="5", style="text-align: center; padding: 40px;")
        )]
    else:
        rows = []
        for _, row in results.iterrows():
            rows.append(
                Tr(
                    Td(str(row["Case_ID"])),
                    Td(str(row["First_Name"])),
                    Td(str(row["Last_Name"])),
                    Td(str(row["Crime_Type"])),
                    Td(format_status(row["Case_Status"]))
                )
            )
        rows_content = rows

    return Div(
        header_nav(),
        Div(
            cls="container"
        )(
            Div(
                cls="results-section"
            )(
                H2(f"Case ID: {case_id}"),
                Table(
                    Thead(
                        Tr(
                            Th("Case ID"),
                            Th("First Name"),
                            Th("Last Name"),
                            Th("Crime"),
                            Th("Status")
                        )
                    ),
                    Tbody(*rows_content)
                )
            ),
            A("← Back to Dashboard", href="/", cls="back-link")
        )
    )

@rt("/duplicates")
def show_duplicates():
    """Show duplicate cases"""
    result = duplicate_cases()
    
    if len(result) == 0:
        return Div(
            H3("Duplicate Cases"),
            P("No duplicate cases found.", style="color: #666; font-style: italic;"),
            style="margin-top: 16px;"
        )
    
    rows = []
    for _, row in result.iterrows():
        rows.append(
            Tr(
                Td(str(row["Case_ID"])),
                Td(str(row["First_Name"])),
                Td(str(row["Last_Name"])),
                Td(str(row["Crime_Type"])),
                Td(format_status(row["Case_Status"]))
            )
        )
    
    return Div(
        H3("Duplicate Cases"),
        Table(
            Thead(
                Tr(
                    Th("Case ID"),
                    Th("First Name"),
                    Th("Last Name"),
                    Th("Crime"),
                    Th("Status")
                )
            ),
            Tbody(*rows),
            style="width: 100%; margin-top: 16px;"
        ),
        style="margin-top: 16px;"
    )

@rt("/missing")
def show_missing():
    """Show missing values"""
    result = missing_values()
    
    rows = []
    for column, count in result.items():
        if count > 0:
            rows.append(
                Tr(
                    Td(str(column)),
                    Td(str(int(count)), style="text-align: center; font-weight: 600; color: #d32f2f;")
                )
            )
    
    if len(rows) == 0:
        return Div(
            H3("Missing Values Report"),
            P("No missing values found - database is complete!", style="color: #2e7d32; font-style: italic;"),
            style="margin-top: 16px;"
        )
    
    return Div(
        H3("Missing Values Report"),
        Table(
            Thead(
                Tr(
                    Th("Column"),
                    Th("Missing Count")
                )
            ),
            Tbody(*rows),
            style="width: 100%; margin-top: 16px;"
        ),
        style="margin-top: 16px;"
    )

@rt("/workload")
def show_workload():
    """Show officer workload"""
    result = officer_workload()
    
    if len(result) == 0:
        return Div(
            H3("Officer Workload"),
            P("No officer workload data found.", style="color: #666; font-style: italic;"),
            style="margin-top: 16px;"
        )
    
    rows = []
    for _, row in result.iterrows():
        rows.append(
            Tr(
                Td(str(row["Officer_Assigned"])),
                Td(str(int(row["Cases Assigned"])), style="text-align: center; font-weight: 600; color: #b289f6;")
            )
        )
    
    return Div(
        H3("Officer Workload"),
        Table(
            Thead(
                Tr(
                    Th("Officer"),
                    Th("Cases Assigned")
                )
            ),
            Tbody(*rows),
            style="width: 100%; margin-top: 16px;"
        ),
        style="margin-top: 16px;"
    )

serve()

