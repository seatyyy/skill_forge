import pandas as pd
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Cluster A: filter → sort → extract
# ---------------------------------------------------------------------------

_A1_df = pd.DataFrame({
    "product": ["Widget", "Gadget", "Doohickey", "Sprocket", "Thingamajig", "Gizmo"],
    "revenue": [5000, 8000, 3000, 7500, 2000, 6000],
    "region": ["West", "West", "East", "West", "East", "North"],
})

_A2_df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dan", "Eve", "Frank", "Grace"],
    "dept": ["Eng", "Sales", "Eng", "Eng", "HR", "Eng", "Sales"],
    "tenure": [5, 3, 8, 2, 4, 10, 1],
})

_A3_df = pd.DataFrame({
    "order_id": ["ORD-101", "ORD-102", "ORD-103", "ORD-104", "ORD-105", "ORD-106"],
    "status": ["shipped", "pending", "shipped", "shipped", "cancelled", "shipped"],
    "quantity": [50, 20, 80, 30, 10, 60],
})

_A4_df = pd.DataFrame({
    "student_id": ["S01", "S02", "S03", "S04", "S05", "S06", "S07"],
    "grade": ["A", "B", "A", "A", "C", "A", "B"],
    "gpa": [3.9, 3.2, 3.95, 3.7, 2.8, 3.85, 3.1],
})

_A5_df = pd.DataFrame({
    "item_name": ["Bolts", "Nails", "Screws", "Washers", "Rivets", "Pins"],
    "stock": [5, 50, 8, 3, 100, 7],
    "reorder_priority": [2, 10, 3, 1, 15, 4],
})

# ---------------------------------------------------------------------------
# Cluster B: normalize → filter → extract
# ---------------------------------------------------------------------------

_B1_df = pd.DataFrame({
    "user_id": ["U1", "U2", "U3", "U4", "U5", "U6"],
    "email": ["Alice@Gmail.COM", "bob@yahoo.com", "Carol@GMAIL.com",
              "dan@gmail.COM", "eve@outlook.com", "frank@Gmail.com"],
})

_B2_df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["  Alice  ", " Bob", "  Andrew ", "Anna  ", " Carl ", "  Amy", " Brian  "],
})

_B3_df = pd.DataFrame({
    "user_id": ["U1", "U2", "U3", "U4", "U5", "U6"],
    "country_code": ["us", "UK", "Us", "ca", "US", "us"],
})

_B4_df = pd.DataFrame({
    "product_id": ["P1", "P2", "P3", "P4", "P5", "P6"],
    "product_name": ["widget pro", "basic gadget", "pro sprocket",
                     "mega pro tool", "simple bolt", "pro widget x"],
})

_B5_df = pd.DataFrame({
    "contact_id": ["C1", "C2", "C3", "C4", "C5", "C6"],
    "phone": ["(555) 123-4567", "555.987.6543", "(555)111-2222",
              "5551234", "555-999-8888", "(555) 000 1111"],
})

# ---------------------------------------------------------------------------
# Cluster C: date delta → filter → count
# ---------------------------------------------------------------------------

_today = datetime(2026, 3, 8)

_C1_df = pd.DataFrame({
    "user_id": ["U1", "U2", "U3", "U4", "U5", "U6", "U7"],
    "signup_date": [
        _today - timedelta(days=10),
        _today - timedelta(days=45),
        _today - timedelta(days=5),
        _today - timedelta(days=90),
        _today - timedelta(days=25),
        _today - timedelta(days=3),
        _today - timedelta(days=60),
    ],
    "active": [True, True, True, False, True, True, False],
})

_C2_df = pd.DataFrame({
    "order_id": ["O1", "O2", "O3", "O4", "O5", "O6"],
    "order_date": [
        _today - timedelta(days=2),
        _today - timedelta(days=10),
        _today - timedelta(days=5),
        _today - timedelta(days=1),
        _today - timedelta(days=14),
        _today - timedelta(days=6),
    ],
    "amount": [100, 200, 150, 50, 300, 75],
})

