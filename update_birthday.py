import pathlib
import re
from datetime import date

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


if __name__ == '__main__':
    # Get Age
    age = date.today().year - 2005;

    readme_path = root / 'README.md'
    readme = readme_path.open().read()
    
    # Update Age
    rewritten_count = replace_writing(readme, 'age', age, inline=True)
    readme_path.open('w').write(rewritten_count)