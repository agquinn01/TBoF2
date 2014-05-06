import os, datetime
import requests
from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template
import operator

app = Flask(__name__)   # create our flask app



dossierItems = {}

dossierItems['00'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'00', 'title':'?', 'route':'/itemblank', 'chapter':'1'}
dossierItems['01'] = {'image':'static/img/dossier/Toki_vid.png', 'index':'01','title':'TOKI_VID', 'route':'/item01', 'chapter':'1', 'video':'http://vimeo.com/93462324', 'related':['02','03','05','06','16','25','27','37','45']}
dossierItems['02'] = {'image':'static/img/dossier2/dossier02.jpg', 'index':'02','title':'STEVEN', 'route':'/item02', 'chapter':'1', 'related':['03']}
dossierItems['03'] = {'image':'static/img/dossier2/dossier03.jpg', 'index':'03','title':'FRANK', 'route':'/item03', 'chapter':'1', 'related':['01','02','03','04','10']}
dossierItems['04'] = {'image':'static/img/dossier2/dossier04.jpg', 'index':'04','title':'MATILDA', 'route':'/item04', 'chapter':'1', 'related':['01','02','03','07','08','15','19','23']}
dossierItems['05'] = {'image':'static/img/dossier2/dossier05.jpg', 'index':'05','title':'CALICO', 'route':'/item05', 'chapter':'1', 'related':['01','02','06','16','37','45','55','56']}
dossierItems['06'] = {'image':'static/img/dossier2/dossier06.jpg', 'index':'06','title':'CALICO SITES', 'route':'/item06', 'chapter':'1', 'related':['01','02','05','16','37','45','55','56']}
dossierItems['07'] = {'image':'static/img/dossier2/dossier07.jpg', 'index':'07','title':'DARK NETWORK', 'route':'/item07', 'chapter':'1', 'related':['04','08','15']}
dossierItems['08'] = {'image':'static/img/dossier2/dossier08.jpg', 'index':'08','title':'BLACK PHONE', 'route':'/item08', 'chapter':'1', 'related':['04','07','15']}

dossierItems['09'] = {'image':'static/img/dossier2/dossier09.jpg', 'index':'09','title':'BAZAAR', 'route':'/item09', 'chapter':'2', 'related':['03']}
dossierItems['10'] = {'image':'static/img/dossier2/dossier10.jpg', 'index':'10','title':'PERSUASIVE MEMORY', 'route':'/item10', 'chapter':'2', 'related':['03']}
dossierItems['11'] = {'image':'static/img/dossier2/dossier11.jpg', 'index':'11','title':'DDOS', 'route':'/item11', 'chapter':'2', 'related':['03']}
# dossierItems['00'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'00', 'title':'?', 'route':'/itemblank', 'chapter':'1'}
# dossierItems['01'] = {'image':'static/img/dossier/Dossier01.jpg', 'index':'01','title':'STEVEN', 'route':'/item1', 'chapter':'1'}
# dossierItems['02'] = {'image':'static/img/dossier/Dossier012.jpg', 'index':'02','title':'FRANK', 'route':'/item2', 'chapter':'1'}
# dossierItems['03'] = {'image':'static/img/dossier/Dossier013.jpg', 'index':'03','title':'TOKI', 'route':'/item3', 'chapter':'1'}
# dossierItems['03.1'] = {'image':'static/img/dossier/Toki_vid.png', 'index':'03.1','title':'TOKI_VID', 'route':'/item3_1', 'chapter':'1', 'video':'http://vimeo.com/93462324'}
# dossierItems['04'] = {'image':'static/img/dossier/Dossier014.jpg', 'index':'04','title':'PILOT DETAIL', 'route':'/item4', 'chapter':'1'}
# dossierItems['05'] = {'image':'static/img/dossier/Dossier015.jpg', 'index':'05','title':'PILOT HISTORY', 'route':'/item5', 'chapter':'2'}
# dossierItems['06'] = {'image':'static/img/dossier/Dossier016.jpg', 'index':'06','title':'FOX', 'route':'/item6', 'chapter':'2'}
# dossierItems['07'] = {'image':'static/img/dossier/Dossier017.jpg', 'index':'07','title':'SNAKE AND MOLE', 'route':'/item7', 'chapter':'2'}
# dossierItems['08'] = {'image':'static/img/dossier/Dossier018.jpg', 'index':'08','title':'BEE AND OWL', 'route':'/item8', 'chapter':'2'}
# dossierItems['09'] = {'image':'static/img/dossier/Dossier019.jpg', 'index':'09','title':'SALLY', 'route':'/item9', 'chapter':'2'}
# dossierItems['10'] = {'image':'static/img/dossier/Dossier0110.jpg', 'index':'10','title':'CALICO', 'route':'/item10', 'chapter':'2', 'related':['01','02','03','04','05','09','11']}
# dossierItems['11'] = {'image':'static/img/dossier/MedCityCalico.png', "index":"11",'title':'CALICO WEB 1', 'route':'/item11', 'chapter':'2'}




