from iob_core import iob_core


class axi_interconnect(iob_core):
    def __init__(self, *args, **kwargs):
        self.set_default_attribute("version", "0.1")

        super().__init__(*args, **kwargs)
