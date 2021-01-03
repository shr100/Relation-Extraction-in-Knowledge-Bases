from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score
import csv
import glob
import warnings
import numpy as np
from sklearn import metrics
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import sklearn

def logistic_regressor():
	Xtrain = []
	ytrain = []

	list_of_ip = glob.glob("K_means/*.txt")
	for ip in list_of_ip:
		if(ip == "K_means/people.person.children_pos.txt"):
			f1 = open("K_means/people.person.children_pos.txt","r")
			pos1 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.children_neg.txt"):
			f1 = open("K_means/people.person.children_neg.txt","r")
			neg1 = f1.readlines()
			f1.close()

		if(ip == "K_means/government.political_party.politicians_in_this_party_pos.txt"):
			f1 = open("K_means/government.political_party.politicians_in_this_party_pos.txt","r")
			pos2 = f1.readlines()
			f1.close()

		if(ip == "K_means/government.political_party.politicians_in_this_party_neg.txt"):
			f1 = open("K_means/government.political_party.politicians_in_this_party_neg.txt","r")
			neg2 = f1.readlines()
			f1.close()

		if(ip == "K_means/education.educational_institution.students_graduates_pos.txt"):
			f1 = open("K_means/education.educational_institution.students_graduates_pos.txt","r")
			pos3 = f1.readlines()
			f1.close()

		if(ip == "K_means/education.educational_institution.students_graduates_neg.txt"):
			f1 = open("K_means/education.educational_institution.students_graduates_neg.txt","r")
			neg3 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.film.genre_pos.txt"):
			f1 = open("K_means/film.film.genre_pos.txt","r")
			pos4 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.film.genre_neg.txt"):
			f1 = open("K_means/film.film.genre_neg.txt","r")
			neg4 = f1.readlines()
			f1.close()

		if(ip == "K_means/business.company.industry_pos.txt"):
			f1 = open("K_means/business.company.industry_pos.txt","r")
			pos5 = f1.readlines()
			f1.close()

		if(ip == "K_means/business.company.industry_neg.txt"):
			f1 = open("K_means/business.company.industry_neg.txt","r")
			neg5 = f1.readlines()
			f1.close()

		if(ip == "K_means/award.award_honor.award_winner_pos.txt"):
			f1 = open("K_means/award.award_honor.award_winner_pos.txt","r")
			pos6 = f1.readlines()
			f1.close()

		if(ip == "K_means/award.award_honor.award_winner_neg.txt"):
			f1 = open("K_means/award.award_honor.award_winner_neg.txt","r")
			neg6 = f1.readlines()
			f1.close()

		if(ip == "K_means/book.written_work.author_pos.txt"):
			f1 = open(ip,"r")
			pos7 = f1.readlines()
			f1.close()

		if(ip == "K_means/book.written_work.author_neg.txt"):
			f1 = open(ip,"r")
			neg7 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.actor.character_pos.txt"):
			f1 = open(ip,"r")
			pos8 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.actor.character_neg.txt"):
			f1 = open(ip,"r")
			neg8 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.actor.film_pos.txt"):
			f1 = open(ip,"r")
			pos9 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.actor.film_neg.txt"):
			f1 = open(ip,"r")
			neg9 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.film.directed_by_pos.txt"):
			f1 = open(ip,"r")
			pos10 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.film.directed_by_neg.txt"):
			f1 = open(ip,"r")
			neg10 = f1.readlines()
			f1.close()

		if(ip == "K_means/organization.company_acquired.acquiring_company_pos.txt"):
			f1 = open(ip,"r")
			pos11 = f1.readlines()
			f1.close()

		if(ip == "K_means/organization.company_acquired.acquiring_company_neg.txt"):
			f1 = open(ip,"r")
			neg11 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.film.production_companies_pos.txt"):
			f1 = open(ip,"r")
			pos12 = f1.readlines()
			f1.close()

		if(ip == "K_means/film.film.production_companies_neg.txt"):
			f1 = open(ip,"r")
			neg12 = f1.readlines()
			f1.close()

		if(ip == "K_means/music.artist.album_pos.txt"):
			f1 = open(ip,"r")
			pos13 = f1.readlines()
			f1.close()

		if(ip == "K_means/music.artist.album_neg.txt"):
			f1 = open(ip,"r")
			neg13 = f1.readlines()
			f1.close()

		if(ip == "K_means/music.group_member.group_pos.txt"):
			f1 = open(ip,"r")
			pos14 = f1.readlines()
			f1.close()

		if(ip == "K_means/music.group_member.group_neg.txt"):
			f1 = open(ip,"r")
			neg14 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.deceased_person.place_of_death_pos.txt"):
			f1 = open(ip,"r")
			pos15 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.deceased_person.place_of_death_neg.txt"):
			f1 = open(ip,"r")
			neg15 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.ethnicity_pos.txt"):
			f1 = open(ip,"r")
			pos16 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.ethnicity_neg.txt"):
			f1 = open(ip,"r")
			neg16 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.family_pos.txt"):
			f1 = open(ip,"r")
			pos17 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.family_neg.txt"):
			f1 = open(ip,"r")
			neg17 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.nationality_pos.txt"):
			f1 = open(ip,"r")
			pos18 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.nationality_neg.txt"):
			f1 = open(ip,"r")
			neg18 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.parents_pos.txt"):
			f1 = open(ip,"r")
			pos19 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.parents_neg.txt"):
			f1 = open(ip,"r")
			neg19 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.place_of_birth_pos.txt"):
			f1 = open(ip,"r")
			pos20 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.place_of_birth_neg.txt"):
			f1 = open(ip,"r")
			neg20 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.profession_pos.txt"):
			f1 = open(ip,"r")
			pos21 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.profession_neg.txt"):
			f1 = open(ip,"r")
			neg21 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.sibling_pos.txt"):
			f1 = open(ip,"r")
			pos22 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.sibling_neg.txt"):
			f1 = open(ip,"r")
			neg22 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.spouse_pos.txt"):
			f1 = open(ip,"r")
			pos23 = f1.readlines()
			f1.close()

		if(ip == "K_means/people.person.spouse_neg.txt"):
			f1 = open(ip,"r")
			neg23 = f1.readlines()
			f1.close()

		if(ip == "K_means/sports.team.pro_athlete_pos.txt"):
			f1 = open(ip,"r")
			pos24 = f1.readlines()
			f1.close()

		if(ip == "K_means/sports.team.pro_athlete_neg.txt"):
			f1 = open(ip,"r")
			neg24 = f1.readlines()
			f1.close()

		
	for item in pos1:
		Xtrain.append(item)
		ytrain.append(1)
	for item in neg1:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos2:
		Xtrain.append(item)
		ytrain.append(2)
	for item in neg2:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos3:
		Xtrain.append(item)
		ytrain.append(3)
	for item in neg3:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos4:
		Xtrain.append(item)
		ytrain.append(4)
	for item in neg4:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos5:
		Xtrain.append(item)
		ytrain.append(5)
	for item in neg5:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos6:
		Xtrain.append(item)
		ytrain.append(6)
	for item in neg6:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos7:
		Xtrain.append(item)
		ytrain.append(7)
	for item in neg7:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos8:
		Xtrain.append(item)
		ytrain.append(8)
	for item in neg8:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos9:
		Xtrain.append(item)
		ytrain.append(9)
	for item in neg9:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos10:
		Xtrain.append(item)
		ytrain.append(10)
	for item in neg10:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos11:
		Xtrain.append(item)
		ytrain.append(11)
	for item in neg11:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos12:
		Xtrain.append(item)
		ytrain.append(12)
	for item in neg12:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos13:
		Xtrain.append(item)
		ytrain.append(13)
	for item in neg13:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos14:
		Xtrain.append(item)
		ytrain.append(14)
	for item in neg14:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos15:
		Xtrain.append(item)
		ytrain.append(15)
	for item in neg15:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos16:
		Xtrain.append(item)
		ytrain.append(16)
	for item in neg16:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos17:
		Xtrain.append(item)
		ytrain.append(17)
	for item in neg17:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos18:
		Xtrain.append(item)
		ytrain.append(18)
	for item in neg18:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos19:
		Xtrain.append(item)
		ytrain.append(19)
	for item in neg19:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos20:
		Xtrain.append(item)
		ytrain.append(20)
	for item in neg20:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos21:
		Xtrain.append(item)
		ytrain.append(21)
	for item in neg21:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos22:
		Xtrain.append(item)
		ytrain.append(22)
	for item in neg22:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos23:
		Xtrain.append(item)
		ytrain.append(23)
	for item in neg23:
		Xtrain.append(item)
		ytrain.append(0)

	for item in pos24:
		Xtrain.append(item)
		ytrain.append(24)
	for item in neg24:
		Xtrain.append(item)
		ytrain.append(0)




	Xtest = []
	ytest = []
	with open("Test_data/test.csv") as file:
		readcsv = csv.reader(file)
		for row in readcsv :
			if(row[1]=="CHILD_OF"):
				Xtest.append(row[0])
				ytest.append(1)

			elif(row[1]=="POLITICAL_AFFILIATION"):
				Xtest.append(row[0])
				ytest.append(2)

			elif(row[1]=="EDUCATED_AT"):
				Xtest.append(row[0])
				ytest.append(3)

			elif(row[1]=="NATIONALITY"):
				Xtest.append(row[0])
				ytest.append(18)

			elif(row[1]=="PLACE_OF_BIRTH"):
				Xtest.append(row[0])
				ytest.append(20)

			elif(row[1]=="SPOUSE"):
				Xtest.append(row[0])
				ytest.append(23)

			else:
				Xtest.append(row[0])
				ytest.append(0)



	#vect = CountVectorizer(analyzer = "word", min_df=5, ngram_range=(1, 1),token_pattern = "\s*\-\>\s[a-z0-9\/]*\s\([a-z:]+\)")
	#vect = CountVectorizer(analyzer = "word", min_df=5, ngram_range=(1, 1),token_pattern = "\s[A-Za-z0-9]*")
	vect = CountVectorizer(analyzer = "word", min_df=5, ngram_range=(1, 1))
	# vect = CountVectorizer(min_df=5, ngram_range=(1, 1))
	X_train = vect.fit(Xtrain).transform(Xtrain)
	#print(vect.get_feature_names())
	#vect = CountVectorizer(analyzer = "word", min_df=5, ngram_range=(1, 1))
	X_test=vect.transform(Xtest)
	X_train = X_train.tocsc(X_train)
	X_test = X_test.tocsc(X_test)
	#X_scaled = sklearn.preprocessing.scale(X_train,with_mean=False)
	scaler = StandardScaler(with_mean=False)
	scaler.fit(X_train)
	#print("Mean : ",scaler.mean_[0])
	X_scaled = scaler.transform(X_train)
	X_train = X_scaled
	#scaler.fit(X_test)
	Xtest_scaled = scaler.transform(X_test)
	X_test = Xtest_scaled
	#print("Mean : ", X_scaled.mean(axis = 0))
	#print("Var : ", X_scaled.var(axis = 0))
