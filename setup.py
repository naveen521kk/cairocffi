import sys

from setuptools import setup

if sys.version_info.major < 3:
    raise RuntimeError(
        'cairocffi does not support Python 2.x anymore. '
        'Please use Python 3 or install an older version of cairocffi.')
from wheel.bdist_wheel import bdist_wheel

class BdistWheel(bdist_wheel):
    def get_tag(self):
        return ('py3', 'none') + bdist_wheel.get_tag(self)[2:]
cmdclass = {
    'bdist_wheel': BdistWheel,
}
setup(
    cmdclass=cmdclass,
    cffi_modules=[
        'cairocffi/ffi_build.py:ffi',
        'cairocffi/ffi_build.py:ffi_pixbuf'],
    setup_requires=['setuptools_scm[toml]']
)
