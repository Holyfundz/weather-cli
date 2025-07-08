import requests
from rich import print
def weather():
    city = input("Enter the name of city: ")
    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url)
        if response.ok:
            print(f"[bold cyan]Weather:[/bold cyan] {response.text}")
        else:
            print("[red]Failed to fetch weather info[/red]")
    except Exception as e:
        print(f"[red]Error:[/red] {e}")
 