foundItems = {}

foundItems['01'] = {"value":False,"index":"01", 'chapter':'1'}
foundItems['02'] = {"value":False,"index":"02", 'chapter':'1'}
foundItems['03'] = {"value":False,"index":"03", 'chapter':'1'}
foundItems['04'] = {"value":False,"index":"04", 'chapter':'1'}
foundItems['05'] = {"value":False,"index":"05", 'chapter':'1'}
foundItems['06'] = {"value":False,"index":"06", 'chapter':'1'}
foundItems['07'] = {"value":False,"index":"07", 'chapter':'1'}
foundItems['08'] = {"value":False,"index":"08", 'chapter':'1'}
foundItems['09'] = {"value":False,"index":"09", 'chapter':'1'}
foundItems['10'] = {"value":False,"index":"10", 'chapter':'2'}
foundItems['11'] = {"value":False,"index":"11", 'chapter':'2'}

global myPage
myPage = '1'

#This is a model for how a route should work
# @app.route("/item1")
# def item1():
# 	foundItems['1'] = True
	
# 	templateData = {
# 		'currentItem' : dosseirItems['1']
# 	}
# 	# render the template, pass in the animals dictionary refer to it as 'animals'
# 	return render_template("item.html", **templateData)	
# #

@app.route("/bof1")
def text():

	newMark = ''
	# myPage = '11'
	global myPage
	prevPage = ''
	myCurrentPage = request.args.get('changepage', 'help')
	if myCurrentPage != 'help':
		myPage = myCurrentPage


	bookMark = request.args.get('q','query')
	# myCurrentPage = request.args.get('mycurrentpage','query')
	# if myCurrentPage != 'query':
	# 	myPage = myCurrentPage

	if bookMark != 'query':
		newMark = bookMark


	# nextPage = str(int(currentPage)+1)
	# if currentPage == "1":
	# 	prevPage = "1"
	# else:
	# 	prevPage = str(int(currentPage)-1)

	# query = request.args.get('q','#peanuts')



	templateData = {
	'title' : 'The Book of Frank',
	'page' : "1",
	# 'currentPage': currentPage,
	'newMark' : newMark,
	'bookMark': bookMark,
	'myPage' : myPage,
	# 'nextPage' : nextPage,
	# 'prevPage' : prevPage
	}
	return render_template("bof1_test.html", **templateData)

@app.route("/itemblank")
def itemblank():
	templateData = {
	'title' : dossierItems['00']['title'],
	'image' : dossierItems['00']['image']
	}
	return render_template("item.html", **templateData)

@app.route("/item01")
def item01():
	foundItems['01']['value'] = True
	dossierItems['01'] = {'image':'static/img/dossier/Toki_vid.png', 'index':'01','title':'TOKI_VID', 'route':'/item01', 'chapter':'1', 'video':'http://vimeo.com/93462324', 'related':['02','03','05','06','16','25','27','37','45']}
	templateData = {
	'title' : dossierItems['01']['title'],
	'image' : dossierItems['01']['image'],
	'video' : dossierItems['01']['video']
	}
	return render_template("video_item.html", **templateData)

@app.route("/item02")
def item02():
	foundItems['02']['value'] = True
	dossierItems['02'] = {'image':'static/img/dossier2/dossier02.jpg', 'index':'02','title':'STEVEN', 'route':'/item02', 'chapter':'1', 'related':['03']}
	templateData = {
	'title' : dossierItems['02']['title'],
	'image' : dossierItems['02']['image']
	}
	return render_template("item1.html", **templateData)

@app.route("/item03")
def item03():
	foundItems['03']['value'] = True
	dossierItems['03'] = {'image':'static/img/dossier2/dossier03.jpg', 'index':'03','title':'FRANK', 'route':'/item03', 'chapter':'1', 'related':['01','02','03','04','10']}
	templateData = {
	'title' : dossierItems['03']['title'],
	'image' : dossierItems['03']['image']
	}
	return render_template("item1.html", **templateData)


@app.route("/item04")
def item04():
	foundItems['04']['value'] = True
	dossierItems['04'] = {'image':'static/img/dossier2/dossier04.jpg', 'index':'04','title':'MATILDA', 'route':'/item04', 'chapter':'1', 'related':['01','02','03','07','08','15','19','23']}
	templateData = {
	'title' : dossierItems['04']['title'],
	'image' : dossierItems['04']['image']
	}
	return render_template("item1.html", **templateData)

