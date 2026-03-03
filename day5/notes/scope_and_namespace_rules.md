# Scope and Namespace Rules

## Local Scope
Variables created inside a function are strictly local to that function's Memory Frame. They do not exist in the outside world.

## Global Scope
Variables created at the highest structural level of your script (zero indentation). They persist for the entire lifetime of the program execution.

## The LEGB Rule
When you reference a variable `x`, Python searches scopes in this strict order:
1. **L**ocal (Inside the current function)
2. **E**nclosing (Inside any parent functions, if nested)
3. **G**lobal (At the module/script level)
4. **B**uilt-in (Python's native keywords like `len`, `range`)

## Shadowing Variables
If a global variable is named `count`, and you define a local variable `count` inside your function, the local variable "shadows" (hides) the global one. Any modifications only affect the local version.

## Why Globals are Dangerous in CP
If you use global variables to store graph traversal states, and run multiple test cases in a single script, Test Case 2 will accidentally read the polluted, mutated data left over from Test Case 1.
*Always pass state as a parameter or initialize it fresh inside the solver function.*

## The Pure Function Principle
A pure function maps Input to Output. That is its only interaction with the universe. It refuses to read from Global scope, and refuses to write to Global scope.\n