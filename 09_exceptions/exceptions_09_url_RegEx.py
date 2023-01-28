# Check the antigravity module code. Use similar way to open any URL given by user.
# Remember to check if URL is correct, it can start with:
#     https://
#     http://
#     www
#     bez www
# And may end with:
#     .pl
#     .com
# If given address is not a link, rise the URLError exception, which will inform that the URL is wrong.
# Rewrite it with regula expressions (RegEx).
import re
import urllib.error
import webbrowser


def main():
    exceptions(get_url())


def get_url():
    user_url = input(f'Type URL of the page You want to open ->  ')
    return user_url


def exceptions(url):
    beginnings = re.search("^https://", url) or re.search("^http://", url) or re.search("^www", url)
    if not beginnings:
        raise urllib.error.URLError("The URL should start with https://, http:// or www")
    else:
        pass
    ends = re.search(".pl$", url) or re.search(".com$", url)
    if not ends:
        raise urllib.error.URLError('The url should end with ".pl" or ".com"')
    else:
        webbrowser.open(url)


if __name__ == "__main__":
    main()
