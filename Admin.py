# -*- coding: utf-8 -*-
'''
管理员模块
1.浏览图书
    管理员可以浏览图书，快速选择要管理的书籍
    书籍管理包括：书籍上架、下架，修改书籍库存和价格
    在图书浏览界面，可以选择书籍上架功能
    在书籍详情界面，可以下架，修改库存和价格
2.搜索图书
    管理员通过搜索书籍进行书籍的管理
3.统计功能
    按日统计销量和销售额，如统计11月每日的销售情况
    按月统计销量和销售额，如统计2017年12个月每月的销售情况
    统计近十年的销售情况，如统计2008-2017年每年的销售情况
4.订单管理
    管理员可以通过订单管理来查看用户下单的日期以及该订单的收货信息
5.个人信息
    管理员可以修改个人的信息
    故那里员可以修改登陆的账号和密码
Author: Jachin
Data: 2017- 11- 19
'''
from HeadFile import *


class Admin(Frame):
    def __init__(self, windows_Admin=None):
        Frame.__init__(self, windows_Admin)
        windows_Admin.title('Admin')
        windows_Admin.geometry("740x458+330+150")
        windows_Admin.resizable(0, 0)
        self.Main(windows_Admin)
        windows_Admin.mainloop()

    def Main(self, windows_Admin):
        '''
        程序主界面？反正有负责整个软件的五大功能的组成
        :param windows_Admin:
        :return:
        '''
        # 五个图标
        self.ico_book = ImageTk.PhotoImage(Image.open(r'ico\book.png'))
        self.ico_user = ImageTk.PhotoImage(Image.open(r'ico\user.png'))
        self.ico_search = ImageTk.PhotoImage(Image.open(r'ico\search.png'))
        self.ico_order = ImageTk.PhotoImage(Image.open(r'ico\order.png'))
        self.ico_statistics = ImageTk.PhotoImage(Image.open(r'ico\statistics.png'))

        self.FrameMenu = tk.LabelFrame(windows_Admin, text='', background='white')
        self.FrameMenu.place(relx=0, rely=0, relheight=1, relwidth=0.13, )

        self.b_book = tk.Button(self.FrameMenu, image=self.ico_book, command=self.b_book
                                , relief='groove')
        self.b_book.grid(column=1, row=0)

        self.b_search = tk.Button(self.FrameMenu, image=self.ico_search, command=self.b_search
                                  , relief='groove')
        self.b_search.grid(column=1, row=1)

        self.b_statistics = tk.Button(self.FrameMenu, image=self.ico_statistics, command=self.b_statistics
                                      , relief='groove')
        self.b_statistics.grid(column=1, row=2)

        self.b_order = tk.Button(self.FrameMenu, image=self.ico_order, command=self.b_order
                                 , relief='groove')
        self.b_order.grid(column=1, row=3)
        self.b_admin = tk.Button(self.FrameMenu, image=self.ico_user, command=self.b_admin
                                 , relief='groove')
        self.b_admin.grid(column=1, row=4)

        self.Page()

    def Page(self):
        '''
        图书浏览主界面设计，包括翻页浏览
        :return:
        '''
        cur.execute('select ISBN,Bname from book')
        self.BookInfo = cur.fetchall()

        def pro():
            if self.bookpage > 0:
                self.bookpage -= 1
                self.Page()

        def nex():
            if self.bookpage < self.maxpage:
                self.bookpage += 1
                self.Page()

        self.Btn = ['b_book' + str(i) for i in range(8)]
        self.Lab = ['l_name' + str(i) for i in range(8)]
        self.Im = ['im' + str(i) for i in range(8)]
        self.relx = [0.05, 0.26, 0.47, 0.68]

        style = Style()
        style.configure('book.TLabel', relief='flat'
                        , wraplength=100, justify='center'
                        , font=(u'幼圆', 12), anchor='n'
                        , background='white')

        self.FramePage = tk.LabelFrame(windows_Admin, text='书籍', background='white')
        self.FramePage.place(relx=0.13, rely=0, relheight=1, relwidth=0.88, )

        self.bp = ImageTk.PhotoImage(Image.open(r'ico\pro.png'))
        self.bn = ImageTk.PhotoImage(Image.open(r'ico\next.png'))
        self.up = ImageTk.PhotoImage(Image.open(r'ico\upload.png'))
        self.imNone = ImageTk.PhotoImage(Image.open(r'ico\none.png'))

        self.b_pro = tk.Button(self.FramePage, relief='groove', command=pro, image=self.bp)
        self.b_pro.place(relx=0.88, rely=0.38, relwidth=0.1, relheight=0.1)
        # 54.395 54.6375

        self.b_next = tk.Button(self.FramePage, relief='groove', command=nex, image=self.bn)
        self.b_next.place(relx=0.88, rely=0.48, relwidth=0.1, relheight=0.1)

        j = -1
        for i in range(8):
            if j < self.num:
                j += 1

            self.path = r''
            if self.bookpage < self.maxpage:
                self.path = r"thu\%s.thumbnail" % self.BookInfo[8 * self.bookpage + i][0]
                self.Lab[i] = Label(self.FramePage, text=self.BookInfo[8 * self.bookpage + i][1], style='book.TLabel')
            elif self.bookpage == self.maxpage and j < self.num:
                self.path = r"thu\%s.thumbnail" % self.BookInfo[8 * self.bookpage + j][0]
                self.Lab[i] = Label(self.FramePage, text=self.BookInfo[8 * self.bookpage + i][1], style='book.TLabel')

            elif self.bookpage == self.maxpage and j >= self.num:
                self.path = r"ico\none.png"
                self.Lab[i] = Label(self.FramePage, text='', anchor='n')
            try:
                self.Im[i] = ImageTk.PhotoImage(Image.open(self.path))
            except:
                self.Im[i] = ImageTk.PhotoImage(Image.open(r'ico\none.png'))
            self.Btn[i] = tk.Button(self.FramePage, bg='white', image=self.Im[i]
                                    , command=self.Det, relief='groove')

            # 位置
            if i < 4:
                self.Btn[i].place(relx=self.relx[i], rely=0.05, relwidth=0.16, relheight=0.345)
                self.Lab[i].place(relx=self.relx[i], rely=0.4, relwidth=0.16, relheight=0.09)
            elif i >= 4:
                self.Btn[i].place(relx=self.relx[i - 4], rely=0.5, relwidth=0.16, relheight=0.345)
                self.Lab[i].place(relx=self.relx[i - 4], rely=0.85, relwidth=0.16, relheight=0.09)

            if self.bookpage == self.maxpage and j >= self.num:
                self.Btn[i].place_forget()
                self.Lab[i].place_forget()

        # 按钮事件
        def do0(event):
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 0][0]

        self.Btn[0].bind('<Button-1>', do0)

        def do1(event):
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 1][0]

        self.Btn[1].bind('<Button-1>', do1)

        def do2(event):
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 2][0]

        self.Btn[2].bind('<Button-1>', do2)

        def do3(event):
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 3][0]

        self.Btn[3].bind('<Button-1>', do3)

        def do4(event):
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 4][0]

        self.Btn[4].bind('<Button-1>', do4)

        def do5(event):
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 5][0]

        self.Btn[5].bind('<Button-1>', do5)

        def do6(event):
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 6][0]

        self.Btn[6].bind('<Button-1>', do6)

        def do7(event):
            self.BookInfoISBN = self.BookInfo[8 * self.bookpage + 7][0]

        self.Btn[7].bind('<Button-1>', do7)

        # 书籍上架
        button_upload = tk.Button(self.FramePage, image=self.up, relief='groove', command=self.addBook)
        button_upload.place(relx=0.88, rely=0.18, relwidth=0.1, relheight=0.15)

    def Det(self):
        '''
        详情页查看界面设计
        :return:
        '''
        style = Style()
        style.configure('bookDet.TLabel', relief='flat'
                        , font=(u'幼圆', 12), anchor='center'
                        , background='white', foreground='#4141CF')
        style.configure('TButton', background='blue', foreground='black', font=(u'幼圆', 12), anchor='center')
        self.FrameNone = tk.LabelFrame(windows_Admin, text='详情', background='white')
        self.FrameNone.place(relx=0.13, rely=0, relheight=1, relwidth=1, )

        self.FrameDet = tk.LabelFrame(self.FrameNone, background='white')
        self.FrameDet.place(relx=0.145, rely=-0.01, relheight=1, relwidth=0.6, )

        def Back():
            self.FrameNone.destroy()

        # 图标
        P_det = tk.Canvas(self.FrameDet, bg='#FFFFFF')
        self.im_det = ImageTk.PhotoImage(Image.open(r'ico\det2.png'))
        P_det.create_image(0.4, 8, anchor='nw', image=self.im_det)
        P_det.place(relx=0.02, rely=0.01, relwidth=0.16, relheight=0.18)
        comm = "select Bname,Bauth,Bpub,ISBN,Bprice,Bstock from book where ISBN = '%s'" % self.BookInfoISBN
        cur.execute(comm)
        self.BookDetInfo = cur.fetchall()
        self.bookValues = ['a', 'b', 'c', 'd', 'e', 'f']
        self.Text_list = ['Text_name' + str(i) for i in range(6)]
        Lab_list = ['lab_name' + str(i) for i in range(6)]
        Lab_name = ['书名', '作者', '出版社', 'ISBN', '价格', '库存']

        for i in range(6):
            self.bookValues[i] = tk.StringVar(value='%s' % self.BookDetInfo[0][i])

            # 文本框，标签和分割线
            self.Text_list[i] = Entry(self.FrameDet, textvariable=self.bookValues[i]
                                      , font=(14), justify='center', state='readonly')
            Lab_list[i] = Label(self.FrameDet, text=Lab_name[i], style='bookDet.TLabel')

        # 0书名 1作者 2出版社 3ISBN 4价格 5库存
        self.Text_list[0].place(relx=0.37, rely=0.07, relwidth=0.5, relheight=0.06)
        self.Text_list[1].place(relx=0.18, rely=0.3, relwidth=0.7, relheight=0.06)
        self.Text_list[2].place(relx=0.18, rely=0.4, relwidth=0.7, relheight=0.06)
        self.Text_list[3].place(relx=0.18, rely=0.5, relwidth=0.7, relheight=0.06)
        self.Text_list[4].place(relx=0.18, rely=0.6, relwidth=0.5, relheight=0.06)
        self.Text_list[5].place(relx=0.18, rely=0.7, relwidth=0.5, relheight=0.06)

        Lab_list[0].place(relx=0.25, rely=0.07, relwidth=0.1, relheight=0.06)
        Lab_list[1].place(relx=0.06, rely=0.3, relwidth=0.1, relheight=0.06)
        Lab_list[2].place(relx=0.03, rely=0.40, relwidth=0.15, relheight=0.06)
        Lab_list[3].place(relx=0.06, rely=0.5, relwidth=0.12, relheight=0.06)
        Lab_list[4].place(relx=0.06, rely=0.60, relwidth=0.1, relheight=0.06)
        Lab_list[5].place(relx=0.07, rely=0.7, relwidth=0.1, relheight=0.06)

        self.btn_EditPrice = Button(self.FrameDet, text='修改价格', command=self.modifyPrice, style='TButton')
        self.btn_EditPrice.place(relx=0.70, rely=0.6, relwidth=0.18, relheight=0.06)

        self.btn_EditStock = Button(self.FrameDet, text='修改库存', command=self.modifyStock, style='TButton')
        self.btn_EditStock.place(relx=0.70, rely=0.7, relwidth=0.18, relheight=0.06)

        self.btn_Down = Button(self.FrameDet, text='下架', command=self.removeBook, style='TButton')
        self.btn_Down.place(relx=0.37, rely=0.80, relwidth=0.12, relheight=0.08)

        self.btn_Back = Button(self.FrameDet, text='返回', command=Back, style='TButton')
        self.btn_Back.place(relx=0.73, rely=0.80, relwidth=0.12, relheight=0.08)

        style.configure('TSeparator', background='#000000')
        Line1 = Separator(self.FrameDet, orient='horizontal', style='Line1.TSeparator')
        Line1.place(relx=0., rely=0.2, relwidth=1, relheight=0.008)

    def Order(self):
        '''
        订单界面设计
        :return:
        '''
        self.FrameOrder = tk.LabelFrame(windows_Admin, text='订单管理', background='white')
        self.FrameOrder.place(relx=0.13, rely=0, relheight=1, relwidth=0.87, )

        # Treeview组件，6列，显示表头，带垂直滚动条
        self.libox_OrderInfo = Treeview(self.FrameOrder,
                                        columns=('c1', 'c2', 'c3', 'c4'), )
        # show="tree")
        self.libox_OrderInfo.column('c1', width=20, anchor='center')
        self.libox_OrderInfo.column('c2', width=8, anchor='center')
        self.libox_OrderInfo.column('c3', width=8, anchor='center')
        self.libox_OrderInfo.column('c4', width=8, anchor='center')
        # 设置每列表头标题文本
        self.libox_OrderInfo.heading('c1', text='书名')
        self.libox_OrderInfo.heading('c2', text='数量')
        self.libox_OrderInfo.heading('c3', text='总价')
        self.libox_OrderInfo.heading('c4', text='付款')

        self.libox_OrderInfo.place(relx=0.1, rely=0.08, relwidth=0.77, relheight=0.7)
        # 滚动条
        ysb = Scrollbar(self.FrameOrder, orient='vertical', command=self.libox_OrderInfo.yview)
        xsb = Scrollbar(self.FrameOrder, orient='horizontal', command=self.libox_OrderInfo.xview)
        self.libox_OrderInfo.configure(yscroll=ysb.set, xscroll=xsb.set)
        ysb.config(command=self.libox_OrderInfo.yview)
        xsb.config(command=self.libox_OrderInfo.xview)
        ysb.pack(side=tk.RIGHT, fill=tk.Y)
        xsb.pack(side=tk.BOTTOM, fill=tk.X)

        order_check = tk.Button(self.FrameOrder, text='查看详情', relief='groove', command=self.checkOrder)
        order_check.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

    def Search(self):
        '''
        搜索界面设计
        :return:
        '''
        self.style = Style()
        self.style.configure('TSeparator', background='#000000')
        self.style.configure('search.TLabel', anchor='w', font=(u'幼圆', 14), background='white'
                             , relief='flat')

        self.FrameSearch = tk.LabelFrame(windows_Admin, background='white', text='搜索')
        self.FrameSearch.place(relx=0.13, rely=0, relwidth=0.87, relheight=1, )

        self.labelSearchBName = Label(self.FrameSearch, text='书名', style='search.TLabel')
        # self.labelSearchBName.place(relx = 0.2,rely = 0.07,relwidth = 0.148,relheight = 0.06)

        self.textSearch = tk.Text(self.FrameSearch, font=18, relief='solid')
        self.textSearch.place(relx=0.22, rely=0.05, relwidth=0.4, relheight=0.06)

        self.buttonSearch = tk.Button(self.FrameSearch, text='Search', command=self.event_search, relief='groove')
        self.buttonSearch.place(relx=0.65, rely=0.05, relwidth=0.11, relheight=0.07)

        self.var = tk.StringVar()
        self.var.set('书名')

        self.r1 = Radiobutton(windows_Admin, text='书名', variable=self.var, value='书名')
        self.r1.place(relx=0.35, rely=0.17, relwidth=0.07, relheight=0.05)
        self.r2 = Radiobutton(windows_Admin, text='作者', variable=self.var, value='作者')
        self.r2.place(relx=0.45, rely=0.17, relwidth=0.07, relheight=0.05)

        self.Line1 = Separator(self.FrameSearch, orient='horizontal', style='Line1.TSeparator')
        self.Line1.place(relx=0.14, rely=0.22, relwidth=0.69, relheight=0.007)

        self.Line2 = Separator(self.FrameSearch, orient='vertical', style='Line1.TSeparator')
        self.Line2.place(relx=0.14, rely=-0.015, relwidth=0.002, relheight=1.1)
        self.Line2 = Separator(self.FrameSearch, orient='vertical', style='Line1.TSeparator')
        self.Line2.place(relx=0.83, rely=-0.015, relwidth=0.002, relheight=1.1)

        # Treeview组件，6列，显示表头，带垂直滚动条
        self.libox_bookInfo = Treeview(self.FrameSearch,
                                       columns=('c1', 'c2'),
                                       show="headings")
        self.libox_bookInfo.column('c1', width=80, anchor='center')
        self.libox_bookInfo.column('c2', width=80, anchor='center')

        # 设置每列表头标题文本
        self.libox_bookInfo.heading('c1', text='书名')
        self.libox_bookInfo.heading('c2', text='作者')

        # 滚动条
        self.libox_bookInfo.place(relx=0.2, rely=0.3, relwidth=0.57, relheight=0.5)
        ysb = Scrollbar(self.FrameSearch, orient='vertical', command=self.libox_bookInfo.yview)
        xsb = Scrollbar(self.FrameSearch, orient='horizontal', command=self.libox_bookInfo.xview)
        self.libox_bookInfo.configure(yscroll=ysb.set, xscroll=xsb.set)
        ysb.config(command=self.libox_bookInfo.yview)
        xsb.config(command=self.libox_bookInfo.xview)
        ysb.pack(side=tk.RIGHT, fill=tk.Y)
        xsb.pack(side=tk.BOTTOM, fill=tk.X)

        self.btnShowDet = tk.Button(self.FrameSearch, text='查看详情', command=self.SearchToDet, relief='groove')
        self.btnShowDet.place(relx=0.66, rely=0.85, relwidth=0.11, relheight=0.07)

        # self.libox_bookInfo.bind('<Double-Button-1>',self.SearchToDet)

    def Statistics(self):
        '''
        统计界面-设计
        :return:
        '''
        # TODO 统计页面设计及相应的功能

        self.style.configure('TSeparator', background='#000000')

        self.FrameStatistics = tk.LabelFrame(windows_Admin, background='white', text='统计')
        self.FrameStatistics.place(relx=0.13, rely=0, relwidth=0.87, relheight=1, )

        FrameStatistics = tk.LabelFrame(self.FrameStatistics)
        FrameStatistics.place(relx=0.2, rely=0.08, relwidth=0.55, relheight=0.8)

        label_date = Label(FrameStatistics, text='按日统计', anchor='center', font=14, foreground='blue')
        label_date.place(relx=0.0, rely=0, relwidth=1, relheight=0.1)
        line_date = Separator(FrameStatistics, style='TSeparator')
        line_date.place(relx=0.0, rely=0.08, relwidth=1, relheight=0.001)
        label_date = tk.Label(FrameStatistics, text='输入月份', font=10)
        label_date.place(relx=0.0, rely=0.1, relwidth=0.25, relheight=0.1)
        self.entry_date = Entry(FrameStatistics, font=14)
        self.entry_date.place(relx=0.25, rely=0.1, relwidth=0.2, relheight=0.1)
        btn_date = tk.Button(FrameStatistics, text='统计销量', relief='groove', font=10, command=self.stastic_dateS)
        btn_date.place(relx=0.45, rely=0.1, relwidth=0.25, relheight=0.1)
        btn_dates = tk.Button(FrameStatistics, text='统计销售额', relief='groove', font=10, command=self.stastic_dateP)
        btn_dates.place(relx=0.7, rely=0.1, relwidth=0.3, relheight=0.1)

        label_date = Label(FrameStatistics, text='按月统计', anchor='center', font=14, foreground='blue')
        label_date.place(relx=0.0, rely=0.35, relwidth=1, relheight=0.1)
        line_moth = Separator(FrameStatistics, style='TSeparator')
        line_moth.place(relx=0.0, rely=0.43, relwidth=1, relheight=0.001)
        label_moth = tk.Label(FrameStatistics, text='输入年份', font=10)
        label_moth.place(relx=0.0, rely=0.45, relwidth=0.25, relheight=0.1)
        self.entry_moth = Entry(FrameStatistics, font=14)
        self.entry_moth.place(relx=0.25, rely=0.45, relwidth=0.2, relheight=0.1)
        btn_moth = tk.Button(FrameStatistics, text='统计销量', relief='groove', font=10, command=self.stastic_mothS)
        btn_moth.place(relx=0.45, rely=0.45, relwidth=0.25, relheight=0.1)
        btn_moths = tk.Button(FrameStatistics, text='统计销售额', relief='groove', font=10, command=self.stastic_mothP)
        btn_moths.place(relx=0.7, rely=0.45, relwidth=0.3, relheight=0.1)

        label_date = Label(FrameStatistics, text='按年统计', anchor='center', font=14, foreground='blue')
        label_date.place(relx=0.0, rely=0.7, relwidth=1, relheight=0.1)
        line_year = Separator(FrameStatistics, style='TSeparator')
        line_year.place(relx=0.0, rely=0.78, relwidth=1, relheight=0.001)
        btn_year = tk.Button(FrameStatistics, text='统计销量', relief='groove', font=10, command=self.stastic_yearS)
        btn_year.place(relx=0.2, rely=0.8, relwidth=0.25, relheight=0.1)
        btn_years = tk.Button(FrameStatistics, text='统计销售额', relief='groove', font=10, command=self.stastic_yearP)
        btn_years.place(relx=0.5, rely=0.8, relwidth=0.3, relheight=0.1)

    def Admin(self):
        '''
        管理员界面设计
        :return:
        '''
        cur.execute("select * from administrator")
        adminInfo = cur.fetchall()
        self.text_adminUser = tk.StringVar(value='%s' % adminInfo[0][1].encode('utf-8').strip())
        self.text_adminName = tk.StringVar(value='%s' % adminInfo[0][2])
        self.text_adminEamil = tk.StringVar(value='%s' % adminInfo[0][4])

        style = Style()
        style.configure('Admin.TLabel', anchor='w', font=(u'幼圆', 14), background='white'
                        , relief='flat', foreground='#4141CF')

        self.FrameUser = tk.LabelFrame(windows_Admin, text='', background='#fff')
        self.FrameUser.place(relx=0.13, rely=0, relheight=1, relwidth=0.87)

        self.FrameAdmin = tk.LabelFrame(self.FrameUser, text='')  # ,background = '#fff')
        self.FrameAdmin.place(relx=0.2, rely=0.2, relwidth=0.55, relheight=0.6)

        label_admin = tk.Label(self.FrameAdmin, text='管理员信息', font=14, anchor='center')
        label_admin.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.09)

        Line_s = Separator(self.FrameAdmin, orient='horizontal', style='Line1.TSeparator')
        Line_s.place(relx=0.0, rely=0.09, relwidth=1, relheight=0.007)

        label_adminUser = Label(self.FrameAdmin, text='账号', font=14)
        label_adminName = Label(self.FrameAdmin, text='名字', font=14)
        label_adminEamil = Label(self.FrameAdmin, text='邮箱', font=14)
        label_adminUser.place(relx=0.08, rely=0.2, relwidth=0.2, relheight=0.1)
        label_adminName.place(relx=0.08, rely=0.4, relwidth=0.2, relheight=0.1)
        label_adminEamil.place(relx=0.08, rely=0.6, relwidth=0.2, relheight=0.1)
        self.entry_adminUser = Entry(self.FrameAdmin, textvariable=self.text_adminUser, font=(u'宋体', 14),
                                     state='readonly')
        self.entry_adminName = Entry(self.FrameAdmin, textvariable=self.text_adminName, font=(u'宋体', 14),
                                     state='readonly')
        self.entry_adminEamil = Entry(self.FrameAdmin, textvariable=self.text_adminEamil, font=(u'宋体', 14),
                                      state='readonly')

        self.entry_adminUser.place(relx=0.28, rely=0.2, relwidth=0.6, relheight=0.12)
        self.entry_adminName.place(relx=0.28, rely=0.4, relwidth=0.6, relheight=0.12)
        self.entry_adminEamil.place(relx=0.28, rely=0.6, relwidth=0.6, relheight=0.12)

        self.btnEditPswd = tk.Button(self.FrameAdmin, text='修改密码', command=self.EditAdminPswd
                                     , relief='groove', font=(u'幼圆', 14))
        self.btnEditUserInfo = tk.Button(self.FrameAdmin, text='修改信息', command=self.event_editAdminInfo
                                         , relief='groove', font=(u'幼圆', 14))
        self.btnEditPswd.place(relx=0.12, rely=0.8, relwidth=0.3, relheight=0.12)
        self.btnEditUserInfo.place(relx=0.58, rely=0.8, relwidth=0.3, relheight=0.12)

    def EditAdminPswd(self):
        '''
        账户个人修改密码时弹出的界面-设计
        :return:
        '''
        FrameEditPswd = tk.LabelFrame(self.FrameUser)

        FrameEditPswd.place(relx=0.2, rely=0.2, relwidth=0.55, relheight=0.6)
        # windows_Admin.withdraw()windows_Admin.state("zoomed")
        # windows_Admin.deiconify()
        label_pswd = tk.Label(FrameEditPswd, text='修改密码', font=14, anchor='center')
        label_pswd.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.09)

        label_orgin = Label(FrameEditPswd, text='原密码', font=14)
        label_newpswd = Label(FrameEditPswd, text='新密码', font=14)
        label_repswd = Label(FrameEditPswd, text='新密码', font=14)
        label_orgin.place(relx=0.08, rely=0.2, relwidth=0.2, relheight=0.1)
        label_newpswd.place(relx=0.08, rely=0.4, relwidth=0.2, relheight=0.1)
        label_repswd.place(relx=0.08, rely=0.6, relwidth=0.2, relheight=0.1)
        entry_orgin = Entry(FrameEditPswd, font=(u'宋体', 14))
        entry_newpswd = Entry(FrameEditPswd, font=(u'宋体', 14), show='*')
        entry_repswd = Entry(FrameEditPswd, font=(u'宋体', 14), show='*')

        entry_orgin.place(relx=0.28, rely=0.2, relwidth=0.6, relheight=0.12)
        entry_newpswd.place(relx=0.28, rely=0.4, relwidth=0.6, relheight=0.12)
        entry_repswd.place(relx=0.28, rely=0.6, relwidth=0.6, relheight=0.12)

        Line_s = Separator(FrameEditPswd, orient='horizontal', style='Line1.TSeparator')
        Line_s.place(relx=0.0, rely=0.09, relwidth=1, relheight=0.007)

        def RePswd():
            '''
            确认修改密码，检测原密码是否正确。新密码是否输入一致
            全部信息确认无误后提交到数据库
            :return:
            '''
            cur.execute('select Apswd from administrator')
            # conn.commit()
            userPswd = cur.fetchall()
            if entry_orgin.get() != userPswd[0][0]:
                showerror('Error', '原密码错误')
            elif entry_newpswd.get() == entry_repswd.get():
                if entry_newpswd.get() != '':
                    comm = "update administrator set Apswd = '%s'" % (entry_repswd.get())
                    cur.execute(comm)
                    conn.commit()
                    FrameEditPswd.destroy()
                    showinfo('提示', '修改成功')
                else:
                    showerror('错误', '密码不能为空')
            else:
                showerror('错误', '两次输入密码不一致')

        btnEditUserInfo = tk.Button(FrameEditPswd, text='确认修改', command=RePswd, relief='groove', font=(u'幼圆', 14))
        btnEditUserInfo.place(relx=0.58, rely=0.8, relwidth=0.3, relheight=0.12)

    def addBook(self):
        '''图书上架界面'''
        style = Style()
        style.configure('bookDet.TLabel', relief='flat'
                        , font=(u'幼圆', 12), anchor='center'
                        , background='white', foreground='#4141CF')
        style.configure('TButton', relief='flat', font=(u'幼圆', 12), anchor='center')
        self.FrameNone = tk.LabelFrame(windows_Admin, text='上架', background='white')
        self.FrameNone.place(relx=0.13, rely=0, relheight=1, relwidth=1, )

        self.FrameAdd = tk.LabelFrame(self.FrameNone, background='white')
        self.FrameAdd.place(relx=0.145, rely=-0.01, relheight=1, relwidth=0.6, )

        def Back():
            self.FrameNone.destroy()

        self.btn_addB = Button(self.FrameAdd, text='返回', command=Back, style='TButton')
        self.btn_addB.place(relx=0.76, rely=0.88, relwidth=0.12, relheight=0.08)

        self.btn_readd = Button(self.FrameAdd, text='确定上架', style='TButton', command=self.event_addBook)
        self.btn_readd.place(relx=0.5, rely=0.88, relwidth=0.24, relheight=0.08)

        # 图标
        P_det = tk.Canvas(self.FrameAdd, bg='#FFFFFF')
        self.im_det = ImageTk.PhotoImage(Image.open(r'ico\det2.png'))
        P_det.create_image(0.4, 8, anchor='nw', image=self.im_det)
        P_det.place(relx=0.02, rely=-0.0, relwidth=0.16, relheight=0.18)

        self.BookDetInfo = cur.fetchall()
        self.Text_listup = ['Text_name' + str(i) for i in range(7)]
        Lab_list = ['lab_name' + str(i) for i in range(7)]
        Lab_name = ['书名', '作者', '价格', '出版社', 'ISBN', '简介', '库存']

        for i in range(7):
            # 文本框，标签和分割线
            self.Text_listup[i] = tk.Text(self.FrameAdd
                                          , font=(14), relief='solid')
            Lab_list[i] = Label(self.FrameAdd, text=Lab_name[i], style='bookDet.TLabel')

        self.Text_listup[0].place(relx=0.37, rely=0.082, relwidth=0.5, relheight=0.06)
        self.Text_listup[1].place(relx=0.18, rely=0.24, relwidth=0.7, relheight=0.06)
        self.Text_listup[2].place(relx=0.18, rely=0.42, relwidth=0.25, relheight=0.06)
        self.Text_listup[3].place(relx=0.18, rely=0.33, relwidth=0.7, relheight=0.06)
        self.Text_listup[4].place(relx=0.55, rely=0.42, relwidth=0.33, relheight=0.06)
        self.Text_listup[5].place(relx=0.18, rely=0.5, relwidth=0.7, relheight=0.35)
        self.Text_listup[6].place(relx=0.18, rely=0.88, relwidth=0.18, relheight=0.06)

        Lab_list[0].place(relx=0.25, rely=0.08, relwidth=0.1, relheight=0.06)
        Lab_list[1].place(relx=0.06, rely=0.24, relwidth=0.1, relheight=0.06)
        Lab_list[2].place(relx=0.06, rely=0.42, relwidth=0.1, relheight=0.06)
        Lab_list[3].place(relx=0.04, rely=0.33, relwidth=0.12, relheight=0.06)
        Lab_list[4].place(relx=0.45, rely=0.42, relwidth=0.1, relheight=0.06)
        Lab_list[5].place(relx=0.07, rely=0.5, relwidth=0.1, relheight=0.06)
        Lab_list[6].place(relx=0.07, rely=0.88, relwidth=0.1, relheight=0.06)

        style.configure('TSeparator')
        Line1 = Separator(self.FrameAdd, orient='horizontal', style='Line1.TSeparator')
        Line1.place(relx=0., rely=0.196, relwidth=1, relheight=0.006)

        S = Scrollbar(self.FrameAdd)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        S.config(command=self.Text_listup[5].yview)
        self.Text_listup[5].config(yscrollcommand=S.set)


