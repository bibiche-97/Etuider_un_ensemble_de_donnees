#!/usr/bin/env python
# coding: utf-8

# # Études des données provennant de l'enquête du National Instant Criminal Check System (NCIS) du FBI sur l'achat et le contrôle des armes à feu.
# 
# 

# # Introduction:
# 
# >Le NICS est utilisé pour déterminer si un acheteur potentiel est éligible pour acheter des armes à feu ou explosifs.Les armureries font appel à ce système pour s'assurer que chaque client n'a pas de casier judiciaire ou n'est pas autrement inéligible pour faire un achat.
# 
# >Les données contiennent le nombre de contrôles d'armes à feu par mois, États et type d'armes.Pour étudier l'ensembles des données provennant de l'enquête mener par le NCIS sur l'achat et le contrôle d'armes à feu nous allons explorer les données du fichier **gun_data.csv**. Notre analyse sera focaliser sur les réponses que l'on apportera aux questions posées dans les lignes qui suives.
# 

# # Questions:
# Pour etudier l'ensembles des données; nous tenterons de poser ces questions suivantes;
# 1. Quelles sont les types d'armes les plus achetés en moyenne ?
# 2. Quels États ont connu la plus forte croissance dans enregistrements d'armes à feu ?
# 3. Quelle est la tendance générale des armes à feu ?   
# > Dans les lignes qui suives nous allons proceder à la préparation des données

# # Préparations des données
# > Dans cette phase nous allons importer les modules necessaire pour l'analyse des données,charger les données,inspecter les données et néttoyer les données.

# ### Importations de l'ensemble des paquages et modules requisent pour le projet

# In[1]:


# import modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# > Dans cette cellule nous avons importer l'ensembles des modules qui nous serons utile pour la réussite de ce projet

# ### Chargement des données

# In[3]:


#load dataset
df_gun=pd.read_csv('data/gun_data.csv')


# ### Inspections des données

# #### Entête

# In[4]:


# entête du dataset
df_gun.head(10)


# > Ici vous voyez le resumer des 10 premiéres lignes du fichiers **gun_data.csv**

# #### Tailles

# In[5]:


## La tailes,le nombres de lignes et de colonnes 
print('Nombre de ligne et de colonne {}'.format(df_gun.shape))
print("Taille du fichier {}".format(df_gun.size))


# > Le dataset comptes en totale 12484 lignes,27 colonnes et une taille de 337095

# #### Les colonnes 

# In[8]:


#les colonnes du dataset
df_gun.columns


# > Ici on a l'ensembles des colonnes du dataset

# #### Typages des données

# In[9]:


#les differentes types des colonnes
df_gun.dtypes


# > Vous voyez les differentes types de l'ensembles des variables du dataset; On a des entiers **(int64)**, des flottants **(float64)** et des chaines de caractéres **(object)**

# #### Details sur les données

# In[10]:


# les details avec la fontions info() de Pandas
df_gun.info()


# > Cette cellules vous montre en details les differentes colonnes du dataset, le nombre de valeurs non-null et le types de chaque colonne. Parexemple ici la colonne **prepawn_handgun** est de type float et à **10542** valeurs non-null 

# #### Description ou statistique sur les données

# In[11]:


#statistique descriptives 
df_gun.describe()


# >On a les statistique descriptive comme le moyenne, la mediane, l'ecartype etc, des colonnes de types numeriques

# ### Nettoyages des données

# #### Check des valeurs manquantes

# In[13]:


#check des valeurs manquantes
print(df_gun.isna().sum())


# > Oups! On constate que l'on a beaucoup de valeur manquante parexemple la colone **permit_recheck** a 11385 valeur manquantes.
# On va proceder par la suppression des valeurs manquantes

# In[15]:


# je copy le dataframe df_gun dans df_gun_cp
df_gun_cp=df_gun.copy()
df_gun_cp.head(8)


# > Cette copie nous permettra de pouvoir la comparaison des deux dataframes apres le néttoyages des données

# #### Suppression des valeurs manquantes

# In[16]:


# suppression des valeurs manquantes
df_gun_cp.dropna(inplace=True)
sum(df_gun_cp.isnull().sum())


