from types import SimpleNamespace

_messages = {
    "main": """
Welcome to the financializer!

Choose from the following:
    1) Enter an expense
    2) Enter a source of income

    Q) Quit

Selection: """,
    "freq": """How often is it paid?
    1) annually
    2) semi-annually (every 6 months)
    3) monthly
    4) bi-weekly
    5) weekly

Choice: """,
    "confirm": "Does this look good? [Y/n]: "
}

msgs = SimpleNamespace(**_messages)


freqs = {
    "1": "annual",
    "2": "semi-annual",
    "3": "monthly",
    "4": "bi-weekly",
    "5": "weekly"
}