class Application(Admin):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Admin中。
    def __init__(self, master=None):
        self.style = Style()
        # 设置列表的标题风格
        self.style.configure("Treeview.Heading", foreground='blue')
        self.style.configure("Treeview", font=12)

        cur = conn.cursor()
        cur.execute('select ISBN,Bname from book')
        self.BookInfo = cur.fetchall()
        self.bookpage = 0
        self.maxpage = len(self.BookInfo) / 8
        self.num = 0
        if self.maxpage < (len(self.BookInfo) / 8.0):
            self.num = len(self.BookInfo) % 8

        self.Cid = Cid

        Admin.__init__(self, master)

    # 主界面按钮对应的事件
    def b_book(self, event=None):
        '''书籍页面'''
        pass
        self.Page()

    def b_search(self, event=None):
        '''搜索界面'''
        pass
        self.Search()

    def b_statistics(self, event=None):
        '''统计界面'''
        pass
        self.Statistics()

    def b_order(self, event=None):
        '''
        显示用户的订单
        '''
        self.Order()

        cur.execute("select distinct Oid from orderinfo")
        self.OrderInfo = cur.fetchall()
        if self.OrderInfo:
            self.OrderBookInfos = []
            for j in self.OrderInfo:
                comm = "select Bname,Ocount,price from orderinfo where Oid = '%s'" % (str(j[0]))
                cur.execute(comm)
                self.OrderBookInfo = cur.fetchall()
                self.OrderBookInfos.append(self.OrderBookInfo)

            for i in range(len(self.OrderInfo)):
                root_node = self.libox_OrderInfo.insert('', 'end', text=[self.OrderInfo[i][0]], open=False)
                price = 0
                for j in range(len(self.OrderBookInfos[i])):
                    self.libox_OrderInfo.insert(root_node, 'end',
                                                v=[str(self.OrderBookInfos[i][j][0].encode('utf-8')).strip(),
                                                   self.OrderBookInfos[i][j][1], self.OrderBookInfos[i][j][2]])
                    price += int(self.OrderBookInfos[i][j][2])
                self.libox_OrderInfo.insert(root_node, 'end', v=['', '', '', price])

        else:
            self.libox_OrderInfo.insert('', 'end', text=['你还没有下过订单'])

    def checkOrder(self):
        '''查看订单详情，可以查看收货人的相关信息'''
        try:
            list_box_orderID = self.libox_OrderInfo.item(self.libox_OrderInfo.focus(), "text")
            comm = "select * from Orderdetail where oid = '%s'" % str(list_box_orderID)
            cur.execute(comm)
            info = cur.fetchall()
            info = info[0]
            s = "下单日期：%s\n姓名：%s\n住址：%s\n手机：%s\n邮编：%d" \
                % (str(info[1].encode('utf-8')), str(info[2].encode('utf-8'))
                   , str(info[3].encode('utf-8')), str(info[4].encode('utf-8')), info[5])
            showinfo("详情", s)  # 显示详情
        except:
            showwarning('提醒', '请选择要查看的订单')

    def b_admin(self, event=None):
        '''管理员界面'''
        self.Admin()

    # ^主界面的按钮对应的功能^

    def SearchToDet(self):
        '''
        从搜索结果打开书籍详情页
        :return:
        '''
        try:
            list_box_bookname = self.libox_bookInfo.item(self.libox_bookInfo.focus(), "values")[0]
            for i in self.BookInfo:
                if list_box_bookname == i[1]:
                    self.BookInfoISBN = i[0]
                    break
            self.Det()

        except:
            showwarning('提醒', '没有选择的项目')

    def event_search(self):
        '''
        完成搜索功能，支持模糊搜索，把搜索结果添加到treeview中
        :return:
        '''
        cur.execute('select ISBN,Bname,Bauth from book')
        self.BookInfo = cur.fetchall()
        self.libox_bookInfo.delete(*self.libox_bookInfo.get_children())
        if self.var.get() == u'书名':
            for i in range(len(self.BookInfo)):
                if self.textSearch.get("1.0") in self.BookInfo[i][1]:
                    self.libox_bookInfo.insert('', i, v=[self.BookInfo[i][1], self.BookInfo[i][2]])
        if self.var.get() == u'作者':
            for i in range(len(self.BookInfo)):
                if self.textSearch.get("1.0") in self.BookInfo[i][2]:
                    self.libox_bookInfo.insert('', i, v=[self.BookInfo[i][1], self.BookInfo[i][2]])

    def generate_orderInfo(self, Rid):
        '''生成相应插入订单表的命令。返回一个列表'''
        comms = []
        t = str(time.time())[0:-3]
        Oid = t[3:7] + time.strftime("%Y%m%d%H", time.localtime())[1:-2] + str(self.Cid) + t[7:10]
        date = time.strftime("%Y-%m-%d", time.localtime())
        for i in self.order_shopInfo:
            print i[0].encode('utf-8')
            print type(i[0].encode('utf-8'))
            cur.execute("select Bname from book where ISBN = '%s'" % (i[0].encode('utf-8')))
            Bname = cur.fetchall()
            Bname = Bname[0][0]
            comm = "insert into orderinfo values('%s',%d,%d,'%s','%s','%s',%d,%.2f)" % (Oid, self.Cid, Rid, date, Bname
                                                                                        , str(i[0].encode('utf-8')),
                                                                                        int(i[1]), float(i[2]))
            comm = comm.encode('utf-8')
            comms.append(comm)
        return comms

    # 管理员个人页面对应功能，检查输入信息的格式
    def event_editAdminInfo(self):
        '''
        编辑用户信息，将文本框设置为普通模式
        将按钮文本显示为确认
        '''
        self.entry_adminUser.configure(state='normal')
        self.entry_adminName.configure(state='normal')
        self.entry_adminEamil.configure(state='normal')
        self.btnEditUserInfo.configure(text='确认', command=self.event_confirm)

    def event_confirm(self):
        '''
        确认管理员修改信息,将模式设置为不可用
        读取文本框的数据，写回数据库，并提示完成修改
        '''
        # 把三个文本框的内容添加到adminInfo列表中
        self.adminInfo = []
        self.adminInfo.append(str(self.entry_adminUser.get().encode('utf-8')))
        self.adminInfo.append(self.entry_adminName.get())
        self.adminInfo.append(self.entry_adminEamil.get())
        # 判断信息填写格式
        self.justy_adminInfo()
        if self.adminInfoFlag:
            self.entry_adminUser.configure(state='readonly')
            self.entry_adminName.configure(state='readonly')
            self.entry_adminEamil.configure(state='readonly')

            self.btnEditUserInfo.configure(text='修改信息', command=self.event_editAdminInfo)
            comm = "update administrator set Auser='%s',Aname='%s',Aemail='%s'" % (
                self.adminInfo[0], self.adminInfo[1], self.adminInfo[2])
            comm = str(comm.encode('utf-8'))
            try:
                cur.execute(comm)
                conn.commit()
                showinfo('提示', '修改成功')
            except:
                showerror('糟糕', '修改失败')

    def justy_adminInfo(self):
        '''
        判断管理员填写信息是否正确
        :return:
        '''
        self.adminInfoFlag = True
        if not self.adminInfo[0].isalnum():
            showerror('错误', '账号只能由字母和数字组成')
            self.adminInfoFlag = False

        if '' == self.adminInfo[1]:
            showerror('错误', '名字不能为空')
            self.adminInfoFlag = False

        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.adminInfo[2]) == None:
            showerror('错误', 'Email格式错误')
            self.adminInfoFlag = False

    # ^管理员个人页面对应功能，检查输入信息的格式^

    # 详情页对应功能，修改价格，库存，书籍下架，验证价格输入的格式
    def justfy_price(self):
        # 修改价格时，价格格式的判断
        flag_price = True
        reg = r'[0-9]{1,}.[0-9]{2}'
        res = re.match(reg, str(self.Text_list[4].get().encode('utf-8')))
        if not res:
            showerror('错误', '价格格式错误')
            flag_price = False
        return flag_price

    def modifyPrice(self):
        '''修改价格功能，修改成功后更新购物车的总价格'''

        # 点击确认修改后，验证数据格式，提交到数据库，控件模式改变
        def modifyp():
            # step 1 验证数据正确性，价格不能<0.格式为 __.__
            if self.justfy_price():
                # 命令。更新书籍表的价格，记住，这里的书籍价格格式是__.__
                comm_updatebook = "update book set Bprice = '%s' where ISBN = '%s'" % (
                str(self.Text_list[4].get().encode('utf-8'))
                , str(self.Text_list[3].get().encode('utf-8')))
                ISBN = str(self.Text_list[3].get().encode('utf-8'))
                # 执行书籍表价格的更新命令。未提交
                cur.execute(comm_updatebook)
                # 如果购物车中有要修改价格的书，则获取购物车中的书籍数量，返回的是一个列表
                comm_selectshop = "select distinct Ocount from shopping where ISBN = '%s'" % (
                str(self.Text_list[3].get().encode('utf-8')))
                cur.execute(comm_selectshop)
                Ocount = cur.fetchall()
                for i in Ocount:  # i[0]是一个int类型数据
                    # 计算得到总价
                    price = i[0] * float(self.Text_list[4].get().encode('utf-8').strip('元'))  # 总价price是一个float类型的数据
                    # 命令。更新购物车的价格
                    comm_updateShop = "update shopping set price = %.2f where ISBN = '%s' and Ocount = %d" % (
                    price, ISBN, i[0])
                    cur.execute(comm_updateShop)
                try:
                    conn.commit()
                    showinfo('提示', '修改成功')
                    self.Text_list[4].configure(state='readonly')
                    self.btn_EditPrice.configure(text='修改价格', command=self.modifyPrice)
                except:
                    showerror('糟糕', '修改失败')

        # 正式部分，将文本框模式改为可用，修改按钮文字和绑定的事件
        self.Text_list[4].configure(state='normal')
        self.btn_EditPrice.configure(text='确认修改', command=modifyp)

    def modifyStock(self):
        '''修改库存'''

        # 定义事件
        # 点击确认修改后，验证数据格式，提交到数据库，控件模式改变
        def modifys():
            # step 1 验证数据格式，只能为整数且不能<0,使用isdigit()函数其实杜绝了输入小于0的情况，因为不能输入负号233
            if str(self.Text_list[5].get().encode('utf-8')).isdigit():
                # step 2 提交修改到数据库
                ISBN = self.Text_list[3].get()
                comm = "update book set Bstock = %d where ISBN = '%s'" % (int(self.Text_list[5].get()), ISBN)
                comm = comm.encode('utf-8')
                try:
                    cur.execute(comm)
                    conn.commit()
                    showinfo('提示', '修改成功')
                    self.Text_list[5].configure(state='readonly')
                    self.btn_EditStock.configure(text='修改库存', command=self.modifyStock)
                except:
                    showerror('糟糕', '无法修改')
            else:
                showwarning('提醒', '库存只能为整数&不能小于 0 ')

        # 正式部分。修改文本框为可用。修改按钮文字和绑定的事件
        self.Text_list[5].configure(state='normal')
        self.btn_EditStock.configure(text='确认修改', command=modifys)

    def removeBook(self):
        '''书籍下架功能'''
        # 对下架操作进行确认
        if 'yes' == askquestion('提醒', '确定下架%s?' % self.Text_list[0].get().encode('utf-8')):

            # 获取详细页书籍的ISBN
            comm = "delete from book where ISBN = '%s'" % self.Text_list[3].get()
            try:
                cur.execute(comm)
                conn.commit()
                showinfo('提示', '下架成功')
            except:
                showerror('糟糕', '下架失败')
        else:
            showinfo('提示', '你取消了操作')

    # ^详情页对应功能，修改价格，库存，书籍下架，验证价格输入的格式^

    # 书籍上架页面对应功能，检查输入信息的格式,添加书籍
    def justfyBookInfo(self):
        '''检测上架书籍信息的格式'''
        flag_book = True
        if '' == self.Text_listup[0].get("0.0", "end").encode('utf-8').strip():
            showerror('错误', '书名不能为空')
            flag_book = False
        if '' == self.Text_listup[1].get("0.0", "end").encode('utf-8').strip():
            showerror('错误', '作者不能为空')
            flag_book = False
        # 价格
        reg = r'[0-9]{1,}.\d{2}元'
        res = re.match(reg, str(self.Text_listup[2].get("0.0", "end").encode('utf-8').strip()))
        if not res:
            showerror('错误', '价格格式错误')
            flag_book = False
        if '' == self.Text_listup[3].get("0.0", "end").encode('utf-8').strip():
            showerror('错误', '出版社不能为空')
            flag_book = False
        # ISBN
        if not str(self.Text_listup[4].get("0.0", "end").encode('utf-8').strip()).isdigit() or len(
                str(self.Text_listup[4].get("0.0", "end").encode('utf-8').strip())) != 13:
            showerror('错误', 'ISBN格式有误')
            flag_book = False
        if '' == self.Text_listup[5].get("0.0", "end").encode('utf-8').strip():
            showerror('错误', '简介不能为空')
            flag_book = False
        # 库存
        if not str(self.Text_listup[6].get("0.0", "end").encode('utf-8').strip()).isdigit():
            showerror('错误', '库存只能为整数')
            flag_book = False
        return flag_book

    def event_addBook(self):
        '''书籍上架'''
        newBookInfo = []
        # ['0书名', '1作者', '2价格', '3出版社', '4ISBN', '5简介', '6库存']
        # [ 'ISBN','书名', '作者', '价格', '出版社', '简介', '库存']
        if self.justfyBookInfo():
            for i in range(7):
                newBookInfo.append(self.Text_listup[i].get("0.0", "end").encode('utf-8').strip())

            comm = "insert into book values ('%s','%s','%s','%s','%s','%s',%d)" % (newBookInfo[4], newBookInfo[0]
                                                                                   , newBookInfo[1], newBookInfo[2],
                                                                                   newBookInfo[3], newBookInfo[5],
                                                                                   int(newBookInfo[6]))
            try:
                cur.execute(comm)
                conn.commit()
                showinfo('提示', '上架成功')
            except:
                showerror('糟糕', '上架失败')

    # ^书籍上架页面对应功能，检查输入信息的格式,添加书籍%^

    # 统计界面按钮对应的功能
    def xy(self):
        CountDate = [0 for i in range(31)]
        PriceDate = [0.0 for i in range(31)]

        cur.execute('select * from StaticInfo')
        info = cur.fetchall()
        date = [i[0].encode('utf-8').replace('-', '') for i in info]
        for i in range(len(date)):
            CountDate[int(date[i][-2:]) - 1] = info[i][1] + CountDate[int(date[i][-2:]) - 1]
            PriceDate[int(date[i][-2:]) - 1] = info[i][2] + PriceDate[int(date[i][-2:]) - 1]
        x = [i for i in range(1, 32)]
        d = str(date[0][0:4]) + '-' + str(date[0][4:6])
        return x, CountDate, PriceDate, d

    def drawDayPlot(self, xData, yData, d):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # 柱状图

        ax.bar(xData, yData, facecolor='#9999ff', edgecolor='white', align='center')

        # 显示数字
        for x, y in zip(xData, yData):
            ax.text(x, y, y, ha='center', va='bottom')

        xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
        ax.xaxis.set_major_locator(xmajorLocator)
        # ax.yaxis.set_major_locator(xmajorLocator)
        plt.xlim(0.5, 31.5)

        # 设置坐标轴信息
        plt.xtext = plt.xlabel(u'%s' % d)
        plt.ytext = plt.ylabel(u'Sales')

        # 出现网格
        plt.grid(True)

        plt.show()

    def stastic_dateS(self):
        # 按日期统计销量
        '''先获取要统计哪一月的情况 如果数据库没有信息的或，提示，否则显示统计结果。
            统计包括销量和销售额
        '''
        pass
        reg = r'[0-9]{2}'
        res = re.match(reg, str(self.entry_date.get().encode('utf-8')))
        if res:
            date_get = int(self.entry_date.get().encode('utf-8'))
            if date_get <= 12 and date_get > 0:
                date_get = self.entry_date.get().encode('utf-8')
                cur.execute('select Odate,Ocount,price from orderinfo')
                infos = cur.fetchall()
                date = [i[0].encode('utf-8').replace('-', '') for i in infos]
                info = []
                for i in infos:
                    if date_get in date[0][4:6]:
                        info.append(i)
                if info:
                    x, yc, yp, d = self.xy()
                    self.drawDayPlot(x, yc, d)
                else:
                    showinfo('提示', '该月份无销售')
            else:
                showwarning('警告', '输入正确的月份')
        else:
            showwarning('警告', '输入两位数的月份,如:01')

    def stastic_dateP(self):
        # 按日期统计销售额
        '''先获取要统计哪一月的情况 如果数据库没有信息的或，提示，否则显示统计结果。
            统计包括销量和销售额
        '''
        pass
        reg = r'[0-9]{2}'
        res = re.match(reg, str(self.entry_date.get().encode('utf-8')))
        if res:
            date_get = int(self.entry_date.get().encode('utf-8'))
            if date_get <= 12 and date_get > 0:
                date_get = self.entry_date.get().encode('utf-8')
                cur.execute('select Odate from orderinfo')
                infos = cur.fetchall()
                date = [i[0].encode('utf-8').replace('-', '') for i in infos]
                info = []
                for i in infos:
                    if date_get in date[0][4:6]:
                        info.append(i)
                if info:
                    x, yc, yp, d = self.xy()
                    self.drawDayPlot(x, yp, d)
                else:
                    showinfo('提示', '该月份无销售')
            else:
                showwarning('警告', '输入正确的月份')
        else:
            showwarning('警告', '输入两位数的月份,如:01')

    def mothxy(self):
        CountDate = [0 for i in range(12)]
        PriceDate = [0.0 for i in range(12)]
        cur.execute('select * from StaticInfo')
        info = cur.fetchall()
        date = [i[0].encode('utf-8').replace('-', '') for i in info]
        for i in range(len(date)):
            CountDate[int(date[i][4:6]) - 1] = info[i][1] + CountDate[int(date[i][4:6]) - 1]
            PriceDate[int(date[i][4:6]) - 1] = info[i][2] + PriceDate[int(date[i][4:6]) - 1]
        x = [i for i in range(1, 13)]
        d = str(date[0][0:4])
        return x, CountDate, PriceDate, d

    def drawMothPlot(self, xData, yData, d):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # 柱状图

        ax.bar(xData, yData, facecolor='#9999ff', edgecolor='white', align='center')

        # 显示数字
        for x, y in zip(xData, yData):
            ax.text(x, y, y, ha='center', va='bottom')

        xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
        ax.xaxis.set_major_locator(xmajorLocator)
        # ax.yaxis.set_major_locator(xmajorLocator)
        plt.xlim(0.5, 12.5)

        # 设置坐标轴信息
        plt.xtext = plt.xlabel(u'%s' % d)
        plt.ytext = plt.ylabel(u'Sales')

        # 出现网格
        plt.grid(True)

        plt.show()

    def stastic_mothS(self):
        # 按月份统计销量
        reg = r'[0-9]{4}'
        res = re.match(reg, str(self.entry_moth.get().encode('utf-8')))
        if res:
            date_get = int(self.entry_moth.get().encode('utf-8'))
            if date_get > 0:
                date_get = self.entry_moth.get().encode('utf-8')
                cur.execute('select Odate,Ocount,price from orderinfo')
                infos = cur.fetchall()
                date = [i[0].encode('utf-8').replace('-', '') for i in infos]
                info = []
                for i in infos:
                    if date_get in date[0][:4]:
                        info.append(i)
                if info:
                    x, yc, yp, d = self.mothxy()
                    self.drawMothPlot(x, yc, d)
                else:
                    showinfo('提示', '该年无销售')
            else:
                showwarning('警告', '输入正确的年份')
        else:
            showwarning('警告', '输入4位数的年份,如:2017')

    def stastic_mothP(self):
        # 按月份统计销售额
        reg = r'[0-9]{4}'
        res = re.match(reg, str(self.entry_moth.get().encode('utf-8')))
        if res:
            date_get = int(self.entry_moth.get().encode('utf-8'))
            if date_get > 0:
                date_get = self.entry_moth.get().encode('utf-8')
                cur.execute('select Odate from orderinfo')
                infos = cur.fetchall()
                date = [i[0].encode('utf-8').replace('-', '') for i in infos]
                info = []
                for i in infos:
                    if date_get in date[0][:4]:
                        info.append(i)
                if info:
                    x, yc, yp, d = self.mothxy()
                    self.drawMothPlot(x, yp, d)
                else:
                    showinfo('提示', '该年无销售')
            else:
                showwarning('警告', '输入正确的年份')
        else:
            showwarning('警告', '输入4位数的年份,如:2017')

    # 年
    def yearxy(self):

        CountDate = [0 for i in range(10)]
        PriceDate = [0.0 for i in range(10)]

        cur.execute('select * from StaticInfo')
        info = cur.fetchall()
        date = [i[0].encode('utf-8').replace('-', '') for i in info]
        x = [i for i in range(int(date[-1][:4]) - 9, int(date[-1][:4]) + 1)]
        for i in range(len(date)):
            CountDate[x.index(int(info[i][0][:4]))] += info[i][1]
            PriceDate[x.index(int(info[i][0][:4]))] += info[i][2]

        d = str(int(date[-1][:4]) - 9)
        return x, CountDate, PriceDate, d

    def drawYearPlot(self, xData, yData, d):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # 柱状图

        ax.bar(xData, yData, facecolor='#9999ff', edgecolor='white', align='center')

        # 显示数字
        for x, y in zip(xData, yData):
            ax.text(x, y, y, ha='center', va='bottom')

        xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为1的倍数
        ax.xaxis.set_major_locator(xmajorLocator)
        # ax.yaxis.set_major_locator(xmajorLocator)
        plt.xlim(int(d) - 0.5, int(d) + 9.5)

        # 设置坐标轴信息
        plt.xtext = plt.xlabel(u'%s To Now' % d)
        plt.ytext = plt.ylabel(u'Sales')

        # 出现网格
        plt.grid(True)

        plt.show()

    def stastic_yearS(self):
        # 按年统计销量
        try:
            x, yc, yp, d = self.yearxy()
            self.drawYearPlot(x, yc, d)
        except:
            showinfo('提示', '十年无销售')

    def stastic_yearP(self):
        # 按年统计销售额
        try:
            x, yc, yp, d = self.yearxy()
            self.drawYearPlot(x, yp, d)
        except:
            showinfo('提示', '十年无销售')


windows_Admin = tk.Tk()
Application(windows_Admin)
cur.close()
conn.close()