_C3_df = pd.DataFrame({
    "emp_id": ["E1", "E2", "E3", "E4", "E5", "E6"],
    "hire_date": [
        _today - timedelta(days=365),
        _today - timedelta(days=900),
        _today - timedelta(days=200),
        _today - timedelta(days=500),
        _today - timedelta(days=100),
        _today - timedelta(days=1500),
    ],
    "dept": ["Eng", "Sales", "Eng", "HR", "Eng", "Sales"],
})

_C4_df = pd.DataFrame({
    "event_id": ["EV1", "EV2", "EV3", "EV4", "EV5", "EV6"],
    "event_date": [
        _today + timedelta(days=5),
        _today + timedelta(days=20),
        _today + timedelta(days=10),
        _today + timedelta(days=3),
        _today + timedelta(days=30),
        _today + timedelta(days=12),
    ],
    "venue": ["Hall A", "Hall B", "Hall A", "Hall C", "Hall B", "Hall A"],
})

_C5_df = pd.DataFrame({
    "user_id": ["U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8"],
    "birthdate": [
        _today - timedelta(days=365 * 20),
        _today - timedelta(days=365 * 30),
        _today - timedelta(days=365 * 22),
        _today - timedelta(days=365 * 17),
        _today - timedelta(days=365 * 19),
        _today - timedelta(days=365 * 25),
        _today - timedelta(days=365 * 24),
        _today - timedelta(days=365 * 15),
    ],
})

# ---------------------------------------------------------------------------
# Cluster D: groupby → aggregate → sort → slice
# ---------------------------------------------------------------------------

_D1_df = pd.DataFrame({
    "region": ["West", "East", "West", "North", "East", "North", "West", "East", "South", "South"],
    "revenue": [5000, 3000, 7000, 4000, 6000, 2000, 3000, 8000, 1000, 5000],
    "product": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A"],
})

_D2_df = pd.DataFrame({
    "customer": ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice",
                 "Carol", "Bob", "Alice", "Bob", "Carol", "Bob",
                 "Alice", "Bob"],
    "order_id": [f"O{i}" for i in range(1, 15)],
    "amount": [100, 50, 200, 150, 75, 300, 125, 80, 90, 60, 200, 45, 110, 95],
})

_D3_df = pd.DataFrame({
    "dept": ["Eng", "Sales", "Eng", "HR", "Sales", "Eng", "HR", "Sales"],
    "employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "salary": [120000, 80000, 110000, 70000, 90000, 130000, 75000, 85000],
})

_D4_df = pd.DataFrame({
    "category": ["Electronics", "Clothing", "Electronics", "Food",
                 "Clothing", "Food", "Electronics", "Books", "Books"],
    "product": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9"],
    "units_sold": [500, 200, 300, 150, 100, 400, 250, 50, 80],
})

_D5_df = pd.DataFrame({
    "venue": ["Arena", "Hall", "Arena", "Park", "Hall", "Arena", "Park", "Hall"],
    "event": ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"],
    "attendees": [500, 200, 300, 100, 250, 400, 150, 300],
    "capacity": [1000, 600, 1000, 200, 600, 1000, 200, 600],
})


# ---------------------------------------------------------------------------
# Compute expected outputs
# ---------------------------------------------------------------------------

# Cluster A
_A1_expected = _A1_df[_A1_df["region"] == "West"].sort_values("revenue", ascending=False)["product"].tolist()
_A2_expected = _A2_df[_A2_df["dept"] == "Eng"].sort_values("tenure", ascending=False)["name"].tolist()
_A3_expected = _A3_df[_A3_df["status"] == "shipped"].sort_values("quantity", ascending=False)["order_id"].tolist()
_A4_expected = _A4_df[_A4_df["grade"] == "A"].sort_values("gpa", ascending=False)["student_id"].tolist()
_A5_expected = _A5_df[_A5_df["stock"] < 10].sort_values("reorder_priority")["item_name"].tolist()

# Cluster B
_B1_expected = _B1_df.assign(email=_B1_df["email"].str.lower())\
    .query("email.str.endswith('@gmail.com')")["email"].tolist()
_B2_expected = _B2_df.assign(name=_B2_df["name"].str.strip())\
    .query("name.str.startswith('A')")["name"].tolist()
_B3_expected = _B3_df.assign(country_code=_B3_df["country_code"].str.upper())\
    .query("country_code == 'US'")["user_id"].tolist()
