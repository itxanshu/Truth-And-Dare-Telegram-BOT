import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# List of truth questions
truths = [
    "What is the most embarrassing thing that has ever happened to you?",
    "What is the craziest thing you have ever done?",
    "What is your biggest fear?",
    "What is the most illegal thing you have ever done?",
    "What is the worst date you have ever been on?",
    "What is your biggest regret?",
    "What is the most embarrassing thing you have ever done in front of your crush?",
    "What is the most childish thing you still do?",
    "What is the most ridiculous thing you have ever bought?",
    "What is the most embarrassing thing in your room right now?",
    "What was the last lie you told?",
    "Have you ever cheated on a test or an exam?",
    "What is your biggest fear?",
    "What is the craziest thing you have ever done?",
    "Have you ever stolen anything?",
    "What is your biggest regret?",
    "Have you ever been in love with someone you couldn't be with?",
    "Have you ever lied to get out of trouble?",
    "Have you ever been in a physical fight?",
    "What is the worst thing you have ever done to someone?",
    "Have you ever been attracted to someone of the same gender?",
    "What is the most embarrassing thing that has ever happened to you?",
    "Have you ever been caught doing something you shouldn't have been doing?",
    "What is the most illegal thing you have ever done?",
    "Have you ever cheated on a partner?",
    "What is the most embarrassing thing you have ever done in front of a crush?",
    "Have you ever lied to a friend to avoid hanging out with them?",
    "What is the most childish thing you still do?",
    "Have you ever gotten into a car accident?",
    "What is the most ridiculous thing you have ever bought?",
    "Have you ever used someone else's toothbrush?",
    "What is the most embarrassing thing in your room right now?",
    "Have you ever been in trouble with the law?",
    "What is the worst date you have ever been on?",
    "Have you ever had a one-night stand?",
    "What is the most embarrassing thing you have ever said in public?",
    "Have you ever lied on your resume or job application?",
    "What is the most embarrassing thing you have ever worn?",
    "Have you ever cheated on a diet or exercise routine?",
    "What is the most embarrassing thing you have ever done on social media?",
    "Have you ever shoplifted?",
    "What is the most embarrassing thing you have ever done in front of your parents?",
    "Have you ever been in a hit and run accident?",
    "What is the most embarrassing thing you have ever said in front of your crush?",
    "Have you ever told a secret that you were sworn to keep?",
    "What is the most illegal thing you have ever done and gotten away with?",
    "Have you ever been fired from a job?",
    "What is the most embarrassing thing you have ever done at work?",
    "Have you ever been in love with someone who was already in a relationship?",
    "What is the most embarrassing thing you have ever done while drunk?",
    "Have you ever lied to get out of trouble with your parents?",
    "What is the most embarrassing thing you have ever done while on a date?",
    "Have you ever stolen something from a friend?",
    "What is the most embarrassing thing you have ever done in front of your teacher?",
    "Have you ever gotten into a fight with a family member?",
    "What is the most illegal thing you have ever done but didn't get caught?",
    "Have you ever lied to your partner about where you were?",
    "What is the most embarrassing thing you have ever done in front of a group of people?",
    "Have you ever been in a car with someone who was driving under the influence?",
    "What is the most embarrassing thing you have ever done on a video call?",
    "Have you ever been fired from a job for doing something wrong?",
    "What is the most embarrassing thing you have ever done in front of a celebrity?",
    "Have you ever been in a car accident that was your fault?",
    "What is the most embarrassing thing you have ever done in front of your",


]

