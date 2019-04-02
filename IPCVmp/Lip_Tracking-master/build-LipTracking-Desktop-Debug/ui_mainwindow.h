/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>
#include "qcustomplot.h"

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QLabel *bwImage;
    QPushButton *selectVideoButton;
    QTextBrowser *videoFilePathText;
    QSlider *frameSlider;
    QCustomPlot *finalImage;
    QPushButton *webcamButton;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1067, 687);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        bwImage = new QLabel(centralWidget);
        bwImage->setObjectName(QString::fromUtf8("bwImage"));
        bwImage->setGeometry(QRect(70, 100, 351, 311));
        bwImage->setAutoFillBackground(false);
        bwImage->setStyleSheet(QString::fromUtf8("Background-color: #000;"));
        selectVideoButton = new QPushButton(centralWidget);
        selectVideoButton->setObjectName(QString::fromUtf8("selectVideoButton"));
        selectVideoButton->setGeometry(QRect(180, 490, 75, 23));
        videoFilePathText = new QTextBrowser(centralWidget);
        videoFilePathText->setObjectName(QString::fromUtf8("videoFilePathText"));
        videoFilePathText->setGeometry(QRect(260, 490, 371, 31));
        frameSlider = new QSlider(centralWidget);
        frameSlider->setObjectName(QString::fromUtf8("frameSlider"));
        frameSlider->setGeometry(QRect(390, 440, 160, 19));
        frameSlider->setOrientation(Qt::Horizontal);
        finalImage = new QCustomPlot(centralWidget);
        finalImage->setObjectName(QString::fromUtf8("finalImage"));
        finalImage->setGeometry(QRect(610, 90, 341, 331));
        finalImage->setAutoFillBackground(true);
        webcamButton = new QPushButton(centralWidget);
        webcamButton->setObjectName(QString::fromUtf8("webcamButton"));
        webcamButton->setGeometry(QRect(180, 550, 471, 91));
        webcamButton->setCheckable(true);
        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        bwImage->setText(QApplication::translate("MainWindow", "TextLabel", nullptr));
        selectVideoButton->setText(QApplication::translate("MainWindow", "Select Video", nullptr));
        webcamButton->setText(QApplication::translate("MainWindow", "Webcam", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
