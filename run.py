from Youtube.TestCase import TestCase

with TestCase() as TC:
    TC.home_page()
    TC.scroll_down()
    TC.play_quick_pick_non_login()
    TC.sign_in()
    TC.play_quick_pick_login()
    TC.search_specific_song()