#	print("Xtrain sample : ",X_train[273825, 15591])
	#print("Xtest sample scaled : ",X_test)
	print("Scaling done")

	param_grid = {'C': [0.001, 0.01, 0.1, 1, 10]}
	print("Before Grid search")
	grid = GridSearchCV(LogisticRegression(penalty='l2', dual = False,solver='lbfgs',random_state=0,multi_class='auto',fit_intercept=True,max_iter = 20000), param_grid, cv=10)
	print("Before Grid fit")
	grid.fit(X_train, ytrain)
	print("After Grid fit")
	best_score = grid.best_score_ * 100
	print("Best cross-validation score for logistic regression : " +str(best_score))
	print("Best parameters: ", grid.best_params_)

   #Training our model with the best estimator and determining accuracy scores from the predictions
	if(grid.best_params_['C'] == 0.001):
		clflr=LogisticRegression(penalty='l2', dual = False, C=0.001,solver='lbfgs',random_state=0,multi_class='auto',fit_intercept=True,max_iter = 20000)

	if(grid.best_params_['C'] == 0.01):
		clflr=LogisticRegression(penalty='l2',dual = False,C=0.01,solver='lbfgs',random_state=0,multi_class='auto',fit_intercept=True,max_iter = 20000)

	if(grid.best_params_['C'] == 0.1):
		clflr=LogisticRegression(penalty='l2',dual = False,C=0.1,solver='lbfgs',random_state=0,multi_class='auto',fit_intercept=True,max_iter = 20000)

	if(grid.best_params_['C'] == 1):
		clflr=LogisticRegression(penalty='l2',dual = False,C=1,solver='lbfgs',random_state=0,multi_class='auto',fit_intercept=True,max_iter = 20000)

	if(grid.best_params_['C'] == 10):
		clflr=LogisticRegression(penalty='l2',dual = False,C=10,solver='lbfgs',random_state=0,multi_class='auto',fit_intercept=True,max_iter = 20000)

	print("Before Log fit")
	clflr.fit(X_train, ytrain)
	print("Before Log predict")
	y_pred=clflr.predict(X_test)

	acc = accuracy_score(y_pred, ytest)
	print('\nAccuracy : ', acc*100)
	np.set_printoptions(threshold=sys.maxsize)
	print("Full confusion matrix : ",confusion_matrix(ytest, y_pred))
	print("Labelled confusion matrix : ",confusion_matrix(ytest, y_pred,labels=[0,1,2,3,18,20,23]))

	precision = metrics.precision_score(ytest, y_pred, average='weighted', labels=[0,1,2,3,18,20,23])
	print("Precision : ", precision)
	with warnings.catch_warnings():
		warnings.filterwarnings("ignore")
	recall = metrics.recall_score(ytest, y_pred, average='weighted', labels=[0,1,2,3,18,20,23])
	print("Recall : ",recall)
	beta=0.5
	# beta less than 1 to favour precision
	F1=((beta**2+1)*precision*recall)/(((beta**2)*precision)+recall)
	print("\nF1 Score for Logistic Regressor :", F1*100)



def main():
	logistic_regressor()
main()