# > Ici on vient de supprimer toutes les valeurs manquantes

# #### Checks des valeus dupliquées

# In[17]:


# Valeur dupliqué
df_gun_cp.duplicated().sum()


# > Le dataset n'as pas de valeurs dupliquées

# #### Checks des valeurs uniques

# In[18]:


# Valeurs unique
df_gun_cp.nunique()


# #### Checks des valeurs abérrentes:
# > Ici on va utilisé le **Diagramme en moustâche** avec **seaborn.boxplot**. 
# > J'ai utilisé le Boxplot pour detecter les valeurs aberrantes dans l'ensemble des données et de pouvoir supprimé les valeurs extrêmes afin de faciliter l'exploration de l'analyse des données.Les graphes suivantes de resumés les variables de maniére simple et visuel, d'identifier les valeurs aberrentes et de comprendre la repartition des observations.

# In[19]:


def var_extreme(arg):
    sns.boxplot(x=arg,y='month',data=df_gun_cp)


# In[20]:


var_extreme('permit')


# > Repartition du **permit** en fonction du mois **month**

# In[21]:


var_extreme('permit_recheck')  


# >Repartition du **permit_recheck** en fonction de **month**

# In[22]:


var_extreme('returned_handgun')  


# In[23]:


var_extreme('returned_long_gun')  


# In[24]:


var_extreme('returned_other')


# In[25]:


var_extreme('handgun')  


# In[26]:


var_extreme('long_gun')


# In[27]:


var_extreme('other')


# In[28]:


var_extreme('redemption_long_gun')


# In[29]:


var_extreme('multiple')


# In[30]:


var_extreme('admin')


# In[31]:


var_extreme('prepawn_handgun')


# In[32]:


var_extreme('prepawn_long_gun')


# In[33]:


var_extreme('prepawn_other')


# In[34]:


var_extreme('redemption_handgun')


# In[35]:


var_extreme('redemption_other')


# In[36]:


var_extreme('rentals_handgun')


# In[37]:


var_extreme('rentals_long_gun')


# In[38]:


var_extreme('private_sale_handgun')


# In[39]:


var_extreme('private_sale_long_gun')


# In[40]:


var_extreme('private_sale_other')


# In[41]:


var_extreme('return_to_seller_handgun')


# In[42]:


var_extreme('return_to_seller_long_gun')


# In[43]:


var_extreme('return_to_seller_other')


# In[44]:


var_extreme('totals')


# #### Utilisation de la methode des quantiles pour supprimer les valeurs extrêmes

# In[45]:


# methode des quantiles
def methode_quartiles(col):
    g10 =df_gun_cp[col].quantile(0.10)
    g90 =df_gun_cp[col].quantile(0.90)
    df_gun_cp[col] = np.where(df_gun_cp[col]< g10, g10, df_gun_cp[col])
    df_gun_cp[col] = np.where(df_gun_cp[col]> g90, g90, df_gun_cp[col])
    sns.boxplot(x=col,y='month', data=df_gun_cp)
    plt.show()


# In[46]:


methode_quartiles('permit')


# In[47]:


methode_quartiles('permit_recheck')


# In[48]:


methode_quartiles('returned_handgun')


# In[49]:


methode_quartiles('returned_long_gun')


# In[50]:


methode_quartiles('returned_other')


# In[51]:


methode_quartiles('handgun')


# In[52]:


methode_quartiles('long_gun')


# In[53]:


methode_quartiles('other')


# In[54]:


methode_quartiles('redemption_long_gun')


# In[55]:


methode_quartiles('multiple')


# In[56]:


methode_quartiles('admin')


# In[57]:


methode_quartiles('prepawn_handgun')


# In[58]:


methode_quartiles('prepawn_long_gun')


# In[59]:


methode_quartiles('prepawn_other')


# In[60]:


methode_quartiles('redemption_handgun')


# In[61]:


methode_quartiles('redemption_other')


# In[62]:


methode_quartiles('rentals_handgun')


# In[63]:


methode_quartiles('rentals_long_gun')


# In[64]:


methode_quartiles('private_sale_handgun')


# In[65]:


