#!/usr/bin/env python3
"""
Test script for the Letter Counter MCP Server
"""

import sys
import os

# Add the server directory to the path
sys.path.insert(0, os.path.dirname(__file__))

from server import count_letters_ as count_letters

def test_count_letters():
    """Test the count_letters function with various inputs"""
    
    # Test case 1: Basic functionality
    result = count_letters("hello", "l")
    print(f"Test 1 - count_letters('hello', 'l'): {result}")
    assert result["count"] == 2
    assert result["positions"] == [2, 3]
    
    # Test case 2: No matches
    result = count_letters("hello", "x")
    print(f"Test 2 - count_letters('hello', 'x'): {result}")
    assert result["count"] == 0
    assert result["positions"] == []
    
    # Test case 3: Case insensitive
    result = count_letters("Hello", "h")
    print(f"Test 3 - count_letters('Hello', 'h'): {result}")
    assert result["count"] == 1
    assert result["positions"] == [0]
    
    # Test case 4: Multiple occurrences
    result = count_letters("Mississippi", "s")
    print(f"Test 4 - count_letters('Mississippi', 's'): {result}")
    assert result["count"] == 4
    assert result["positions"] == [2, 3, 5, 6]
    
    # Test case 5: Empty word
    result = count_letters("", "a")
    print(f"Test 5 - count_letters('', 'a'): {result}")
    assert result["count"] == 0
    assert "error" in result
    
    # Test case 6: Invalid letter (multiple characters)
    result = count_letters("hello", "ll")
    print(f"Test 6 - count_letters('hello', 'll'): {result}")
    assert result["count"] == 0
    assert "error" in result
    
    print("All tests passed!")

if __name__ == "__main__":
    test_count_letters()
