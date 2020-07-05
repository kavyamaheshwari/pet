from django.contrib import admin
from .models import User
from .models import Pet
from .models import Pet_type
from .models import Breed
from .models import Que
from .models import Answer
from .models import Feedback
from .models import Contact

# Register your models here.
admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Pet_type)
admin.site.register(Breed)
admin.site.register(Que)
admin.site.register(Answer)
admin.site.register(Feedback)
admin.site.register(Contact)
