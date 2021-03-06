Description
-----------

This tool is designed to visualize plant organization based on data from
[Prairie Moon Nursery](https://www.prairiemoon.com/) (PMN).

For each plant, PMN lists other plants that will pair well with it under
the category "Pair with..." at the bottom of the product listing.
For each plant specified, a node (circle) is created. If a plant is 
considered a good pairing according to PMN, an edge (line) is drawn between
the nodes for each plant.

Use
---

Current operation requires a CSV file (can be created in Excel or Google Sheets),
that contains the pairing information.

To run:

`plot_network.py plant-pairing-data.csv`

Output:
-------

A file called `plant_network.html` will be generated and automatically opened
in your web browser where you can visualize the information.

Contribute:
-----------

Do you have an idea for making this tool better? If you are on Github
contribute by either making an issue or forking and making a pull request.
Not a software developer but still have an idea? No problem! Send me an email
(click on my bio) with your idea and I will do my best to incorporate it.

Disclaimer:
-----------

This is a hobby project for me and I will develop it as I have time to do so.
Contributions always welcome. I am not getting paid by anyone, including PMN,
to develop this tool.