_B4_expected = _B4_df.assign(product_name=_B4_df["product_name"].str.title())\
    .query("product_name.str.contains('Pro')")["product_id"].tolist()
_B5_expected = _B5_df.assign(phone=_B5_df["phone"].str.replace(r"\D", "", regex=True))\
    .query("phone.str.len() == 10")["phone"].tolist()

# Cluster C
_C1_expected = int(_C1_df.assign(days_since=(pd.Timestamp(_today) - _C1_df["signup_date"]).dt.days)\
    .query("days_since < 30").shape[0])
_C2_expected = int(_C2_df.assign(order_age=(pd.Timestamp(_today) - _C2_df["order_date"]).dt.days)\
    .query("order_age <= 7").shape[0])
_C3_expected = int(_C3_df.assign(tenure_years=(pd.Timestamp(_today) - _C3_df["hire_date"]).dt.days / 365)\
    .query("tenure_years < 2").shape[0])
_C4_expected = int(_C4_df.assign(days_until=(_C4_df["event_date"] - pd.Timestamp(_today)).dt.days)\
    .query("days_until <= 14").shape[0])
_C5_expected = int(_C5_df.assign(age=(pd.Timestamp(_today) - _C5_df["birthdate"]).dt.days / 365)\
    .query("18 <= age <= 25").shape[0])

# Cluster D
_D1_expected = _D1_df.groupby("region")["revenue"].sum()\
    .sort_values(ascending=False).head(3).index.tolist()
_D2_expected = _D2_df.groupby("customer")["order_id"].count()\
    .loc[lambda x: x > 5].index.tolist()
_D3_expected = _D3_df.groupby("dept")["salary"].mean()\
    .sort_values(ascending=False).index[0]
_D4_expected = _D4_df.groupby("category")["units_sold"].sum()\
    .sort_values().head(2).index.tolist()
_D5_expected = _D5_df.assign(over=_D5_df["attendees"] > _D5_df["capacity"])\
    .query("over").groupby("venue")["event"].count().index.tolist()
# D5 recompute: venues where total attendees > total capacity
_D5_agg = _D5_df.groupby("venue").agg({"attendees": "sum", "capacity": "first"}).reset_index()
_D5_expected = _D5_agg[_D5_agg["attendees"] > _D5_agg["capacity"]]["venue"].tolist()


# ---------------------------------------------------------------------------
# TASKS list
# ---------------------------------------------------------------------------

