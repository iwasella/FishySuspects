init python:
    gallery_mia = Gallery()
    gallery_mia.transition = fade

    # Page 1 (2 buttons: test_1 to test_2)
    gallery_mia.button("test_1")
    gallery_mia.image("A1")

    gallery_mia.button("test_2")
    gallery_mia.image("A2")

    # Page 2 (6 buttons: test_3 to test_8)
    gallery_mia.button("test_3")
    gallery_mia.image("B1")

    gallery_mia.button("test_4")
    gallery_mia.image("B2")

    gallery_mia.button("test_5")
    gallery_mia.image("B3")

    gallery_mia.button("test_6")
    gallery_mia.image("B4")

    gallery_mia.button("test_7")
    gallery_mia.image("B5")

    gallery_mia.button("test_8")
    gallery_mia.image("B6")

    # Page 3 (9 buttons: test_9 to test_17)
    gallery_mia.button("test_9")
    gallery_mia.image("C1")

    gallery_mia.button("test_10")
    gallery_mia.image("C2")

    gallery_mia.button("test_11")
    gallery_mia.image("C3")

    gallery_mia.button("test_12")
    gallery_mia.image("C4")

    gallery_mia.button("test_13")
    gallery_mia.image("C5")

    gallery_mia.button("test_14")
    gallery_mia.image("C6")

    gallery_mia.button("test_15")
    gallery_mia.image("C7")

    gallery_mia.button("test_16")
    gallery_mia.image("C8")

    gallery_mia.button("test_17")
    gallery_mia.image("C9")

screen gallery():
    tag menu
    default page = 1

    # Main gallery layout
    vbox:
        xalign 0.5
        yalign 0.4
        spacing 20

        # PAGE 1 (2 images -> grid 2 1)
        if page == 1:
            text "Game Art" xalign 0.5
            grid 2 1:
                spacing 15
                vbox:
                    add gallery_mia.make_button("test_1", unlocked="thumb_1")
                    text "Cover Art" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_2", unlocked="thumb_2")
                    text "Characters" xalign 0.5
                

        # PAGE 2 (6 images -> grid 3 2)
        elif page == 2:
            text "Character Art" xalign 0.5
            grid 3 2:
                spacing 15
                vbox:
                    add gallery_mia.make_button("test_3", unlocked="thumb_3")
                    text "Sherlobster" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_4", unlocked="thumb_4")
                    text "Comissioner" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_5", unlocked="thumb_5")
                    text "Pufferfish" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_6", unlocked="thumb_6")
                    text "Gobius" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_7", unlocked="thumb_7")
                    text "CCs" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_8", unlocked="thumb_8")
                    text "Jell" xalign 0.5

        # PAGE 3 (9 images -> grid 3 3)
        elif page == 3:
            text "Background Art" xalign 0.5
            grid 3 3:
                spacing 15
                vbox:
                    add gallery_mia.make_button("test_9", unlocked="thumb_9")
                    text "Sherlobster Office" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_10", unlocked="thumb_10")
                    text "Party Entrance" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_11", unlocked="thumb_11")
                    text "Ballroom" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_12", unlocked="thumb_12")
                    text "Orchestra" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_13", unlocked="thumb_13")
                    text "Appetizers" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_14", unlocked="thumb_14")
                    text "Hallway" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_15", unlocked="thumb_15")
                    text "Guest Room" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_16", unlocked="thumb_16")
                    text "Gobius Office" xalign 0.5
                vbox:
                    add gallery_mia.make_button("test_17", unlocked="thumb_17")
                    text "Dead as Hell" xalign 0.5

        else:
            text "Sorry, this page does not exist." xalign 0.5


    # Return button
    textbutton _("Return") action Return():
        align (0.0, 1.0)
        text_size 40
        left_margin 25
        bottom_margin 25

# Page navigation bar
    vbox:
            xalign 0.03
            yalign 0.1
            spacing 10
            textbutton "Page 1" action SetScreenVariable("page", 1)
            textbutton "Page 2" action SetScreenVariable("page", 2)
            textbutton "Page 3" action SetScreenVariable("page", 3)