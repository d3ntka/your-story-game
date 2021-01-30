image gal1 = im.FactorScale("images/cg/raven_window_clear.jpg", 0.25)
image gal2 = im.FactorScale("images/cg/cg tavern wall.jpg", 0.25)

#image beach_button = im.FactorScale("bg/sort_of_beautiful_beach_day.jpg", 0.25)
image glock_button = "placeholder/klodka.jpg"
init python:

    # Step 1. Create the gallery object.
    g_bg = Gallery()

    # Step 2. Add buttons and images to the gallery.

    # A button with an image that is always unlocked.
    g_bg.button("button1")
    g_bg.image("raven_window_clear")

    g_bg.button("button2")
    g_bg.image("anim_cg_tavern_wall")
    #g_bg.unlock("anim_cg_tavern_wall")
    # A button that contains an image that automatically unlocks.
    #g.button("dawn")
    #g.image("dawn1")
    #g.unlock("dawn1")

    # This button has multiple images assocated with it. We use unlock_image
    # so we don't have to call both .image and .unlock. We also apply a
    # transform to the first image.
    g_bg.button("dark")
    g_bg.unlock_image("tavern_door_lia_eyesclosed")
    #g_bg.transform(dissolve)
    g_bg.unlock_image("tavern_door_lia_eyesopened")
    #g.unlock_image("beach2")
    #g.unlock_image("beach3")

    # This button has a condition associated with it, allowing the game
    # to choose which images unlock.
    #g.button("end1")
    #g.condition("persistent.unlock_1")
    #g.image("transfer")
    #g.image("moonpic")
    #g.image("girlpic")
    #g.image("nogirlpic")
    #g.image("bad_ending")

    #g.button("end2")
    #g.condition("persistent.unlock_2")
    #g.image("library")
    #g.image("beach1 nomoon")
    #g.image("bad_ending")

    # The last image in this button has an condition associated with it,
    # so it will only unlock if the user gets both endings.
    #g.button("end3")
    #g.condition("persistent.unlock_3")
    #g.image("littlemary2")
    #g.image("littlemary")
    #g.image("good_ending")
    #g.condition("persistent.unlock_3 and persistent.unlock_4")

    #g.button("end4")
    #g.condition("persistent.unlock_4")
    #g.image("hospital1")
    #g.image("hospital2")
    #g.image("hospital3")
    #g.image("heaven")
    #g.image("white")
    #g.image("good_ending")
    #g.condition("persistent.unlock_3 and persistent.unlock_4")

    # The final two buttons contain images that show multiple pictures
    # at the same time. This can be used to compose character art onto
    # a background.
    #g.button("dawn mary")
    #g.unlock_image("dawn1", "mary dawn wistful")
    #g.unlock_image("dawn1", "mary dawn smiling")
    #g.unlock_image("dawn1", "mary dawn vhappy")

    #g.button("dark mary")
    #g.unlock_image("beach2", "mary dark wistful")
    #g.unlock_image("beach2", "mary dark smiling")
    #g.unlock_image("beach2", "mary dark vhappy")

    g_bg.locked_button = "glock_button"

    # The transition used when switching images.
    g_bg.transition = dissolve


################################################################################
# The gallery screen we use.
################################################################################
screen gallery():

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "cg tavern wall"

    # A grid of buttons.
    grid 1 3:

        xfill True
        yfill True

        # Call make_button to show a particular button.
        add g_bg.make_button("button1", "gal1", xalign=0.5, yalign=0.5)
        add g_bg.make_button("button2", "gal2", xalign=0.5, yalign=0.5)
        add g_bg.make_button("dark", "gal2", xalign=0.5, yalign=0.5)



        #add g.make_button("dawn", "gal-dawn.png", xalign=0.5, yalign=0.5)
        #add g.make_button("end1", "gal-end1.png", xalign=0.5, yalign=0.5)

        #add g.make_button("end2", "gal-end2.png", xalign=0.5, yalign=0.5)
        #add g.make_button("end3", "gal-end3.png", xalign=0.5, yalign=0.5)
        #add g.make_button("end4", "gal-end4.png", xalign=0.5, yalign=0.5)

        #add g.make_button("dark mary", "gal-dark_mary.png", xalign=0.5, yalign=0.5)
        #add g.make_button("dawn mary", "gal-dawn_mary.png", xalign=0.5, yalign=0.5)
        #add g.make_button("title", "title.png", xalign=0.5, yalign=0.5)


        # The screen is responsible for returning to the main menu. It could also
        # navigate to other gallery screens.
    textbutton "Return" action Return() xalign 0.1 yalign 0.9
