#!/usr/bin/python3
"""Creating a Simple Templating Program"""

import os

def generate_invitations(template, attendees):
    """
    Generating personalised invitation files for each attendee
    """
    # Checking input types
    if not isinstance(template, str):
        print("ERROR: Template NOT valid - needs to be a string.")
        exit()
    if not isinstance(attendees, list) or not all(isinstance(person, dict) for person in attendees):
        print("ERROR: Attendees list not valid - needs to be a list of dictionaries")
        exit()
        
    # Handling Empty Inputs
    if template == "":
        print("ERROR: Template CANNOT be empty")
        exit()
    if attendees == []:
        print("ERROR: Attendees CANNOT be empty")
        exit()
         
    # Process each attendee
    for index, person in enumerate(attendees, start=1):
        # get(variable, NA) means that get name other set to N/A if null
        # or NA used to ensure other values such as None, "", False or 0 is also default to NA
        name = person.get("name", "N/A") or "N/A"
        event_title = person.get("event_title", "N/A") or "N/A"
        event_date = person.get("event_date", "N/A") or "N/A"
        event_location = person.get("event_location", "N/A") or "N/A"
            
        # Making the personalised invitations
        invitation = template.replace("{name}", name) \
                        .replace("{event_title}", event_title) \
                        .replace("{event_date}", event_date) \
                        .replace("{event_location}", event_location)
        
        # Generate Output files
        output_filename = f"output_{index}.txt"
        
        if os.path.exists(output_filename):
            print(f"ERROR: {output_filename} already exists")
            continue

        try:
            with open(output_filename, "w") as f:
                f.write(invitation)
        except IOError as e:
                print(f"ERROR: Failed to write to {output_filename}. Error : {e}")
        
        
# Testing program
if __name__ == "__main__":
# Read template from template.txt
    with open('template.txt', 'r') as file:
        template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)
