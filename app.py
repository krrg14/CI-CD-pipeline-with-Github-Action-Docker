from flask import Flask, render_template

app = Flask(__name__)

PROGRAMS = [
    {
        "number": "01",
        "title": "Mysuru Palace Illumination",
        "category": "A city of a thousand lights",
        "date": "October 11–20",
        "time": "7:00 PM – 10:00 PM",
        "image": "/static/images/mysore-palace-dasara-illumination.jpg",
        "alt": "Mysore Palace illuminated with festival lights at night",
        "class": "program-card--wide",
    },
    {
        "number": "02",
        "title": "Jumboo Savari",
        "category": "The grand elephant procession",
        "date": "October 20",
        "time": "2:30 PM onwards",
        "image": "/static/images/mysore-dasara-procession.jpg",
        "alt": "Decorated Dasara elephants passing crowds during the Mysore procession",
        "class": "",
    },
    {
        "number": "03",
        "title": "Cultural Evenings",
        "category": "Music, dance & living traditions",
        "date": "October 11–19",
        "time": "6:00 PM – 9:00 PM",
        "image": "/static/images/mysore-dasara-crowds.jpg",
        "alt": "Performers and spectators at a Mysore Dasara street celebration",
        "class": "",
    },
    {
        "number": "04",
        "title": "Torchlight Parade",
        "category": "A spectacular night finale",
        "date": "October 20",
        "time": "7:00 PM onwards",
        "image": "/static/images/mysore-dasara-procession.jpg",
        "alt": "The Mysore Dasara elephant procession moving through the city",
        "class": "program-card--wide",
    },
]

EVENTS = [
    {
        "day": "11",
        "month": "OCT",
        "title": "Navaratri Begins",
        "detail": "Ten days of devotion, music and celebration",
        "location": "Mysuru",
        "image": "/static/images/mysore-palace-dasara-illumination.jpg",
        "alt": "Mysore Palace shining with Dasara illumination",
    },
    {
        "day": "18",
        "month": "OCT",
        "title": "Dasara Cultural Night",
        "detail": "An evening of dance, song and local artists",
        "location": "Open Air Stage",
        "image": "/static/images/mysore-dasara-crowds.jpg",
        "alt": "A Mysore Dasara procession and its large crowd of spectators",
    },
    {
        "day": "20",
        "month": "OCT",
        "title": "Vijayadashami",
        "detail": "The grand procession and Dasara finale",
        "location": "Mysuru Palace to Bannimantap",
        "image": "/static/images/mysore-dasara-procession.jpg",
        "alt": "Decorated elephants lead the Mysore Dasara procession",
    },
]

GALLERY = [
    {
        "image": "/static/images/mysore-ambari.jpg",
        "alt": "The flower-decorated golden ambari carried in the Mysore Dasara procession",
        "caption": "The spirit of the procession",
        "class": "gallery-item--tall",
    },
    {
        "image": "/static/images/mysore-palace-dasara-illumination.jpg",
        "alt": "Mysore Palace illuminated for Dasara",
        "caption": "Palace after dark",
        "class": "",
    },
    {
        "image": "/static/images/mysore-dasara-crowds.jpg",
        "alt": "Performers and spectators at the Mysore Dasara procession",
        "caption": "Culture takes center stage",
        "class": "",
    },
    {
        "image": "/static/images/mysore-dasara-procession.jpg",
        "alt": "The Mysore Dasara procession passing spectators",
        "caption": "A city in celebration",
        "class": "gallery-item--wide",
    },
    {
        "image": "/static/images/mysore-palace-night-illumination.jpg",
        "alt": "Mysore Palace glowing with lights after dark",
        "caption": "Ten nights of light",
        "class": "",
    },
]


@app.get("/")
def home():
    return render_template("index.html", programs=PROGRAMS, events=EVENTS, gallery=GALLERY)


if __name__ == "__main__":
    app.run(debug=True)