# List of dare tasks
dares = [
    "Eat a spoonful of mustard.",
    "Do 10 push-ups.",
    "Sing a song out loud.",
    "Act like a chicken for 30 seconds.",
    "Call a friend and tell them you love them.",
    "Wear your clothes inside out for the rest of the game.",
    "Text your ex and say you miss them.",
    "Do a dance in public.",
    "Say the alphabet backwards.",
    "Make a funny face and take a picture.",
    "Do the worm in the middle of a crowded area.",
    "Sing a song in a public place without any instrumental accompaniment.",
    "Call a random person and sing them a song.",
    "Lick the floor.",
    "Perform a striptease for the group.",
    "Do a handstand for a minute.",
    "Do a cartwheel in public.",
    "Text your ex and tell them you still have feelings for them.",
    "Run around the room with your underwear on your head.",
    "Wear your clothes inside out for the rest of the day.",
    "Let someone else do your makeup.",
    "Let someone give you a wedgie.",
    "Eat a spoonful of cinnamon.",
    "Put an ice cube down your shirt and let it melt.",
    "Eat a piece of raw onion.",
    "Do a silly dance in public.",
    "Put on a blindfold and do five minutes of interpretive dance.",
    "Eat a spoonful of hot sauce.",
    "Have a conversation with a stranger while wearing a ridiculous hat.",
    "Jump into a pool fully clothed.",
    "Call your crush and ask them out on a date.",
    "Put peanut butter on your face and let your dog lick it off.",
    "Eat a spoonful of mayonnaise.",
    "Text your crush and tell them how you feel about them.",
    "Wear a ridiculous outfit to the grocery store.",
    "Take a shot of vinegar.",
    "Give someone a piggyback ride.",
    "Run around the block in your underwear.",
    "Eat a raw egg.",
    "Do a trust fall with someone you just met.",
    "Put on a pair of heels and walk around in them for an hour.",
    "Eat a spoonful of soy sauce.",
    "Make a prank call to a friend.",
    "Take a selfie with a stranger.",
    "Do a handstand against the wall for five minutes.",
    "Sing karaoke in public.",
    "Wear your clothes backwards for a day.",
    "Put a spoonful of sugar in your mouth and try to whistle.",
    "Do a headstand for a minute.",
    "Make a paper airplane and throw it at someone.",
    "Eat a spoonful of mustard.",
    "Have a staring contest with someone.",
    "Speak in a different accent for the rest of the day.",
    "Do a cartwheel down a hill.",
    "Walk up to a stranger and say “I love you”.",
    "Eat a spoonful of hot mustard.",
    "Tell a joke in a public place and see if anyone laughs.",
    "Wear a clown nose for an entire day.",
    "Walk backwards for an hour.",
    "Eat a spoonful of wasabi.",
    "Go up to someone and ask for a piggyback ride.",
    "Speak in a whisper for the rest of the day.",
    "Dance like nobody's watching in a public place.",
    "Take a shot of hot sauce.",
    "Make a silly face and take a selfie with a stranger.",
    "Run up a hill and back down.",
    "Put on a blindfold and have someone feed you something.",
    "Make a silly sound every time you speak for the rest of the day.",
    "Do a silly walk in public.",
    "Eat a spoonful of horseradish.",
    "Jump up and down for a minute.",
    "Walk on your hands for five minutes.",
    "Tell a stranger your deepest darkest secret.",
    "Wear a tutu to the grocery store.",
    "Take a shot of olive oil.",
    "Ask a stranger to take a picture with you.",
    "Wear a sombrero for the rest of the day",

]

# Function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Truth or Dare! Type /truth or /dare to play.")

# Function to handle the /truth command
def truth(update, context):
    question = random.choice(truths)
    context.bot.send_message(chat_id=update.effective_chat.id, text=question)

# Function to handle the /dare command
def dare(update, context):
    task = random.choice(dares)
    context.bot.send_message(chat_id=update.effective_chat.id, text=task)

# Function to handle invalid commands
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# Set up the bot
updater = Updater(token='Your Token',use_context=True)
dispatcher = updater.dispatcher

# Add command handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('truth', truth))
dispatcher.add_handler(CommandHandler('dare', dare))

# Add handler for unknown commands
dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# Start the bot
updater.start_polling()

