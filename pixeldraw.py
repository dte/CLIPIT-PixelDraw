#Setup Paths
import sys
sys.path.append("/inputs/CLIPIT")

#Run the script

prompts = "Colorful cosmic cloud swirl. #pixelart" #@param {type:"string"}
aspect = "widescreen" #@param ["widescreen", "square"]
use_pixeldraw = True #@param {type:"boolean"}

## Simple setup
from clipit import clipit

## these are good settings for pixeldraw
clipit.reset_settings()
clipit.add_settings(prompts=prompts, aspect=aspect)
clipit.add_settings(quality="better", scale=2.5)
clipit.add_settings(use_pixeldraw=use_pixeldraw)


### YOU CAN ADD YOUR OWN CUSTOM SETTING HERE ####
# this is the example of how to run longer with less frequent display
# clipit.add_settings(iterations=500, display_every=50)
clipit.add_settings(outputs='/outputs/generatedFaces')


settings = clipit.apply_settings()
clipit.do_init(settings)
clipit.do_run(settings)

#   --result-dir=