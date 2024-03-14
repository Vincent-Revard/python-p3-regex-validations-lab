import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r""
name_regex = re.compile(r"[A-Z]{1}[a-z]*[\s\'][A-Z]{1}[a-z]+(-[A-Z]{1}[a-z]+)*")
# Allow spaces, single quotes, and hyphens


phone_number = r""
phone_regex = re.compile(r"^(\(\d{3}\)\s?|\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}$")


email_address = r""
email_regex = re.compile(r"^[A-z._%+-][A-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
