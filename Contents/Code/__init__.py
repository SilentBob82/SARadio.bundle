ART_JAC = 'radio.jpg'
ICON_JAC = 'radio_icon.jpg'
ICON_JACARANDA = 'jac_logo.jpg'
ICON_5FM = '5FM_logo.jpg'
ICON_702 = '702_logo.jpg'
ICON_RSG = 'RSG_logo.jpg'
NAME = 'South African Radio'
NAME_JAC = 'Jacaranda 94.2 FM'
NAME_5FM = '5FM'
NAME_702 = '702 Talk Radio'
NAME_RSG = 'RSG'
STREAM_URL_JAC = 'https://edge.iono.fm/xice/jacarandafm_live_medium.aac'
STREAM_URL_5FM = 'http://capeant.antfarm.co.za:8000/5fm'
STREAM_URL_702 = 'http://19523.live.streamtheworld.com:80/FM702_SC'
STREAM_URL_RSG = 'http://capeant.antfarm.co.za:8000/RSG'
####################################################################################################
def Start():

	ObjectContainer.art = R(ART_JAC)
	ObjectContainer.title1 = NAME_JAC
	TrackObject.thumb = R(ICON_JAC)

####################################################################################################     
@handler('/music/BayFM999', NAME, thumb=ICON_JAC, art=ART_JAC)
def MainMenu():

	oc = ObjectContainer()
	oc.add(CreateTrackObject(url=STREAM_URL_JAC, title=NAME_JAC , iconc=ICON_JACARANDA))
	oc.add(CreateTrackObject(url=STREAM_URL_5FM, title=NAME_5FM , iconc=ICON_5FM))
	oc.add(CreateTrackObject(url=STREAM_URL_702, title=NAME_702 , iconc=ICON_702))
	oc.add(CreateTrackObject(url=STREAM_URL_RSG, title=NAME_RSG , iconc=ICON_RSG))
	return oc

####################################################################################################
def CreateTrackObject(url, title, iconc, include_container=False):

	track_object = TrackObject(
		key = Callback(CreateTrackObject, url=url, title=title, include_container=True),
		rating_key = url,
		title = title,
	        thumb = R(iconc),
		items = [
			MediaObject(
				parts = [
					PartObject(key=Callback(PlayAudio, url=url, ext='mp3'))
				],
				container = Container.MP3,
				bitrate = 40,
				audio_codec = AudioCodec.MP3,
				audio_channels = 2
			)
		]
	)

	if include_container:
		return ObjectContainer(objects=[track_object])
	else:
		return track_object

####################################################################################################
def PlayAudio(url):

	return Redirect(url)
