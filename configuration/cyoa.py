# configuration/cyoa.py

settings = {
  "story": "catdragon" # Name of the storyfile to use. Expects it to be cyoa_<story>.py
}

def parameter(name, settings=settings):
  if name in settings: return settings[name]
  return False
