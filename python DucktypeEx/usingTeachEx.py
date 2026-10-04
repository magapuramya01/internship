class Teacher:
    def teach(self):
        print("Teacher is teaching")


class YouTubeInstructor:
    def teach(self):
        print("YouTube instructor is teaching")


def start_teaching(obj):
    obj.teach()


start_teaching(Teacher())
start_teaching(YouTubeInstructor())