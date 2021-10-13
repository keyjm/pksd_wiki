class WikiPageLocators:
    # locators and other constants
    CONTENT_LINKS_LOC = "//*[@id='toc']/ul/li/a"
    CONTENT_HEADINGS_LOC = "//*[@id='toc']/ul/li/a/span[2]"
    PAGE_HEADINGS_LOC = "//*[@class='mw-parser-output']/h2"
    PERSONIFIED_CONCEPT_NIKE_LOC = "//*[@id='mw-content-text']/div[1]/table[3]/tbody/tr[6]/td/div/ul/li[13]/a"
    NIKE_POP_UP_LOC = "//*[@class='mwe-popups-extract']/p"
    NIKE_LINK_LOC = "//*[@class='div-col']/ul/li/a[@title='Nike (mythology)']"
    NIKE_FAMILY_TREE_IMG = "//*[@id='mw-content-text']/div[1]/table[4]/tbody"
    NIKE_POPUP_MSG = "In ancient Greek religion, Nike was a goddess who personified victory. " \
                     "Her Roman equivalent was Victoria."