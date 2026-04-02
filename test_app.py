from visualizer import app

def test_header_present():
    layout = app.layout
    assert layout.children[0].children == "Pink Morsel Sales Dashboard"

def test_graph_present():
    layout = app.layout
    graph = layout.children[2]
    assert graph.id == "sales-chart"

def test_region_picker_present():
    layout = app.layout
    radio = layout.children[1]
    assert radio.id == "region-filter"