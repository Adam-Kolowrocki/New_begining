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
import webbrowser
import urllib.error


def main():
    exceptions(get_url())


def get_url():
    user_url = input(f'Type URL of the page You want to open ->  ')
    return user_url


def exceptions(url):
    starts = ("https://", "http://", "www")
    if url[0:8] != starts[0] and url[0:7] != starts[1] and url[0:3] != starts[2]:
        raise urllib.error.URLError("The URL should start with ...")
    ends = (".pl", ".com")
    if url[-4:] != ends[1] and url[-3:] != ends[0]:
        raise urllib.error.URLError('The url should end with ".pl" or ".com"')
    webbrowser.open(url)


if __name__ == "__main__":
    main()