TASKS = [
    # --- Cluster A: filter → sort → extract ---
    {
        "id": "A1",
        "cluster": "A",
        "description": "Given a sales dataframe with columns [product, revenue, region], "
                       "return the product names for the West region sorted by revenue descending.",
        "dataframe": _A1_df,
        "expected_output": _A1_expected,
    },
    {
        "id": "A2",
        "cluster": "A",
        "description": "Given an employees dataframe with columns [name, dept, tenure], "
                       "return the names of Engineering employees sorted by tenure descending.",
        "dataframe": _A2_df,
        "expected_output": _A2_expected,
    },
    {
        "id": "A3",
        "cluster": "A",
        "description": "Given an orders dataframe with columns [order_id, status, quantity], "
                       "return the order IDs for shipped orders sorted by quantity descending.",
        "dataframe": _A3_df,
        "expected_output": _A3_expected,
    },
    {
        "id": "A4",
        "cluster": "A",
        "description": "Given a students dataframe with columns [student_id, grade, gpa], "
                       "return the student IDs of students with grade A sorted by GPA descending.",
        "dataframe": _A4_df,
        "expected_output": _A4_expected,
    },
    {
        "id": "A5",
        "cluster": "A",
        "description": "Given an inventory dataframe with columns [item_name, stock, reorder_priority], "
                       "return item names where stock is below 10, sorted by reorder priority ascending.",
        "dataframe": _A5_df,
        "expected_output": _A5_expected,
    },
    # --- Cluster B: normalize → filter → extract ---
    {
        "id": "B1",
        "cluster": "B",
        "description": "Given a users dataframe with columns [user_id, email], "
                       "lowercase all emails, keep only @gmail.com addresses, return the email list.",
        "dataframe": _B1_df,
        "expected_output": _B1_expected,
    },
    {
        "id": "B2",
        "cluster": "B",
        "description": "Given a contacts dataframe with columns [id, name], "
                       "strip whitespace from names, keep names starting with 'A', return the name list.",
        "dataframe": _B2_df,
        "expected_output": _B2_expected,
    },
    {
        "id": "B3",
        "cluster": "B",
        "description": "Given a users dataframe with columns [user_id, country_code], "
                       "uppercase all country codes, keep only 'US', return the user_id list.",
        "dataframe": _B3_df,
        "expected_output": _B3_expected,
    },
    {
        "id": "B4",
        "cluster": "B",
        "description": "Given a products dataframe with columns [product_id, product_name], "
                       "title-case all product names, keep those containing 'Pro', return the product_id list.",
        "dataframe": _B4_df,
        "expected_output": _B4_expected,
    },
    {
        "id": "B5",
        "cluster": "B",
        "description": "Given a contacts dataframe with columns [contact_id, phone], "
                       "remove all non-digit characters from phone numbers, keep only 10-digit ones, return the phone list.",
        "dataframe": _B5_df,
        "expected_output": _B5_expected,
    },
    # --- Cluster C: date delta → filter → count ---
    {
        "id": "C1",
        "cluster": "C",
        "description": "Given a users dataframe with columns [user_id, signup_date, active], "
                       "compute days since signup (from 2026-03-08), keep users who signed up within the last 30 days, return the count.",
        "dataframe": _C1_df,
        "expected_output": _C1_expected,
    },
    {
        "id": "C2",
        "cluster": "C",
        "description": "Given an orders dataframe with columns [order_id, order_date, amount], "
                       "compute order age in days (from 2026-03-08), keep orders within the last 7 days, return the count.",
        "dataframe": _C2_df,
        "expected_output": _C2_expected,
    },
    {
        "id": "C3",
        "cluster": "C",
        "description": "Given an employees dataframe with columns [emp_id, hire_date, dept], "
                       "compute tenure in years (from 2026-03-08), keep employees with less than 2 years, return the count.",
        "dataframe": _C3_df,
        "expected_output": _C3_expected,
    },
    {
        "id": "C4",
        "cluster": "C",
        "description": "Given an events dataframe with columns [event_id, event_date, venue], "
                       "compute days until event (from 2026-03-08), keep events within the next 14 days, return the count.",
        "dataframe": _C4_df,
        "expected_output": _C4_expected,
    },
    {
        "id": "C5",
        "cluster": "C",
        "description": "Given a users dataframe with columns [user_id, birthdate], "
                       "compute age in years (from 2026-03-08), keep users aged 18 to 25 inclusive, return the count.",
        "dataframe": _C5_df,
        "expected_output": _C5_expected,
    },
    # --- Cluster D: groupby → aggregate → sort → slice ---
    {
        "id": "D1",
        "cluster": "D",
        "description": "Given a sales dataframe with columns [region, revenue, product], "
                       "group by region, sum revenue, return the top 3 regions by total revenue.",
        "dataframe": _D1_df,
        "expected_output": _D1_expected,
    },
    {
        "id": "D2",
        "cluster": "D",
        "description": "Given an orders dataframe with columns [customer, order_id, amount], "
                       "group by customer, count orders, return customers with more than 5 orders.",
        "dataframe": _D2_df,
        "expected_output": _D2_expected,
    },
    {
        "id": "D3",
        "cluster": "D",
        "description": "Given an employees dataframe with columns [dept, employee, salary], "
                       "group by department, compute average salary, return the department with the highest average.",
        "dataframe": _D3_df,
        "expected_output": _D3_expected,
    },
    {
        "id": "D4",
        "cluster": "D",
        "description": "Given a products dataframe with columns [category, product, units_sold], "
                       "group by category, sum units_sold, return the bottom 2 categories by total units.",
        "dataframe": _D4_df,
        "expected_output": _D4_expected,
    },
    {
        "id": "D5",
        "cluster": "D",
        "description": "Given an events dataframe with columns [venue, event, attendees, capacity], "
                       "group by venue summing attendees and taking the first capacity, "
                       "return venues where total attendees exceed capacity.",
        "dataframe": _D5_df,
        "expected_output": _D5_expected,
    },
]
