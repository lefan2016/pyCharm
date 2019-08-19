# coding=utf8
import os


print u"{}{}".format('name', u'中文名')
file_path = __file__
config_ui_file_path = os.path.join(os.path.split(file_path)[0], 'config/build_ui.config').replace('\\', '/')
print config_ui_file_path