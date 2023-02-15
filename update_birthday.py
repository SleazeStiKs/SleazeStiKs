import pathlib
import re
from datetime import datetime, date
import dateutil

root = pathlib.Path(__file__).parent.resolve()


def replace_writing(content, marker, chunk, inline=False):
    r = re.compile(
        r'<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->'.format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = '\n{}\n'.format(chunk)
    chunk = '<!-- {} starts -->{}<!-- {} ends -->'.format(marker, chunk, marker)
    return r.sub(chunk, content)

def birthday():
    # Get the current date
    now = datetime.datetime.utcnow()
    now = now.date()

    # Get the difference between the current date and the birthday
    age = dateutil.relativedelta.relativedelta(now, date(2005, 4, 3))
    age = age.years

    return age

if __name__ == '__main__':
    readme_path = root / 'README.md'
    readme = readme_path.open().read()
    
    # Update Age
    rewritten_count = replace_writing(readme, 'age', birthday(), inline=True)
    readme_path.open('w').write(rewritten_count)