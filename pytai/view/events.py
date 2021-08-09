
import enum

class Events(enum.Enum):
        
    # User refreshes the view
    REFRESH            = enum.auto()
    
    # Application needs to set the status bar
    SET_STATUS         = enum.auto()
    
    # Application needs to display error
    SHOW_ERROR         = enum.auto()
    
