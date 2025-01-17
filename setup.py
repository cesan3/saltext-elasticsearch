# pylint: disable=missing-module-docstring
import sys

import semantic_release
import setuptools

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass

if __name__ == "__main__":
    setuptools.setup(use_scm_version=True)
