#!/usr/bin/env python3
"""
Letter Counter MCP Server

A FastMCP server that provides a tool to count letters and find their positions in a word.
"""

from typing import Dict, List, Any
from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Letter Counter")


@mcp.tool()
def count_letters(word: str, letter: str) -> Dict[str, Any]:
    """
    Count occurrences of a letter in a word and return both count and positions.
    
    Args:
        word (str): The word to search in
        letter (str): The letter to count (single character)
    
    Returns:
        Dict containing:
        - count: Number of occurrences of the letter
        - positions: List of 0-based positions where the letter appears
        - word: The original word
        - letter: The letter that was searched for
    """
    return count_letters_(word, letter)

def count_letters_(word: str, letter: str) -> Dict[str, Any]:
    if not word:
        return {
            "count": 0,
            "positions": [],
            "word": word,
            "letter": letter,
            "error": "Word cannot be empty"
        }
    
    if not letter or len(letter) != 1:
        return {
            "count": 0,
            "positions": [],
            "word": word,
            "letter": letter,
            "error": "Letter must be a single character"
        }
    
    # Convert to lowercase for case-insensitive comparison
    word_lower = word.lower()
    letter_lower = letter.lower()
    
    positions = []
    count = 0
    
    for i, char in enumerate(word_lower):
        if char == letter_lower:
            positions.append(i)
            count += 1
    
    return {
        "count": count,
        "positions": positions,
        "word": word,
        "letter": letter
    }

if __name__ == "__main__":
    mcp.run()
