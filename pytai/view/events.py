
import enum

class Events(enum.Enum):
        
    # User refreshes the view
    REFRESH            = enum.auto()
    
    # Application needs to set the status bar
    SET_STATUS         = enum.auto()
    
    # Application needs to display error
    SHOW_ERROR         = enum.auto()

    # User selects item from structure tree
    STRUCTURE_SELECTED = enum.auto()

    # User wants to jump to offset
    GOTO               = enum.auto()
    
