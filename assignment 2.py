def report_format(function):
    def wrapper(self):
        print("="*40)
        print("         Report Generator")
        print("="*40)
        
        function(self)
        
        print("="*40)
        print("          End Of Report")
        print("="*40)
    return wrapper

class Report:
    def __init__(self,title,section):
        self.title = title
        self.section = section
        
    @classmethod
    def sample_report(cls):
        title = "Student Performance Report"
        section = [
            "Name: Sai",
            "Roll no:46",
            "Python : A+",
            "MFC : FR",
            "Attendance : 10"
        ]
        return cls(title,section)
    
    @report_format
    def display(self):
        
        print("Title :",self.title)
        print()
        
        for item in self.section:
            print(item)
            
    def __str__(self):
        return f"Report Title:{self.title}"
    def __len__(self):
        return len(self.section)
    
report= Report.sample_report()
print(report)
print("Total section:",len(report))

report.display()
        
    
        
    
    
