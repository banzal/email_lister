# email_lister
A Python script to make Email Lists from Raw Text/XLSX Files

Facing a prodblem of extracting several emails from a text file, I decided to create this simple Python based email list maker. The working priciple is based on Regex and Pattern Matching. The files are read, word by word (for txt_read.py) or cell by cell (for reader.py), patterrn matched with a regex designed to match emails, which then are added to a set to avoid duplicates. This is done for all words/cells in  the given file, after which they are converted to a data frame, added in lexicographic order. Once the data frame is made, they are conveniently converted to a CSV file, which then can be exported into any e-mail management program for bulk emailing.
