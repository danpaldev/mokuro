from mokuro import __main__
import sys
import os
parent_mokuro_folder = os.path.abspath(os.getcwd())
sys.path.insert(0, parent_mokuro_folder)

comic_text_detector_folder = os.path.join(
    parent_mokuro_folder, "comic_text_detector")
sys.path.insert(0, comic_text_detector_folder)


# Now you can import the __main__ script and call its main function

if __name__ == "__main__":
    # Keep sys.argv[0] as "__main__.py" and add all other arguments passed to run_cli.py
    sys.argv[0] = "__main__.py"
    __main__.main()
