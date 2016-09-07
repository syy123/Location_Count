# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:48:48 2016

@author: Administrator
"""


import wx
import pprint

about_txt = u'''人数检测'''

class DataXferValidator(wx.PyValidator):
    def __init__(self, data, key):
        wx.PyValidator.__init__(self)
        self.data = data
        self.key = key
    def Clone(self):
        return DataXferValidator(self.data, self.key)
    def Validate(self, win):
        return True
    def TransferToWindow(self):
        textCtrl = self.GetWindow()
        textCtrl.SetValue(self.data.get(self.key, ""))
        return True
    
    def TransferFromWindow(self):
        textCtrl = self.GetWindow()
        self.data[self.key] = textCtrl.GetValue()
        return True

class MyDialog(wx.Dialog):
    def __init__(self, data):
        wx.Dialog.__init__(self, None, -1, "Validators:data transfer")
        about = wx.StaticText(self, -1, about_txt)
        #name_l = wx.StaticText(self, -1, "Name:")
        email_l = wx.StaticText(self, -1, u"训练时间:")
        phone_l = wx.StaticText(self, -1, u"人    数:")
        
        #self.name_t = wx.TextCtrl(self, validator = DataXferValidator(data, "name"))
        self.email_t = wx.TextCtrl(self, validator = DataXferValidator(data, "email"))
        self.phone_t = wx.TextCtrl(self, validator = DataXferValidator(data, "phone"))
        
        okay = wx.Button(self, wx.ID_OK)
        #self.Bind(wx.EVT_BUTTON, self.OkTest, okay)
        okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(about, 0, wx.ALL, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.ALL, 5)
        
        fgs = wx.FlexGridSizer(3, 2, 5,5)
        #fgs.Add(name_l, 0, wx.ALIGN_RIGHT)
        #fgs.Add(self.name_t, 0, wx.EXPAND)
        fgs.Add(email_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.email_t, 0, wx.EXPAND)
       
        fgs.Add(phone_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.phone_t, 0, wx.EXPAND)
        
        fgs.AddGrowableCol(1)
        sizer.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)
        
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(sizer)
        sizer.Fit(self)


class MyFrame(wx.Frame):
    def __init__(self,parent,iD,title):
        wx.Frame.__init__(self,parent,iD,title)
        panel = wx.Panel(self, -1)
        button = wx.Button(panel, -1, u"测试")
        self.Bind(wx.EVT_BUTTON, self.TEST, button)
        self.label1 = wx.StaticText(panel,-1,u"人数",size=(50,20),pos=(20,20))
        self.number = wx.TextCtrl(panel, -1,size=(100,20),pos=(50,20))
        self.label2 = wx.StaticText(panel, -1, u'训练时间', size=(50,20),pos=(160,20))
        self.time = wx.TextCtrl(panel, -1, size = (100, 20), pos = (220, 20))
    def TEST(self, event):        
        data = {"name":"SunYuana"}
        dlg = MyDialog(data)
        dlg.ShowModal()
        #dlg.Destroy()
        #wx.MessageBox("you enterd these values:\n\n" + pprint.pformat(data))
        #wx.MessageBox("you enterd these values:\n\n" + (data))
        print type(data),data.get('phone')
        self.number.SetValue(str(data.get('phone')))
        self.time.AppendText(str(data.get('email')))
        if str(data.get('phone')) != 'None':
            print u'参数',int(self.number.GetValue())
        else:
            wx.MessageBox(u"请配置参数")
            #wx.MessageDialog(self, u"请重新配置参数", "MessageBox", style=wx.OK, pos=wx.DefaultPosition)
            print u"请重新输入参数 "
class MyApp(wx.App):
    def OnInit(self):
        frame= MyFrame(None, -1, "syy")
        frame.Show(True)
        return True

def mainFunc():
    app = MyApp(0)
    app.MainLoop()

if __name__=='__main__':
    mainFunc()
    
    
    
'''if __name__ == "__main__":
    app = wx.PySimpleApp()
    choices = ["Alpha", "Baker", "Charlie", "Delta"]
    dialog = wx.SingleChoiceDialog(None, "Pick A Word", "Choices", choices)
    if dialog.ShowModal() == wx.ID_OK:
        print "You selected:%s\n" % dialog.GetStringSelection()
    dialog.Destroy()
    dialog = wx.TextEntryDialog(None, "what kind of text would you like to enter?","TextEntry","Default Value",
                                style=wx.OK|wx.CANCEL)
    if dialog.ShowModal() == wx.ID_OK:
        print "you enterd: %s" %dialog.GetValue()
    dialog.Destroy()'''
