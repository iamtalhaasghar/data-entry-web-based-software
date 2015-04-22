#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__, template_folder='view')

import crudapp.controller.control
