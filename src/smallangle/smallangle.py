import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Here you give a number for how many values of sin you want between 0 and 2 pi.",
    )
def sin(number):
    """This command gives you a list of sine values
    between 0 and 2 pi.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    help="Here you give a number for how many values of tan you want between 0 and 2 pi.",
    default=10
    )
def tan(number):
    """This command gives you a list of tangent values
    between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)



if __name__ == "__main__":
    cmd_group()