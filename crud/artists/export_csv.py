from .models import *
from django.http import HttpResponse

def export_csv(modeladmin, request, queryset):
    import csv
    import simplejson as json
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=artist_musics.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Title"),
        smart_str(u"Duration"),
        smart_str(u"Spotify Published"),
        smart_str(u"Youtube Published"),
        smart_str(u"Artist"),
    ])
    for obj in queryset:
        dic_obj = Music.getMusicsOfArtist(obj.name)
        for i, item in enumerate(dic_obj):
            json_str = json.dumps(dic_obj[i], use_decimal=True)
            json_obj = json.loads(json_str)
            writer.writerow([
                smart_str(json_obj.get("id")),
                smart_str(json_obj.get("title")),
                smart_str(json_obj.get("duration")),
                smart_str(json_obj.get("spotify_published")),
                smart_str(json_obj.get("youtube_published")),
                smart_str(obj.name),
            ])
    return response