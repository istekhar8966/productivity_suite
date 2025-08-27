#!/usr/bin/env python
# Contains all functions for the notes manager feature.

from rich.console import Console
import sqlite3

console = Console()

def add_note(conn, content):
    """Adds a new note to the database."""
    try:
        c = conn.cursor()
        c.execute("INSERT INTO notes (content) VALUES (?)", (content,))
        conn.commit()
        console.print("[green]✓ Note added.[/green]")
    except sqlite3.Error as e:
        console.print(f"[red]Error adding note: {e}[/red]")

def view_notes(conn):
    """Retrieves and displays all notes from the database using simple text formatting."""
    try:
        c = conn.cursor()
        c.execute("SELECT id, content FROM notes ORDER BY id DESC")
        notes = c.fetchall()

        if not notes:
            console.print("[yellow]No notes yet.[/yellow]")
            return

        console.print()
        for note in notes:
            # Displaying notes as simple styled text is cleaner than using panels.
            console.print(f"[bold cyan]Note #{note[0]}[/bold cyan]")
            console.print(f"{note[1]}\n")

    except sqlite3.Error as e:
        console.print(f"[red]Error viewing notes: {e}[/red]")