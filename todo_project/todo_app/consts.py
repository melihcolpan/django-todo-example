#!/usr/bin/python
# -*- coding: utf-8 -*-

from todo_project.settings import SECRET_KEY

JWT_SECRET = SECRET_KEY
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 157784760
