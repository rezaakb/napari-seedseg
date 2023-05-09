import numpy as np

from napari_seedseg import SeedSegWidget



def test_1(make_napari_viewer):

    # make viewer and add an image layer using our fixture
    viewer = make_napari_viewer()
    viewer.add_image(np.random.random((100, 100)))

    # create our widget, passing in the viewer
    my_widget = SeedSegWidget(viewer)

    res = my_widget.validate_confirm()


    assert res == True


def test_2(make_napari_viewer):

    # make viewer and add an image layer using our fixture
    viewer = make_napari_viewer()

    # create our widget, passing in the viewer
    my_widget = SeedSegWidget(viewer)

    res = my_widget.validate_confirm()


    assert res == False