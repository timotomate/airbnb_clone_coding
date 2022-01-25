from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    help = 'YOU ARE FUCKED UP'

    def add_arguments(self, parser): #명령어 뒤에 변수 뭐 추가할꺼임
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )
    
    def handle(self, *args, **options): #실제 명령어가 뭐 수행하는지
        times = options.get("times")
        for t in range(0, int(times)):
            print("i love you")