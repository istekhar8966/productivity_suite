#!/usr/bin/env python
# Contains all functions for the to-do list feature.

from rich.console import Console
from rich.table import Table
import sqlite3

console = Console()

def add_task(conn, task):
    """Adds a new task to the database."""
    try:
        c = conn.cursor()
        c.execute("INSERT INTO todos (task, status) VALUES (?, ?)", (task, 'pending'))
        conn.commit()
        console.print("[green]✓ Task added.[/green]")
    except sqlite3.Error as e:
        console.print(f"[red]Error adding task: {e}[/red]")

def remove_task(conn, task_id):
    """Removes a task from the database by its ID."""
    try:
        c = conn.cursor()
        c.execute("DELETE FROM todos WHERE id = ?", (task_id,))
        conn.commit()
        console.print("[green]✓ Task removed.[/green]")
    except sqlite3.Error as e:
        console.print(f"[red]Error removing task: {e}[/red]")

def update_task(conn, task_id, new_task):
    """Updates the description of a task by its ID."""
    try:
        c = conn.cursor()
        c.execute("UPDATE todos SET task = ? WHERE id = ?", (new_task, task_id))
        conn.commit()
        console.print("[green]✓ Task updated.[/green]")
    except sqlite3.Error as e:
        console.print(f"[red]Error updating task: {e}[/red]")

def list_tasks(conn):
    """Retrieves all tasks and displays them in a clean, borderless table."""
    try:
        c = conn.cursor()
        c.execute("SELECT id, task, status FROM todos ORDER BY id")
        tasks = c.fetchall()

        if not tasks:
            console.print("[yellow]No tasks yet. Add one to get started![/yellow]")
            return

        # A borderless table is cleaner and simpler than a boxed one.
        table = Table.grid(padding=(0, 2))
        table.add_column(style="cyan")  # ID
        table.add_column(style="magenta") # Task
        table.add_column(style="green") # Status

        for task in tasks:
            table.add_row(f"[{task[0]}]", task[1], f"({task[2]})")

        console.print(table)

    except sqlite3.Error as e:
        console.print(f"[red]Error listing tasks: {e}[/red]")