@app.route("/item05")
def item05():
	foundItems['05']['value'] = True
	dossierItems['05'] = {'image':'static/img/dossier2/dossier05.jpg', 'index':'05','title':'CALICO', 'route':'/item05', 'chapter':'1', 'related':['01','02','06','16','37','45','55','56']}
	templateData = {
	'title' : dossierItems['05']['title'],
	'image' : dossierItems['05']['image']
	}
	return render_template("item1.html", **templateData)

@app.route("/item06")
def item06():
	foundItems['06']['value'] = True
	dossierItems['06'] = {'image':'static/img/dossier2/dossier06.jpg', 'index':'06','title':'CALICO SITES', 'route':'/item06', 'chapter':'1', 'related':['01','02','05','16','37','45','55','56']}
	templateData = {
	'title' : dossierItems['06']['title'],
	'image' : dossierItems['06']['image']
	}
	return render_template("item1.html", **templateData)

@app.route("/item07")
def item07():
	foundItems['07']['value'] = True
	dossierItems['07'] = {'image':'static/img/dossier2/dossier07.jpg', 'index':'07','title':'DARK NETWORK', 'route':'/item07', 'chapter':'1', 'related':['04','08','15']}
	templateData = {
	'title' : dossierItems['07']['title'],
	'image' : dossierItems['07']['image']
	}
	return render_template("item1.html", **templateData)

@app.route("/item08")
def item08():
	foundItems['08']['value'] = True
	dossierItems['08'] = {'image':'static/img/dossier2/dossier08.jpg', 'index':'08','title':'BLACK PHONE', 'route':'/item08', 'chapter':'1', 'related':['04','07','15']}
	templateData = {
	'title' : dossierItems['08']['title'],
	'image' : dossierItems['08']['image']
	}
	return render_template("item1.html", **templateData)

@app.route("/item09")
def item09():
	foundItems['09']['value'] = True
	dossierItems['09'] = {'image':'static/img/dossier2/dossier09.jpg', 'index':'09','title':'BAZAAR', 'route':'/item09', 'chapter':'2', 'related':['03']}
	templateData = {
	'title' : dossierItems['09']['title'],
	'image' : dossierItems['09']['image']
	}
	return render_template("item1.html", **templateData)

