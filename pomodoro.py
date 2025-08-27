#!/usr/bin/env python
# Implements the Pomodoro timer feature.

import time
from rich.console import Console
from rich.align import Align
from rich.live import Live
from rich.text import Text
from digital_clock import generate_clock_text

console = Console()

def run_timer(timer_type: str, minutes: int):
    """Runs a countdown timer for a given number of minutes."""
    total_seconds = minutes * 60

    try:
        with Live(console=console, screen=True, redirect_stderr=False, transient=True) as live:
            while total_seconds >= 0:
                mins, secs = divmod(total_seconds, 60)
                time_str = f"{mins:02d}:{secs:02d}"
                
                # Generate the large clock display from the helper module.
                clock_text = generate_clock_text(time_str)
                
                display_block = Text(f"{timer_type}\n\n{clock_text}", justify="center")
                
                live.update(Align.center(display_block, vertical="middle"))
                
                if total_seconds == 0:
                    break
                    
                time.sleep(1)
                total_seconds -= 1
    except KeyboardInterrupt:
        console.print("\n[yellow]Timer stopped.[/yellow]")
        return

    console.print(f"[bold green]✓ {timer_type} finished![/bold green]")

def start_pomodoro():
    """Handles user input for the timer sessions."""
    try:
        work_minutes_str = console.input("[cyan]Enter work duration in minutes (default: 25):[/cyan] ") or "25"
        break_minutes_str = console.input("[cyan]Enter break duration in minutes (default: 5):[/cyan] ") or "5"
        work_minutes = int(work_minutes_str)
        break_minutes = int(break_minutes_str)
    except ValueError:
        console.print("[red]Invalid input. Using default values (25/5).[/red]")
        work_minutes = 25
        break_minutes = 5

    run_timer(f"{work_minutes} Minute Work Session", work_minutes)
    run_timer(f"{break_minutes} Minute Break", break_minutes)