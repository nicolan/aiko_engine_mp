# configuration/cyoa_minizork.py
#
# Story file for the Choose Your Own Adventure (CYOA) interpreter
#
# Node types:
#
# text node (one or two exits)
# combat node (battle, with two exits)
# end node (zero exits)
# start (same as choice node)

# Node properties:
# type: one of "combat", "text", "end", "start" (start node must be called 'start')
# name: text 
# text: text (limit 32 characters)
# choices[{choicename,nodename},...]
#
# TODO:
# some sort of combat using sliders and tappers or something.
story = {
    "name": "Cat and Dragon",
	"start":{
		"type": "start", 
		"text":"Once upon a time, there was a cat.", 
		"choices":[("Next","beginning1"),]
	},
	"beginning1":{
		"type": "text", 
		"text":"The cat really wanted to fly.", 
		"choices":[("Steal wings?","stealwings"),("Magic portion?","potion")]
	},
	"stealwings":{
		"type": "text", 
		"text":"The cat saw a dragon. Hmmm!", 
		"choices":[("Next","stealwings1")]
	},
    "stealwings1":{
        "type":"text",
        "text":"I will steal their wings",
        "choices":[("Wait til dragon sleeps","dragonsleep"),("Trick dragon","dragontrick")]
    },
    "dragonsleep":{
        "type":"text",
        "text":"The cat crept to the sleeping dragon",
        "choices":[("Next","dragonsleep1")]
    },
    "dragonsleep1":{
        "type":"text",
        "text":"The cat clawed at the wings!",
        "choices":[("Next","dragonsleep2")]
    },
    "dragonsleep2":{
        "type":"text",
        "text":"The unhappy dragon roared fire",
        "choices":[("Uh oh","dragonsleep3")]
    },
    "dragonsleep3":{
        "type":"text",
        "text":"The cat fled, tail alight.",
        "choices":[("Ow! Meow!","endfail")]
    },
    "endfail":{
        "type":"end",
        "text":"The cat decided walking was just fine after all"
    },
    "dragontrick":{
        "type":"text",
        "text":"The cat sauntered up to the dragon",
        "choices":[("Say hello?","trickhello"),("Tell a joke","trickjoke")]
    },
    "trickhello":{
        "type":"text",
        "text":"G'day, friend dragon. How's it goin'?",
        "choices":[("Next","trickhello1")],
    },
    "trickhello1":{
        "type":"text",
        "text":"The grumpy dragon: What do you want?",
        "choices":[("Tell the truth","trickhellowing"),("Flatter them","trickhelloflatter")],
    },
    "trickhellowing":{
        "type":"text",
        "text":"Just your wings! Would you share?",
        "choices":[("Next","trickhellowing1")],
    },
    "trickhellowing1":{
        "type":"text",
        "text":"The dragon laughed, then nodded: Sure",
        "choices":[("Next","trickhellowing2")],
    },
    "trickhellowing2":{
        "type":"text",
        "text":"There was a shimmer, and the cat had wings!",
        "choices":[("Time to fly","trickhellowing3")],
    },
    "trickhellowing3":{
        "type":"text",
        "text":"The cat was flying and soaring",
        "choices":[("Try to land","trickhellowingcrash"),("Fly more!","trickhellowing3")]
    },
    "trickhellowingcrash":{
        "type":"text",
        "text":"The cat crashed, sliding into the dragon.",
        "choices":[("I meant that","dragonfriend")],
    },
    "dragonfriend":{
        "type":"text",
        "text":"The dragon laughed and took their wings back",
        "choices":[("Next","dragonfriend1")],
    },
    "dragonfriend1":{
        "type":"text",
        "text":"Little cat, ride on my back any time.",
        "choices":[("Flying time!","end")],
    },
    
    "trickhelloflatter":{
        "type":"text",
        "text":"Why dragon, your scales are so shiny.",
        "choices":[("Purr generously","trickhelloflatter1"),("Lick paw","trickhelloflatter1")],
    },
    "trickhelloflatter1":{
        "type":"text",
        "text":"The dragon rumbles: I know. You woke me up!",
        "choices":[("Slow blink","trickhello1")],
    },
    
    "trickjoke":{
        "type":"text",
        "text":"What do you call a dragon with no silver?",
        "choices":[("Tell punchline","trickjoke1")],
    },
    "trickjoke1":{
        "type":"text",
        "text":"A dron.",
        "choices":[("Laugh","trickjoke2")],
    },
    "trickjoke2":{
        "type":"text",
        "text":"The dragon stares at you, unamused.",
        "choices":[("Try again","trickjoke3"),("Flick tail anxiously", "trickhello1")],
    },
    "trickjoke3":{
        "type":"text",
        "text":"Why did the dragon stop fighting knights?",
        "choices":[("Tell punchline","trickjoke4"),("Wait and see","trickjokewait")],
    },
    "trickjoke4":{
        "type":"text",
        "text":"They were sick of canned food!",
        "choices":[("Laugh","dragonsleep2")],
    },
    "trickjokewait":{
        "type":"text",
        "text":"The dragon snickered, then chuckled, then laughed",
        "choices":[("Purr contentedly","dragonfriend1")],
    },
    "potion":{
        "type":"text",
        "text":"The cat thought a dragon might have a potion.",
        "choices":[("Sneak up to treasure hoard","potionhoard")],
    },
    "potionhoard":{
        "type":"text",
        "text":"The cat stalked up to the hoard. A potion bottle!",
        "choices":[("Grab and go","potionsteal"),("Ask first","potionask")],
    },
    "potionsteal":{
        "type":"text",
        "text":"When safely away, the cat drank the potion",
        "choices":[("But what does it do?","potionsteal1")],
    },
    "potionsteal1":{
        "type":"text",
        "text":"Shablam! The cat turned into a penguin.",
        "choices":[("Turn me back into a cat!","potionstealrevert"),("Stay as a penguin","potionstealtux")],
    },
    "potionstealrevert":{
        "type":"text",
        "text":"After a day, the potion wore off, phew!",
        "choices":[("Time for a nap","endfail")],
    },
    "potionstealtux":{
        "type":"end",
        "text":"Penguins rule! Look at the handsome tux.",
    },
    "potionask":{
        "type":"text",
        "text":"Excuse me, may I have this potion?",
        "choices":[("Next","potionask1")],
    },
    "potionask1":{
        "type":"text",
        "text":"The dragon lifted a lazy eyelid.",
        "choices":[("Smile hopefully","potionask2")],
    },
    "potionask2":{
        "type":"text",
        "text":"Take it, I have hundreds.",
        "choices":[("Yippee, grab and go","potionsteal")],
    },
	"end": {
		"type": "end", 
		"text":"The cat and dragon flew often."
	}
}
