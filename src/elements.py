#!/usr/bin/python3

#URLs
web = "http://www.informatics.jax.org/vocab/gene_ontology/"

# Locators by Class
moleFuncClass = ".jstree-anchor"
firstUserChoiceClass = "enter-form__choose-user"
settingsBtnClass = "user-menu__settings"

# Locators by CSS selector
goTermDetailTable = "#termPaneDetails"
listExpandableCss = "aria-expanded"
categoryCss = "#treeViewDiv ul li a"
categorySubItemsCss = '#treeViewDiv ul li [aria-expanded="false"] a'
checkIfExpandableCss = '[aria-expanded="false"]'
expandSubItemButtonCss = "i"
collectAllSubItemsCss = ".jstree-default a"
searchBarInputCss = "[name='term']"
searchResultsDivsCss = "[id='searchResults'] div"
searchResultLinkCss = "a"