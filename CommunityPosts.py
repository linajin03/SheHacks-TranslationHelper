import uuid


class Post:
    """A post made on the Speak-Easy community page.

    === Attributes ===
    name: the name of the Speak-Easy community poster.
    post_id: randomly generated id of the post
    caption: the caption of the Speak-Easy post.
    thread: the replies of the post.
    """
    _name: str
    post_id: uuid
    caption: str
    thread: list

    def __init__(self, name: str, caption: str) -> None:
        """Initialize the instance attributes of Post.

        Preconditions:
            len(caption) < 280
        """
        self._name = name
        self.caption = caption
        self.post_id = uuid.uuid1()
        self.thread = []


class Reply:
    """A Reply made on the Speak-Easy community page.

    === Attributes ===
    name: the name of the Speak-Easy community replier.
    post_id: randomly generated id of the Reply.
    caption: the caption of the Speak-Easy Reply.
    """
    name: str
    post_id: uuid
    caption: str

    # NOTE: replies cannot be replied to.
    def __init__(self, name: str, caption: str) -> None:
        self.name = name
        self.caption = caption
        self.post_id = uuid.uuid1()


# Front End: class PostManager is only initialized one time when the app is
# started up. It is very important you create just ONE PostManager object
class PostManager:
    """A manager responsible for keeping track of all the posts and replies in
    the Speak-Easy community.
    === Attributes ===
    post_datadict: the dictionary database of all posts
    """
    post_datadict: dict

    def __init__(self):
        self.post_datadict = {}

    # Everytime the user submits a post, call the PostManager object's
    # add_post functionality
    def add_post(self, post_id: uuid, name: str, caption: str) -> None:
        """Adds a post to the Speak-Easy community database.
        """
        obj = Post(name, caption)
        self.post_datadict[post_id] = obj

    def add_reply(self, main_post_id: uuid, reply: Reply) -> None:
        """Adds a reply to the thread of the original post.
        """
        self.post_datadict[main_post_id].thread.append(reply)

# # Sample code from main
# def main():
#     database = PostManager()
#     # now I have database.post_datadict -> {}
#
#     # but everytime the user submits something we have
#     # the post_id, post_thread, dict, etc.
#     # we just add to the database object
#
#     # we can access it using
#     for entry in database.post_datadict:
#         # do some operation
#
#         # we can view each post's text like this
#         print(entry.caption)
#
#         # we can see each reply with
#         print(entry.thread)
