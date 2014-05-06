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

dossierItems['09'] = {'image':'static/img/dossier2/dossier09.jpg', 'index':'09','title':'BAZAAR', 'route':'/item09', 'chapter':'2', 'related':['10']}
dossierItems['10'] = {'image':'static/img/dossier2/dossier10.jpg', 'index':'10','title':'PERSUASIVE MEMORY', 'route':'/item10', 'chapter':'2', 'related':['09']}
dossierItems['11'] = {'image':'static/img/dossier2/dossier11.jpg', 'index':'11','title':'DDOS', 'route':'/item11', 'chapter':'2', 'related':['03']}
dossierItems['12'] = {'image':'static/img/dossier2/dossier12.jpg', 'index':'12','title':'FARADY BOX', 'route':'/item12', 'chapter':'2', 'related':['01','04','15']}
dossierItems['13'] = {'image':'static/img/dossier2/dossier13.jpg', 'index':'13','title':'TOR IRL', 'route':'/item13', 'chapter':'2', 'related':['04','15']}
dossierItems['14'] = {'image':'static/img/dossier2/dossier14.jpg', 'index':'14','title':'GUILTY', 'route':'/item14', 'chapter':'2', 'related':['15']}
dossierItems['15'] = {'image':'static/img/dossier2/dossier15.jpg', 'index':'15','title':'OMER', 'route':'/item15', 'chapter':'2', 'related':['04','07','08','12','13','14','17','19','23','25','27']}
dossierItems['16'] = {'image':'static/img/dossier2/dossier16.jpg', 'index':'16','title':'ABA', 'route':'/item16', 'chapter':'2', 'related':['01','05','06','37']}
dossierItems['17'] = {'image':'static/img/dossier2/dossier17.jpg', 'index':'17','title':'DEEP WEB', 'route':'/item17', 'chapter':'2', 'related':['15']}
dossierItems['18'] = {'image':'static/img/dossier2/dossier18.jpg', 'index':'18','title':'AUDITORS', 'route':'/item18', 'chapter':'2', 'related':['05']}
dossierItems['19'] = {'image':'static/img/dossier2/dossier19.jpg', 'index':'19','title':'UNSTABLE TECH', 'route':'/item19', 'chapter':'2', 'related':['04','15','23']}
dossierItems['20'] = {'image':'static/img/dossier2/dossier20.jpg', 'index':'20','title':'FACE TRACKING', 'route':'/item20', 'chapter':'2', 'related':['21','23']}
dossierItems['21'] = {'image':'static/img/dossier2/dossier21.jpg', 'index':'21','title':'EUCLID', 'route':'/item21', 'chapter':'2', 'related':['20','22']}
dossierItems['22'] = {'image':'static/img/dossier2/dossier22.jpg', 'index':'22','title':'BEHAVIOR TRACKING', 'route':'/item22', 'chapter':'2', 'related':['20','21']}
dossierItems['23'] = {'image':'static/img/dossier2/dossier23.jpg', 'index':'23','title':'THE BANK', 'route':'/item23', 'chapter':'2', 'related':['03','04','15','19']}
dossierItems['24'] = {'image':'static/img/dossier2/dossier24.jpg', 'index':'24','title':'DNA', 'route':'/item24', 'chapter':'2', 'related':['03','04','15','19']}
dossierItems['25'] = {'image':'static/img/dossier2/dossier25.jpg', 'index':'25','title':'MASK & COLLAR', 'route':'/item25', 'chapter':'2', 'related':['01','03','04','15','19','26','55']}
dossierItems['26'] = {'image':'static/img/dossier2/dossier26.jpg', 'index':'26','title':'WIRESHARK', 'route':'/item26', 'chapter':'2', 'related':['01','15','25','55']}
dossierItems['27'] = {'image':'static/img/dossier2/dossier27.jpg', 'index':'27','title':'BUNNY MEMORY', 'route':'/item27', 'chapter':'2', 'related':['01','15']}
dossierItems['28'] = {'image':'static/img/dossier2/dossier28.jpg', 'index':'28','title':'DUMB TECH', 'route':'/item28', 'chapter':'2', 'related':['04','15']}
dossierItems['29'] = {'image':'static/img/dossier2/dossier29.jpg', 'index':'29','title':'INTERVIEW', 'route':'/item29', 'chapter':'2', 'related':['30','47','58']}
dossierItems['30'] = {'image':'static/img/dossier2/dossier30.jpg', 'index':'30','title':'POLITICIAN', 'route':'/item30', 'chapter':'2', 'related':['29','47','58']}

dossierItems['31'] = {'image':'static/img/dossier2/dossier31.jpg', 'index':'31','title':"FRANK'S DREAMS", 'route':'/item31', 'chapter':'3', 'related':['02']}
dossierItems['32'] = {'image':'static/img/dossier2/dossier32.jpg', 'index':'32','title':'SHITTY CITY', 'route':'/item32', 'chapter':'3', 'related':['15','34','38']}
dossierItems['33'] = {'image':'static/img/dossier2/dossier33.jpg', 'index':'33','title':'ANTI-AGING', 'route':'/item33', 'chapter':'3', 'related':['05','06']}
dossierItems['34'] = {'image':'static/img/dossier2/dossier34.jpg', 'index':'34','title':'AL', 'route':'/item34', 'chapter':'3', 'related':['15','32','40','42','43','44','45']}
dossierItems['35'] = {'image':'static/img/dossier2/dossier35.jpg', 'index':'35','title':'RECORDS', 'route':'/item35', 'chapter':'3', 'related':['01','34','45']}
dossierItems['36'] = {'image':'static/img/dossier2/dossier36.jpg', 'index':'36','title':'MALFUNCTION', 'route':'/item36', 'chapter':'3', 'related':['01']}
dossierItems['37'] = {'image':'static/img/dossier2/dossier37.jpg', 'index':'37','title':'ABA MODULES', 'route':'/item37', 'chapter':'3', 'related':['01','05','06','16','37.1']}
dossierItems['37.1'] = {'image':'static/img/dossier2/dossier38.jpg', 'index':'37.1','title':'ABA HISTORY', 'route':'/item37_1', 'chapter':'3', 'related':['01','05','06','16','37']}
dossierItems['38'] = {'image':'static/img/dossier2/dossier38.jpg', 'index':'38','title':'CHURCH', 'route':'/item38', 'chapter':'3', 'related':['32','34']}
dossierItems['39'] = {'image':'static/img/dossier2/dossier39.jpg', 'index':'39','title':'AUGMENTATION', 'route':'/item39', 'chapter':'3', 'related':['05','18']}
dossierItems['40'] = {'image':'static/img/dossier2/dossier40.jpg', 'index':'40','title':'DRUG TRADE', 'route':'/item40', 'chapter':'3', 'related':['01','02','06','40','55','56']}
dossierItems['41'] = {'image':'static/img/dossier2/dossier41.jpg', 'index':'41','title':'ATLANTIS ARTICLE', 'route':'/item41', 'chapter':'3', 'related':['46']}
dossierItems['42'] = {'image':'static/img/dossier2/dossier42.jpg', 'index':'42','title':'MOB AND DRUGS', 'route':'/item42', 'chapter':'3', 'related':['01','05','06','34','44','45']}
dossierItems['43'] = {'image':'static/img/dossier2/dossier43.jpg', 'index':'43','title':"DEVIL'S BREATH", 'route':'/item43', 'chapter':'3', 'related':['34']}
dossierItems['44'] = {'image':'static/img/dossier2/dossier44.jpg', 'index':'44','title':'DRIVER', 'route':'/item44', 'chapter':'3', 'related':['34','40','42','46']}
dossierItems['45'] = {'image':'static/img/dossier2/dossier45.jpg', 'index':'45','title':'GREGORY VICTOR', 'route':'/item45', 'chapter':'3', 'related':['01','05','06','34','35','42','43']}
dossierItems['46'] = {'image':'static/img/dossier2/dossier46.jpg', 'index':'46','title':'ATLANTIS MAP', 'route':'/item46', 'chapter':'3', 'related':['41','42']}