@app.route("/item10")
def item10():
	foundItems['10']['value'] = True
	dossierItems['10'] = {'image':'static/img/dossier2/dossier10.jpg', 'index':'10','title':'PERSUASIVE MEMORY', 'route':'/item10', 'chapter':'2', 'related':['03']}
	relatedItems = []

	for item in dossierItems['10']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems['10']['title'],
	'image' : dossierItems['10']['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item11")
def item11():
	foundItems['11']['value'] = True
	dossierItems['11'] = {'image':'static/img/dossier2/dossier11.jpg', 'index':'11','title':'DDOS', 'route':'/item11', 'chapter':'2', 'related':['03']}
	templateData = {
	'title' : dossierItems['11']['title'],
	'image' : dossierItems['11']['image']
	}
	return render_template("item1.html", **templateData)

@app.route("/clear")
def clear():
	dossierItems['01'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'01','title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['02'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'02','title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['03'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'03','title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['04'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'04','title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['05'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'05','title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['06'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'06','title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['07'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'07','title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['08'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'08','title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['09'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'09','title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['10'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'10','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['11'] = {'image':'static/img/dossier/Dossier_blank.jpg', "index":"11",'title':'?', 'route':'/itemblank', 'chapter':'2'}

	return render_template("clear.html")

@app.route("/showall")
def showall():
	foundItems['01'] = {"value":True,"index":"01", 'chapter':'1'}
	foundItems['02'] = {"value":True,"index":"02", 'chapter':'1'}
	foundItems['03'] = {"value":True,"index":"03", 'chapter':'1'}
	foundItems['04'] = {"value":True,"index":"04", 'chapter':'1'}
	foundItems['05'] = {"value":True,"index":"05", 'chapter':'1'}
	foundItems['06'] = {"value":True,"index":"06", 'chapter':'1'}
	foundItems['07'] = {"value":True,"index":"07", 'chapter':'1'}
	foundItems['08'] = {"value":True,"index":"08", 'chapter':'1'}
	foundItems['09'] = {"value":True,"index":"09", 'chapter':'1'}
	foundItems['10'] = {"value":True,"index":"10", 'chapter':'2'}
	foundItems['11'] = {"value":True,"index":"11", 'chapter':'2'}
	
	dossierItems['00'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'00', 'title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['01'] = {'image':'static/img/dossier/Toki_vid.png', 'index':'01','title':'TOKI_VID', 'route':'/item01', 'chapter':'1', 'video':'http://vimeo.com/93462324', 'related':['02','03','05','06','16','25','27','37','45']}
	dossierItems['02'] = {'image':'static/img/dossier2/dossier02.jpg', 'index':'02','title':'STEVEN', 'route':'/item02', 'chapter':'1', 'related':['03']}
	dossierItems['03'] = {'image':'static/img/dossier2/dossier03.jpg', 'index':'03','title':'FRANK', 'route':'/item03', 'chapter':'1', 'related':['01','02','03','04','10']}
	dossierItems['04'] = {'image':'static/img/dossier2/dossier04.jpg', 'index':'04','title':'MATILDA', 'route':'/item04', 'chapter':'1', 'related':['01','02','03','07','08','15','19','23']}
	dossierItems['05'] = {'image':'static/img/dossier2/dossier05.jpg', 'index':'05','title':'CALICO', 'route':'/item05', 'chapter':'1', 'related':['01','02','06','16','37','45','55','56']}
	dossierItems['06'] = {'image':'static/img/dossier2/dossier06.jpg', 'index':'06','title':'CALICO SITES', 'route':'/item06', 'chapter':'1', 'related':['01','02','05','16','37','45','55','56']}
	dossierItems['07'] = {'image':'static/img/dossier2/dossier07.jpg', 'index':'07','title':'DARK NETWORK', 'route':'/item07', 'chapter':'1', 'related':['04','08','15']}
	dossierItems['08'] = {'image':'static/img/dossier2/dossier08.jpg', 'index':'08','title':'BLACK PHONE', 'route':'/item08', 'chapter':'1', 'related':['04','07','15']}
	
	dossierItems['09'] = {'image':'static/img/dossier2/dossier09.jpg', 'index':'09','title':'BAZAAR', 'route':'/item09', 'chapter':'2', 'related':['03']}
	dossierItems['10'] = {'image':'static/img/dossier2/dossier10.jpg', 'index':'10','title':'PERSUASIVE MEMORY', 'route':'/item10', 'chapter':'2', 'related':['03']}
	dossierItems['11'] = {'image':'static/img/dossier2/dossier11.jpg', 'index':'11','title':'DDOS', 'route':'/item11', 'chapter':'2', 'related':['03']}
	
	return render_template("clear.html")


@app.route("/dc1")
def dc1():
	currentItems = []
	chapter1Items = []

	for k,v in foundItems.iteritems():
		if foundItems[k]['value'] and foundItems[k]['chapter'] == '1':
			chapter1Items.append(dossierItems[foundItems[k]['index']])

		elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '1':
			dossierItems[foundItems[k]['index']]['title'] = '?'
			dossierItems[foundItems[k]['index']]['image'] = 'static/img/dossier/Dossier_blank.jpg'
			dossierItems[foundItems[k]['index']]['route'] = '/itemblank'
			chapter1Items.append(dossierItems[foundItems[k]['index']])

		else:
			pass

	chapter1Items.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : 'These are the items found in Chapter 1',
	'chapter1Items' : chapter1Items,
	}

	return render_template("dc1.html", **templateData)	

@app.route("/dc2")
def dc2():
	currentItems = []
	chapter2Items = []
	chapter2Sorted = []

	for k,v in foundItems.iteritems():
		if foundItems[k]['value'] and foundItems[k]['chapter'] == '2':
			chapter2Items.append(dossierItems[foundItems[k]['index']])

		elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '2':
			dossierItems[foundItems[k]['index']]['title'] = '?'
			dossierItems[foundItems[k]['index']]['image'] = 'static/img/dossier/Dossier_blank.jpg'
			dossierItems[foundItems[k]['index']]['route'] = '/itemblank'
			chapter2Items.append(dossierItems[foundItems[k]['index']])

		else:
			pass

	chapter2Items.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : 'These are the items found in Chapter 2',
	'chapter2Items' : chapter2Items,
	'chapter2Sorted' : chapter2Sorted
	}

	return render_template("dc2.html", **templateData)	

@app.route("/list")
def list():


	# currentItems = []
	# chapter1Items = []
	# chapter2Items = []
	# chapter3Items = []
	# chapter4Items = []
	# chapter5Items = []
	# for k,v in foundItems.iteritems():
	# 	if foundItems[k]['value'] and foundItems[k]['chapter'] == '1':
	# 		chapter1Items.append(dossierItems[foundItems[k]['index']])

	# 	elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '1':
	# 		chapter1Items.append(dossierItems['0'])
		
	# 	elif foundItems[k]['value'] and foundItems[k]['chapter'] == '2':
	# 		chapter2Items.append(dossierItems[foundItems[k]['index']])

	# 	elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '2':
	# 		chapter2Items.append(dossierItems['0'])

	# 	else:
	# 		pass
	# 	# print foundItems

	templateData = {
	'myPage' : myPage,
	'title' : 'This is the list page'
	# 'chapter1Items' : chapter1Items,
	# 'chapter2Items' : chapter2Items
	}
	return render_template("dossier.html", **templateData)	


@app.route("/home")
def home():
	return render_template("home.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	