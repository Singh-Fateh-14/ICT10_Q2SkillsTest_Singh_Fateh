from pyscript import window

# Dictionary containing all required club details
# Fields: Name, Description, Meeting Time, Location, Moderator, Members
club_data = {
    "Marching Band": {
        "Description": "Musical marching ensemble for school events.",
        "Meeting Time": "Tuesday and Wednesday 03:00-4:30 PM",
        "Location": "Band Room",
        "Moderator": "Mr. Emilio Alumno",
        "Members": 35
    },
    "Glee Club": {
        "Description": "Vocal group specializing in choir and singing.",
        "Meeting Time": "Monday 03:00- 05:00 PM",
        "Location": "High School Music Room",
        "Moderator": "Mr. Denver Martin",
        "Members": 25
    },
    "Dance Club": {
        "Description": "Performing arts club focusing on various dance styles.",
        "Meeting Time": "Tuesday 03:00 - 05:00 PM",
        "Location": "Teatro Preciosa",
        "Moderator": "Mr. Alfred Cases",
        "Members": 40
    },
    "Math Club": {
        "Description": "Enhancing mathematical skills and competitions.",
        "Meeting Time": "Monday 02:30- 03:00 PM",
        "Location": "Room 404",
        "Moderator": "Mr. Nicole Gabuya",
        "Members": 20
    },
    "Science Club": {
        "Description": "Exploration of scientific concepts and experiments.",
        "Meeting Time": "Tuesday 03:00 - 04:00 PM",
        "Location": "Room 404",
        "Moderator": "Ms. Jameelyn Maramag",
        "Members": 30
    },
    "Communications Arts Club": {
        "Description": "Focusing on journalism, speech, and literature.",
        "Meeting Time": "Wed 03:00-4:00 PM, Fri 03:00-4:00 PM",
        "Location": "Room 406",
        "Moderator": "Ms. Yannis Fernandez",
        "Members": 22
    },
    "COCC": {
        "Description": "Cadet Officer Candidate Course leadership training.",
        "Meeting Time": "Wednesday 02:30 -04:30 PM",
        "Location": "Quadrangle / Teatro Preciosa",
        "Moderator": "SSgt. Jemima David PA (Res)",
        "Members": 50
    },
    "Social Science Club": {
        "Description": "Study of society and social relationships.",
        "Meeting Time": "Tuesday 03:00 - 4:00 PM",
        "Location": "Room 409",
        "Moderator": "Mr. Roberto Lim",
        "Members": 18
    },
    "Volleyball Varsity": {
        "Description": "Official school volleyball team training.",
        "Meeting Time": "Wednesday 03:00 - 04:00 PM",
        "Location": "Quadrangle",
        "Moderator": "Mr. Adrian Ruiz",
        "Members": 15
    },
    "Basketball Varsity": {
        "Description": "Official school basketball team training.",
        "Meeting Time": "Monday 03:00 - 04:00 PM",
        "Location": "Quadrangle",
        "Moderator": "Mr. Adrian Ruiz",
        "Members": 15
    }
}

# Function to display the information using Python
def display_club_info(event):
    doc = window.document
    selected_club = doc.getElementById("club_list").value
    
    if selected_club in club_data:
        info = club_data[selected_club]
        
        # Formatting the output string to show all dictionary items
        output = (
            f"Club Name: {selected_club}\n"
            f"Description: {info['Description']}\n"
            f"Meeting Time: {info['Meeting Time']}\n"
            f"Location: {info['Location']}\n"
            f"Moderator: {info['Moderator']}\n"
            f"Number of Members: {info['Members']}"
        )
        
        # Displaying the content and making the box visible
        doc.getElementById("display_area").style.display = "block"
        doc.getElementById("club_content").innerText = output