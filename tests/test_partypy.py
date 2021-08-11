from partypy.simulate import simulate_party
from partypy.plotting import plot_simulation
from partypy.datasets import load_party
import pandas as pd
import altair as alt
from pytest import raises, fixture


@fixture()
def test_data():
    return {
        "p_0": [0, 0, 0],  # 3 guests with probability 0 of attending
        "p_1": [1],        # 1 guests with probability 1 of attending
    }


def test_simulate_party(test_data):
    assert isinstance(simulate_party(test_data["p_0"]), pd.DataFrame)
    assert simulate_party(test_data["p_0"], 10)["Total guests"].sum() == 0
    assert simulate_party(test_data["p_1"], 10)["Total guests"].sum() == 10
    with raises(ValueError):
        simulate_party([0], n_simulations=-5)


def test_plot_simulation(test_data):
    results = simulate_party(test_data["p_0"])
    plot = plot_simulation(results)
    assert isinstance(plot, alt.Chart)
    assert plot.mark == "bar"
    assert plot.data["Total guests"].sum() == 0


def test_load_party():
    df = load_party()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100