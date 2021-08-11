from partypy.simulate import simulate_party
from partypy.plotting import plot_simulation
import pandas as pd
import altair as alt
from pytest import raises  


def test_simulate_party():
    p_0 = [0, 0, 0]
    p_1 = [1]
    assert isinstance(simulate_party(p_0), pd.DataFrame)
    assert simulate_party(p_0, 10)["Total guests"].sum() == 0
    assert simulate_party(p_1, 10)["Total guests"].sum() == 10
    with raises(ValueError):  # here is our new test
        simulate_party([0], n_simulations=-5)


def test_plot_simulation():
    p_0 = [0, 0, 0]
    results = simulate_party(p_0)
    plot = plot_simulation(results)
    assert isinstance(plot, alt.Chart)
    assert plot.mark == "bar"
    assert plot.data["Total guests"].sum() == 0