from flask import Blueprint, render_template
from flask_login import current_user, login_required
from website.stats_support import make_stats
import random

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    if current_user.is_authenticated:
        return render_template('user-homepage.html')
    else:
        return render_template('homepage.html')
        
@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', stats = make_stats())

@views.route('/games')
def games():
    return render_template('gamepage.html')

# Game 1 - reaction time
@views.route('/games/reactionTime')
def reactionTime():
    return

# Game 2 - sequence memory
@views.route('/games/sequenceMemory')
def sequenceMemory():
    return render_template("sequence-startscreen.html")

@views.route('/games/sequenceMemoryRunGame')
def displaySequence():
    return render_template("sequence-run-game.html")

# Game 3 - word generation
@views.route('/games/wordGeneration')
def wordGeneration():
    return render_template('wordGeneration.html')

# Game 4 - matching colors
@views.route('/games/matchingColors')
def matchingColors():
    return render_template('matchingColors-startscreen.html')

@views.route('/games/matchingColorsRunGame')
def displayGrid():
    return render_template("matchingColors-run-game.html")

# Game 5 - pattern memory
@views.route('/games/patternMemory')
def patternMemory():
    return render_template("pattern-startscreen.html")

@views.route('/games/patternMemoryRunGame')
def displayPattern():
    return render_template("pattern-run-game.html")

# Game 6 - quick calculus
@views.route('/games/calculus')
def calculus():
    return render_template('calculus-startscreen')

@views.route('/games/calculusRunGame')
def calculusExecution():
    return render_template('calculus-run-game.html')

# Game 7 - aim training
@views.route('/games/aimTraining')
def aimTraining():
    return render_template("aimTraining-startscreen.html")

@views.route('/games/aimTrainingRunGame')
def aimSession():
    return render_template("aimTraining-run-game.html")

# Game 8
@views.route('games/game8')
def game8():
    return
