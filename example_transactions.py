from lifechoices import *
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# First we will create some constants
INFLATION_RATE = .05
RETIREMENT_DATE = datetime(2045, 1, 1)

# Now let's create some accounts for our "young self"
# This is an account called "Savings" starting with 0 dollars, that inflates at 10% APR compounded daily
# (but with a constant inflation rate factored in), that starts on October 2nd 2020
Accounts_Young = [Account("Savings", 0.0, 0.1-INFLATION_RATE, datetime(2020, 10, 2))]

# We are going to Save $1,000 a month into our savings account
Transfers_Young = [Monthly("Salary", 1000, "Savings")]

# A plan is our main input to our processing/plotting function, and it just holds our accounts and transfers as lists
Starting_Plan = Plan(
    accounts=Accounts_Young,
    transfers=Transfers_Young
)

# Now we are going to create some accounts for our older self
# Our APR is going to lower to 7% in retirement so it's a safer account
# We are not going to put any money in it yet, as that will be determined by how much money
# we have made in life
Accounts_Old = [Account("Savings", 0.0, 0.07 - INFLATION_RATE, RETIREMENT_DATE)]

# We are going to need $1,000 a month in retirement to live on (living under a bridge)
Transfers_Old = [Monthly("Salary", -1000, "Savings")]

# Now we will learn about bridges. Bridges allow us to apply "logic" to our actions on certain dates.
# This bridge moves all the money in our current plan's account, and puts it in our old person savings account.
# All bridges do is take a plan and output a new plan. They activate on a date.
def retirement_bridge(p: Plan) -> Plan:
    Accounts_Old[0].amount = p.accounts[0].amount
    return Plan(
        accounts=Accounts_Old,
        transfers=Transfers_Old
    )

# We make a list of our bridges which in this case is just one
# We put our bridge function inside our bridge class, as well as an activation date
# which in this case is our retirement date.
Bridges = [
    Bridge(RETIREMENT_DATE, retirement_bridge)
]

# And now we plot!
data = plot_accounts(
    starting_plan=Starting_Plan,
    bridges=Bridges,
    from_date=datetime(2020, 10, 2),
    to_date=datetime(2080, 1, 1))
df = pd.DataFrame(data)
df = df.set_index("Date")
df.plot()
plt.show()