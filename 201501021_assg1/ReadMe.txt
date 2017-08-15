Stop words are the words that doesn't have meaning of its own but have
importance when added to a sentence at appropriatly.
So for searching we can ignore stop words and also ignore it while creating the
index so its important to find stop words and remove them.

I tried detecting top 50 stop words I used different methods and analysed it in
following way :

1) In case of Bahasa Indonesia I calculated the frequency of each words from the
first 100000 pages of wikipedia dump and sorted them according to there frequency
and extracted the top 50 words by manually eliminating the words which are some
tag words and also a part of url (like : www, br, etc.).

2) In case of Hindi language I did the same process but I have used an ad-hoc
approach as it is my local language and I've enough knowledge of it and I noticed
that stop words in Hindi are of small word lenght so I also kept a limit on the
word length of the stop word (limit of maxLen : 4) and got good result as
compared to normal approach.

Expirements :
Tried to use other approaches like multiplying the word frequency of each word
with the number of pages that contains that word(to eliminate the context/subject
specific words) but the results are not as good as previous approach so I didn't
use it for finding the final result.

Result for Bahasa Indonesia :
dan
yang
di
dari
dengan
pada
ini
dalam
adalah
untuk
tahun
oleh
sebagai
ke
cite
Indonesia
atau
bahasa
Kabupaten
tidak
menjadi
publisher
juga
Berkas
itu
accessdate
negara
merupakan
kota
orang
Kota
Bahasa
memiliki
lebih
dapat
tersebut
Pada
satu
daerah
telah
seperti
nbsp
lain
Kategori
bahwa
wilayah
sebuah
Jawa
besar
antara


Result for Hindi :
के
में
की
नया
का
और
है
से
को
एक
पर
भी
लिए
यह
हैं
इस
भारत
ने
किया
कि
नहीं
कर
गाँव
गया
ही
जो
जाता
रूप
करने
हो
या
तो
साथ
तथा
था
अपने
बाद
जिला
जिले
होता
तक
नाम
एवं
कुछ
वह
लेख
जा
आधार
अन्य
भाषा
