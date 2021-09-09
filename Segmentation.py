import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("persona.csv")
df.head()

df.info()
#Eksik verimiz yok ve 3 object 2 int değişkenlerimiz var.

df["SOURCE"].unique()
#2 tane android & iOS
df["PRICE"].nunique()
# 6 tane var.
df["PRICE"].value_counts()
# satışların sayısına bakıldı. en çok 29 birime satılmış.
df["PRICE"].groupby(df["COUNTRY"]).value_counts()


df["PRICE"].groupby(df["COUNTRY"]).agg("sum")
# Ülke bazında kazanılan rakamları aşağıda görebiliriz. En çok satış USA da bulunmakta.

df["PRICE"].groupby(df["SOURCE"]).value_counts()
#Android ve ios a göre kırılım yapılıp satış sayıları görüntülenmiştir.

df["PRICE"].groupby(df["COUNTRY"]).agg("mean")

df["PRICE"].groupby(df["SOURCE"]).agg("mean")
#ANDROID satışımız daha çok olmuş

df.groupby(["SOURCE","COUNTRY"]).agg({"PRICE":"mean"})
#Ülke kaynak kırılımında fiyat oratalamalarıı gördük, genel anlamda TUR android en yüksek fiyat ortalamasında.
#df.drop("RevenuebyCountry",inplace=True,axis=1)
#------GÖREV 2 ---------

df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg(["sum","mean"])
#hem toplam hem ortalama kazançları sıraladım ayrıca ortalamalara da bakacağız.
df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg("mean")
# Bu kırılımlarda ortalama kazançlar aşağıdadır.



#------GÖREV 3 ---------

agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg("mean")
agg_df = agg_df.sort_values(by="PRICE",ascending=False)

agg_df
#Çıktıyı agg_df olarak kaydettim ve price a göre sıraladım.

#------GÖREV 4 ---------

agg_df = agg_df.reset_index()
agg_df

#Indexler sıfırlandı, yeni indexlerimiz atandı.

type(agg_df)
agg_df.info()

#------GÖREV 5 ---------

agg_df["AGE"] = agg_df["AGE"].astype("object")


bins = [0,18,23,30,40,70]

lab = ["0_18", "19_23", "24_30", "31_40", "41_70"]

agg_df.head()

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"],bins,labels=lab)
agg_df.head()


#------GÖREV 6 ---------
agg_df.head()


agg_df["customer_level_based"] = [col[0] +"_" + col[1] +"_"+ col[2] + "_" +col[5] for col in agg_df.values]
agg_df.head()

persona = agg_df.groupby("customer_level_based").agg("mean")

persona.head()



#------GÖREV 7 ---------

agg_df["segment"] = pd.qcut(agg_df["PRICE"],4,labels=["D","C","B","A"])

agg_df.groupby("segment").agg(["sum","max","mean"])

agg_df.head()

CSegment = agg_df[agg_df["segment"]=="C"]

CSegment.head()
CSegment.describe().T
CSegment.min()
CSegment.groupby("SEX").agg("mean")
CSegment.groupby("AGE").agg("mean")

#Csegmentinde min ile max arasında büyük değişiklikler yok normal bir dağılım diyebiliriz fiyata göre
#cinsiyete göre kadınlar biraz olsun daha fazla ödeme yapıyor.
#yaşın küçük olması genellikle daha fazla getiri sağlıyor, kadınlara da biraz olsun daha çok hitap ediyorsa kız/kadınlara yönelik satışları veya paylaşımları olabilir.




#------GÖREV 7 son analiz ---------

agg_df.groupby("segment").agg(["sum","max","mean"])

new_cust = "tur_android_female_31_40"

d = agg_df.groupby("customer_level_based").agg(["sum","max","mean"])
d = d.reset_index()

d[d["customer_level_based"] == new_cust]
#agg_df[agg_df["AGE_CAT"] == "31_40" & agg_df["SOURCE"] == "android"]["customer_level_based"]

new_cust2 = "fra_ios_female_31_40"

d[d["customer_level_based"] == new_cust2]

agg_df[agg_df["customer_level_based"] == new_cust2]
agg_df[agg_df["customer_level_based"] == new_cust]

# Tur android kullanna kadın kullanıcının segmenti A olarak belirlendi ve min max değerlerini de d ile bakınca görebiliyoruz.
#Tur kullanıcı da 41.83 ortalama getiri sağlayacak.
#-----------------------------------------------------------------
# FRA olan kullanıcımız da C segmentinde bulunmakta, 33 birim ya da 32 birim getiri sağlayabilir.



