# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import unittest

from gaiatest import GaiaTestCase


class TestDebug(GaiaTestCase):

    expect_debug = False

    @unittest.expectedFailure
    def test_debug_expected(self):
        self.expect_debug = True
        self.lockscreen.unlock()
        self.assertTrue(False)

    def test_debug_not_expected(self):
        self.expect_debug = False
        self.assertTrue(True)

    def tearDown(self):
        GaiaTestCase.tearDown(self)
        debug_path = os.path.join('debug', self.__class__.__name__, self._testMethodName)
        for file_name in ['screenshot.png']:
            file_exists = os.path.isfile(os.path.join(debug_path, file_name))
            if self.expect_debug:
                self.assertTrue(file_exists)
            else:
                self.assertFalse(file_exists)
