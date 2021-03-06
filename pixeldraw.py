#Setup Paths
import sys
sys.path.append("clipit")
sys.path.append("/clipit")
sys.path.append("CLIP")
sys.path.append("/CLIP")
sys.path.append("diffvg")
sys.path.append("/diffvg")
sys.path.append("taming-transformers")
sys.path.append("/taming-transformers")


#Run the script

prompts = "Fantom is a global, decentralized network with validators and community members from all around the world. #pixelart" #@param {type:"string"}
# prompts = "Kitchen renovations made simple." #@param {type:"string"}
# prompts = "A web app that makes kitchen renovations simple." #@param {type:"string"}

aspect = "widescreen" #@param ["widescreen", "square"]
use_pixeldraw = True #@param {type:"boolean"}

## Simple setup
import clipit

## these are good settings for pixeldraw
clipit.reset_settings()
clipit.add_settings(prompts=prompts, aspect=aspect)
clipit.add_settings(quality="better", scale=2.5)
clipit.add_settings(use_pixeldraw=use_pixeldraw)


### YOU CAN ADD YOUR OWN CUSTOM SETTING HERE ####
# this is the example of how to run longer with less frequent display
# clipit.add_settings(iterations=500, display_every=50)
# clipit.add_settings(outputs='/outputs/pixels')


settings = clipit.apply_settings()
clipit.do_init(settings)
clipit.do_run(settings)

#   --result-dir=
