import re

import oli2d


def test_oli2d_version() -> None:
    assert re.match(r"\d+\.\d+\.\d+", oli2d.__version__)