methode_quartiles('private_sale_long_gun')


# In[66]:


methode_quartiles('private_sale_other')


# In[67]:


methode_quartiles('return_to_seller_handgun')


# In[68]:


methode_quartiles('return_to_seller_long_gun')


# In[69]:


methode_quartiles('return_to_seller_other')


# In[70]:


methode_quartiles('totals')


# #### suppression des valeurs extêmes avec la transformation algorithmique methode des log
# > Ici on traite simplement les variables dont leurs valeurs extrêmes n'ont pas été nettoyer par la methode des quartiles.

# In[71]:


#fonction avec log
def changement_dechelle(col):
    print("Transformation algorithmique")
    #les fonction log se trouve dans numpy
    df_gun_cp[col] = df_gun_cp[col]
    df_gun_cp[col] = df_gun_cp[col].map(lambda i: np.log(i) if i>0 else 0)
    sns.boxplot(x=col, y='month',data=df_gun_cp)
    plt.show()


# In[72]:


changement_dechelle('permit_recheck')


# In[73]:


changement_dechelle('returned_handgun')


# In[74]:


changement_dechelle('returned_long_gun')


# In[75]:


changement_dechelle('admin')


# In[76]:


changement_dechelle('returned_other')


# In[77]:


changement_dechelle('redemption_handgun')


# In[78]:


changement_dechelle('private_sale_handgun')


# In[79]:


changement_dechelle('private_sale_long_gun')


# In[80]:


changement_dechelle('private_sale_other')


# In[81]:


changement_dechelle('return_to_seller_handgun')


# In[82]:


changement_dechelle('return_to_seller_long_gun')


# #### Suppression des valeurs extrêmes 
# > On doit supprimer les valeurs extrêmes des variables n'ont pas été propre apres l'utilisation de la methode des **quartiles** et de la methode **log** 

# In[83]:


# fonction pour supprimer les valeurs extrêmes
def suppression_valeur(col):
    #Supprimer les valeurs externes(Conserver les valeurs interquartiles)
    print("Suppression des valeurs externes(Conservation des valeurs interquartiles) \n")
    q1 = df_gun_cp[col].quantile(0.25)
    q3 = df_gun_cp[col].quantile(0.75)
    index = df_gun_cp[(df_gun_cp[col]<q1) | (df_gun_cp[col] >q3)].index
    print(index)
    df_gun_cp.drop(index, inplace =True)
    sns.boxplot(x=col,y='month', data=df_gun_cp)
    plt.show()


# In[84]:


suppression_valeur('permit_recheck')


# In[85]:


suppression_valeur('admin')


# In[86]:


suppression_valeur('returned_other')


# In[87]:


suppression_valeur('private_sale_handgun')


# In[88]:


suppression_valeur('private_sale_other')


# In[89]:


suppression_valeur('private_sale_long_gun')


# In[90]:


suppression_valeur('return_to_seller_handgun')


# In[91]:


suppression_valeur('return_to_seller_long_gun')


# > Apres l'utilisation de l'ensemble des methodes pour la visualisation,l'observation et la suppression des valeurs extrêmes, On va passer à la suppression des colonnes inutiles où des colonnes que l'on peu s'en passer pour faire notre analyse.

# #### Suppression des colonnes inutiles
# > - admin
# > - permit_recheck
# > - returned_other
# > - rentals_long_gun
# > - rentals_handgun
# > - return_to_seller_handgun
# > - return_to_seller_long_gun
# > - return_to_seller_other
# > - private_sale_handgun
# > - private_sale_long_gun
# > - private_sale_other

# In[92]:


df_gun_cp.drop(['admin','permit_recheck','returned_other','rentals_long_gun','rentals_handgun',
                'return_to_seller_handgun','return_to_seller_long_gun','return_to_seller_other',
                'private_sale_handgun','private_sale_long_gun','private_sale_other'],axis=1,inplace=True)


# > La suppression des colonnes mentionner dans la cellules ci-dessus met fin notre étape de nettoyages des données. Ceci etant fait, nous allons passer a la phase de **l'analyses exploratoires des données**

# # Analyse Exploratoires des données

