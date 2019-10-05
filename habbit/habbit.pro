#-------------------------------------------------
#
# Project created by QtCreator 2019-09-22T14:41:37
#
#-------------------------------------------------

QT       += core gui
QT       += sql

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = habbit
TEMPLATE = app
CONFIG += c++11

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

CONFIG += c++11

SOURCES += \
    add_daily_task_window.cpp \
    create_account_window.cpp \
    daily_tasks_structure.cpp \
    history_structure.cpp \
        database.cpp \
    login_window.cpp \
        main.cpp \
    main_window.cpp \
    manage_daily_tasks_window.cpp

HEADERS += \
    add_daily_task_window.h \
    create_account_window.h \
    daily_tasks_structure.h \
    history_structure.h \
        database.h \
    login_window.h \
    main_window.h \
    manage_daily_tasks_window.h

FORMS += \
        adddailytaskwindow.ui \
        createaccountwindow.ui \
        loginwindow.ui \
        mainwindow.ui \
        managedailytasks.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES +=
