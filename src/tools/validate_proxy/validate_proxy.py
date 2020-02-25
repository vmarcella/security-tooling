"""
Validate what information the proxy server is sending to other servers over http.

This tool is only meant for local use.
"""
import argparse
import http.server
import socketserver


def __parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", metavar="p", type=int, default=3333)
    return parser.parse_args()


def __main() -> None:
    args = __parse_args()

    Http_handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", args.port), Http_handler) as httpd:
        print(f"Validating IPs on {args.port}")
        httpd.serve_forever()


if __name__ == "__main__":
    __main()
