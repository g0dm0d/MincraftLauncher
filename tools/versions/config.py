class Config():
    def __init__(self, location, version, javapath, arguments, runner) -> None:
        self.location = location
        self.version = version
        self.javapath = javapath
        self.arguments = arguments
        self.runner = runner
