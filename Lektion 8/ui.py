# Se till att namnet på denna fil är ui.py
# importera med "import ui"

ui_width = 40

def line(dots = False):
    if not dots:
        print("-" * ui_width)
    else:
        print("*" * ui_width)
        
def header(header):
    print(f"| {header.center(ui_width)}|")

def echo(echo):
    print(f"| {echo} ")

def prompt(inp):
    inp = input("Val: ")
    print(f"| {inp}")

