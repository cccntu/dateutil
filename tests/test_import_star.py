"""Test for the "import *" functionality.

As import * can be only done at module level, it has been added in a separate file
"""
import pytest

prev_locals = list(locals())
from bs_dateutil import *

new_locals = {
    name: value for name, value in locals().items() if name not in prev_locals
}
new_locals.pop("prev_locals")


@pytest.mark.import_star
def test_imported_modules():
    """Test that `from bs_dateutil import *` adds modules in __all__ locally"""
    import bs_dateutil.easter
    import bs_dateutil.parser
    import bs_dateutil.relativedelta
    import bs_dateutil.rrule
    import bs_dateutil.tz
    import bs_dateutil.utils
    import bs_dateutil.zoneinfo

    assert bs_dateutil.easter == new_locals.pop("easter")
    assert bs_dateutil.parser == new_locals.pop("parser")
    assert bs_dateutil.relativedelta == new_locals.pop("relativedelta")
    assert bs_dateutil.rrule == new_locals.pop("rrule")
    assert bs_dateutil.tz == new_locals.pop("tz")
    assert bs_dateutil.utils == new_locals.pop("utils")
    assert bs_dateutil.zoneinfo == new_locals.pop("zoneinfo")

    assert not new_locals
