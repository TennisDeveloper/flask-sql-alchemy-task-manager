
#We need to import os once again, in order to utilize environment variables within this file.
# We also need to import the 'app' variable that we've created within our taskmanager
# package, defined in the init file.import os
import os
from taskmanager import app

#The last step to run our application is to tell our app how and where to run the application.
# This is the same process we've seen before, checking that the 'name' class is equal to
# the default 'main' string, wrapped in double underscores.
# If it's a match, then we need to have our app running, which will take three arguments:
# 'host', 'port', and 'debug'.

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
