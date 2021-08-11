from partypy.simulate import simulate_party
from partypy.plotting import plot_simulation
import pandas as pd
import altair as alt


def test_simulate_party():
    p_0 = [0, 0, 0]  # 3 guests with probability 0 of attending
    p_1 = [1]        # 1 guest with probability 1 of attending
    assert isinstance(simulate_party(p_0), pd.DataFrame)        # simulate_party outputs a dataframe
    assert simulate_party(p_0, 10)["Total guests"].sum() == 0   # 0 probability, 10 simulations gives 0 sum
    assert simulate_party(p_1, 10)["Total guests"].sum() == 10  # 1 probability, 10 simulations gives 10 sum


def test_plot_simulation():
    p_0 = [0, 0, 0]  # 3 guests with probability 0 of attending
    results = simulate_party(p_0)
    plot = plot_simulation(results)
    assert isinstance(plot, alt.Chart)  # plot_simulation outputs an alt.chart
    assert plot.mark == "bar"           # chart type is "bar"
    assert plot.data["Total guests"].sum() == 0  # 0 probability gives 0 sum
    