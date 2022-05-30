from tea_app.models import Teas, Colors
if Colors.objects.get(name='Green').color_id==1:
    print("Database already initialized")
else:
    c= Colors(name='Green')
    c.save()
    c= Colors(name='Black')
    c.save()
    c= Colors(name='Red')
    c.save()
    t=Teas(name='Green Tea',description='Test text',countries='China')
    t.color=Colors.objects.get(name='Green')
    t.save()
    t=Teas(name='Black Tea',description='',countries='India')
    t.color=Colors.objects.get(name='Black')
    t.save()
    print("Database initialized")


