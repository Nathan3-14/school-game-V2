from datetime import datetime

def error(message: str, console, message_start: str="Err"):
    display_message = f"[red]{message_start}[/red]: {message}"
    console.print(display_message)