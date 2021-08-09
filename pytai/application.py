from . import view as v
from . import model as m

class Application():
    def __init__(self, *args, **kwargs):

        # These callbacks are used to notify the application
        #  of events from the view
        callbacks = {
            v.Events.REFRESH:             self.cb_refresh,
        }

        self.view = v.View(title = "PyTai", callbacks = callbacks)
        self.model = m.Model()


    def run(self) -> None:
        """Run the application."""
        self.view.mainloop()

    def cb_refresh(self) -> None:
        """Callback for an event where the user refreshes the view."""
        # TODO
        self.view.set_status("Refreshing...")