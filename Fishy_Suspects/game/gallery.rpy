init python:
    # Step 1: Instantiate the Gallery object
    gallery_mia = Gallery()
    gallery_mia.transition = fade

    # Step 2: Define buttons and images
    gallery_mia.button("test_a")
    gallery_mia.unlock_image("A1")
    gallery_mia.unlock_image("A2")
    gallery_mia.unlock_image("A3")

    gallery_mia.button("test_b")
    gallery_mia.unlock_image("B1")
    gallery_mia.unlock_image("B2")

    gallery_mia.button("test_c")
    gallery_mia.unlock_image("C1")

    gallery_mia.button("test_d")
    gallery_mia.unlock_image("D1")

    gallery_mia.button("test_e")
    gallery_mia.unlock_image("E1")


screen gallery():
    tag menu
    default page = 1

    add "background"

    # Main gallery layout
    vbox:
        xalign 0.5
        yalign 0.4
        spacing 20

        if page == 1:
            text "You are on page 1" xalign 0.5
            grid 2 2:
                spacing 10
                vbox:
                    add gallery_mia.make_button(name="test_a", locked="thumb_lock", unlocked="thumb_a")
                    text gallery_mia.get_fraction(name="test_a", format='{seen}/{total}') xalign 0.5
                vbox:
                    add gallery_mia.make_button(name="test_b", locked="thumb_lock", unlocked="thumb_b")
                    text gallery_mia.get_fraction(name="test_b", format='{seen}/{total}') xalign 0.5
                vbox:
                    add gallery_mia.make_button(name="test_c", locked="thumb_lock", unlocked="thumb_c")
                    text gallery_mia.get_fraction(name="test_c", format='{seen}/{total}') xalign 0.5
                vbox:
                    add gallery_mia.make_button(name="test_d", locked="thumb_lock", unlocked="thumb_d")
                    text gallery_mia.get_fraction(name="test_d", format='{seen}/{total}') xalign 0.5

        elif page == 2:
            text "You are on page 2" xalign 0.5
            # Uses a grid or layout matching the item count
            vbox:
                xalign 0.5
                add gallery_mia.make_button(name="test_e", locked="thumb_lock", unlocked="thumb_e")
                text gallery_mia.get_fraction(name="test_e", format='{seen}/{total}') xalign 0.5

        elif page == 3:
            text "You are on page 3" xalign 0.5

        else:
            text "Sorry, this page does not exist." xalign 0.5

    # Page navigation bar
    frame:
        xalign 0.5
        yalign 0.85
        hbox:
            spacing 10
            textbutton "Page 1" action SetScreenVariable("page", 1)
            textbutton "Page 2" action SetScreenVariable("page", 2)
            textbutton "Page 3" action SetScreenVariable("page", 3)

    # Return button
    frame:
        xalign 0.5
        yalign 0.95
        xpadding 10
        ypadding 10
        textbutton "Return" action Return()