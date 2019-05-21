import datetime
import webbrowser

class Handover():
    
    def __init__(self):
        self.date = datetime.datetime.now()
        self.nowDate = self.date.date()
        self.nowTime = self.date
        self.startDate = self.nowDate
        self.endDate = str(self.nowDate)
        print(self.nowTime.weekday())
        if 0 <= self.nowTime.weekday() < 4: 
            if self.nowTime >= morningStart and self.nowTime < afternoonStart:
                self.startTime = "05:40:00"
                self.endTime = "13:40:00"
            elif self.nowTime >= afternoonStart and self.nowTime < nightStart2:
                self.startTime = "13:40:00"
                self.endTime = "21:40:00"
            elif self.nowTime >= nightStart1 and self.nowTime < morningStart:
                self.startTime = "21:40:00"
                self.endTime = "05:40:00"
                self.startDate = str(self.startDate.replace(day = self.startDate.day - 1))
        elif 5 <= self.nowTime.weekday() <= 6 or self.nowTime.weekday() == 0:
            if self.nowTime >= weekendkDay and self.nowTime < weekendNight2:
                self.startTime = "5:40:00"
                self.endTime = "17:40:00"
            if self.nowTime >= weekendNight1 and self.nowTime < weekendDay:
                self.startTime = "17:40:00"
                self.endTime = "05:40:00"
                self.startDate = str(self.startDate.replace(day = self.startDate.day - 1))
                
        self.url = "https://arcelormittalprod.service-now.com/incident_list.do?sysparm_query=sys_created_onBETWEENjavascript:gs.dateGenerate(%27" + str(self.startDate) + "%27%2C%27" + str(self.startTime) + "%27)@javascript:gs.dateGenerate(%27" + str(self.endDate) + "%27%2C%27" + str(self.endTime) + "%27)%5Ecaller_id%3D9b2b60930f037d0041dd715ce1050eff%5EORcaller_id%3D1524d7d3db777e885fdd728dae9619e8%5EORcaller_id%3Dddd88436db78aa405fdd328dae9619ce%5EORcaller_id%3D5a637ddedbd96384e3e649ee3b9619c4%5EORcaller_id%3D142c1d00dbcfd7887cca83305b9619b1%5EORcaller_id%3D40daa83d0f9a310041dd715ce1050e31%5EORcaller_id%3D52a2e2040f6b394041dd715ce1050e34%5EORcaller_id%3D36925ec4db5bfe8cb2147ecaae96190f%5EORcaller_id%3D8eebf1fc0f4e31008e97bd5ce1050ee9%5EORcaller_id%3D9d5de9e5930022005bc5f179077ffb07%5Eu_requested_for%3D9b2b60930f037d0041dd715ce1050eff%5EORu_requested_for%3D1524d7d3db777e885fdd728dae9619e8%5EORu_requested_for%3D5a637ddedbd96384e3e649ee3b9619c4%5EORu_requested_for%3Dddd88436db78aa405fdd328dae9619ce%5EORu_requested_for%3D142c1d00dbcfd7887cca83305b9619b1%5EORu_requested_for%3D40daa83d0f9a310041dd715ce1050e31%5EORu_requested_for%3D52a2e2040f6b394041dd715ce1050e34%5EORu_requested_for%3D36925ec4db5bfe8cb2147ecaae96190f%5EORu_requested_for%3D8eebf1fc0f4e31008e97bd5ce1050ee9&sysparm_first_row=1&sysparm_view=ess"
        webbrowser.open(self.url)
        
        
time = datetime.datetime.now()
morningStart = time.replace(hour = 6, minute = 10, second = 0, microsecond = 0)
afternoonStart = time.replace(hour = 14, minute = 10, second = 0, microsecond = 0)
nightStart1 = time.replace(day = (time.day - 1), hour = 22, minute = 10, second = 0, microsecond = 0)
nightStart2 = time.replace(day = time.day , hour = 22, minute = 10, second = 0, microsecond = 0)
weekendDay = morningStart
weekendNight1 =  time.replace(day = (time.day - 1), hour = 18, minute = 10, second = 0, microsecond = 0)
weekendNight2 =  time.replace(day = time.day, hour = 18, minute = 10, second = 0, microsecond = 0)


if __name__ == "__main__":
    Handover()
