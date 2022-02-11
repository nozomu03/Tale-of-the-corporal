image bg_hallway_sepia = im.Sepia("bg_hallway.png")
image gwon_nem_sepia = im.Sepia("gwon_nem.png")
image main_atten_sepia = im.Sepia("main_atten.png")

image crack_glass2 = "crack_glass.png"
image crack_glass3 = "crack_glass.png"
transform bluring:
    blur 100.0
    linear 4.0 blur 8.0
