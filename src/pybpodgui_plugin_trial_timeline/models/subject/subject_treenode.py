import logging

logger = logging.getLogger(__name__)

class SubjectTreeNode(object):

    def create_sessiontreenode(self, session):
        node = super(SubjectTreeNode, self).create_sessiontreenode(session)

        self.trialtimeline_action = self.tree.add_popup_menu_option(
            'Trial Timeline', 
            session.open_trialtimeline_window,
            item=node
            )

        self.trialtimeline_detached_action = self.tree.add_popup_menu_option(
            'Trial Timeline (Detached)', 
            session.open_trialtimeline_window_detached,
            item=node
            )

        return node