# goit_homework_8

function `get_birthdays_per_week` from `remind_birthdays.py` 
prints reminding notification with names of given
users whose birthdays are in the following week

For example:
  *     Friday: Ryan
        Monday: Andrew, Anna
        Wednesday: William

Users whose birthdays was on Saturday and Sunday are printed on Monday


`users` is a list of dicts. Each dict represents user and has keys 
`'name'` and `'birthday'`
                
birthday may be given as `datetime` or `date` or `str` object
    
For making date from str it uses `SUPPORTED_STRING_DATE_FORMATS`
