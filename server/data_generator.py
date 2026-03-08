import pandas as pd

TASKS = [
    {
        "id": "A1",
        "cluster": "A",                        # never shown to agent
        "description": "Given a sales dataframe with columns [product, revenue, units], "
                       "return the product names sorted by revenue descending.",
        "hidden_subtask": "sort_values",
        "dataframe": pd.DataFrame({
            "product": ["Widget", "Gadget", "Doohickey"],
            "revenue": [5000, 8000, 3000],
            "units": [100, 160, 60]
        }),
        "expected_output": ["Gadget", "Widget", "Doohickey"],
    },
    # ... 19 more
]