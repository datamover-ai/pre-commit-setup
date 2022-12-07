# -*- coding: utf-8 -*-

import pytest

from scr.math import calculate_log


class TestLog:
    """Test natural log function."""

    def test_function(self):
        """Check that log(1) = 0."""
        result = calculate_log(x=1)
        assert result == pytest.approx(0, rel=1e-09, abs=1e-09)
