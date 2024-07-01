# coding: utf-8
# ------------------------------
_version_ = "0.3.0"
_author_ = "Kei Ueda"
# ------------------------------
import os
import subprocess
try:
    from importlib import reload
except:
    pass
# ------------------------------
import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omUI
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2.QtCore import *
from PySide2.QtGui import *
import PySide2.QtWidgets as QtWidgets
try:
    import shiboken2
except:
    pass
# ------------------------------

TOOLNAME = 'Camera Exporter'

# ------------------------------

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(348, 572)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy1)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.camera_refresh_button = QPushButton(self.centralwidget)
        self.camera_refresh_button.setObjectName(u"camera_refresh_button")

        self.horizontalLayout_4.addWidget(self.camera_refresh_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.camera_list = QListWidget(self.centralwidget)
        self.camera_list.setObjectName(u"camera_list")
        self.camera_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.camera_list.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.camera_list)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.sub_5_button = QPushButton(self.centralwidget)
        self.sub_5_button.setObjectName(u"sub_5_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sub_5_button.sizePolicy().hasHeightForWidth())
        self.sub_5_button.setSizePolicy(sizePolicy2)
        self.sub_5_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_7.addWidget(self.sub_5_button)

        self.sub_1_button = QPushButton(self.centralwidget)
        self.sub_1_button.setObjectName(u"sub_1_button")
        sizePolicy2.setHeightForWidth(self.sub_1_button.sizePolicy().hasHeightForWidth())
        self.sub_1_button.setSizePolicy(sizePolicy2)
        self.sub_1_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_7.addWidget(self.sub_1_button)

        self.frame_handle_line = QLineEdit(self.centralwidget)
        self.frame_handle_line.setObjectName(u"frame_handle_line")
        sizePolicy1.setHeightForWidth(self.frame_handle_line.sizePolicy().hasHeightForWidth())
        self.frame_handle_line.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.frame_handle_line)

        self.add_1_button = QPushButton(self.centralwidget)
        self.add_1_button.setObjectName(u"add_1_button")
        sizePolicy2.setHeightForWidth(self.add_1_button.sizePolicy().hasHeightForWidth())
        self.add_1_button.setSizePolicy(sizePolicy2)
        self.add_1_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_7.addWidget(self.add_1_button)

        self.add_5_button = QPushButton(self.centralwidget)
        self.add_5_button.setObjectName(u"add_5_button")
        sizePolicy2.setHeightForWidth(self.add_5_button.sizePolicy().hasHeightForWidth())
        self.add_5_button.setSizePolicy(sizePolicy2)
        self.add_5_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_7.addWidget(self.add_5_button)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.all_exp_type_radio = QRadioButton(self.centralwidget)
        self.ext_group = QButtonGroup(MainWindow)
        self.ext_group.setObjectName(u"ext_group")
        self.ext_group.addButton(self.all_exp_type_radio)
        self.all_exp_type_radio.setObjectName(u"all_exp_type_radio")
        self.all_exp_type_radio.setChecked(True)

        self.horizontalLayout_2.addWidget(self.all_exp_type_radio)

        self.ma_exp_type_radio = QRadioButton(self.centralwidget)
        self.ext_group.addButton(self.ma_exp_type_radio)
        self.ma_exp_type_radio.setObjectName(u"ma_exp_type_radio")
        self.ma_exp_type_radio.setCheckable(True)
        self.ma_exp_type_radio.setChecked(False)

        self.horizontalLayout_2.addWidget(self.ma_exp_type_radio)

        self.abc_exp_type_radio = QRadioButton(self.centralwidget)
        self.ext_group.addButton(self.abc_exp_type_radio)
        self.abc_exp_type_radio.setObjectName(u"abc_exp_type_radio")

        self.horizontalLayout_2.addWidget(self.abc_exp_type_radio)

        self.fbx_exp_type_radio = QRadioButton(self.centralwidget)
        self.ext_group.addButton(self.fbx_exp_type_radio)
        self.fbx_exp_type_radio.setObjectName(u"fbx_exp_type_radio")

        self.horizontalLayout_2.addWidget(self.fbx_exp_type_radio)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.current_line = QLineEdit(self.centralwidget)
        self.current_line.setObjectName(u"current_line")
        font = QFont()
        font.setPointSize(7)
        self.current_line.setFont(font)

        self.horizontalLayout_8.addWidget(self.current_line)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.export_line = QLineEdit(self.centralwidget)
        self.export_line.setObjectName(u"export_line")
        self.export_line.setFont(font)

        self.horizontalLayout_5.addWidget(self.export_line)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.use_scene_name_check = QCheckBox(self.centralwidget)
        self.use_scene_name_check.setObjectName(u"use_scene_name_check")

        self.verticalLayout.addWidget(self.use_scene_name_check)

        self.remain_cam_check = QCheckBox(self.centralwidget)
        self.remain_cam_check.setObjectName(u"remain_cam_check")
        self.remain_cam_check.setChecked(True)

        self.verticalLayout.addWidget(self.remain_cam_check)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 10, -1, -1)
        self.bake_button = QPushButton(self.centralwidget)
        self.bake_button.setObjectName(u"bake_button")

        self.horizontalLayout_11.addWidget(self.bake_button)

        self.export_button = QPushButton(self.centralwidget)
        self.export_button.setObjectName(u"export_button")

        self.horizontalLayout_11.addWidget(self.export_button)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.bake_and_export_button = QPushButton(self.centralwidget)
        self.bake_and_export_button.setObjectName(u"bake_and_export_button")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.bake_and_export_button.setFont(font1)

        self.verticalLayout.addWidget(self.bake_and_export_button)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.open_export_button = QPushButton(self.centralwidget)
        self.open_export_button.setObjectName(u"open_export_button")

        self.horizontalLayout_9.addWidget(self.open_export_button)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 348, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CameraList", None))
        self.camera_refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Frame Handle", None))
        self.sub_5_button.setText(QCoreApplication.translate("MainWindow", u"\u25bc5", None))
        self.sub_1_button.setText(QCoreApplication.translate("MainWindow", u"\u25bc1", None))
        self.frame_handle_line.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.add_1_button.setText(QCoreApplication.translate("MainWindow", u"\u25b31", None))
        self.add_5_button.setText(QCoreApplication.translate("MainWindow", u"\u25b35", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Export type", None))
        self.all_exp_type_radio.setText(QCoreApplication.translate("MainWindow", u"all", None))
        self.ma_exp_type_radio.setText(QCoreApplication.translate("MainWindow", u"ma", None))
        self.abc_exp_type_radio.setText(QCoreApplication.translate("MainWindow", u"abc", None))
        self.fbx_exp_type_radio.setText(QCoreApplication.translate("MainWindow", u"fbx", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Current Path", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Export Name", None))
        self.use_scene_name_check.setText(QCoreApplication.translate("MainWindow", u"use SceneName ", None))
        self.remain_cam_check.setText(QCoreApplication.translate("MainWindow", u"temp cam_group not delete", None))
        self.bake_button.setText(QCoreApplication.translate("MainWindow", u"Bake", None))
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.bake_and_export_button.setText(QCoreApplication.translate("MainWindow", u"Bake and Export", None))
        self.open_export_button.setText(QCoreApplication.translate("MainWindow", u"Open ExportDir", None))
    # retranslateUi



def undoable(func):
    def _undoable(*args):
        try:
            cmds.undoInfo(openChunk=True)
            return func(*args)
        finally:
            cmds.undoInfo(closeChunk=True)
    return _undoable

class GUI(MayaQWidgetBaseMixin, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.close_exists_window()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.set_window_pos()
        self.setWindowTitle('{} {}'.format(TOOLNAME, _version_))

        self.ui.export_button.clicked.connect(self.export_button_clicked)
        self.ui.bake_button.clicked.connect(self.bake_button_clicked)
        self.ui.bake_and_export_button.clicked.connect(self.bake_and_export_button_clicked)
        
        self.ui.camera_refresh_button.clicked.connect(self.set_camera_list)

        # plus minus button
        self.ui.add_1_button.clicked.connect(self.add_1_button_clicked)
        self.ui.add_5_button.clicked.connect(self.add_5_button_clicked)
        self.ui.sub_1_button.clicked.connect(self.sub_1_button_clicked)
        self.ui.sub_5_button.clicked.connect(self.sub_5_button_clicked)

        self.ui.ext_group.buttonClicked.connect(self.get_ext_type)

        self.ui.use_scene_name_check.stateChanged.connect(self.use_scene_name_check_state_changed)
        self.ui.open_export_button.clicked.connect(self.open_export_button_clicked)

        self.set_camera_list()
        self.update_ui()

    # ------------------------------
    def get_ext_type(self):
        self.ext_type = self.ui.ext_group.checkedButton().text().split('_exp')[0]
        return self.ext_type
    # ------------------------------

    # add 1
    def add_1_button_clicked(self):
        frame_handle_line = self.ui.frame_handle_line.text()
        frame_handle = float(frame_handle_line)
        self.ui.frame_handle_line.setText(str(frame_handle + 1))
    # add 5
    def add_5_button_clicked(self):
        frame_handle_line = self.ui.frame_handle_line.text()
        frame_handle = float(frame_handle_line)
        self.ui.frame_handle_line.setText(str(frame_handle + 5))
    # sub 1
    def sub_1_button_clicked(self):
        frame_handle_line = self.ui.frame_handle_line.text()
        frame_handle = float(frame_handle_line)
        self.ui.frame_handle_line.setText(str(frame_handle - 1))
    # sub 5
    def sub_5_button_clicked(self):
        frame_handle_line = self.ui.frame_handle_line.text()
        frame_handle = float(frame_handle_line)
        self.ui.frame_handle_line.setText(str(frame_handle - 5))

    def use_scene_name_check_state_changed(self):
        check = self.ui.use_scene_name_check.isChecked()
        if check:
            self.ui.export_line.setText('cam_'+self.current_scene_name)
        else:
            if len(self.ui.current_line.text().split('_'))<4:
                print('SceneNameの命名規則が正しくありません。\n少なくとも「_」で5つ以上に分割できる必要があります。')
                self.ui.use_scene_name_check.setChecked(False)
            else:
                self.ui.export_line.setText(parse_scene_name(self.ui.current_line.text()) )
        return

    # ------------------------------
    # 状態を確認しUIを更新する
    def update_ui(self):
        current_scene_path = cmds.file(q=True, sn=True)
        current_scene_name = os.path.basename(current_scene_path).split('.')[0]
        self.ui.current_line.setText(current_scene_name)

        self.current_scene_path = current_scene_path
        self.current_scene_name = current_scene_name

        if len(current_scene_name.split('_'))<4:
            export_name = parse_scene_name(current_scene_name)
            self.ui.use_scene_name_check.setChecked(True)
        else:
            export_name = parse_scene_name(current_scene_name)
            self.ui.use_scene_name_check.setChecked(False)

        current_dir = os.path.dirname(current_scene_path)
        output_dir = os.path.join(current_dir, '_camera')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.output_dir = output_dir
        self.ui.export_line.setText(export_name)

        # camere scale
        self.cam_scale = 0
        if self.ui.frame_handle_line == '':
            self.frame_range = False

    # ------------------------------
    def get_frame_range(self):
        # framehandle
        frame_handle = self.ui.frame_handle_line.text()
        # frame range
        sframe = cmds.playbackOptions(q=True, min=True)
        eframe = cmds.playbackOptions(q=True, max=True)
        sframe = float(sframe) - float(frame_handle)
        eframe = float(eframe) + float(frame_handle)
        frame_range = [sframe, eframe]
        return frame_range
    # ------------------------------

    def bake_button_clicked(self):
        result = self.bake()
        if result:
            cmds.inViewMessage(amg='Bake finished', pos='botLeft', fade=True, fot=2000)
        return True

    def export_button_clicked(self):
        result = self.export()
        if result:
            cmds.inViewMessage(amg='Export finished', pos='botLeft', fade=True, fot=2000)
        return True

    def bake_and_export_button_clicked(self):
        # bake
        result = self.bake()
        if result is False:
            return False
        # export
        result = self.export()
        if result:
            cmds.inViewMessage(amg='Bake and Export finished', pos='botLeft', fade=True, fot=2000)
        
    # ------------------------------
    def bake(self):
        # UIのカメラリスト
        tg_cam_list = self.get_camera_list()

        # framehandle
        frame_range = self.get_frame_range()

        # scene timewarp
        scene_timewarp = is_scene_timewarp()

        # camera scale
        self.cam_scale = 1

        # step value        
        self.step_value = 1.0
        
        # ext type
        self.ext_type = self.get_ext_type()

        info_dic = {
            'cam_scale': self.cam_scale,
            'frame_range': frame_range,
            'scene_timewarp': scene_timewarp,
            'ext_type': self.ext_type,
            'step_value': self.step_value,
            'tg_cam_list': tg_cam_list
        }

        result = bake_main(**info_dic)
        return result
        
        
    def export(self):
        # tg_cam_list
        tg_cam_list = self.get_camera_list()
        if tg_cam_list is False:
            cmds.inViewMessage(amg='Camera not selected', pos='botLeft', fade=True, fot=2000)
            return False
        # ext type
        self.ext_type = self.get_ext_type()
        # export path
        export_path = os.path.join(self.output_dir, self.ui.export_line.text())
        self.ma_cam_path = '{}.ma'.format(export_path)
        self.abc_cam_path = '{}.abc'.format(export_path)
        self.fbx_cam_path = '{}.fbx'.format(export_path)    
        
        remain_cam = self.ui.remain_cam_check.isChecked()
        info_dic = {
            'tg_cam_list': tg_cam_list,
            'frame_range': self.get_frame_range(),
            'ext_type': self.ext_type,
            'ma_cam_path': self.ma_cam_path,
            'abc_cam_path': self.abc_cam_path,
            'fbx_cam_path': self.fbx_cam_path,
            'remain_cam': remain_cam,
        }

        result = export_main(**info_dic)
        return result
        
        
    # ------------------------------
    def get_camera_list(self):
        # UIからカメラリスト取得
        tg_cam_list = []
        for i in range(self.ui.camera_list.count()):
            item = self.ui.camera_list.item(i)
            if item.text() == 'Camera not found':
                cmds.inViewMessage(amg='Camera not found', pos='botLeft', fade=True, fot=2000)
                return False
            if item.isSelected():
                tg_cam_list.append(item.text())
        if len(tg_cam_list) == 0:
            cmds.inViewMessage(amg='Camera not selected', pos='botLeft', fade=True, fot=2000)
            return False
        return tg_cam_list
        
    def set_camera_list(self):
        self.ui.camera_list.clear()
        if not cmds.ls(type='camera'):
            print('Camera not found')

        for cam_shape in cmds.ls(type='camera'):
            if cmds.getAttr('{}.orthographic'.format(cam_shape)):
                continue
            if 'shotcam' in cam_shape:
                continue
            cam = cmds.listRelatives(cam_shape, p=True, f=True)[0].split('|')[-1]
            if '|' in cam_shape:
                cmds.inViewMessage(amg='Duplicated camera found: {}'.format(cam), pos='botLeft', fade=True, fot=2000, bkc=0x00FF0000)
                continue
            if cam == 'persp':
                continue
            self.ui.camera_list.addItem(cam)
        if self.ui.camera_list.count() == 0:
            self.ui.camera_list.addItem('Camera not found')
        else:
            # select 1st item
            self.ui.camera_list.setCurrentRow(0)


    def close_exists_window(self):
        try:
            ptr = omUI.MQtUtil.mainWindow()
            if ptr is not None:
                child_list = shiboken2.wrapInstance(
                    int(ptr), QtWidgets.QMainWindow).children()
                for c in child_list[:]:
                    if self.__class__.__name__ == c.__class__.__name__:
                        try:
                            c.close()
                        except Exception as e:
                            print(e)
        except:
            pass

    def set_window_pos(self):
        try:
            desktop = QtWidgets.qApp.desktop()
            activeScreen = desktop.screenNumber(desktop.cursor().pos())
            desktopCenter = desktop.screenGeometry(activeScreen).center()
            w_w = desktopCenter.x()
            w_h = desktopCenter.y()
            framesize = self.ui.frameSize()
            self.move(w_w-framesize.width()/2, w_h-framesize.height()/2)
        except:
            pass

    def open_export_button_clicked(self):
        if os.path.exists(self.output_dir):
            _path = self.output_dir
        else:
            _path = os.path.dirname(self.current_scene_path)
        # folder open
        subprocess.Popen('explorer "{}"'.format(_path.replace('/', '\\')))


def parse_scene_name(scene_name):
    export_name = ('cam_{}'.format(scene_name))
    # MPMV_M01_C0260_anim_v002.ma
    # _区切りで{プロジェクト名}{曲ナンバー}{カット}{タスク}{バージョン}を取得　できなければシーン名を使用
    result = True
    if len(scene_name.split('_'))>4:
        ver = scene_name.split('_')[-1].split('.')[0]
        cut = scene_name.split('_')[-3]
        m_ver = scene_name.split('_')[-4]
        project = scene_name.split('_')[0]
        export_name = 'cam_{}_{}_{}'.format(m_ver, cut, ver)
        result = False
    return export_name

# ------------------------------
def unlock_current_layer():
    try:
        anim_layer_list = cmds.ls(type='animLayer')
        for anim_layer in anim_layer_list:
            cmds.animLayer(anim_layer, e=True, lock=False)
    except:
        pass


def apply_euler_filter(obj_list):
    xyz = ['.rotateX', '.rotateY', '.rotateZ']
    for obj in obj_list:
        anim_cv = map(lambda x: cmds.connectionInfo(obj+x, sfd=True), xyz)
        anim_cv = map(lambda x: x.rstrip('.output'), anim_cv)
        try:
            anim_cv = filter(lambda x: cmds.nodeType(x) in ['animCurveTL', 'animCurveTU', 'animCurveTA', 'animCurveTT'], anim_cv)
            cmds.filterCurve(anim_cv, f='euler')
        except:
            print('# Euler FilterFailed: '+obj+' #')
            continue
        print('# Euler Filter Success: '+obj+' #')


# ------------------------------

def export_ma(ma_path):
    if not os.path.exists(os.path.dirname(ma_path)):
        os.makedirs(os.path.dirname(ma_path))
    cmds.file(ma_path, force=True, options='v=0', typ='mayaAscii', pr=True, es=True, f=True)


def export_fbx(fbx_path):
    if not os.path.exists(os.path.dirname(fbx_path)):
        os.makedirs(os.path.dirname(fbx_path))
    if cmds.pluginInfo('fbxmaya', q=True, l=True) == 0:
        cmds.loadPlugin('fbxmaya')
    print(fbx_path)
    cmds.file(fbx_path, force=True, options='v=0', typ='FBX export', pr=True, es=True, f=True)


def export_abc(abc_path, sframe, eframe):
    if not os.path.exists(os.path.dirname(abc_path)):
        os.makedirs(os.path.dirname(abc_path))
    if cmds.pluginInfo('AbcExport', q=True, l=True) == 0:
        cmds.loadPlugin('AbcExport')
    cmds.evaluationManager(mode='off')
    obj_txt = ''
    for obj in cmds.ls(sl=True):
        obj_txt = obj_txt + '-root ' + obj + ' '
    strAbc = ''
    strAbc = strAbc+'-frameRange '+str(sframe)+' '+str(eframe)+' '
    strAbc = strAbc+'-uvWrite '
    strAbc = strAbc+'-worldSpace '
    strAbc = strAbc+'-eulerFilter '
    strAbc = strAbc+'-dataFormat ogawa '
    strAbc = strAbc+ '-file '+ abc_path.replace('\\','/') + ' '
    strAbc = strAbc+ obj_txt
    strAbc = strAbc+''
    print ('AbcExport -j ' + strAbc)
    print(mel.eval('AbcExport -verbose -j ' + '"' + strAbc + '"'))

# ------------------------------

def bake_main(**kwargs):
    # frame_range
    frame_range = kwargs['frame_range']
    sframe = frame_range[0]
    eframe = frame_range[1]
    # tg_cam_list
    tg_cam_list = kwargs['tg_cam_list']
    cams = tg_cam_list
    # scene_timewarp
    scene_time_warp = kwargs['scene_timewarp']
    # step_value
    step_value = kwargs['step_value']
    # cam_scale
    cam_scale = kwargs['cam_scale']

    unlock_current_layer()
    # shapeAttrs = ['fl','hfa','vfa','lsr','fs','fd','sa','coi','ncp','fcp', 'locatorScale', 'centerOfInterest', 'rotateOrder']
    shapeAttrs = ['fl']
    result_cams = []
    from_cam = []
    to_cam = []
    print(cams)
    for i in range(len(cams)):
        _cam = cmds.camera()[0]
        _cam = cmds.rename(_cam, 'shotcam')
        to_cam.append(_cam)
        from_cam.append(cams[i])

    if scene_time_warp == True:
        for i in range(len(to_cam)):
            time_set_list = []
            time_value_set_list = []
            shape_value_set_list = []

            cmds.setAttr("time1.enableTimewarp", 1)
            _frame = sframe
            while True:
                cmds.currentTime(_frame)
                warp_time = cmds.getAttr("time1.outTime", time=_frame)
                time_set_list.append([_frame, warp_time])
                _frame += step_value
                if _frame > eframe:
                    break
            cmds.setAttr("time1.enableTimewarp", 1)
            for time_set in time_set_list:
                t = time_set[0]
                warp_time = time_set[1]
                print(t, warp_time)
                cmds.currentTime(t)
                try:
                    attrsTrans = cmds.xform(from_cam[i],q=True,ws=True,t=True)
                    attrsRot = cmds.xform(from_cam[i],q=True,ws=True,ro=True)
                    time_value_set_list.append([t, attrsTrans, attrsRot])
                    for shapeAttr in shapeAttrs:
                        shape_value_set_list.append([t, shapeAttr, cmds.getAttr(from_cam[i]+'.'+shapeAttr)])
                except Exception as e:
                    print(e)
            cmds.setAttr("time1.enableTimewarp", 0)
            for time_list in time_value_set_list:
                frame = time_list[0]
                attrsTrans = time_list[1]
                attrsRot = time_list[2]
                cmds.currentTime(frame)
                cmds.setKeyframe(to_cam[i],t=frame, v=attrsTrans[0], at='tx')
                cmds.setKeyframe(to_cam[i],t=frame, v=attrsTrans[1], at='ty')
                cmds.setKeyframe(to_cam[i],t=frame, v=attrsTrans[2], at='tz')
                cmds.setKeyframe(to_cam[i],t=frame, v=attrsRot[0], at='rx')
                cmds.setKeyframe(to_cam[i],t=frame, v=attrsRot[1], at='ry')
                cmds.setKeyframe(to_cam[i],t=frame, v=attrsRot[2], at='rz')
            for shape_value_set in shape_value_set_list:
                shape_attr = shape_value_set[1]
                shape_value = shape_value_set[2]
                frame = shape_value_set[0]
                cmds.setKeyframe(to_cam[i],t=frame, v=shape_value, at=shape_attr)
    else:
        for t in range(int(sframe),int(eframe+1)):
            cmds.currentTime(t)
            for i in range(len(to_cam)):
                attrsTrans = cmds.xform(from_cam[i],q=True,ws=True,t=True)
                attrsRot = cmds.xform(from_cam[i],q=True,ws=True,ro=True)
                cmds.setKeyframe(to_cam[i],t=cmds.currentTime(q=True), v=attrsTrans[0], at='tx')
                cmds.setKeyframe(to_cam[i],t=cmds.currentTime(q=True), v=attrsTrans[1], at='ty')
                cmds.setKeyframe(to_cam[i],t=cmds.currentTime(q=True), v=attrsTrans[2], at='tz')
                cmds.setKeyframe(to_cam[i],t=cmds.currentTime(q=True), v=attrsRot[0], at='rx')
                cmds.setKeyframe(to_cam[i],t=cmds.currentTime(q=True), v=attrsRot[1], at='ry')
                cmds.setKeyframe(to_cam[i],t=cmds.currentTime(q=True), v=attrsRot[2], at='rz')
                cmds.setAttr("{}.filmFit".format(to_cam[i]), cmds.getAttr('{}.filmFit'.format(from_cam[i])))
        # for t in range(int(sframe),int(eframe+1)):
            for i in range(len(to_cam)):
                # cmds.currentTime(t)
                # if int(cam_scale) !=0:
                #     cmds.setKeyframe(to_cam[i],t=cmds.currentTime(q=True), v=float(cam_scale), at='.cs')
                # else:
                #     camScale = cmds.getAttr(from_cam[i]+'.cameraScale')
                #     cmds.setKeyframe(to_cam[i],t=cmds.currentTime(q=True), v=camScale, at='.cs')
                for thisAttr in shapeAttrs:
                    cmds.setKeyframe(to_cam[i],t=cmds.currentTime(q=True), v=cmds.getAttr(from_cam[i]+'.'+thisAttr), at='.'+thisAttr)

    # lock
    for i in range(len(to_cam)):
        try:
            cmds.setAttr(from_cam[i]+'.'+thisAttr, lock=False)
        except:
            pass

        cmds.setAttr(to_cam[i]+'.renderable', True)
        cmds.setAttr(to_cam[i]+'.renderable', lock=False)
        cmds.setAttr(to_cam[i]+'.rotateAxisX', cmds.getAttr(from_cam[i]+'.rotateAxisX'))
        cmds.setAttr(to_cam[i]+'.rotateAxisY', cmds.getAttr(from_cam[i]+'.rotateAxisY'))
        cmds.setAttr(to_cam[i]+'.rotateAxisZ', cmds.getAttr(from_cam[i]+'.rotateAxisZ'))

        for thisAttr in shapeAttrs:
            cmds.setAttr(to_cam[i]+'.'+thisAttr,lock=True)
        unlock_list = ['.cs', '.ncp', '.fcp','.lls']
        for thisAttr in unlock_list:
            cmds.setAttr(to_cam[i]+thisAttr,lock=False)

        cmds.setAttr(to_cam[i]+'.translate',lock=True)
        cmds.setAttr(to_cam[i]+'.rotate',lock=True)
        cmds.setAttr(to_cam[i]+'.scale',lock=True)
        cmds.setAttr(to_cam[i]+'.ro',lock=True)

        result_cams.append([to_cam[i], from_cam[i]])

        mel.eval('setAttr '+to_cam[i]+'.bestFitClippingPlanes true')

    apply_euler_filter(to_cam)

    return result_cams


def export_main(**kwargs):
    # frame_range
    frame_range = kwargs['frame_range']
    sframe = frame_range[0]
    eframe = frame_range[1]
    
    # ext_type
    ext_type = kwargs['ext_type']
    
    cams = get_baked_cam_list() 
    if ext_type == 'ma' or ext_type == 'all':
        cmds.select(cams, r=True)
        ma_cam_path = kwargs['ma_cam_path']
        export_ma(ma_cam_path)
    if ext_type == 'fbx' or ext_type == 'all':
        cmds.select(cams, r=True)
        fbx_cam_path = kwargs['fbx_cam_path']
        export_fbx(fbx_cam_path)
    if ext_type == 'abc' or ext_type == 'all':
        cmds.select(cams, r=True)
        abc_cam_path = kwargs['abc_cam_path']
        export_abc(abc_cam_path, sframe, eframe)

    # 一時的なカメラを削除
    if 'remain_cam' in kwargs.keys():
        if kwargs['remain_cam'] == False:
            cmds.delete(cams)


def get_baked_cam_list():
    _cams = cmds.ls('shotcam*', type='camera')
    cams = []
    for cam in _cams:
        cams.append(cmds.listRelatives(cam, p=True, f=True)[0])
    return cams
    
    
def is_scene_timewarp():
    scene_timewarp = False
    try:
        if cmds.getAttr('time1.enableTimewarp') and cmds.listConnections('time1.timewarpIn_Raw') == True:
            scene_timewarp = True
        else:
            scene_timewarp = False
    except:
        scene_timewarp = True
    return scene_timewarp


def runs():
    ui = GUI()
    ui.show()
    return True


if __name__ == '__main__':
    runs()