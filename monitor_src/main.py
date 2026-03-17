import sys
from web_render import app


def main():
    print(f"args: {sys.argv}")
    app.run(debug=True, port=5000)

main()
