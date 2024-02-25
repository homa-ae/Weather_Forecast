from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")

name = "Weather Forecast"
default_task = "publish"

@init
def initialize(project):
    project.set_property("dir_source_main_python", "src")  
    project.set_property("dir_source_unittest_python", "src/tests")  
    project.depends_on("requests")  
