""" 
In a file called watch.py, implement a function called parse that expects a str of HTML as input, 
extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, 
and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below:
http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0

Assume that the value of src will be surrounded by double quotes. 
And assume that the input will contain no more than one such URL. 
If the input does not contain any such URL at all, return None.

Because some HTML attributes are optional, you could instead minimally embed just the below:
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages 
    (e.g., https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter, shareable youtu.be URLs 
        (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.

 """
import re
import sys

tiny_url = ""

def main():
    output = parse(input("HTML: "))
    print(f'{output}')


def parse(s):
    replacement_str = "https://youtu.be"
    if matches := re.search(r'src="(http|https)?://(?:www\.)?youtube\.com/embed/(.+)"', s, re.IGNORECASE): 
        extract = matches.group(2)
        if extract_id := re.search(r'^(.+) (.+)$', extract):
            # print(extract_id.group(1).split(" "))
            tmp = extract_id.group(1).split(" ")
            id = tmp[0].strip('"')
            tiny_url = replacement_str + '/' + id 
            
        else:
            tiny_url = replacement_str + '/' + extract
            # print(extract)

        return tiny_url
    else:
        return "None"

if __name__ == "__main__":
    main()
