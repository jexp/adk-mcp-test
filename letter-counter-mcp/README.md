# Letter Counter MCP Server

A FastMCP server that provides a tool to count letters and find their positions in a word.

## Features

The server provides a single tool:

### `count_letters(word: str, letter: str)`

Counts occurrences of a specific letter in a word and returns both the count and positions.

**Parameters:**
- `word` (str): The word to search in
- `letter` (str): The letter to count (single character)

**Returns:**
A dictionary containing:
- `count`: Number of occurrences of the letter
- `positions`: List of 0-based positions where the letter appears
- `word`: The original word
- `letter`: The letter that was searched for

**Features:**
- Case-insensitive matching
- Returns exact positions (0-based indexing)
- Error handling for invalid inputs

## Usage

### Running the Server

```bash
cd letter-counter-mcp
python server.py
```

### Testing

Run the test suite to verify functionality:

```bash
cd letter-counter-mcp
python test.py
```

## Examples

```python
# Count letter 'l' in "hello"
count_letters("hello", "l")
# Returns: {"count": 2, "positions": [2, 3], "word": "hello", "letter": "l"}

# Count letter 's' in "Mississippi" 
count_letters("Mississippi", "s")
# Returns: {"count": 4, "positions": [2, 3, 5, 6], "word": "Mississippi", "letter": "s"}

# Case insensitive matching
count_letters("Hello", "h")
# Returns: {"count": 1, "positions": [0], "word": "Hello", "letter": "h"}

# No matches found
count_letters("hello", "x")
# Returns: {"count": 0, "positions": [], "word": "hello", "letter": "x"}
```

## Error Handling

The tool handles various error cases:

- Empty word: Returns error message
- Invalid letter (not single character): Returns error message
- Non-string inputs: Type validation

## Integration

This MCP server can be integrated with various MCP clients and used as part of larger language model workflows for text analysis tasks.