# Nous allons commencer par faire une petite comparaison des données avant et apres le nettoyages

# In[93]:


#Avant netoyages
print('*********** Avant le nettoyages nous avions {} lignes et {} colonnes et la tailles etait {} ********** '.format(df_gun.shape[0],df_gun.shape[1],df_gun.size))


# In[94]:


# apres nettoyages
print('*********** Aprés le nettoyages nous avons {} lignes et {} colonnes et la tailles est de {} ********** '.format(df_gun_cp.shape[0],df_gun_cp.shape[1],df_gun_cp.size))


# > Les données nettoyer seront enregsitrer dans un nouveau fichiers CSV

# In[95]:


# Enregstrement d'un nouveau fichier csv
df_gun_cp.to_csv('data/gun_data_clean.csv',index=False)


# In[96]:


# Lecture du nouveau fichier
df=pd.read_csv('data/gun_data_clean.csv')


# In[97]:


# utilisation de la methode tail() qui affiche les 5 derniers lignes du dataset 
df.tail()


# > Affichages des 5 derniers lignes du dataset avcc la methodes tail() de pandas; dans le celulles suivante nous allons voir les details du dataset

# In[98]:


df.info()


# > Les details sur les données; nous allons montrer les statistique descriptif des variables de types numériques;Ici on a 770 entrées (0 à 769).Vous avez aussi le nom des colonnes, leurs types et le nombres de valeurs non_null. Vous allez constater que l'on 770 entrées, toutes les colonnes on 770 valeurs non-null donc pas de valeurs null.

# In[99]:


df.describe()


# > Ici vous voyez les statistiques descriptives . La cellules suivantes vous montrera une vue globale sur la repartitins des données a l'aide d'un diagramme appelé histogramme de la methode **hist()** de pandas

# In[100]:


# Histogramme
df.hist(figsize=(40,36),legend=True)


# > Ici On a une vue globales sur l'ensembles des variables du dataset. Sur les cellules qui vont suivre nous allons tenter des repondres au questions qui ont été poser dans la phase question un peu en haut.

# ## Quelles sont les types d'armes  les plus achetés en moyenne?

# In[102]:


# la moyenne
print(" {} d'armes de poing sont utilisées en moyenne ".format(df['handgun'].mean()))
df.hist(legend=True,column='handgun',figsize=(10,8))


# > 7858.079999999994 d'armes de poing sont utilisées en moyenne . La repartition des armes de poings en moyenne
# 
# 

# In[103]:


print(" {} d'armes d'épaules sont utilisées en moyenne ".format(df['long_gun'].mean()))
df['long_gun'].hist(figsize=(10,8),legend=True)


# >  6021.217021276602d'armes d'épaules sont utilisées en moyenne. On a la repartitions d'armes d'épaules en moyenne
# 

# In[104]:


print("{} autres types d'armes sont utilisées en moyenne ".format(df['other'].mean()))
df['other'].hist(legend=True,figsize=(10,8))


# > 399.2817021276595 autres types d'armes sont utilisées en moyenne .Repartition d'autres types d'armes en moyennes

# In[105]:


handgun = df['handgun'].mean()
long_gun = df['long_gun'].mean()
other = df['other'].mean()
arme = np.array([handgun,long_gun,other])
plt.pie(arme,labels=['handgun','long_gun','other'])


# > On constate les types d'armes les plus achetés sont les armes de poing **(handgun)** ensuite vient les armes d'épaules **(long_gun)**

# ## Quels États ont connu la plus forte croissance dans enregistrements d'armes à feu ?

# In[106]:


df.groupby('state').handgun.mean()


# In[107]:


hand=df.groupby('state').mean().handgun
hand.plot(kind='bar',title='types armes par etats',color='orange',alpha=1)
plt.xlabel('Etat',fontsize=18,)
plt.ylabel('Arme de poing',fontsize=18)


# >Ce graphe visualise l'ensemble des armes de poing Enregsitré en moyenne dans chaque États

# In[108]:


df.groupby('state').mean().long_gun


# In[109]:


long=df.groupby('state').mean().long_gun
long.plot(kind='bar',title='types armes par etats en moye',color='green',alpha=1)
plt.xlabel('Etat',fontsize=18)
plt.ylabel('Arme d\'epaules',fontsize=18)


