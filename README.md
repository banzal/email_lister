# @.CSV (email lister)
## A Python script to make Email Lists from Raw Text/XLSX Files

![logo](https://github.com/lasnab/email_lister/blob/master/logo.png?raw=true)

@csv is a Python Script I whipped up when I had a bunch of emails spread over a text document, with no specific delimitting values or patterns I could use to parse the input and seperate the emails from it.Having recently worked with Regular Expressions, I thought this would be a good opportunity for me to get more comfortable using them and apply them to a real-life application project.The working priciple is based on Regex and Pattern Matching. The files are read, word by word (for txt_read.py) or cell by cell (for reader.py), patterrn matched with a regex designed to match emails, which then are added to a set to avoid duplicates. This is done for all words/cells in  the given file, after which they are converted to a data frame, added in lexicographic order. Once the data frame is made, they are conveniently converted to a CSV file, which then can be exported into any e-mail management program for bulk emailing.