dossierItems['47'] = {'image':'static/img/dossier2/dossier47.jpg', 'index':'47','title':'CONNOR SULLIVAN', 'route':'/item47', 'chapter':'4', 'related':['29','30','48','49','50','51','52','53','54','59']}
dossierItems['48'] = {'image':'static/img/dossier2/dossier48.jpg', 'index':'48','title':'SELENE', 'route':'/item48', 'chapter':'4', 'related':['48','49','50','51','52','53','54','57','58']}
dossierItems['49'] = {'image':'static/img/dossier2/dossier49.jpg', 'index':'49','title':'AT MAGNA CARTA', 'route':'/item49', 'chapter':'4', 'related':['46','50','51','52','53','54','55']}
dossierItems['50'] = {'image':'static/img/dossier2/dossier50.jpg', 'index':'50','title':'AT HISTORY', 'route':'/item50', 'chapter':'4', 'related':['46','47','48','49','51','52','53','54','55']}
dossierItems['51'] = {'image':'static/img/dossier2/dossier51.jpg', 'index':'51','title':'AENGUS', 'route':'/item51', 'chapter':'4', 'related':['46','47','48','49','50','52','53','54','55']}
dossierItems['52'] = {'image':'static/img/dossier2/dossier52.jpg', 'index':'52','title':'AT ECONOMICS', 'route':'/item52', 'chapter':'4', 'related':['46','47','48','49','50','51','53','54','55']}
dossierItems['53'] = {'image':'static/img/dossier2/dossier53.jpg', 'index':'53','title':'AT RELIGION', 'route':'/item53', 'chapter':'4', 'related':['46','47','48','49','50','51','52','54','55']}
dossierItems['54'] = {'image':'static/img/dossier2/dossier54.jpg', 'index':'54','title':'AT PRODUCTION', 'route':'/item54', 'chapter':'4', 'related':['46','47','48','49','50','51','52','53','55']}
dossierItems['55'] = {'image':'static/img/dossier2/dossier55.jpg', 'index':'55','title':'AT MASTER PLAN', 'route':'/item55', 'chapter':'4', 'related':['46','47','48','49','50','51','52','53','54']}
dossierItems['56'] = {'image':'static/img/dossier2/dossier56.jpg', 'index':'56','title':'SALLY', 'route':'/item56', 'chapter':'4', 'related':['01','02','06','40','55','56']}
dossierItems['57'] = {'image':'static/img/dossier2/dossier57.jpg', 'index':'57','title':'AT DRUG TRADE', 'route':'/item57', 'chapter':'4', 'related':['01','02','06']}
dossierItems['58'] = {'image':'static/img/dossier2/dossier58.jpg', 'index':'58','title':'TRADE EMBARGO', 'route':'/item58', 'chapter':'4', 'related':['29','30']}
dossierItems['59'] = {'image':'static/img/dossier2/dossier59.jpg', 'index':'59','title':'TERRORIST TRANSMITION', 'route':'/item59', 'chapter':'4', 'related':['29','30','39','46','50','54','57','60']}
dossierItems['60'] = {'image':'static/img/dossier2/dossier60.jpg', 'index':'60','title':'INVENTED TERRORIST', 'route':'/item60', 'chapter':'4', 'related':['29','30','39','46','50','54','57','59']}



foundItems = {}

foundItems['01'] = {"value":False,"index":"01", 'chapter':'1'}
foundItems['02'] = {"value":False,"index":"02", 'chapter':'1'}
foundItems['03'] = {"value":False,"index":"03", 'chapter':'1'}
foundItems['04'] = {"value":False,"index":"04", 'chapter':'1'}
foundItems['05'] = {"value":False,"index":"05", 'chapter':'1'}
foundItems['06'] = {"value":False,"index":"06", 'chapter':'1'}
foundItems['07'] = {"value":False,"index":"07", 'chapter':'1'}
foundItems['08'] = {"value":False,"index":"08", 'chapter':'1'}

foundItems['09'] = {"value":False,"index":'09', 'chapter':'2'}
foundItems['10'] = {"value":False,"index":'10', 'chapter':'2'}
foundItems['11'] = {"value":False,"index":'11', 'chapter':'2'}
foundItems['12'] = {"value":False,"index":'12', 'chapter':'2'}
foundItems['13'] = {"value":False,"index":'13', 'chapter':'2'}
foundItems['14'] = {"value":False,"index":'14', 'chapter':'2'}
foundItems['15'] = {"value":False,"index":'15', 'chapter':'2'}
foundItems['16'] = {"value":False,"index":'16', 'chapter':'2'}
foundItems['17'] = {"value":False,"index":'17', 'chapter':'2'}
foundItems['18'] = {"value":False,"index":'18', 'chapter':'2'}
foundItems['19'] = {"value":False,"index":'19', 'chapter':'2'}
foundItems['20'] = {"value":False,"index":'20', 'chapter':'2'}
foundItems['21'] = {"value":False,"index":'21', 'chapter':'2'}
foundItems['22'] = {"value":False,"index":'22', 'chapter':'2'}
foundItems['23'] = {"value":False,"index":'23', 'chapter':'2'}
foundItems['24'] = {"value":False,"index":'24', 'chapter':'2'}
foundItems['25'] = {"value":False,"index":'25', 'chapter':'2'}
foundItems['26'] = {"value":False,"index":'26', 'chapter':'2'}
foundItems['27'] = {"value":False,"index":'27', 'chapter':'2'}
foundItems['28'] = {"value":False,"index":'28', 'chapter':'2'}
foundItems['29'] = {"value":False,"index":'29', 'chapter':'2'}
foundItems['30'] = {"value":False,"index":'30', 'chapter':'2'}

foundItems['31'] = {"value":False,"index":'31', 'chapter':'3'}
foundItems['32'] = {"value":False,"index":'32', 'chapter':'3'}
foundItems['33'] = {"value":False,"index":'33', 'chapter':'3'}
foundItems['34'] = {"value":False,"index":'34', 'chapter':'3'}
foundItems['35'] = {"value":False,"index":'35', 'chapter':'3'}
foundItems['36'] = {"value":False,"index":'36', 'chapter':'3'}
foundItems['37'] = {"value":False,"index":'37', 'chapter':'3'}
foundItems['37.1'] = {"value":False,"index":"37.1", 'chapter':'3'}
foundItems['38'] = {"value":False,"index":'38', 'chapter':'3'}
foundItems['39'] = {"value":False,"index":'39', 'chapter':'3'}
foundItems['40'] = {"value":False,"index":'40', 'chapter':'3'}
foundItems['41'] = {"value":False,"index":'41', 'chapter':'3'}
foundItems['42'] = {"value":False,"index":'42', 'chapter':'3'}
foundItems['43'] = {"value":False,"index":'43', 'chapter':'3'}
foundItems['44'] = {"value":False,"index":'44', 'chapter':'3'}
foundItems['45'] = {"value":False,"index":'45', 'chapter':'3'}
foundItems['46'] = {"value":False,"index":'46', 'chapter':'3'}

foundItems['47'] = {"value":False,"index":'47', 'chapter':'4'}
foundItems['48'] = {"value":False,"index":'48', 'chapter':'4'}
foundItems['49'] = {"value":False,"index":'49', 'chapter':'4'}
foundItems['50'] = {"value":False,"index":'50', 'chapter':'4'}
foundItems['51'] = {"value":False,"index":'51', 'chapter':'4'}
foundItems['52'] = {"value":False,"index":'52', 'chapter':'4'}
foundItems['53'] = {"value":False,"index":'53', 'chapter':'4'}
foundItems['54'] = {"value":False,"index":'54', 'chapter':'4'}
foundItems['55'] = {"value":False,"index":'55', 'chapter':'4'}
foundItems['56'] = {"value":False,"index":'56', 'chapter':'4'}
foundItems['57'] = {"value":False,"index":'57', 'chapter':'4'}
foundItems['58'] = {"value":False,"index":'58', 'chapter':'4'}
foundItems['59'] = {"value":False,"index":'59', 'chapter':'4'}
foundItems['60'] = {"value":False,"index":'60', 'chapter':'4'}
















global myPage
myPage = '1'


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
	return render_template("bof1_test2.html", **templateData)

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
	dossierItems['01'] = {'image':'static/img/dossier/Toki_vid.png', 'index':'01','title':'TOKI_VID', 'route':'/item01', 'chapter':'1', 'video':'http://vimeo.com/93462324', 'related':['02','03','05','06']} # ,'16','25','27','37','45'
	relatedItems = []

	for item in dossierItems['01']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems['01']['title'],
	'image' : dossierItems['01']['image'],
	'video' : dossierItems['01']['video'],
	'relatedItems' : relatedItems
	}
	return render_template("video_item.html", **templateData)

