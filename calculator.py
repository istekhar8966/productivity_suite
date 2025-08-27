#!/usr/bin/env python
# A simple, non-interactive calculator module.

import operator

def get_operator_fn(op: str):
    """Maps an operator string to a function from the operator module."""
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
    }.get(op)

def evaluate_expression(expression: str) -> str:
    """
    Safely evaluates a simple arithmetic expression string.
    Avoids using `eval()` for security reasons, instead parsing the expression manually.
    Expected format: "number operator number" (e.g., "5 * 3").
    """
    try:
        parts = expression.split()
        if len(parts) != 3:
            return "[red]Invalid format. Use: number operator number (e.g., 5 * 3)[/red]"
        
        num1 = float(parts[0])
        op_str = parts[1]
        num2 = float(parts[2])

        op_fn = get_operator_fn(op_str)
        if not op_fn:
            return f"[red]Unknown operator: {op_str}[/red]"

        result = op_fn(num1, num2)
        return f"[green]Result: {result}[/green]"
    except ValueError:
        return "[red]Invalid numbers in expression.[/red]"
    except ZeroDivisionError:
        return "[red]Error: Division by zero.[/red]"
    except Exception as e:
        return f"[red]An unexpected error occurred: {e}[/red]"