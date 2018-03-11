from flask_script import Command
import IPython
import pandas as pd
import os
from app import db

class REPL(Command):
    "runs the shell"

    def run(self):
        IPython.embed()