# > Ce graphe visualise l'ensemble des armes d'epaules Enregsitré en moyenne dans chaque États

# In[110]:


df.groupby('state').mean().other


# In[111]:


other=df.groupby('state').mean().other
other.plot(kind='bar',title='types armes par etats',color='blue',alpha=1)
plt.xlabel('Etat',fontsize=18)
plt.ylabel('Autres types d\'armes',fontsize=18)


# > Ce graphe visualise les autres types d'armes Enregsitré dans chaque États en moyennne.

# Ces graphes montre que les États comme **California,Colorado, Florida, Missouri, Texas,Tennessee,Virginia,Wisconsin** Ont connu le grandes nombres d'enregistrement d'armes de toutes types.
# 

# In[112]:


a=df.groupby(['handgun','long_gun','other']).count()['state']
a


# In[113]:


a.plot()
plt.suptitle('Achat de types par Etat')
plt.xlabel('State',fontsize=18)
plt.ylabel('Type armes',fontsize=18)
plt.show()


# In[118]:


b=df.groupby(['handgun','long_gun','other']).count()['month']
b


# In[119]:


b.plot()
plt.suptitle('Achat de types par mois')
plt.xlabel('month',fontsize=18)
plt.ylabel('Type armes',fontsize=18)
plt.show()


# ## Quelle est la tendance générale des armes ? 

# In[116]:


df[['handgun','long_gun','other']].mean()


# In[117]:


df[['handgun','long_gun','other']].plot(kind='bar')
plt.suptitle('Visualisation de la tendance des armes en generale')
plt.xlabel('Armes',fontsize=18)
plt.ylabel('Quantité',fontsize=18)
plt.show()


# > Ce Graphe explicite l'achat et le contrôle de l'ensemble des armes au sein du **NCIS** .Ceci montre la tendance generale des armes enregistrées

# # Conclusion

# In[120]:


# calcul la moyenne des types d'armes
lamda=np.array(df[['handgun','long_gun','other']].mean())


# In[121]:


plt.bar(['handgun','long_gun','other'],lamda,color=['red','green','blue'])
plt.suptitle('Achat moyenn des armes en fonction de leur types')
plt.xlabel('Types armes',fontsize=18)
plt.ylabel('Nombre Moyenne',fontsize=18)
plt.show()


# L'etude montre que les types d'armes le plus achetés par les acheteurs sont les armes poing (**handgun**).Le diagramme en bar utilisé montre une visualisation clair et nette sur l'achat des types d'armes en moyenne.

# In[122]:


long = df["long_gun"].max()
long


# In[123]:


# utilisation de la fonction query() de pandas
df.query('long_gun == 17932.8')


# In[124]:


hand =df["handgun"].max()
hand


# In[125]:


df.query('handgun == 28476.000000000004')


# > Les statistiques montrent que les Etats **Texas, California,Colorado, Florida, Missouri,Tennessee,Virginia,Wisconsin,Minnesota...**, on connue une nombre importante d'enregistrement d'arme à feu par mois. Donc le taux de criminalité est tres importantes dans ces zones.
# L'analyse montre aussi que le nombre d'armes contrôlés  aux sein du NCIS est tres éléves.

# ### Limites
# > Dans notre processus d'analyse nous avons rencontré certaines probléme:
# Parexemple la correlation entre les variables du dataset et ceci peut avoir un impact sur l'analyse des l'ensembles des données.

# In[126]:


df.corr()


# > Ici on constate la correlation 
# avec les variables du dataset est tres importantes et cela peu impacter sur les predictions à venir

# ## Réferences
# 
# <ul>
#     <li><a href="https://pandas.pydata.org/docs/">Pandas</a></li>
#     <li><a href="https://numpy.org/doc/">Numpy</a></li>
#    <li><a href="https://matplotlib.org/stable/tutorials/introductory/pyplot.html">Matplotlib</a></li>
#    <li><a href="https://seaborn.pydata.org/generated/seaborn.boxplot.html">Seaborn</a></li>
# </ul>

# In[ ]:




