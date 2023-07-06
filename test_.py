import pytest
from dash.testing.application_runners import import_app

def test_app_elements(dash_duo):
    from app import create_my_dash_app 

    app = create_my_dash_app()
    dash_duo.start_server(app)

    header = dash_duo.wait_for_element("#graph_settings_header")
    assert header.text == "Graph Settings:"
    assert dash_duo.wait_for_element("#sales_graph")
    assert dash_duo.wait_for_element("#region_filter")
