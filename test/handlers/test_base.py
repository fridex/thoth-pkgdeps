#!/usr/bin/env python3
# thoth-package-extract
# Copyright(C) 2018, 2019, 2020 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Testing base handler."""

import pytest

from thoth.package_extract.handlers import HandlerBase

from ..case import raw_and_recover_changes


class TestHandlerBase:
    """Test :class:thoth.package_extract.handlers.HandlerBase."""

    class FooHandler(HandlerBase):  # noqa D106
        def run(self, input_text):  # noqa D102
            return ["foo"]

    class BarHandler(HandlerBase):  # noqa D106
        def run(self, input_text):  # noqa D102
            return ["boo"]

    @raw_and_recover_changes
    def test_register(self):  # noqa D102
        HandlerBase.register(TestHandlerBase.FooHandler)
        HandlerBase.register(TestHandlerBase.BarHandler)

        assert HandlerBase.get_handler_names() == [
            TestHandlerBase.FooHandler.__name__,
            TestHandlerBase.BarHandler.__name__,
        ]

    @raw_and_recover_changes
    def test_instantiate_handlers(self):  # noqa D102
        HandlerBase.register(TestHandlerBase.FooHandler)
        HandlerBase.register(TestHandlerBase.BarHandler)

        instantiated_handlers = list(HandlerBase.instantiate_handlers())
        assert len(instantiated_handlers) == 2
        assert type(instantiated_handlers[0] == TestHandlerBase.FooHandler)
        assert type(instantiated_handlers[0] == TestHandlerBase.BarHandler)

    def test_run(self):  # noqa D102
        with pytest.raises(NotImplementedError):
            HandlerBase().run("Foo")

    def test_initial_setup(self):  # noqa D102
        assert set(HandlerBase.get_handler_names()) == {"YUM", "PIP3"}
