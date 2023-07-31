/********************************************************************************
** Form generated from reading UI file 'maeve mockupYCqXWU.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAEVE_20_MOCKUPYCQXWU_H
#define MAEVE_20_MOCKUPYCQXWU_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Maeve
{
public:
    QWidget *centralwidget;
    QTabWidget *tabWidget;
    QWidget *ToDoList;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QFrame *frame;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QProgressBar *progressBar;
    QFrame *frame_2;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QProgressBar *progressBar_2;
    QWidget *ReadingList;
    QWidget *Wardrobe;
    QWidget *Banking;

    void setupUi(QMainWindow *Maeve)
    {
        if (Maeve->objectName().isEmpty())
            Maeve->setObjectName(QStringLiteral("Maeve"));
        Maeve->setEnabled(true);
        Maeve->resize(664, 546);
        QSizePolicy sizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::MinimumExpanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Maeve->sizePolicy().hasHeightForWidth());
        Maeve->setSizePolicy(sizePolicy);
        Maeve->setAutoFillBackground(false);
        Maeve->setAnimated(true);
        centralwidget = new QWidget(Maeve);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setGeometry(QRect(0, 0, 661, 541));
        ToDoList = new QWidget();
        ToDoList->setObjectName(QStringLiteral("ToDoList"));
        scrollArea = new QScrollArea(ToDoList);
        scrollArea->setObjectName(QStringLiteral("scrollArea"));
        scrollArea->setGeometry(QRect(0, 9, 651, 501));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QStringLiteral("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 649, 499));
        frame = new QFrame(scrollAreaWidgetContents);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setGeometry(QRect(10, 10, 351, 111));
        frame->setAutoFillBackground(true);
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        label = new QLabel(frame);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(10, 10, 101, 16));
        label_2 = new QLabel(frame);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(270, 10, 81, 20));
        label_3 = new QLabel(frame);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(10, 40, 321, 41));
        label_3->setTextFormat(Qt::AutoText);
        label_3->setScaledContents(true);
        label_3->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        label_3->setWordWrap(true);
        progressBar = new QProgressBar(frame);
        progressBar->setObjectName(QStringLiteral("progressBar"));
        progressBar->setGeometry(QRect(10, 90, 331, 16));
        progressBar->setValue(24);
        frame_2 = new QFrame(scrollAreaWidgetContents);
        frame_2->setObjectName(QStringLiteral("frame_2"));
        frame_2->setGeometry(QRect(10, 130, 351, 111));
        frame_2->setAutoFillBackground(true);
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        label_4 = new QLabel(frame_2);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(10, 10, 101, 16));
        label_5 = new QLabel(frame_2);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(270, 10, 81, 20));
        label_6 = new QLabel(frame_2);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(10, 40, 321, 41));
        label_6->setTextFormat(Qt::AutoText);
        label_6->setScaledContents(true);
        label_6->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        label_6->setWordWrap(true);
        progressBar_2 = new QProgressBar(frame_2);
        progressBar_2->setObjectName(QStringLiteral("progressBar_2"));
        progressBar_2->setGeometry(QRect(10, 90, 331, 16));
        progressBar_2->setValue(24);
        scrollArea->setWidget(scrollAreaWidgetContents);
        tabWidget->addTab(ToDoList, QString());
        ReadingList = new QWidget();
        ReadingList->setObjectName(QStringLiteral("ReadingList"));
        tabWidget->addTab(ReadingList, QString());
        Wardrobe = new QWidget();
        Wardrobe->setObjectName(QStringLiteral("Wardrobe"));
        tabWidget->addTab(Wardrobe, QString());
        Banking = new QWidget();
        Banking->setObjectName(QStringLiteral("Banking"));
        tabWidget->addTab(Banking, QString());
        Maeve->setCentralWidget(centralwidget);

        retranslateUi(Maeve);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(Maeve);
    } // setupUi

    void retranslateUi(QMainWindow *Maeve)
    {
        Maeve->setWindowTitle(QApplication::translate("Maeve", "MainWindow", nullptr));
#ifndef QT_NO_TOOLTIP
        Maeve->setToolTip(QString());
#endif // QT_NO_TOOLTIP
        label->setText(QApplication::translate("Maeve", "Task #1", nullptr));
        label_2->setText(QApplication::translate("Maeve", "Due: 9/25/2022", nullptr));
        label_3->setText(QApplication::translate("Maeve", "This is the description for task #1.", nullptr));
        label_4->setText(QApplication::translate("Maeve", "Task #2", nullptr));
        label_5->setText(QApplication::translate("Maeve", "Due: 9/25/2022", nullptr));
        label_6->setText(QApplication::translate("Maeve", "This is the description for task #2.", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(ToDoList), QApplication::translate("Maeve", "Tab 1", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(ReadingList), QApplication::translate("Maeve", "Tab 2", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Wardrobe), QApplication::translate("Maeve", "Page", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Banking), QApplication::translate("Maeve", "Page", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Maeve: public Ui_Maeve {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAEVE_20_MOCKUPYCQXWU_H
