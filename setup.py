import py2app

executables = [py2app.Executable("MRMIKE.py")]

py2app.setup(
    name="MR.MIKE",
    options={"build_app": {"packages":["pygame"],
                           "include_files":["icon1.png","Raleway-Medium.ttf"]}},
    executables = executables
    )