@app.route("/item02")
def item02():
	foundItems['02']['value'] = True
	dossierItems['02'] = {'image':'static/img/dossier2/dossier02.jpg', 'index':'02','title':'STEVEN', 'route':'/item02', 'chapter':'1', 'related':['03']}
	relatedItems = []

	for item in dossierItems['02']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems['02']['title'],
	'image' : dossierItems['02']['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item03")
def item03():
	foundItems['03']['value'] = True
	dossierItems['03'] = {'image':'static/img/dossier2/dossier03.jpg', 'index':'03','title':'FRANK', 'route':'/item03', 'chapter':'1', 'related':['01','02','03','04','10']}
	relatedItems = []

	for item in dossierItems['03']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems['03']['title'],
	'image' : dossierItems['03']['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)


@app.route("/item04")
def item04():
	foundItems['04']['value'] = True
	dossierItems['04'] = {'image':'static/img/dossier2/dossier04.jpg', 'index':'04','title':'MATILDA', 'route':'/item04', 'chapter':'1', 'related':['01','02','03','07','08']} # ,'15','19','23'
	relatedItems = []

	for item in dossierItems['04']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems['04']['title'],
	'image' : dossierItems['04']['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item05")
def item05():
	dossierItems['05'] = {'image':'static/img/dossier2/dossier05.jpg', 'index':'05','title':'CALICO', 'route':'/item05', 'chapter':'1', 'related':['01','02','06']} # ,'16','37','45','55','56'
	
	itemIndex = '05'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item06")
def item06():
	foundItems['06']['value'] = True
	dossierItems['06'] = {'image':'static/img/dossier2/dossier06.jpg', 'index':'06','title':'CALICO SITES', 'route':'/item06', 'chapter':'1', 'related':['01','02','05']} # '16','37','45','55','56'
	relatedItems = []

	for item in dossierItems['06']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems['06']['title'],
	'image' : dossierItems['06']['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item07")
def item07():
	foundItems['07']['value'] = True
	dossierItems['07'] = {'image':'static/img/dossier2/dossier07.jpg', 'index':'07','title':'DARK NETWORK', 'route':'/item07', 'chapter':'1', 'related':['04','08']} # ,'15'
	relatedItems = []

	for item in dossierItems['07']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems['07']['title'],
	'image' : dossierItems['07']['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item08")
def item08():
	foundItems['08']['value'] = True
	dossierItems['08'] = {'image':'static/img/dossier2/dossier08.jpg', 'index':'08','title':'BLACK PHONE', 'route':'/item08', 'chapter':'1', 'related':['04','07']} # ,'15'
	relatedItems = []

	for item in dossierItems['08']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))


	templateData = {
	'title' : dossierItems['08']['title'],
	'image' : dossierItems['08']['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item09")
def item09():
	foundItems['09']['value'] = True
	dossierItems['09'] = {'image':'static/img/dossier2/dossier09.jpg', 'index':'09','title':'BAZAAR', 'route':'/item09', 'chapter':'2', 'related':['03']}
	relatedItems = []

	for item in dossierItems['09']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems['09']['title'],
	'image' : dossierItems['09']['image'],
	'relatedItems' : relatedItems
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
	dossierItems['11'] = {'image':'static/img/dossier2/dossier11.jpg', 'index':'11','title':'DDOS', 'route':'/item11', 'chapter':'2', 'related':['03']}
	foundItems['11']['value'] = True
	relatedItems = []

	for item in dossierItems['11']['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems['11']['title'],
	'image' : dossierItems['11']['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item12")
def item12():
	dossierItems['12'] = {'image':'static/img/dossier2/dossier12.jpg', 'index':'12','title':'FARADY BOX', 'route':'/item12', 'chapter':'2', 'related':['03']}
	itemIndex = '12'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item13")
def item13():
	dossierItems['13'] = {'image':'static/img/dossier2/dossier13.jpg', 'index':'13','title':'TOR IRL', 'route':'/item13', 'chapter':'2', 'related':['04','15']}
	itemIndex = '13'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item14")
def item14():	
	dossierItems['14'] = {'image':'static/img/dossier2/dossier14.jpg', 'index':'14','title':'GUILTY', 'route':'/item14', 'chapter':'2', 'related':['15']}
	itemIndex = '14'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item15")
def item15():
	dossierItems['15'] = {'image':'static/img/dossier2/dossier15.jpg', 'index':'15','title':'OMER', 'route':'/item15', 'chapter':'2', 'related':['04','07','08','12','13','14','17','19','23','25','27']}
	itemIndex = '15'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item16")
def item16():
	dossierItems['16'] = {'image':'static/img/dossier2/dossier16.jpg', 'index':'16','title':'ABA', 'route':'/item16', 'chapter':'2', 'related':['01','05','06','37']}
	itemIndex = '16'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item17")
def item17():	
	dossierItems['17'] = {'image':'static/img/dossier2/dossier17.jpg', 'index':'17','title':'DEEP WEB', 'route':'/item17', 'chapter':'2', 'related':['15']}
	itemIndex = '17'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item18")
def item18():	
	dossierItems['18'] = {'image':'static/img/dossier2/dossier18.jpg', 'index':'18','title':'AUDITORS', 'route':'/item18', 'chapter':'2', 'related':['05']}
	itemIndex = '18'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item19")
def item19():	
	dossierItems['19'] = {'image':'static/img/dossier2/dossier19.jpg', 'index':'19','title':'UNSTABLE TECH', 'route':'/item19', 'chapter':'2', 'related':['04','15','23']}
	itemIndex = '19'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item20")
def item20():	
	dossierItems['20'] = {'image':'static/img/dossier2/dossier20.jpg', 'index':'20','title':'FACE TRACKING', 'route':'/item20', 'chapter':'2', 'related':['21','23']}
	itemIndex = '20'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item21")
def item21():	
	dossierItems['21'] = {'image':'static/img/dossier2/dossier21.jpg', 'index':'21','title':'EUCLID', 'route':'/item21', 'chapter':'2', 'related':['20','22']}
	itemIndex = '21'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item22")
def item22():	
	dossierItems['22'] = {'image':'static/img/dossier2/dossier22.jpg', 'index':'22','title':'BEHAVIOR TRACKING', 'route':'/item22', 'chapter':'2', 'related':['20','21']}
	itemIndex = '22'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item23")
def item23():
	dossierItems['23'] = {'image':'static/img/dossier2/dossier23.jpg', 'index':'23','title':'THE BANK', 'route':'/item23', 'chapter':'2', 'related':['03','04','15','19']}
	itemIndex = '23'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item24")
def item24():	
	dossierItems['24'] = {'image':'static/img/dossier2/dossier24.jpg', 'index':'24','title':'DNA', 'route':'/item24', 'chapter':'2', 'related':['03','04','15','19']}
	itemIndex = '24'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item25")
def item25():	
	dossierItems['25'] = {'image':'static/img/dossier2/dossier25.jpg', 'index':'25','title':'MASK & COLLAR', 'route':'/item25', 'chapter':'2', 'related':['01','03','04','15','19','26','55']}
	itemIndex = '25'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item26")
def item26():	
	dossierItems['26'] = {'image':'static/img/dossier2/dossier26.jpg', 'index':'26','title':'WIRESHARK', 'route':'/item26', 'chapter':'2', 'related':['01','15','25','55']}
	itemIndex = '26'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item27")
def item27():	
	dossierItems['27'] = {'image':'static/img/dossier2/dossier27.jpg', 'index':'27','title':'BUNNY MEMORY', 'route':'/item27', 'chapter':'2', 'related':['01','15']}
	itemIndex = '27'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item28")
def item28():	
	dossierItems['28'] = {'image':'static/img/dossier2/dossier28.jpg', 'index':'28','title':'DUMB TECH', 'route':'/item28', 'chapter':'2', 'related':['04','15']}
	itemIndex = '28'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item29")
def item29():	
	dossierItems['29'] = {'image':'static/img/dossier2/dossier29.jpg', 'index':'29','title':'INTERVIEW', 'route':'/item29', 'chapter':'2', 'related':['30','47','58']}
	itemIndex = '29'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item30")
def item30():	
	dossierItems['30'] = {'image':'static/img/dossier2/dossier30.jpg', 'index':'30','title':'POLITICIAN', 'route':'/item30', 'chapter':'2', 'related':['29','47','58']}
	itemIndex = '30'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)


@app.route("/item31")
def item31():
	dossierItems['31'] = {'image':'static/img/dossier2/dossier31.jpg', 'index':'31','title':"FRANK'S DREAMS", 'route':'/item31', 'chapter':'3', 'related':['02']}
	itemIndex = '31'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item32")
def item32():
	dossierItems['32'] = {'image':'static/img/dossier2/dossier32.jpg', 'index':'32','title':'SHITTY CITY', 'route':'/item32', 'chapter':'3', 'related':['15','34','38']}
	itemIndex = '32'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item33")
def item33():
	dossierItems['33'] = {'image':'static/img/dossier2/dossier33.jpg', 'index':'33','title':'ANTI-AGING', 'route':'/item33', 'chapter':'3', 'related':['05','06']}
	itemIndex = '33'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item34")
def item34():
	dossierItems['34'] = {'image':'static/img/dossier2/dossier34.jpg', 'index':'34','title':'AL', 'route':'/item34', 'chapter':'3', 'related':['15','32','40','42','43','44','45']}
	itemIndex = '34'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item35")
def item35():
	dossierItems['35'] = {'image':'static/img/dossier2/dossier35.jpg', 'index':'35','title':'RECORDS', 'route':'/item35', 'chapter':'3', 'related':['01','34','45']}
	itemIndex = '35'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item36")
def item36():
	dossierItems['36'] = {'image':'static/img/dossier2/dossier36.jpg', 'index':'36','title':'MALFUNCTION', 'route':'/item36', 'chapter':'3', 'related':['01']}
	itemIndex = '36'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item37")
def item37():
	dossierItems['37'] = {'image':'static/img/dossier2/dossier37.jpg', 'index':'37','title':'ABA MODULES', 'route':'/item37', 'chapter':'3', 'related':['01','05','06','16','37.1']}
	itemIndex = '37'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item37_1")
def item37_1():
	dossierItems['37.1'] = {'image':'static/img/dossier2/dossier38.jpg', 'index':'37.1','title':'ABA HISTORY', 'route':'/item37_1', 'chapter':'3', 'related':['01','05','06','16','37']}
	itemIndex = '37.1'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item38")
def item38():
	dossierItems['38'] = {'image':'static/img/dossier2/dossier38.jpg', 'index':'38','title':'CHURCH', 'route':'/item38', 'chapter':'3', 'related':['32','34']}
	itemIndex = '38'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item39")
def item39():
	dossierItems['39'] = {'image':'static/img/dossier2/dossier39.jpg', 'index':'39','title':'AUGMENTATION', 'route':'/item39', 'chapter':'3', 'related':['05','18']}
	itemIndex = '39'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item40")
def item40():
	dossierItems['40'] = {'image':'static/img/dossier2/dossier40.jpg', 'index':'40','title':'DRUG TRADE', 'route':'/item40', 'chapter':'3', 'related':['01','02','06','40','55','56']}
	itemIndex = '40'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item41")
def item41():
	dossierItems['41'] = {'image':'static/img/dossier2/dossier41.jpg', 'index':'41','title':'ATLANTIS ARTICLE', 'route':'/item41', 'chapter':'3', 'related':['46']}
	itemIndex = '41'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item42")
def item42():
	dossierItems['42'] = {'image':'static/img/dossier2/dossier42.jpg', 'index':'42','title':'MOB AND DRUGS', 'route':'/item42', 'chapter':'3', 'related':['01','05','06','34','44','45']}
	itemIndex = '42'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item43")
def item43():
	dossierItems['43'] = {'image':'static/img/dossier2/dossier43.jpg', 'index':'43','title':"DEVIL'S BREATH", 'route':'/item43', 'chapter':'3', 'related':['34']}
	itemIndex = '43'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item44")
def item44():
	dossierItems['44'] = {'image':'static/img/dossier2/dossier44.jpg', 'index':'44','title':'DRIVER', 'route':'/item44', 'chapter':'3', 'related':['34','40','42','46']}
	itemIndex = '44'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item45")
def item45():
	dossierItems['45'] = {'image':'static/img/dossier2/dossier45.jpg', 'index':'45','title':'GREGORY VICTOR', 'route':'/item45', 'chapter':'3', 'related':['01','05','06','34','35','42','43']}
	itemIndex = '45'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item46")
def item46():
	dossierItems['46'] = {'image':'static/img/dossier2/dossier46.jpg', 'index':'46','title':'ATLANTIS MAP', 'route':'/item46', 'chapter':'3', 'related':['41','42']}
	itemIndex = '46'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)


@app.route("/item47")
def item47():
	dossierItems['47'] = {'image':'static/img/dossier2/dossier47.jpg', 'index':'47','title':'CONNOR SULLIVAN', 'route':'/item47', 'chapter':'4', 'related':['29','30','48','49','50','51','52','53','54','59']}
	itemIndex = '47'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item48")
def item48():
	dossierItems['48'] = {'image':'static/img/dossier2/dossier48.jpg', 'index':'48','title':'SELENE', 'route':'/item48', 'chapter':'4', 'related':['48','49','50','51','52','53','54','57','58']}
	itemIndex = '48'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item49")
def item49():
	dossierItems['49'] = {'image':'static/img/dossier2/dossier49.jpg', 'index':'49','title':'AT MAGNA CARTA', 'route':'/item49', 'chapter':'4', 'related':['46','50','51','52','53','54','55']}
	itemIndex = '49'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item50")
def item50():
	dossierItems['50'] = {'image':'static/img/dossier2/dossier50.jpg', 'index':'50','title':'AT HISTORY', 'route':'/item50', 'chapter':'4', 'related':['46','47','48','49','51','52','53','54','55']}
	itemIndex = '50'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item51")
def item51():
	dossierItems['51'] = {'image':'static/img/dossier2/dossier51.jpg', 'index':'51','title':'AENGUS', 'route':'/item51', 'chapter':'4', 'related':['46','47','48','49','50','52','53','54','55']}
	itemIndex = '51'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item52")
def item52():
	dossierItems['52'] = {'image':'static/img/dossier2/dossier52.jpg', 'index':'52','title':'AT ECONOMICS', 'route':'/item52', 'chapter':'4', 'related':['46','47','48','49','50','51','53','54','55']}
	itemIndex = '52'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item53")
def item53():
	dossierItems['53'] = {'image':'static/img/dossier2/dossier53.jpg', 'index':'53','title':'AT RELIGION', 'route':'/item53', 'chapter':'4', 'related':['46','47','48','49','50','51','52','54','55']}
	itemIndex = '53'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item54")
def item54():
	dossierItems['54'] = {'image':'static/img/dossier2/dossier54.jpg', 'index':'54','title':'AT PRODUCTION', 'route':'/item54', 'chapter':'4', 'related':['46','47','48','49','50','51','52','53','55']}
	itemIndex = '54'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item55")
def item55():
	dossierItems['55'] = {'image':'static/img/dossier2/dossier55.jpg', 'index':'55','title':'AT MASTER PLAN', 'route':'/item55', 'chapter':'4', 'related':['46','47','48','49','50','51','52','53','54']}
	itemIndex = '55'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item56")
def item56():
	dossierItems['56'] = {'image':'static/img/dossier2/dossier56.jpg', 'index':'56','title':'SALLY', 'route':'/item56', 'chapter':'4', 'related':['01','02','06','40','55','56']}
	itemIndex = '56'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item57")
def item57():
	dossierItems['57'] = {'image':'static/img/dossier2/dossier57.jpg', 'index':'57','title':'AT DRUG TRADE', 'route':'/item57', 'chapter':'4', 'related':['01','02','06']}
	itemIndex = '57'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item58")
def item58():
	dossierItems['58'] = {'image':'static/img/dossier2/dossier58.jpg', 'index':'58','title':'TRADE EMBARGO', 'route':'/item58', 'chapter':'4', 'related':['29','30']}
	itemIndex = '58'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item59")
def item59():
	dossierItems['59'] = {'image':'static/img/dossier2/dossier59.jpg', 'index':'59','title':'TERRORIST TRANSMITION', 'route':'/item59', 'chapter':'4', 'related':['29','30','39','46','50','54','57','60']}
	itemIndex = '59'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
	}
	return render_template("item1.html", **templateData)

@app.route("/item60")
def item60():
	dossierItems['60'] = {'image':'static/img/dossier2/dossier60.jpg', 'index':'60','title':'INVENTED TERRORIST', 'route':'/item60', 'chapter':'4', 'related':['29','30','39','46','50','54','57','59']}
	itemIndex = '60'
	foundItems[itemIndex]['value'] = True
	relatedItems = []

	for item in dossierItems[itemIndex]['related']:
		relatedItems.append(dossierItems[item])

	relatedItems.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : dossierItems[itemIndex]['title'],
	'image' : dossierItems[itemIndex]['image'],
	'relatedItems' : relatedItems
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
	dossierItems['11'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'11','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['12'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'12','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['13'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'13','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['14'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'14','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['15'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'15','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['16'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'16','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['17'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'17','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['18'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'18','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['19'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'19','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['20'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'20','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['21'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'21','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['22'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'22','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['23'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'23','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['24'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'24','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['25'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'25','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['26'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'26','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['27'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'27','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['28'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'28','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['29'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'29','title':'?', 'route':'/itemblank', 'chapter':'2'}
	dossierItems['30'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'30','title':'?', 'route':'/itemblank', 'chapter':'2'}

	dossierItems['31'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'31','title':"?", 'route':'/itemblank', 'chapter':'3'}
	dossierItems['32'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'32','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['33'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'33','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['34'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'34','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['35'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'35','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['36'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'36','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['37'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'37','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['37.1'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'37.1','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['38'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'38','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['39'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'39','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['40'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'40','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['41'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'41','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['42'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'42','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['43'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'43','title':"?", 'route':'/itemblank', 'chapter':'3'}
	dossierItems['44'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'44','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['45'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'45','title':'?', 'route':'/itemblank', 'chapter':'3'}
	dossierItems['46'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'46','title':'?', 'route':'/itemblank', 'chapter':'3'}

	dossierItems['47'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'47','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['48'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'48','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['49'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'49','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['50'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'50','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['51'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'51','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['52'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'52','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['53'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'53','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['54'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'54','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['55'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'55','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['56'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'56','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['57'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'57','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['58'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'58','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['59'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'59','title':'?', 'route':'/itemblank', 'chapter':'4'}
	dossierItems['60'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'60','title':'?', 'route':'/itemblank', 'chapter':'4'}

	
	
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

	foundItems['09'] = {"value":True,"index":'09', 'chapter':'2'}
	foundItems['10'] = {"value":True,"index":'10', 'chapter':'2'}
	foundItems['11'] = {"value":True,"index":'11', 'chapter':'2'}
	foundItems['12'] = {"value":True,"index":'12', 'chapter':'2'}
	foundItems['13'] = {"value":True,"index":'13', 'chapter':'2'}
	foundItems['14'] = {"value":True,"index":'14', 'chapter':'2'}
	foundItems['15'] = {"value":True,"index":'15', 'chapter':'2'}
	foundItems['16'] = {"value":True,"index":'16', 'chapter':'2'}
	foundItems['17'] = {"value":True,"index":'17', 'chapter':'2'}
	foundItems['18'] = {"value":True,"index":'18', 'chapter':'2'}
	foundItems['19'] = {"value":True,"index":'19', 'chapter':'2'}
	foundItems['20'] = {"value":True,"index":'20', 'chapter':'2'}
	foundItems['21'] = {"value":True,"index":'21', 'chapter':'2'}
	foundItems['22'] = {"value":True,"index":'22', 'chapter':'2'}
	foundItems['23'] = {"value":True,"index":'23', 'chapter':'2'}
	foundItems['24'] = {"value":True,"index":'24', 'chapter':'2'}
	foundItems['25'] = {"value":True,"index":'25', 'chapter':'2'}
	foundItems['26'] = {"value":True,"index":'26', 'chapter':'2'}
	foundItems['27'] = {"value":True,"index":'27', 'chapter':'2'}
	foundItems['28'] = {"value":True,"index":'28', 'chapter':'2'}
	foundItems['29'] = {"value":True,"index":'29', 'chapter':'2'}
	foundItems['30'] = {"value":True,"index":'30', 'chapter':'2'}

	foundItems['31'] = {"value":True,"index":'31', 'chapter':'3'}
	foundItems['32'] = {"value":True,"index":'32', 'chapter':'3'}
	foundItems['33'] = {"value":True,"index":'33', 'chapter':'3'}
	foundItems['34'] = {"value":True,"index":'34', 'chapter':'3'}
	foundItems['35'] = {"value":True,"index":'35', 'chapter':'3'}
	foundItems['36'] = {"value":True,"index":'36', 'chapter':'3'}
	foundItems['37'] = {"value":True,"index":'37', 'chapter':'3'}
	foundItems['37.1'] = {"value":True,"index":"37.1", 'chapter':'3'}
	foundItems['38'] = {"value":True,"index":'38', 'chapter':'3'}
	foundItems['39'] = {"value":True,"index":'39', 'chapter':'3'}
	foundItems['40'] = {"value":True,"index":'40', 'chapter':'3'}
	foundItems['41'] = {"value":True,"index":'41', 'chapter':'3'}
	foundItems['42'] = {"value":True,"index":'42', 'chapter':'3'}
	foundItems['43'] = {"value":True,"index":'43', 'chapter':'3'}
	foundItems['44'] = {"value":True,"index":'44', 'chapter':'3'}
	foundItems['45'] = {"value":True,"index":'45', 'chapter':'3'}
	foundItems['46'] = {"value":True,"index":'46', 'chapter':'3'}

	foundItems['47'] = {"value":True,"index":'47', 'chapter':'4'}
	foundItems['48'] = {"value":True,"index":'48', 'chapter':'4'}
	foundItems['49'] = {"value":True,"index":'49', 'chapter':'4'}
	foundItems['50'] = {"value":True,"index":'50', 'chapter':'4'}
	foundItems['51'] = {"value":True,"index":'51', 'chapter':'4'}
	foundItems['52'] = {"value":True,"index":'52', 'chapter':'4'}
	foundItems['53'] = {"value":True,"index":'53', 'chapter':'4'}
	foundItems['54'] = {"value":True,"index":'54', 'chapter':'4'}
	foundItems['55'] = {"value":True,"index":'55', 'chapter':'4'}
	foundItems['56'] = {"value":True,"index":'56', 'chapter':'4'}
	foundItems['57'] = {"value":True,"index":'57', 'chapter':'4'}
	foundItems['58'] = {"value":True,"index":'58', 'chapter':'4'}
	foundItems['59'] = {"value":True,"index":'59', 'chapter':'4'}
	foundItems['60'] = {"value":True,"index":'60', 'chapter':'4'}

	dossierItems['00'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'00', 'title':'?', 'route':'/itemblank', 'chapter':'1'}
	dossierItems['01'] = {'image':'static/img/dossier/Toki_vid.png', 'index':'01','title':'TOKI_VID', 'route':'/item01', 'chapter':'1', 'video':'http://vimeo.com/93462324', 'related':['02','03','05','06','16','25','27','37','45']}
	dossierItems['02'] = {'image':'static/img/dossier2/dossier02.jpg', 'index':'02','title':'STEVEN', 'route':'/item02', 'chapter':'1', 'related':['03']}
	dossierItems['03'] = {'image':'static/img/dossier2/dossier03.jpg', 'index':'03','title':'FRANK', 'route':'/item03', 'chapter':'1', 'related':['01','02','03','04','10']}
	dossierItems['04'] = {'image':'static/img/dossier2/dossier04.jpg', 'index':'04','title':'MATILDA', 'route':'/item04', 'chapter':'1', 'related':['01','02','03','07','08','15','19','23']}
	dossierItems['05'] = {'image':'static/img/dossier2/dossier05.jpg', 'index':'05','title':'CALICO', 'route':'/item05', 'chapter':'1', 'related':['01','02','06','16','37','45','55','56']}
	dossierItems['06'] = {'image':'static/img/dossier2/dossier06.jpg', 'index':'06','title':'CALICO SITES', 'route':'/item06', 'chapter':'1', 'related':['01','02','05','16','37','45','55','56']}
	dossierItems['07'] = {'image':'static/img/dossier2/dossier07.jpg', 'index':'07','title':'DARK NETWORK', 'route':'/item07', 'chapter':'1', 'related':['04','08','15']}
	dossierItems['08'] = {'image':'static/img/dossier2/dossier08.jpg', 'index':'08','title':'BLACK PHONE', 'route':'/item08', 'chapter':'1', 'related':['04','07','15']}

	dossierItems['09'] = {'image':'static/img/dossier2/dossier09.jpg', 'index':'09','title':'BAZAAR', 'route':'/item09', 'chapter':'2', 'related':['10']}
	dossierItems['10'] = {'image':'static/img/dossier2/dossier10.jpg', 'index':'10','title':'PERSUASIVE MEMORY', 'route':'/item10', 'chapter':'2', 'related':['09']}
	dossierItems['11'] = {'image':'static/img/dossier2/dossier11.jpg', 'index':'11','title':'DDOS', 'route':'/item11', 'chapter':'2', 'related':['03']}
	dossierItems['12'] = {'image':'static/img/dossier2/dossier12.jpg', 'index':'12','title':'FARADY BOX', 'route':'/item12', 'chapter':'2', 'related':['01','04','15']}
	dossierItems['13'] = {'image':'static/img/dossier2/dossier13.jpg', 'index':'13','title':'TOR IRL', 'route':'/item13', 'chapter':'2', 'related':['04','15']}
	dossierItems['14'] = {'image':'static/img/dossier2/dossier14.jpg', 'index':'14','title':'GUILTY', 'route':'/item14', 'chapter':'2', 'related':['15']}
	dossierItems['15'] = {'image':'static/img/dossier2/dossier15.jpg', 'index':'15','title':'OMER', 'route':'/item15', 'chapter':'2', 'related':['04','07','08','12','13','14','17','19','23','25','27']}
	dossierItems['16'] = {'image':'static/img/dossier2/dossier16.jpg', 'index':'16','title':'ABA', 'route':'/item16', 'chapter':'2', 'related':['01','05','06','37']}
	dossierItems['17'] = {'image':'static/img/dossier2/dossier17.jpg', 'index':'17','title':'DEEP WEB', 'route':'/item17', 'chapter':'2', 'related':['15']}
	dossierItems['18'] = {'image':'static/img/dossier2/dossier18.jpg', 'index':'18','title':'AUDITORS', 'route':'/item18', 'chapter':'2', 'related':['05']}
	dossierItems['19'] = {'image':'static/img/dossier2/dossier19.jpg', 'index':'19','title':'UNSTABLE TECH', 'route':'/item19', 'chapter':'2', 'related':['04','15','23']}
	dossierItems['20'] = {'image':'static/img/dossier2/dossier20.jpg', 'index':'20','title':'FACE TRACKING', 'route':'/item20', 'chapter':'2', 'related':['21','23']}
	dossierItems['21'] = {'image':'static/img/dossier2/dossier21.jpg', 'index':'21','title':'EUCLID', 'route':'/item21', 'chapter':'2', 'related':['20','22']}
	dossierItems['22'] = {'image':'static/img/dossier2/dossier22.jpg', 'index':'22','title':'BEHAVIOR TRACKING', 'route':'/item22', 'chapter':'2', 'related':['20','21']}
	dossierItems['23'] = {'image':'static/img/dossier2/dossier23.jpg', 'index':'23','title':'THE BANK', 'route':'/item23', 'chapter':'2', 'related':['03','04','15','19']}
	dossierItems['24'] = {'image':'static/img/dossier2/dossier24.jpg', 'index':'24','title':'DNA', 'route':'/item24', 'chapter':'2', 'related':['03','04','15','19']}
	dossierItems['25'] = {'image':'static/img/dossier2/dossier25.jpg', 'index':'25','title':'MASK & COLLAR', 'route':'/item25', 'chapter':'2', 'related':['01','03','04','15','19','26','55']}
	dossierItems['26'] = {'image':'static/img/dossier2/dossier26.jpg', 'index':'26','title':'WIRESHARK', 'route':'/item26', 'chapter':'2', 'related':['01','15','25','55']}
	dossierItems['27'] = {'image':'static/img/dossier2/dossier27.jpg', 'index':'27','title':'BUNNY MEMORY', 'route':'/item27', 'chapter':'2', 'related':['01','15']}
	dossierItems['28'] = {'image':'static/img/dossier2/dossier28.jpg', 'index':'28','title':'DUMB TECH', 'route':'/item28', 'chapter':'2', 'related':['04','15']}
	dossierItems['29'] = {'image':'static/img/dossier2/dossier29.jpg', 'index':'29','title':'INTERVIEW', 'route':'/item29', 'chapter':'2', 'related':['30','47','58']}
	dossierItems['30'] = {'image':'static/img/dossier2/dossier30.jpg', 'index':'30','title':'POLITICIAN', 'route':'/item30', 'chapter':'2', 'related':['29','47','58']}

	dossierItems['31'] = {'image':'static/img/dossier2/dossier31.jpg', 'index':'31','title':"FRANK'S DREAMS", 'route':'/item31', 'chapter':'3', 'related':['02']}
	dossierItems['32'] = {'image':'static/img/dossier2/dossier32.jpg', 'index':'32','title':'SHITTY CITY', 'route':'/item32', 'chapter':'3', 'related':['15','34','38']}
	dossierItems['33'] = {'image':'static/img/dossier2/dossier33.jpg', 'index':'33','title':'ANTI-AGING', 'route':'/item33', 'chapter':'3', 'related':['05','06']}
	dossierItems['34'] = {'image':'static/img/dossier2/dossier34.jpg', 'index':'34','title':'AL', 'route':'/item34', 'chapter':'3', 'related':['15','32','40','42','43','44','45']}
	dossierItems['35'] = {'image':'static/img/dossier2/dossier35.jpg', 'index':'35','title':'RECORDS', 'route':'/item35', 'chapter':'3', 'related':['01','34','45']}
	dossierItems['36'] = {'image':'static/img/dossier2/dossier36.jpg', 'index':'36','title':'MALFUNCTION', 'route':'/item36', 'chapter':'3', 'related':['01']}
	dossierItems['37'] = {'image':'static/img/dossier2/dossier37.jpg', 'index':'37','title':'ABA MODULES', 'route':'/item37', 'chapter':'3', 'related':['01','05','06','16','37.1']}
	dossierItems['37.1'] = {'image':'static/img/dossier2/dossier38.jpg', 'index':'37.1','title':'ABA HISTORY', 'route':'/item37_1', 'chapter':'3', 'related':['01','05','06','16','37']}
	dossierItems['38'] = {'image':'static/img/dossier2/dossier38.jpg', 'index':'38','title':'CHURCH', 'route':'/item38', 'chapter':'3', 'related':['32','34']}
	dossierItems['39'] = {'image':'static/img/dossier2/dossier39.jpg', 'index':'39','title':'AUGMENTATION', 'route':'/item39', 'chapter':'3', 'related':['05','18']}
	dossierItems['40'] = {'image':'static/img/dossier2/dossier40.jpg', 'index':'40','title':'DRUG TRADE', 'route':'/item40', 'chapter':'3', 'related':['01','02','06','40','55','56']}
	dossierItems['41'] = {'image':'static/img/dossier2/dossier41.jpg', 'index':'41','title':'ATLANTIS ARTICLE', 'route':'/item41', 'chapter':'3', 'related':['46']}
	dossierItems['42'] = {'image':'static/img/dossier2/dossier42.jpg', 'index':'42','title':'MOB AND DRUGS', 'route':'/item42', 'chapter':'3', 'related':['01','05','06','34','44','45']}
	dossierItems['43'] = {'image':'static/img/dossier2/dossier43.jpg', 'index':'43','title':"DEVIL'S BREATH", 'route':'/item43', 'chapter':'3', 'related':['34']}
	dossierItems['44'] = {'image':'static/img/dossier2/dossier44.jpg', 'index':'44','title':'DRIVER', 'route':'/item44', 'chapter':'3', 'related':['34','40','42','46']}
	dossierItems['45'] = {'image':'static/img/dossier2/dossier45.jpg', 'index':'45','title':'GREGORY VICTOR', 'route':'/item45', 'chapter':'3', 'related':['01','05','06','34','35','42','43']}
	dossierItems['46'] = {'image':'static/img/dossier2/dossier46.jpg', 'index':'46','title':'ATLANTIS MAP', 'route':'/item46', 'chapter':'3', 'related':['41','42']}

	dossierItems['47'] = {'image':'static/img/dossier2/dossier47.jpg', 'index':'47','title':'CONNOR SULLIVAN', 'route':'/item47', 'chapter':'4', 'related':['29','30','48','49','50','51','52','53','54','59']}
	dossierItems['48'] = {'image':'static/img/dossier2/dossier48.jpg', 'index':'48','title':'SELENE', 'route':'/item48', 'chapter':'4', 'related':['48','49','50','51','52','53','54','57','58']}
	dossierItems['49'] = {'image':'static/img/dossier2/dossier49.jpg', 'index':'49','title':'AT MAGNA CARTA', 'route':'/item49', 'chapter':'4', 'related':['46','50','51','52','53','54','55']}
	dossierItems['50'] = {'image':'static/img/dossier2/dossier50.jpg', 'index':'50','title':'AT HISTORY', 'route':'/item50', 'chapter':'4', 'related':['46','47','48','49','51','52','53','54','55']}
	dossierItems['51'] = {'image':'static/img/dossier2/dossier51.jpg', 'index':'51','title':'AENGUS', 'route':'/item51', 'chapter':'4', 'related':['46','47','48','49','50','52','53','54','55']}
	dossierItems['52'] = {'image':'static/img/dossier2/dossier52.jpg', 'index':'52','title':'AT ECONOMICS', 'route':'/item52', 'chapter':'4', 'related':['46','47','48','49','50','51','53','54','55']}
	dossierItems['53'] = {'image':'static/img/dossier2/dossier53.jpg', 'index':'53','title':'AT RELIGION', 'route':'/item53', 'chapter':'4', 'related':['46','47','48','49','50','51','52','54','55']}
	dossierItems['54'] = {'image':'static/img/dossier2/dossier54.jpg', 'index':'54','title':'AT PRODUCTION', 'route':'/item54', 'chapter':'4', 'related':['46','47','48','49','50','51','52','53','55']}
	dossierItems['55'] = {'image':'static/img/dossier2/dossier55.jpg', 'index':'55','title':'AT MASTER PLAN', 'route':'/item55', 'chapter':'4', 'related':['46','47','48','49','50','51','52','53','54']}
	dossierItems['56'] = {'image':'static/img/dossier2/dossier56.jpg', 'index':'56','title':'SALLY', 'route':'/item56', 'chapter':'4', 'related':['01','02','06','40','55','56']}
	dossierItems['57'] = {'image':'static/img/dossier2/dossier57.jpg', 'index':'57','title':'AT DRUG TRADE', 'route':'/item57', 'chapter':'4', 'related':['01','02','06']}
	dossierItems['58'] = {'image':'static/img/dossier2/dossier58.jpg', 'index':'58','title':'TRADE EMBARGO', 'route':'/item58', 'chapter':'4', 'related':['29','30']}
	dossierItems['59'] = {'image':'static/img/dossier2/dossier59.jpg', 'index':'59','title':'TERRORIST TRANSMITION', 'route':'/item59', 'chapter':'4', 'related':['29','30','39','46','50','54','57','60']}
	dossierItems['60'] = {'image':'static/img/dossier2/dossier60.jpg', 'index':'60','title':'INVENTED TERRORIST', 'route':'/item60', 'chapter':'4', 'related':['29','30','39','46','50','54','57','59']}

	

	
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

@app.route("/dc3")
def dc3():
	currentItems = []
	chapter3Items = []
	chapter3Sorted = []

	for k,v in foundItems.iteritems():
		if foundItems[k]['value'] and foundItems[k]['chapter'] == '3':
			chapter3Items.append(dossierItems[foundItems[k]['index']])

		elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '3':
			dossierItems[foundItems[k]['index']]['title'] = '?'
			dossierItems[foundItems[k]['index']]['image'] = 'static/img/dossier/Dossier_blank.jpg'
			dossierItems[foundItems[k]['index']]['route'] = '/itemblank'
			chapter3Items.append(dossierItems[foundItems[k]['index']])

		else:
			pass

	chapter3Items.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : 'These are the items found in Chapter 3',
	'chapter3Items' : chapter3Items,
	'chapter3Sorted' : chapter3Sorted
	}

	return render_template("dc3.html", **templateData)	

@app.route("/dc4")
def dc4():
	currentItems = []
	chapter4Items = []
	chapter4Sorted = []

	for k,v in foundItems.iteritems():
		if foundItems[k]['value'] and foundItems[k]['chapter'] == '4':
			chapter4Items.append(dossierItems[foundItems[k]['index']])

		elif foundItems[k]['value'] == False and foundItems[k]['chapter'] == '4':
			dossierItems[foundItems[k]['index']]['title'] = '?'
			dossierItems[foundItems[k]['index']]['image'] = 'static/img/dossier/Dossier_blank.jpg'
			dossierItems[foundItems[k]['index']]['route'] = '/itemblank'
			chapter4Items.append(dossierItems[foundItems[k]['index']])

		else:
			pass

	chapter4Items.sort(key=operator.itemgetter('index'))

	templateData = {
	'title' : 'These are the items found in Chapter 2',
	'chapter4Items' : chapter4Items,
	'chapter4Sorted' : chapter4Sorted
	}

	return render_template("dc4.html", **templateData)	

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




# dossierItems['00'] = {'image':'static/img/dossier/Dossier_blank.jpg', 'index':'00', 'title':'?', 'route':'/itemblank', 'chapter':'1'}
# dossierItems['01'] = {'image':'static/img/dossier/Toki_vid.png', 'index':'01','title':'TOKI_VID', 'route':'/item01', 'chapter':'1', 'video':'http://vimeo.com/93462324', 'related':['02','03','05','06','16','25','27','37','45']}
# dossierItems['02'] = {'image':'static/img/dossier2/dossier02.jpg', 'index':'02','title':'STEVEN', 'route':'/item02', 'chapter':'1', 'related':['03']}
# dossierItems['03'] = {'image':'static/img/dossier2/dossier03.jpg', 'index':'03','title':'FRANK', 'route':'/item03', 'chapter':'1', 'related':['01','02','03','04','10']}
# dossierItems['04'] = {'image':'static/img/dossier2/dossier04.jpg', 'index':'04','title':'MATILDA', 'route':'/item04', 'chapter':'1', 'related':['01','02','03','07','08','15','19','23']}
# dossierItems['05'] = {'image':'static/img/dossier2/dossier05.jpg', 'index':'05','title':'CALICO', 'route':'/item05', 'chapter':'1', 'related':['01','02','06','16','37','45','55','56']}
# dossierItems['06'] = {'image':'static/img/dossier2/dossier06.jpg', 'index':'06','title':'CALICO SITES', 'route':'/item06', 'chapter':'1', 'related':['01','02','05','16','37','45','55','56']}
# dossierItems['07'] = {'image':'static/img/dossier2/dossier07.jpg', 'index':'07','title':'DARK NETWORK', 'route':'/item07', 'chapter':'1', 'related':['04','08','15']}
# dossierItems['08'] = {'image':'static/img/dossier2/dossier08.jpg', 'index':'08','title':'BLACK PHONE', 'route':'/item08', 'chapter':'1', 'related':['04','07','15']}
# dossierItems['09'] = {'image':'static/img/dossier2/dossier09.jpg', 'index':'09','title':'BAZAAR', 'route':'/item09', 'chapter':'2', 'related':['10']}
# dossierItems['10'] = {'image':'static/img/dossier2/dossier10.jpg', 'index':'10','title':'PERSUASIVE MEMORY', 'route':'/item10', 'chapter':'2', 'related':['09']}
# dossierItems['11'] = {'image':'static/img/dossier2/dossier11.jpg', 'index':'11','title':'DDOS', 'route':'/item11', 'chapter':'2', 'related':['03']}
# dossierItems['12'] = {'image':'static/img/dossier2/dossier12.jpg', 'index':'12','title':'FARADY BOX', 'route':'/item12', 'chapter':'2', 'related':['01','04','15']}
# dossierItems['13'] = {'image':'static/img/dossier2/dossier13.jpg', 'index':'13','title':'TOR IRL', 'route':'/item13', 'chapter':'2', 'related':['04','15']}
# dossierItems['14'] = {'image':'static/img/dossier2/dossier14.jpg', 'index':'14','title':'GUILTY', 'route':'/item14', 'chapter':'2', 'related':['15']}
# dossierItems['15'] = {'image':'static/img/dossier2/dossier15.jpg', 'index':'15','title':'OMER', 'route':'/item15', 'chapter':'2', 'related':['04','07','08','12','13','14','17','19','23','25','27']}
# dossierItems['16'] = {'image':'static/img/dossier2/dossier16.jpg', 'index':'16','title':'ABA', 'route':'/item16', 'chapter':'2', 'related':['01','05','06','37']}
# dossierItems['17'] = {'image':'static/img/dossier2/dossier17.jpg', 'index':'17','title':'DEEP WEB', 'route':'/item17', 'chapter':'2', 'related':['15']}
# dossierItems['18'] = {'image':'static/img/dossier2/dossier18.jpg', 'index':'18','title':'AUDITORS', 'route':'/item18', 'chapter':'2', 'related':['05']}
# dossierItems['19'] = {'image':'static/img/dossier2/dossier19.jpg', 'index':'19','title':'UNSTABLE TECH', 'route':'/item19', 'chapter':'2', 'related':['04','15','23']}
# dossierItems['20'] = {'image':'static/img/dossier2/dossier20.jpg', 'index':'20','title':'FACE TRACKING', 'route':'/item20', 'chapter':'2', 'related':['21','23']}
# dossierItems['21'] = {'image':'static/img/dossier2/dossier21.jpg', 'index':'21','title':'EUCLID', 'route':'/item21', 'chapter':'2', 'related':['20','22']}
# dossierItems['22'] = {'image':'static/img/dossier2/dossier22.jpg', 'index':'22','title':'BEHAVIOR TRACKING', 'route':'/item22', 'chapter':'2', 'related':['20','21']}
# dossierItems['23'] = {'image':'static/img/dossier2/dossier23.jpg', 'index':'23','title':'THE BANK', 'route':'/item23', 'chapter':'2', 'related':['03','04','15','19']}
# dossierItems['24'] = {'image':'static/img/dossier2/dossier24.jpg', 'index':'24','title':'DNA', 'route':'/item24', 'chapter':'2', 'related':['03','04','15','19']}
# dossierItems['25'] = {'image':'static/img/dossier2/dossier25.jpg', 'index':'25','title':'MASK & COLLAR', 'route':'/item25', 'chapter':'2', 'related':['01','03','04','15','19','26','55']}
# dossierItems['26'] = {'image':'static/img/dossier2/dossier26.jpg', 'index':'26','title':'WIRESHARK', 'route':'/item26', 'chapter':'2', 'related':['01','15','25','55']}
# dossierItems['27'] = {'image':'static/img/dossier2/dossier27.jpg', 'index':'27','title':'BUNNY MEMORY', 'route':'/item27', 'chapter':'2', 'related':['01','15']}
# dossierItems['28'] = {'image':'static/img/dossier2/dossier28.jpg', 'index':'28','title':'DUMB TECH', 'route':'/item28', 'chapter':'2', 'related':['04','15']}
# dossierItems['29'] = {'image':'static/img/dossier2/dossier29.jpg', 'index':'29','title':'INTERVIEW', 'route':'/item29', 'chapter':'2', 'related':['30','47','58']}
# dossierItems['30'] = {'image':'static/img/dossier2/dossier30.jpg', 'index':'30','title':'POLITICIAN', 'route':'/item30', 'chapter':'2', 'related':['29','47','58']}
# dossierItems['31'] = {'image':'static/img/dossier2/dossier31.jpg', 'index':'31','title':"FRANK'S DREAMS", 'route':'/item31', 'chapter':'3', 'related':['02']}
# dossierItems['32'] = {'image':'static/img/dossier2/dossier32.jpg', 'index':'32','title':'SHITTY CITY', 'route':'/item32', 'chapter':'3', 'related':['15','34','38']}
# dossierItems['33'] = {'image':'static/img/dossier2/dossier33.jpg', 'index':'33','title':'ANTI-AGING', 'route':'/item33', 'chapter':'3', 'related':['05','06']}
# dossierItems['34'] = {'image':'static/img/dossier2/dossier34.jpg', 'index':'34','title':'AL', 'route':'/item34', 'chapter':'3', 'related':['15','32','40','42','43','44','45']}
# dossierItems['35'] = {'image':'static/img/dossier2/dossier35.jpg', 'index':'35','title':'RECORDS', 'route':'/item35', 'chapter':'3', 'related':['01','34','45']}
# dossierItems['36'] = {'image':'static/img/dossier2/dossier36.jpg', 'index':'36','title':'MALFUNCTION', 'route':'/item36', 'chapter':'3', 'related':['01']}
# dossierItems['37'] = {'image':'static/img/dossier2/dossier37.jpg', 'index':'37','title':'ABA MODULES', 'route':'/item37', 'chapter':'3', 'related':['01','05','06','16','37.1']}
# dossierItems['37.1'] = {'image':'static/img/dossier2/dossier38.jpg', 'index':'37.1','title':'ABA HISTORY', 'route':'/item37_1', 'chapter':'3', 'related':['01','05','06','16','37']}
# dossierItems['38'] = {'image':'static/img/dossier2/dossier38.jpg', 'index':'38','title':'CHURCH', 'route':'/item38', 'chapter':'3', 'related':['32','34']}
# dossierItems['39'] = {'image':'static/img/dossier2/dossier39.jpg', 'index':'39','title':'AUGMENTATION', 'route':'/item39', 'chapter':'3', 'related':['05','18']}
# dossierItems['40'] = {'image':'static/img/dossier2/dossier40.jpg', 'index':'40','title':'DRUG TRADE', 'route':'/item40', 'chapter':'3', 'related':['01','02','06','40','55','56']}
# dossierItems['41'] = {'image':'static/img/dossier2/dossier41.jpg', 'index':'41','title':'ATLANTIS ARTICLE', 'route':'/item41', 'chapter':'3', 'related':['46']}
# dossierItems['42'] = {'image':'static/img/dossier2/dossier42.jpg', 'index':'42','title':'MOB AND DRUGS', 'route':'/item42', 'chapter':'3', 'related':['01','05','06','34','44','45']}
# dossierItems['43'] = {'image':'static/img/dossier2/dossier43.jpg', 'index':'43','title':"DEVIL'S BREATH", 'route':'/item43', 'chapter':'3', 'related':['34']}
# dossierItems['44'] = {'image':'static/img/dossier2/dossier44.jpg', 'index':'44','title':'DRIVER', 'route':'/item44', 'chapter':'3', 'related':['34','40','42','46']}
# dossierItems['45'] = {'image':'static/img/dossier2/dossier45.jpg', 'index':'45','title':'GREGORY VICTOR', 'route':'/item45', 'chapter':'3', 'related':['01','05','06','34','35','42','43']}
# dossierItems['46'] = {'image':'static/img/dossier2/dossier46.jpg', 'index':'46','title':'ATLANTIS MAP', 'route':'/item46', 'chapter':'3', 'related':['41','42']}
# dossierItems['47'] = {'image':'static/img/dossier2/dossier47.jpg', 'index':'47','title':'CONNOR SULLIVAN', 'route':'/item47', 'chapter':'4', 'related':['29','30','48','49','50','51','52','53','54','59']}
# dossierItems['48'] = {'image':'static/img/dossier2/dossier48.jpg', 'index':'48','title':'SELENE', 'route':'/item48', 'chapter':'4', 'related':['48','49','50','51','52','53','54','57','58']}
# dossierItems['49'] = {'image':'static/img/dossier2/dossier49.jpg', 'index':'49','title':'AT MAGNA CARTA', 'route':'/item49', 'chapter':'4', 'related':['46','50','51','52','53','54','55']}
# dossierItems['50'] = {'image':'static/img/dossier2/dossier50.jpg', 'index':'50','title':'AT HISTORY', 'route':'/item50', 'chapter':'4', 'related':['46','47','48','49','51','52','53','54','55']}
# dossierItems['51'] = {'image':'static/img/dossier2/dossier51.jpg', 'index':'51','title':'AENGUS', 'route':'/item51', 'chapter':'4', 'related':['46','47','48','49','50','52','53','54','55']}
# dossierItems['52'] = {'image':'static/img/dossier2/dossier52.jpg', 'index':'52','title':'AT ECONOMICS', 'route':'/item52', 'chapter':'4', 'related':['46','47','48','49','50','51','53','54','55']}
# dossierItems['53'] = {'image':'static/img/dossier2/dossier53.jpg', 'index':'53','title':'AT RELIGION', 'route':'/item53', 'chapter':'4', 'related':['46','47','48','49','50','51','52','54','55']}
# dossierItems['54'] = {'image':'static/img/dossier2/dossier54.jpg', 'index':'54','title':'AT PRODUCTION', 'route':'/item54', 'chapter':'4', 'related':['46','47','48','49','50','51','52','53','55']]}
# dossierItems['55'] = {'image':'static/img/dossier2/dossier55.jpg', 'index':'55','title':'AT MASTER PLAN', 'route':'/item55', 'chapter':'4', 'related':['46','47','48','49','50','51','52','53','54']]}
# dossierItems['56'] = {'image':'static/img/dossier2/dossier56.jpg', 'index':'56','title':'SALLY', 'route':'/item56', 'chapter':'4', 'related':['01','02','06','40','55','56']}
# dossierItems['57'] = {'image':'static/img/dossier2/dossier57.jpg', 'index':'57','title':'AT DRUG TRADE', 'route':'/item57', 'chapter':'4', 'related':['01','02','06']}
# dossierItems['58'] = {'image':'static/img/dossier2/dossier58.jpg', 'index':'58','title':'TRADE EMBARGO', 'route':'/item58', 'chapter':'4', 'related':['29','30']}
# dossierItems['59'] = {'image':'static/img/dossier2/dossier59.jpg', 'index':'59','title':'TERRORIST TRANSMITION', 'route':'/item59', 'chapter':'4', 'related':['29','30','39','46','50','54','57','60']}
# dossierItems['60'] = {'image':'static/img/dossier2/dossier60.jpg', 'index':'60','title':'INVENTED TERRORIST', 'route':'/item60', 'chapter':'4', 'related':['29','30','39','46','50','54','57','59']}


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




	