# Import FreeSimpleGUI library for creating the graphical user interface
import FreeSimpleGUI as sg
# Import the km_to_miles function from the conversion_def module
from conversion_def import km_to_miles

# Create GUI elements
# Label for the kilometer input
label = sg.Text("Kilometers: ")
# Input box for entering kilometers, with a tooltip and a key for identification
input_box = sg.InputText(tooltip="Enter todo", key="kms")
# Button to trigger the conversion
miles_button = sg.Button("Convert")

# Text element to display the conversion result
output = sg.Text(key="output")

# Create the main window with all GUI elements
window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))

# Main event loop
while True:
    # Read events and values from the window
    event, values = window.read()

    # Use match-case statement to handle different events
    match event:
        case "Convert":
            # Get the kilometer value from the input box
            km = values["kms"]
            # Convert kilometers to miles using the imported function
            result = km_to_miles(km)
            # Update the output text with the conversion result
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            # Break the loop if the window is closed
            break

# Close the window when the loop exits
window.close()