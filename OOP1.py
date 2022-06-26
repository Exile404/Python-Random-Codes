class YouTube:
    def __init__(self,ch_name,creator,videos_list,videos_count,subscriber_Count):
        self.ch_name=ch_name
        self.creator=creator
        self.videos_list=videos_list
        self.videos_count=videos_count
        self.subscriber_Count=subscriber_Count
        self.playlist=[]
    def add_video(self,lst):
        self.videos_list.append(lst)
        self.videos_count+=1
    def subscribe(self,n=None):
        if n==None:
            self.subscriber_Count+=1
        else:
            self.subscriber_Count+=n
    def unsubscribe(self):
        if self.subscriber_Count>0:
            self.subscriber_Count-=1
    def search(self,x):
        l=self.videos_list
        for i in range(len(l)):
            l[i]=l[i].lower()
        x=x.lower()

        if x in l:
            print("Video Found. Want it play?")
        else:
            print("Video not found. Try something else....")
    def details(self):
        print(f'Channel Name: {self.ch_name}')
        print(f"Creator: {self.creator}")
        print(f'videos count: {self.videos_count}')
        print(f'Videos List: ')
        for i in self.videos_list:
            print(i,end=" ")
        print()
        print(f'Subscriber: {self.subscriber_Count}')
        if len(self.playlist)!=0:
            print("PlayList")
            for i in self.playlist:

                print(i,end=" ")
    def add_to_playlist(self,video):
        self.playlist.append(video)

ch1=YouTube("Clever Programmer",'Quazi',['Python Bootcamp','Javascript Crash Course','Django Crash course'],3,50)
# ch1.details()
ch1.add_video("React JS")
# ch1.details()
# ch1.subscribe(50)
# ch1.unsubscribe()
# ch1.details()
# ch1.search("ReAcT jS")
# ch1.add_to_playlist("Python Bootcamp")
# ch1.details()
ch2=YouTube("Programmers Hive","Dhrubo",["C++ Bootcamp"],1,52)
# ch2.details()
print(ch1.creator)