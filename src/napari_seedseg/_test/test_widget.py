import numpy as np

from napari_seedseg import SeedSegWidget

def test_1(make_napari_viewer, capsys):
    # make viewer and add an image layer using our fixture
    viewer = make_napari_viewer
    viewer.add_image(np.random.random((100, 100)))
    
    # create our widget, passing in the viewer
    my_widget = SeedSegWidget(viewer)

    # call our widget method
    my_widget._on_click()

    # read captured output and check that it's as we expected
    captured = capsys.readouterr()

    assert captured.out == "napari has run\n"