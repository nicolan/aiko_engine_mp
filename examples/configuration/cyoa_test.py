# configuration/cyoa_test.py
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
# type: one of "combat", "text", "end", "start"
# name: text
# text: text
# choices[{choicename,nodename},...]
#
# TODO:
# some sort of combat using sliders and tappers or something.
story = {
    "name": "CYOA Test",
	"start":{
		"type": "start", 
		"text":"In the beginning...", 
		"choices":[("was there cheese?","eatcheese"),("was there pie?","eatpie")]
	},
	"eatcheese":{
		"type": "text", 
		"text":"Cheese is so good", 
		"choices":[("eat all the cheese?","end")]
	},
	"eatpie":{
		"type": "text", 
		"text":"Pie is delicious", 
		"choices":[("eat all the pie?","end")]
	},
	"end": {
		"type": "end", 
		"text":"Nomnom nom. You are full."
	}
}
