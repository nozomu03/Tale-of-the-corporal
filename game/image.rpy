image bg_hallway_sepia = im.Sepia("bg_hallway.png")
image gwon_nem_sepia = im.Sepia("gwon_nem.png")
image main_atten_sepia = im.Sepia("main_atten.png")
image bg_hospital_sepia = im.Sepia("bg_hospital.png")
image main_young_sepia = im.Sepia("main_young.png")

image crack_glass2 = "crack_glass.png"
image crack_glass3 = "crack_glass.png"
image blood2 = "blood.png"
image blood3 = "blood.png"
image blood4 = "blood.png"
image blood5 = "blood.png"
image blood6 = "blood.png"
image blood7 = "blood.png"
image blood8 = "blood.png"
image blood9 = "blood.png"
image blood10 = "blood.png"

transform bluring:
    blur 100.0
    linear 4.0 blur 8.0

transform run_trans:
    align(.5, .8)
    zoom 1.5
    linear .1 align(.5, .5)
    linear .1 align(.5, .8)
    repeat 10

