from django.contrib import admin
from .models import Player , Level , TotalLevel


class PlayerAdmin(admin.ModelAdmin):

	list_display = (
		u'id',
		'user',
		'player_name',
		'current_level',
		'score',
		'rank',
		'timestamp',
		)


class LevelAdmin(admin.ModelAdmin):

	list_display = (
			u'id',
			'level_number',
			'question_body',
			'number_of_user',
		)

class TotalLevelAdmin(admin.ModelAdmin):

	list_display = (
		u'id',
		'total_level',
		)


admin.site.register(Player,PlayerAdmin)
admin.site.register(Level,LevelAdmin)
admin.site.register(TotalLevel,TotalLevelAdmin)

