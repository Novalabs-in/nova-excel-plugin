import pytest
import main

def test_novaexcelanalyst_instantiation():
    # Verify that the class NovaExcelAnalyst is inspectable and loadable
    assert hasattr(main, 'NovaExcelAnalyst')

