#!/usr/bin/python
# -*- coding: utf-8 -*-

from todo_project.settings import SECRET_KEY

JWT_SECRET = SECRET_KEY
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 157784760

# Should not be the same as access token. This is an example!
REFRESH_JWT_SECRET = SECRET_KEY
REFRESH_JWT_EXP_DELTA_SECONDS = 1577847600

# Should not be the same as access token. This is an example!
VERIFICATION_JWT_SECRET = SECRET_KEY
VERIFICATION_JWT_EXP_DELTA_SECONDS = 300

HOST_ADDR = ""
