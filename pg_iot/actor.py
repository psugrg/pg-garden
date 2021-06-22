
class Feed:
    """Contains the feed information"""

    def __init__(self, name, topic, queue=None):
        self.name = name
        self.topic = topic
        self.queue = queue


class Actor:
    """An action to be performed """

    def __init__(self, mqtt={}):
        # Submitions
        self.pubs = []
        try:
            for action in mqtt["publish"]:
                self.pubs.append(
                    Feed(action, mqtt["publish"][action]["topic"]))
        except KeyError:
            # Nothing found in "publish" section
            pass

        try:
            for action in mqtt["subscribe&publish"]:
                self.pubs.append(
                    Feed(action, mqtt["subscribe&publish"][action]["topic"]))
        except KeyError:
            # Nothing found in "subscribe&publish" section
            pass

        # Subscriptions
        self.subs = []
        try:
            for action in mqtt["subscribe"]:
                self.subs.append(
                    Feed(action, mqtt["subscribe"][action]["topic"]))
        except KeyError:
            # Nothing found in "subscribe" section
            pass

        try:
            for action in mqtt["subscribe&publish"]:
                self.subs.append(
                    Feed(action, mqtt["subscribe&publish"][action]["topic"]))
        except KeyError:
            # Nothing found in "subscribe&publish" section
            pass

    def run(self, event):
        """Run the Action function interface"""
        raise Exception("Interface implementation missing!")

    def get_sub(self, name) -> Feed:
        """Get subscriptions feed of a given name"""
        for feed in self.subs:
            if feed.name == name:
                return feed
        return None

    def get_pub(self, name) -> Feed:
        """Get publications feed of a give name"""
        for feed in self.pubs:
            if feed.name == name:
                return feed
        return None

    def get_message(self, name):
        """"Get pending message from queue of a given name. Returns None if empty"""
        if not self.get_sub(name).queue.empty():
            return self.get_sub(name).queue.get(False)
        else:
            return None

    def put_message(self, name, message):
        """Put message on the queue of a given name"""
        self.get_pub(name).queue.put(message)
