# Python Learning Journey

## Assignments Overview

### 00 - Introduction & Basic Python Scripts
- Python syntax fundamentals  
- Variables and basic I/O  
- Running Python scripts  
- Simple calculations and printing  

### 01 - Expressions
- Mathematical operations (`+`, `-`, `*`, `/`, `%`, `**`)  
- Logical conditions (`and`, `or`, `not`)  
- Comparison operators (`==`, `!=`, `>`, `<`)  
- Variable assignments and expressions  

### 02 - Lists
- Creating and indexing lists  
- Slicing operations  
- List methods (`append()`, `remove()`, `sort()`)  
- Common list operations  

### 03 - Dictionaries
- Key-value pair storage  
- Accessing and modifying values  
- Dictionary methods (`keys()`, `values()`, `items()`)  
- Iterating through dictionaries  

### 04 - If Statements
- Conditional logic (`if`, `elif`, `else`)  
- Nested conditionals  
- Truthy/falsy values  
- Ternary operators  

### 05 - Loops & Control Flow
- `for` and `while` loops  
- Loop control (`break`, `continue`, `pass`)  
- List/dictionary comprehensions  
- Iterables and iterators  

### 06 - Functions
- Defining and calling functions  
- Parameters and arguments  
- Return values  
- Scope and namespaces  

### 07 - Information Flow
- Program structure and organization  
- Data passing between functions  
- Variable scope (`global`, `nonlocal`)  
- Best practices for clean code  

---

## 🌈 Terminal Formatting with ANSI Escape Codes

Enhance your terminal output with text styling and colors:

### Basic Formatting
```python
print("\033[1mBold Text\033[0m")        # Bold
print("\033[3mItalic Text\033[0m")      # Italic 
print("\033[4mUnderlined Text\033[0m")  # Underline
Color Palette
Code	Color	Example
\033[31m	Red	🔴 Error messages
\033[32m	Green	🟢 Success indicators
\033[33m	Yellow	🟡 Warnings
\033[34m	Blue	🔵 Information
\033[35m	Magenta	🟣 Debugging output
\033[36m	Cyan	🏷️ Labels
Combined Styles
python
Copy
# Bold yellow text
print("\033[1;33mWarning!\033[0m")  

# Underlined cyan text  
print("\033[4;36mImportant:\033[0m")
Pro Tips
Always reset formatting with \033[0m

Combine styles: \033[1;4;31m (Bold+Underline+Red)

For Windows: Use Windows Terminal or enable ANSI support

"Good code is its own best documentation." - Steve McConnell

Happy Coding! 🚀🐍