#!/usr/bin/env python
# This is the main entry point for the Productivity Suite application.

from rich.console import Console
from rich.text import Text
import database
from todo import list_tasks, add_task, remove_task, update_task
from notes import view_notes, add_note
from pomodoro import start_pomodoro
from calculator import evaluate_expression

console = Console()

def get_id_input(prompt: str = "Enter ID: ") -> int | None:
    """Safely gets and validates a numerical ID from the user."""
    try:
        return int(console.input(f"[cyan]{prompt}[/cyan]"))
    except ValueError:
        console.print("[red]Invalid ID. Please enter a number.[/red]")
        return None

def show_todo_menu(conn):
    """Displays and handles the to-do list submenu."""
    while True:
        console.print("\n[bold blue]-- To-Do List --[/bold blue]")
        list_tasks(conn)
        console.print("\n[bold]Menu:[/bold] [a]dd, [r]emove, [u]pdate, [b]ack")
        choice = console.input("[bold cyan]> [/bold cyan]").lower()

        if choice == 'a':
            task = console.input("[cyan]Enter task: [/cyan]")
            if task: add_task(conn, task)
        elif choice == 'r':
            task_id = get_id_input("Enter task ID to remove: ")
            if task_id is not None: remove_task(conn, task_id)
        elif choice == 'u':
            task_id = get_id_input("Enter task ID to update: ")
            if task_id is not None:
                new_task = console.input("[cyan]Enter new task: [/cyan]")
                if new_task: update_task(conn, task_id, new_task)
        elif choice == 'b':
            break
        else:
            console.print("[yellow]Invalid option.[/yellow]")

def show_notes_menu(conn):
    """Displays and handles the notes manager submenu."""
    while True:
        console.print("\n[bold blue]-- Notes --[/bold blue]")
        view_notes(conn)
        console.print("[bold]Menu:[/bold] [a]dd, [b]ack")
        choice = console.input("[bold cyan]> [/bold cyan]").lower()

        if choice == 'a':
            content = console.input("[cyan]Enter note: [/cyan]")
            if content: add_note(conn, content)
        elif choice == 'b':
            break
        else:
            console.print("[yellow]Invalid option.[/yellow]")

def show_calculator_menu():
    """Displays and handles the calculator submenu."""
    console.print("\n[bold blue]-- Calculator --[/bold blue]")
    console.print("Enter an expression (e.g., 5 * 3) or 'back' to exit.")
    while True:
        expression = console.input("[bold cyan]> [/bold cyan]")
        if expression.lower() == 'back': break
        console.print(evaluate_expression(expression))

def main_menu(conn):
    """The main application loop that displays the primary menu."""
    menu_options = {
        "1": ("To-Do List", show_todo_menu),
        "2": ("Notes", show_notes_menu),
        "3": ("Pomodoro Timer", start_pomodoro),
        "4": ("Calculator", show_calculator_menu),
        "5": ("Exit", None)
    }

    while True:
        console.print("\n[bold green]-- PRODUCTIVITY SUITE --[/bold green]")
        for key, (name, _) in menu_options.items():
            console.print(f"  [cyan]{key}[/cyan]. {name}")
        
        choice = console.input("\nEnter your choice: ")

        if choice == '5':
            console.print("[bold cyan]Goodbye![/bold cyan]")
            break

        action = menu_options.get(choice)
        if action:
            handler = action[1]
            console.clear()
            if handler in [show_todo_menu, show_notes_menu]:
                handler(conn)
            else:
                handler()
        else:
            console.print("[red]Invalid choice.[/red]")

if __name__ == '__main__':
    db_conn = database.create_connection()
    if db_conn:
        database.create_tables(db_conn)
        console.clear()
        main_menu(db_conn)
        db_conn.close()
    else:
        console.print("[bold red]Failed to connect to the database.[/bold red]")
