"""
Validate what information the proxy server is sending to other servers over http.

This tool is only meant for local use.
"""
import argparse
import http.server
import os
import socketserver


# TODO have this class pass the directory of the script into the http handler as
# to deliver the correct static content.
class __CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def __parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", metavar="p", type=int, default=3333)
    return parser.parse_args()


def __main() -> None:
    args = __parse_args()

    with socketserver.TCPServer(("", args.port), __CustomRequestHandler) as httpd:
        print(f"Validating IPs on: {args.port}")
        httpd.serve_forever()


if __name__ == "__main__":
    __main()
