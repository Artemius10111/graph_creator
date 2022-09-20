
class GraphButton(Qt.QPushButton):

    def __init__(self, button_text: str, parent=None, able_to_move: bool = False, *args, **kwargs):
        super().__init__(button_text, able_to_move, parent, *args, **kwargs)

    def mousePressEvent(self, event):
        button = event.button()
        if button == Qt.Qt.RightButton:
            print("Right button click!")
            self.setStyleSheet("""QPushButton{
                    background-color: #aaaaff;
                    border: 1px solid black;
                    border-radius: 5px;
                }
                """)
        elif button == Qt.Qt.LeftButton:
            print("Left button click!")
            self.setStyleSheet("""QPushButton{
                    background-color: #ffaaaa;
                    border: 1px solid black;
                    border-radius: 10px;
                }
                """)
        
        if event.buttons() == QtCore.Qt.MidButton:
            mimeData = QtCore.QMimeData()
            drag = QtGui.QDrag(self)
            drag.setMimeData(mimeData)
            drag.exec_(QtCore.Qt.MoveAction)

        return Qt.QPushButton.mousePressEvent(self, event)
