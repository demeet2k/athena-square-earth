#!/usr/bin/env python3
# CRYSTAL: Xi108:W1:A4:S1 | face=S | node=1 | depth=0 | phase=Fixed
# METRO: Me
# BRIDGES: Xi108:W1:A4:S2→Xi108:W2:A4:S1→Xi108:W1:A3:S1→Xi108:W1:A5:S1

"""
test_golden_vectors.py — pytest-compatible test suite

Wraps verifier.py golden vectors as individual pytest test cases.
Run with: python -m pytest test_golden_vectors.py -v
"""

import pytest
from .verifier import ALL_TESTS, run_all

@pytest.fixture(params=ALL_TESTS, ids=[t.__name__ for t in ALL_TESTS])
def golden_test(request):
    return request.param

def test_golden_vector(golden_test):
    """Each golden test vector must pass."""
    result = golden_test()
    assert result.passed, f"{result.name}: {result.detail}"

def test_all_vectors_pass():
    """Meta-test: all vectors pass in one run."""
    results = run_all()
    failed = [r for r in results if not r.passed]
    assert not failed, f"Failed: {[str(r) for r in failed]}"
