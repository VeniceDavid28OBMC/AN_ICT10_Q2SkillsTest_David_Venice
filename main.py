from pyscript import document

clubs = {
    "film": {
        "text": """Thomasian Film Society

Description: A creative organization for students passionate about filmmaking, storytelling, and visual media.
Meeting Time: Tuesday, 3:45–5:30 PM
Location: Computer Lab
Club Moderator: Ms. Pasco
Number of Members: 18""",
        "image": "film.jpg"
    },

    "debate": {
        "text": """Thomasian Debaters Council

Description: An academic club that develops critical thinking, public speaking, and persuasive argumentation.
Meeting Time: Friday, 4:00–6:00 PM
Location: Music Room
Club Moderator: Mr. Cruz
Number of Members: 22""",
        "image": "debate.jpg"
    },

    "cfc": {
        "text": """CFC Youth for Christ
        
Description: A faith-based youth organization focused on spiritual growth, leadership, and service.
Meeting Time: Monday, 4:00–6:00 PM
Location: Gym
Club Moderator: Coach Reyes
Number of Members: 30""",
        "image": "cfc.jpg"
    },

    "bosco": {
        "text": """Bosconian Thomasian Youth Movement

Description: A youth movement centered on values formation, leadership, and community service.
Meeting Time: Monday, 4:00–6:00 PM
Location: Gym
Club Moderator: Coach Reyes
Number of Members: 30""",
        "image": "bosco.jpg"
    },

   "annyeong": {
        "text": """Annyeong Tomasino

Description: A cultural club celebrating Korean language, traditions, and modern culture.
Meeting Time: Tuesday, 3:45–5:30 PM
Location: Computer Lab
Club Moderator: Ms. Pasco
Number of Members: 18""",
        "image": "annyeong.jpg"
    },

    "nihon": {
        "text": """Thomasian Nihon Kyoukai

Description: An organization dedicated to promoting Japanese culture, language, and traditions.
Meeting Time: Friday, 4:00–6:00 PM
Location: Music Room
Club Moderator: Mr. Cruz
Number of Members: 22""",
        "image": "nihon.jpg"
    },

    "yellow": {
        "text": """UST Yellow Jackets

Description: The official pep organization that promotes school spirit and supports athletic events.
Meeting Time: Monday, 4:00–6:00 PM
Location: Gym
Club Moderator: Coach Reyes
Number of Members: 30""",
        "image": "yellow.jpg"
    },

    "media": {
        "text": """Tomasian Media Circle and Talents

Description: A media organization responsible for creative content, documentation, and storytelling.
Meeting Time: Monday, 4:00–6:00 PM
Location: Gym
Club Moderator: Coach Reyes
Number of Members: 30a""",
        "image": "media.jpg"
    },

    "unicef": {
        "text": """UST Volunteers for UNICEF

Description: A humanitarian club advocating for children’s rights and social awareness.
Meeting Time: Monday, 4:00–6:00 PM
Location: Gym
Club Moderator: Coach Reyes
Number of Members: 30""",
        "image": "unicef.jpg"
    },

    "hiraya": {
        "text": """UST Hiraya

Description: A creative and advocacy-based organization promoting Filipino identity and imagination.
Meeting Time: Monday, 4:00–6:00 PM
Location: Gym
Club Moderator: Coach Reyes
Number of Members: 30""",
        "image": "usthiraya.jpg"
    }
}

def show_info(event=None):
    selected = document.getElementById("club").value
    document.getElementById("club_info").innerText = clubs[selected]["text"]
    document.getElementById("club_img").src = clubs[selected]["image"]