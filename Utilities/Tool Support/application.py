# Enter application-specific Python functions here.
# Prefix functions with @expose to be able to use them in derived calculations.

from tailoring2.extensions import *

@toplevel_sources
def tlses(treq):
    return ["", "Source1"]
    #return ["", "Source1", "Common1"]
    #return ["", "Roster", "Course_Setup", "Student_Survey", "Gradebook", "SLC"]


