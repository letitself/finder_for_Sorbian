from bs4 import BeautifulSoup
import requests
import csv


text = '''
3	Abela je woženjeny a ma jednu dźowku.
4	Ablatiw w rozdźělnych rěčach móže tež instrument, čas, wašnje čina wuprajić.
5	Ablatiw wupraji w finšćinje pohibowanje potrjecheneho městna (talolta - "wot doma").
6	“ abo tež „Paris wuchoda“).
7	Ada pak poskića přidatnje móžnosć datoweje abstrakcije z pomocu abstraktnych datowych typow.
8	Adjektiw dyrbi w gramatiskim genusu mjenu roda wotpowědować a připodobnje so tež wotpowědnje při změnje roda.
9	Adjektiwy na -er maja wariantu -rim/us/-um/-a, mjeztym zo adjektiwy na l maja -lim/us/-um/-a.
10	Adjektiwy z jednozłóžkowym zdónkom, kaž na př.
11	Adresowa kniha z lěta 1901 podawa za Kopšin slědowace swójby: Jakub Bjer (Behr, čo.
12	Adresowa kniha z lěta 1901 podawa za Nuknicu slědowace swójby: Donatec (Jakub, čo.
13	A dźěłajo nawuknychu nowe teksty spěwow připódla a po wječorach.
14	AfD dóstanje k prěnjemu razej při krajnych wólbach wjace hłosow hač CDU.
15	Afriski wopiči chlěbowc je štom.
16	“ a garantowaše jej prawo na swójske narodne wuwiće.
17	& A.Gray: Z jednej družinu w Kaliforniskej ale tež Arizona a třomi družinami w Delnjeje Kaliforniskej.
18	Ajapóma, "Hižo sym činił".
19	A ja som z nima raz sobu jěł na to huworowanje na Doły na te dlejke góry hot Syjańskeje drogi.
20	A jeli pak žadyn reelny korjeń njeeksistuje.
21	Akademiskeho towarstwa za łužiske stawizny a rěče a starši serbskeje sekcije.
22	Akkadska rěč (akkadistika), (wuchodo)semitiska (t. r. z arabšćinu přiwuzna rěč Babylonjanow a Assyričanow, je so něhdy w Mezopotamiskej (Irak, Syriska) rěčała, wyše toho w cyłkownej Prědnjej Aziji z wašnjom a wot 3. hač do 1. lěttysaca př.
23	Akkadska rěč wutłóči sumerišćinu jako rěčanu rěč; sumerišćinu wšak wužiwachu dale jako sakralnu, ceremonialnu, literarnu rěč a jako rěč wědomosće.
24	Aktiwne koparske towarstwo w měsće je NK SOŠK.
25	Aktualna HTML-wersija (4.01) bu w lěću 1997 k W3C-poručenju wuzwolena a definuje jenož rěč jako SGML-nałoženje.
26	Aktualna wersija je 38.0.1 wot 11. junija 2015.
27	Aktualnje pak so wo přichodźe łužiskich wotkrytych jamow diskutuje.
28	Albanšćina pisa so konsekwentnje fonetisce.
29	Albertec a wopytowaše wot 1898 do 1904 Krajnostawski wučerski seminar w Budyšinje.
30	Albrechtowce přiběži tule z juha Stara woda.
31	Ale ani potom na knjejstwje pokoj njeběše.
32	Ale běłe sydlerjo su drjewo za twarjenje domow wužiwali.
33	Ale dokelž mějachu jenož jara mało dokumentow w tutym pismje a rěč, kotraž je so z nim napisała, njebě znata, bě dešifrowanje dlěše a sprócniwše hač za třeću špaltu.
34	"Ale dwě dźěsći nochcetej jěsć."
35	Ale hižo krótki čas po tym běchu zdźělenki, po kotrychž zhotowjerjo tutón samozawjazk łamaja.
36	Ale hižo w lěću 1940 buchu zbytki z terciera namakane.
37	Ale jich płodowe mjaso je jenož po wohrěwanju jědźna.
38	Ale mištr jemu wotmołwi: „Tajkich wurěčow dla mje zrěčniwi ludźo twojeho razu wograwaja.“
39	Ale nětko 'Tok Pisin' je akceptowane mjeno rěče.
40	Ale njeje móžno, nałoženja z Google Play Store na druhim systemje hač Android sćahnyć (na př. na normalnym PC), zo by je potom přez USB na Androidowym graće instalowało.
41	Ale po Herće njeje zbožo na swěće ničo trajace, wona je předstawy woneho swěta wo raju měła.
42	Ale poslednja złóžka wostanje njepřizwučna.
43	Ale při njeporjadnym wurjekowanju so wokale připodobnjuja, kaž na př.
44	Ale rozšěrjene sorty su zwjetša bóle kompaktne.
45	Ale so jenož wot něhdźe 70 maćernorěčnikow rěči, tak zo je wohrožena rěč.
46	Ale tež eksistuja žiwochi, kotřiž njetrjebaja kislik, předewšěm při jednobańkowcach.
47	Ale tež na čistej skale wustupuje.
48	Ale tež słód wotwisuje wot družiny a sorty.
49	Ale tež we druhich kóncach swěta wón so rozpřezdrěwaše.
50	Ale twarjenja njeběchu jeničke dźěłowe polo brigady.
51	Ale we woprawdźitosći zakaza wočiwidna wšelakorosć dale přińć, hač k někotrym njedospołnym grupam znamješkow.
52	Ale we wurytych namakanišćach wěnowachu wosebje pomnikam a zanjechachu zwjetša bydlenske štwórće hač na někotre wuwzaća (Ur, Ugarit, Hacilar).
53	Ale wjetše mnóstwa wjedu k běhawje a bluwanju a móžeja dla tworjenja kalciumoweho oksalata škody na jěrchenjow zawinować.
54	Ale w nocy krónowe łopješka su rozšěrjene a kćenja hyacintojće wonjeja.
55	Ale wobchowuje so po konwenciji, doniž so specialisća na chronologiju njedojednaja, kotraž tuchwilu hišće njeje widźeć.
56	Ale wón toho wysokosć njedocpěje.
57	Ale wot lěta 1981 jeje nałožowanje je zakazane.
58	Ale wotstawk na čopomaj (111,694 km/°) je přez wopłonjenje zemje snadnje wjetši hač na ekwatorje (110,574 km/°), dokelž křiwizna na tutym puću wo wok.
59	Ale za nje eksistuje znamješka w IPA-symbole.
60	Alfabet wot Toki Pona je na 14 pismikow wobmjezowany.
61	Alfons Handrik: Wučer Jurij Wjela w Komorowje spomóžnje skutkował.
62	Algirdas Butkevičius je woženjeny a ma jednu dźowku.
63	Alkaloid akonitin najprjedy nerwy rozbudźi a potom lemi.
64	Alnus rugosa) je štom ze swójby brězowych rostlinow (Betulaceae).
65	Alojs Andricki (
66	Alojs Andricki (1914–1943).
67	Alpski dźećel je naha, wjacelětna, zelišćowa, bjezstołpikata rostlina, kotraž docpěje wysokosć mjezy 5 a 15 cm.
68	Alpski dźećel je wot sewejrošpaniskeje horinow hač do Siebenbürgen rozšěrjeny, ale faluje w sewjernych wapnowych Alpach Awstriskeje a Bayerskeje, a južnych wapnowych Alpach wuchodnje wot Sexten.
69	Alpski dźećel ma dwě warianće.
70	Alpski pryšćenc je wity kerčk, kotryž ma 2 m dołhe lězucymi, wodrjewjacymi wubitkami.
71	"Altherrenverband", kotryž polěpši financielnu situaciju towarstwa.
72	Amaconasowu nižinu z najwjetšim tropiskim dešćowym lěsom swěta.
73	Amboparapa pe ogyke, "ja sćěnu kompletnje molowach" Hesakãmba „Wono je dospołnje jasne.“
74	Američenjo běchu teritorij hakle w lěće 1867 wot Rusow kupili.
75	Amurritišćina, ugaritišćina, fenicišćina a staroaramejšćina (aramejšćina), su štyri w Syriskej rěčane sewjerozapadosemitiske rěče z 2. a 1. lěttysaca př.
76	Andricki so wobstajnje spjećowaše z nacionalsocialistami hromadźe dźěłać a bu 2. oktobra 1941 z Drježdźan do Dachauskeho koncentraciskeho lěhwa transportowany.
77	Andricki wopytowaše 1921 ludowu šulu w Radworju, hdźež běše jeho nan šulski nawoda.
78	Android wobsahuje jadro Linux, njeje wšak klasiska distribucija Linux, kaž su za desktop a serwer znate.
79	Angela Merkel běše wot 10. apryla zwjazkowa předsydka swojeje strony.
80	Anita Lehtola bě hač do lěta 2000 tež čłon wot Hedningarna.
81	Anona (Annona cherimola) je rostlina ze swójby anonowych rostlinow (Annonaceae).
82	Ansambl z Michałskeje cyrkwje a Stareje wodarnje je symbol města Budyšina a jedyn z najwoblubowanišich motiwow w sakskim turistiskim wabjenju.
83	Apache OpenOffice je swobodna běrowa software, kotraž wot paketa OpenOffice.org pochadźa.
84	Apfel je bjezkonfesionelny, ženjeny a nan třoch dźěći.
85	A prěni nowoh domu dźěłaćeŕ.
86	Aprikozowc je w lěću zeleny štom, kotryž docpěwa wysokosć wot 4 hač do 8 (10) m.
87	Archangelsk ma někak tři sta pjećdźesat tysac wobydlerjow.
88	Argentinska ma něhdźe 43 milionow wobydlerjow.
89	Aristolochijowa kisalina změni herbske kajkosće a móže tumory wuwabjeć.
90	Arnošt Černik bě nan dźowki a dweju synow.
91	Arnošt Černik ličeše 1956 hišće 9 % wobydlerstwa Spytečanskeje gmejny jako Serbow.
92	Arnošt Černik ličeše 1956 jenož hišće 7 % wobydlerstwa gmejny jako Serbow.
93	Arnošt Černik zwěsći 1956 serbskorěčny podźěl wobydlerstwa wot jenož hišće 33,1 %.
94	Arnošt Muka postaji Andrickeho 1896 za redaktora časopisa „
95	Arnošt Muka: Statistika łužiskich Serbow.
96	Artikl a předłóžku móžemy wurjekować tež kaž dwě słowje, na přikład: kin su, de su, in su.
97	Artikulaciske městno sćěhuje z poslednjeho tutych konsonantow.
98	Asam je swojeho čorneho čaja dla swětodaloko znaty.
99	Assyriska, Babyloniska a Sumer pěstowachu dalokosahace politiske poćahi k susodnym krajam, kotrež buchu tež zdźěla za prowincy mezopotamiskich jadrowych krajow deklarowane.
100	Ast płaći jako wuběrny prědar a dobry přełožowar kěrlušow.
101	;Astronomiska šěrokosć : kut mjez woprawdźitym lotowym směrom a ekwatorowej runinu (njebjeski ekwator).
102	A tak jo mój nan póten to Słabcyc pół žywnosći krynuł, a na tej su byli wěkšy dźěl lute lěda a mało role; a wónej stej byłej jeno dwě peršonje na cyłej žywnosći a njejstej mogłej hobstać a doprjodka pćić a stej lědym tu półowicu hobdźěłałej.
103	A ten wuj jo był mójeje maćerje bratr a mój kmótr, a ta ćota jo była mójeje maćerje sostra, a tak su byli bratry a sostry wše wót jeneje maćerje.
104	Athen je na wobydlerjow a płoninu najwjetše město kraja, přiwšěm pak je gmejna Athen w centrumje kopjenišća Athen-Piraeus poměrnje mała.
105	A to běšo jěšće někotere lěta pjerjej togo drogego lěta…
106	A to: hromadźe pisane a rozdźělene pisane kompozicije.
107	A to je jeje poselstwo za swójby.
108	Atomowe tyłowy metala (atomy bjez wonkownych elektronow) so zwjazuja k metalowemu lěsycy.
109	Atomy su w molekulach přez zhromadne elektronowe poriki zwjazane.
110	A wone steja po dwěmaj na krótkich wurostkach a docpěwaja dołhosć wot 3 hač 7 cm.
111	Awstralski indigo je kerk ze swójby łušćinowcow (łaćonsce: Indigofera australis, Fabaceae).
112	Awtochtone wobydlerstwo słuša do ludu Nencow, kiž je hłownje wot plahowanja sobow žiwy.
113	Awtor studije ma podhlad, zo staj internetowa pornografija a wumocowanje substitutaj, potajkim to jedne narunanje druheho.
114	Babylonskej, kotrež antiksku mezopotamisku kulturu wobchowachu.
115	Baczyński spřećeli so w lěće 1940 ze spisowaćelom Jerzymom Kamilom Weintraubom.
116	Badiski dźećel je hódnotna picowanska rostlina.
117	Bahnowa drěstka je jednolětna rostlina, kotraž docpěwa wysokosć wot 10 hač 45 cm.
118	Bahnowa smjetanka je wjacelětna, zelišćowa rostlina, kotraž docpěwa wysokosć wot 2 m (50-150cm).
119	Bahnowy hróšik docpěwa wysokosć wot 30 hač 100 cm.
120	Bahnowy žiwotnik docpěwa wysokosć wot 60 hač do 120 cm.
121	Bakterije su předewšěm mikroorganizmy.
122	Bałcar zawostaji tři wobšěrne rukopisne dźeniki, kotrež su wažne stawizniske a kulturnostawizniske žórła.
123	Bandmann bu jako direktny kandidat swojeje strony w lěće 2009 z 38,4 % woleny.
124	Banjowcowe rostliny (Cucurbitaceae) su swójba symjencowych rostlinow.
125	Banjul je stejišćo najwjetšeje mošeje w Gambiji kaž tež sydło romsko-katolskeho biskopstwa.
126	Bańkowe membrany wužiwaja tutu kajkosć z by starosćiwje kontrolowali wzajomne skutkowanje mjez swojimi wobsahami a eksternymi chemiskimi wěcami.
127	Banks je tutu skupinu do třoch skupinow Rhyniophyta, Trimerophytophyta a Zosterophyllophyta rozpačił.
128	Bantuske ludy předstaja po zdaću jadro železočasoweje Urewe-kultury, kotraž bě w regionje wulkich wuchodoafriskich jězorow rozšěrjena.
129	Barba je jasno- hač ćěmnozelena, jednobarbiće zelena abo z kremobarbitymi blečkami, abo cyło běła.
130	Barbizna so za barbjenje cyroby (butra, šokolada, twarožk) a tekstilijow wužiwa.
131	Baribal je zwjetša čornobruny a docpěje dołhosć wot 1,5 hač do 1,8 m. Při tym je mjeńši a bóle zawality hač bruny mjedwjedź.
132	Bariki su w nocy aktiwne.
133	Barok je historiski směr wuměłstwa, kotryž bě popularny wot kónca 16. lětstotka hač do spočatka 18. lětstotka, wot kónca renesansy hač do spočatka rokoka.
134	Barokny knježi dom z dźewjeć wóskami a jednymi schodami pod hołym njebjom.
135	Bartl bě wot 1969 do 1971 inoficielny sobudźěłaćer statneje bjezstrašnosće NDR.
136	Baseń ma pjeć linkow w kóždej štučce, melodija k tomu wopřija sydom taktow z nataktom.
137	Basnje a spisał wulcy wažne knihe.
138	Bazlik je jednolětna rostlina, kotraž docpěwa wysokosć wot 20 - 30 cm.
139	Bazlik wužiwa so předewšěm w italskej kuchinje.
140	Bazowe łopjena łučneho šišmanca su kulojte, dołhostołpikate a jenož hač do połojcy dźělene.
141	Beata Szydło je zmandźelena a ma dweju synow.
142	Bě čas bipolarneho swětoweho porjada a horceje wójny započał.
143	Bě centrum Awarskeho chanstwa (XII – 1864).
144	Běchu fazy, kotrež buchu přez wulke mócnarstwa dominowane a druhe, w kotrychž mocy ze susodnych regionow dobywanske wójnske wuprawy wjedźechu.
145	Běchu hač do lěta 1957 samostatna gmejna.
146	Běchu to Budyske tachantstwo, Budyske krajne bohotstwo a feudalne knjejstwo, wot kotrychž měješe kóžde dwaj burskej statokaj.
147	Běchu to poslednje wólby we wjacestronskim systemje.
148	Běchu wone prěnjotnje jenož wotwodźenki z křćenskich mjenow za priwatne wužiće, móžachu so pozdźišo ze samostatnymi křćenskimi mjenami stać.
149	Beethoven słuša hač do dźensnišeho k najznatym komponistam na swěće.
150	Běła brěza je zhorbjeny hač přewisowacy štom, kotryž docpěje wysokosć wot 25 (20-30) m.
151	Běła čapla (Casmerodius albus, syn.: Ardea alba) je ptak ze swójby Ardeidae.
152	Běła čapla ma běłe pjerinu.
153	Běła cycawka je wjacelětna, zelišćowa, zymokruta rostlina.
154	Běła jěrowc je na sewjernej balkanskej połkupje rozšěrjeny.
155	Běła Lederhaut (Sclera) leži w zadnim wobłuku wóčneho jabłuka.
156	Belfast je sydło katolskeho a anglikanskeho biskopa kaž tež uniwersitne a přistawne město.
157	Belgica 23, 1827), dokelž najprjedy wužiwane mjeno Kali soda Moench na zakładźe staršeho, k priority woprawnjeneho homonyma Kali soda Scop., kotryž synonym wot Salsola soda je, njepłaćiwe je.
158	Belka porodźi małeho čerwjeneho haplka z běłym znamjenjom na prědnej noze.
159	Běły dźećel je přecozelena, trawnikojće rosćaca rostlina z nižoležacym, na sukach korjenjenym stołpikom.
160	Běły jězončik (Prunella laciniata) je rostlina ze swójby cycawkowych rostlinow (Lamiaceae).
161	Běły porstnik docpěwa wysokosć wot 5 hač 20 cm.
162	Běły žrawc je najbóle škitana žrawcowa družina swěta, ale tohodla sylnje wohroženy.
163	Benetice leža 4 km sewjerozapadnje wot Světlá nad Sázavou a słušeja k wokrjesej Havlíčkův Brod.
164	Benno, Lipsk 1996, ISBN 3-7462-1118-2 Napohlad cyrkwje je so w běhu lětstotkow zničenjow dla wjelekróć změnił, tak zo njeleži wuznam Božeho domu dźensa w twarjenju samym, ale w jeho róli jako centralna měšćanska cyrkej katolskich Serbow.
165	Beno) wosta jeničce najmjeńši, swj.
166	Bě přećel a spěchowar jezuitskeho rjada.
167	Berezań ma dwórnišćo při železniskej čarje Kijew–
168	Bergen bě w lěće 2000 jedna z dźewjeć kulturnych stolicow Europy.
169	Bergsland bě tež w rozsudnej měrje zamołwity za dalše wuwiće južnosamišćiny k spisownej rěči.
170	Berlinskeho-Zhorjelskeho železniskeho towarstwa bu 1867 na juh wote wsy přez ležownosć Slepo wjedźena.
171	Běrna je wjacelětna, w kulturje jenož jednolětna zelišćowa rostlina.
172	Bernauske dwórnišćo je kónčny dypk linije S 2 Berlinskeje S-Bahn.
173	Běrnjace ryženki móžeja w krótkim času cyłe poła donaha wužrać.
174	Bertelsmann Verlag, München 2002 Tute zmylki wjedźechu naposledk k njedokładnemu postajenju metroweho standarda.
175	Berylium je chemiski element ze symbolom Be a rjadowej ličbu 4. Mjeno hodźi so wotwodźeć wot minerala beryl, beryliumojteho debjenkoweho kamjenja (
176	Bě samo planowane, přetwarić B-šulu w Depsku na A-šulu, štož so pak ženje njezwoprawdźi.
177	Běše na třoch bokach wobdata wot lěsa.
178	Běše stolica bywšeho kraja Mecklenburg-Strelitz a ma něhdźe 21.000 wobydlerjow.
179	Běše tež stajnje zwólniwy, loyalnosć napřećo nacionalsocialistiskej wyšnosći pokazać, z čimž nježněješe pola wšitkich kolegow wothłós.
180	Bě to nabožinski konflikt a tež wojowanje wo móc.
181	Betta splendens je ryba z juhowuchodneje Azije.
182	Bě w lěće 1958 jako premier ze załožerjom pjateje francoskeje republiki a mjez 1959 a 1969 statny prezident.
183	Bě wuběrny stilist serbskeje rěče a zawjedźe fejeton do serbskeje literatury.
184	Bě zmandźeleny z Johanu Thusneldu rodź.
185	Bienst bu w lěće jako direktny kandidat swojeje strony we wólbnym wokrjesu 56 (Delnjošleska Hornja Łužica 1) z 31,2 % hłosow woleny.
186	BioCode chce při tym jednotny system nomenklatury za wšě žiwochi z wuwzaćom wirusow zawjesć, tuž systemy ICBN, IRZN, ICNB a ICNCP narunać.
187	Bislamšćina ma pjeć wokalow, a to a, e, i, o, u. Nimo toho diftongi ae, oe a ao wustupuja.
188	Bissau załoži so potom w 16. lětstotku, při čimž njeje dokładny datum znaty.
189	Bjesadźe bu w lěće 1937 kaž Domowinje samej zakazana dalša dźěławosć.
190	Bjezdwěla wobstajace typologiske a leksikaliske přezjednosće mjezy mongolskimi, tunguziskimi a turkowskimi rěčemi so móžeja tola tež přez wzajomne wobwliwowanje dla rěčnych kontaktow město přez genetiku přiwuznosć wujasnjować.
191	Bjez jeho wědy so wón 1922 wot narodnych mjeńšinow na prezidentskeho kandidata namjetuje.
192	Bjez powětra a kapalneje wody je wón jara žiwjenja njepřećelski wobswět.
193	Bjez swójskeho přičinjenja bu tež ze sobustawom nacionalsocialistiskeho wučerskeho zwjazka (Nationalsozialistischer Lehrerbund, NSLB), kiž běše wotdźěl NSDAP.
194	Bjez wopłodźenja wuńdźechu z Gaie Uranus (njebjo), Ourea (horiny) a Pontus (morjo).
195	& Blanche): Domizna je wuchodny region Srjedźneho morja.
196	Blisko Čopa nadeńdźe so jedyn z najwažnišich hraničnych přechodow mjez Słowakskej a Ukrainu.
197	Blisko dźensnišeho města załoži so hižo w šestym lětstotku do Chrystusa grjekska kolonija z mjenom Phasis (Φάσις).
198	Blisko gmejnskeho dźěla Gruna přeprěkuje přewoz rěku do Hohenprießnitza.
199	Blisko Jampila nadeńdźe so jedyn z najwažnišich hraničnych přechodow mjez Moldawskej a Ukrainu.
200	Blisko města leži wojerske zwučowanišćo Wittstock.
'''
# text = text.lower()
# words = text.split()
# words = [word.strip('.,!;()[]') for word in words]
# words = [word.replace("'s", '') for word in words]
# unique = []
# for word in words:
#     if word not in unique and len(word) > 3:
#         unique.append(word)

unique = ['abela', 'woženjeny', 'jednu', 'dźowku', 'rozdźělnych', 'rěčach', 'móže',
          'wašnje', 'čina', 'wuprajić', 'wupraji', 'finšćinje', 'pohibowanje', 'potrjecheneho', 'městna',
          'wot', 'doma', 'paris', 'wuchoda', 'poskića', 'přidatnje', 'móžnosć', 'datoweje', 'abstrakcije',
          'pomocu', 'abstraktnych', 'datowych', 'typow', 'adjektiw', 'dyrbi', 'gramatiskim', 'genusu',
          'mjenu', 'roda', 'wotpowědować', 'připodobnje', 'wotpowědnje', 'změnje', 'adjektiwy', 'maja', 'wariantu',
          'mjeztym', 'jednozłóžkowym', 'zdónkom', 'adresowa', 'kniha', 'lěta', 'podawa', 'kopšin', 'slědowace', 'swójby:', 'jakub', 'bjer', 'behr', 'nuknicu', 'donatec', 'dźěłajo',
          'nawuknychu', 'nowe', 'teksty', 'spěwow', 'připódla', 'wječorach', 'dóstanje', 'prěnjemu', 'razej',
          'krajnych', 'wólbach', 'wjace', 'hłosow', 'afriski', 'wopiči', 'chlěbowc', 'štom', 'garantowaše',
          'prawo', 'swójske', 'narodne', 'wuwiće', 'a.gray:', 'jednej', 'družinu', 'kaliforniskej', 'arizona', 'třomi', 'družinami',
          'delnjeje', 'ajapóma', '"hižo', 'činił"', 'nima', 'sobu', 'huworowanje', 'doły', 'dlejke', 'góry', 'syjańskeje',
          'drogi', 'jeli', 'žadyn', 'reelny', 'korjeń', 'njeeksistuje', 'akademiskeho', 'towarstwa', 'łužiske', 'stawizny',
          'rěče', 'starši', 'serbskeje', 'sekcije', 'akkadska', 'akkadistika', 'wuchodo)semitiska', 'arabšćinu', 'přiwuzna',
          'babylonjanow', 'assyričanow', 'něhdy', 'mezopotamiskej', 'irak', 'syriska', 'rěčała', 'wyše', 'toho', 'cyłkownej',
          'prědnjej', 'aziji', 'wašnjom', 'lěttysaca', 'wutłóči', 'sumerišćinu', 'jako', 'rěčanu', 'wšak', 'wužiwachu', 'dale', 'sakralnu', 'ceremonialnu', 'literarnu', 'wědomosće', 'aktiwne', 'koparske', 'towarstwo', 'měsće', 'sošk', 'aktualna', 'html-wersija', '4.01', 'lěću', '1997', 'w3c-poručenju', 'wuzwolena', 'definuje', 'jenož', 'sgml-nałoženje', 'wersija', '38.0.1', 'junija', '2015', 'aktualnje', 'přichodźe', 'łužiskich', 'wotkrytych', 'jamow', 'diskutuje', 'albanšćina', 'pisa', 'konsekwentnje', 'fonetisce', 'albertec', 'wopytowaše', '1898', '1904', 'krajnostawski', 'wučerski', 'seminar', 'budyšinje', 'albrechtowce', 'přiběži', 'tule', 'juha', 'stara', 'woda', 'potom', 'knjejstwje', 'pokoj', 'njeběše', 'běłe', 'sydlerjo', 'drjewo', 'twarjenje', 'domow', 'wužiwali', 'dokelž', 'mějachu', 'jara', 'mało', 'dokumentow', 'tutym', 'pismje', 'kotraž', 'napisała', 'njebě', 'znata', 'dešifrowanje', 'dlěše', 'sprócniwše', 'třeću', 'špaltu', '"ale', 'dźěsći', 'nochcetej', 'jěsć."', 'hižo', 'krótki', 'běchu', 'zdźělenki', 'kotrychž', 'zhotowjerjo', 'tutón', 'samozawjazk', 'łamaja', '1940', 'buchu', 'zbytki', 'terciera', 'namakane', 'jich', 'płodowe', 'mjaso', 'wohrěwanju', 'jědźna', 'mištr', 'jemu', 'wotmołwi:', '„tajkich', 'wurěčow', 'zrěčniwi', 'ludźo', 'twojeho', 'razu', 'wograwaja.“', 'nětko', "'tok", "pisin'", 'akceptowane', 'mjeno', 'njeje', 'móžno', 'nałoženja', 'google', 'play', 'store', 'druhim', 'systemje', 'android', 'sćahnyć', 'normalnym', 'přez', 'androidowym', 'graće', 'instalowało', 'herće', 'zbožo', 'swěće', 'ničo', 'trajace', 'wona', 'předstawy', 'woneho', 'swěta', 'raju', 'měła', 'poslednja', 'złóžka', 'wostanje', 'njepřizwučna', 'njeporjadnym', 'wurjekowanju', 'wokale', 'připodobnjuja', 'rozšěrjene', 'sorty', 'zwjetša', 'bóle', 'kompaktne', 'něhdźe', 'maćernorěčnikow', 'rěči', 'wohrožena', 'eksistuja', 'žiwochi', 'kotřiž', 'njetrjebaja', 'kislik', 'předewšěm', 'jednobańkowcach', 'čistej', 'skale', 'wustupuje', 'słód', 'wotwisuje', 'družiny', 'druhich', 'kóncach', 'rozpřezdrěwaše', 'twarjenja', 'njeběchu', 'jeničke', 'dźěłowe', 'polo', 'brigady', 'woprawdźitosći', 'zakaza', 'wočiwidna', 'wšelakorosć', 'přińć', 'někotrym', 'njedospołnym', 'grupam', 'znamješkow', 'wurytych', 'namakanišćach', 'wěnowachu', 'wosebje', 'pomnikam', 'zanjechachu', 'bydlenske', 'štwórće', 'někotre', 'wuwzaća', 'ugarit', 'hacilar', 'wjetše', 'mnóstwa', 'wjedu', 'běhawje', 'bluwanju', 'móžeja', 'tworjenja', 'kalciumoweho', 'oksalata', 'škody', 'jěrchenjow', 'zawinować', 'nocy', 'krónowe', 'łopješka', 'kćenja', 'hyacintojće', 'wonjeja', 'wobchowuje', 'konwenciji', 'doniž', 'specialisća', 'chronologiju', 'njedojednaja', 'tuchwilu', 'hišće', 'widźeć', 'wysokosć', 'njedocpěje', '1981', 'jeje', 'nałožowanje', 'zakazane', 'wotstawk', 'čopomaj', '111,694', 'km/°', 'wopłonjenje', 'zemje', 'snadnje', 'wjetši', 'ekwatorje', '110,574', 'křiwizna', 'puću', 'eksistuje', 'znamješka', 'ipa-symbole', 'alfabet', 'toki', 'pona', 'pismikow', 'wobmjezowany', 'alfons', 'handrik:', 'wučer', 'jurij', 'wjela', 'komorowje', 'spomóžnje', 'skutkował', 'algirdas', 'butkevičius', 'alkaloid', 'akonitin', 'najprjedy', 'nerwy', 'rozbudźi', 'lemi', 'alnus', 'rugosa', 'swójby', 'brězowych', 'rostlinow', 'betulaceae', 'alojs', 'andricki', '1914–1943', 'alpski', 'dźećel', 'naha', 'wjacelětna', 'zelišćowa', 'bjezstołpikata', 'rostlina', 'docpěje', 'mjezy', 'sewejrošpaniskeje', 'horinow', 'siebenbürgen', 'rozšěrjeny', 'faluje', 'sewjernych', 'wapnowych', 'alpach', 'awstriskeje', 'bayerskeje', 'južnych', 'wuchodnje', 'sexten', 'warianće', 'pryšćenc', 'wity', 'kerčk', 'kotryž', 'dołhe', 'lězucymi', 'wodrjewjacymi', 'wubitkami', '"altherrenverband"', 'polěpši', 'financielnu', 'situaciju', 'amaconasowu', 'nižinu', 'najwjetšim', 'tropiskim', 'dešćowym', 'lěsom', 'amboparapa', 'ogyke', 'sćěnu', 'kompletnje', 'molowach"', 'hesakãmba', '„wono', 'dospołnje', 'jasne.“', 'američenjo', 'teritorij', 'hakle', 'lěće', '1867', 'rusow', 'kupili', 'amurritišćina', 'ugaritišćina', 'fenicišćina', 'staroaramejšćina', 'aramejšćina', 'štyri', 'syriskej', 'rěčane', 'sewjerozapadosemitiske', 'wobstajnje', 'spjećowaše', 'nacionalsocialistami', 'hromadźe', 'dźěłać', 'oktobra', '1941', 'drježdźan', 'dachauskeho', 'koncentraciskeho', 'lěhwa', 'transportowany', '1921', 'ludowu', 'šulu', 'radworju', 'hdźež', 'běše', 'jeho', 'šulski', 'nawoda', 'wobsahuje', 'jadro', 'linux', 'klasiska', 'distribucija', 'desktop', 'serwer', 'znate', 'angela', 'merkel', 'apryla', 'zwjazkowa', 'předsydka', 'swojeje', 'strony', 'anita', 'lehtola', '2000', 'čłon', 'hedningarna', 'anona', 'annona', 'cherimola', 'anonowych', 'annonaceae', 'ansambl', 'michałskeje', 'cyrkwje', 'stareje', 'wodarnje', 'symbol', 'města', 'budyšina', 'jedyn', 'najwoblubowanišich', 'motiwow', 'sakskim', 'turistiskim', 'wabjenju', 'apache', 'openoffice', 'swobodna', 'běrowa', 'software', 'paketa', 'openoffice.org', 'pochadźa', 'apfel', 'bjezkonfesionelny', 'ženjeny', 'třoch', 'dźěći', 'prěni', 'nowoh', 'domu', 'dźěłaćeŕ', 'aprikozowc', 'zeleny', 'docpěwa', 'archangelsk', 'někak', 'pjećdźesat', 'tysac', 'wobydlerjow', 'argentinska', 'milionow', 'aristolochijowa', 'kisalina', 'změni', 'herbske', 'kajkosće', 'tumory', 'wuwabjeć', 'arnošt', 'černik', 'dźowki', 'dweju', 'synow', 'ličeše', '1956', 'wobydlerstwa', 'spytečanskeje', 'gmejny', 'serbow', 'zwěsći', 'serbskorěčny', 'podźěl', '33,1', 'muka', 'postaji', 'andrickeho', '1896', 'redaktora', 'časopisa', 'muka:', 'statistika', 'artikl', 'předłóžku', 'móžemy', 'wurjekować', 'słowje', 'přikład:', 'artikulaciske', 'městno', 'sćěhuje', 'poslednjeho', 'tutych', 'konsonantow', 'asam', 'swojeho', 'čorneho', 'čaja', 'swětodaloko', 'znaty', 'assyriska', 'babyloniska', 'sumer', 'pěstowachu', 'dalokosahace', 'politiske', 'poćahi', 'susodnym', 'krajam', 'kotrež', 'zdźěla', 'prowincy', 'mezopotamiskich', 'jadrowych', 'krajow', 'deklarowane', 'płaći', 'wuběrny', 'prědar', 'dobry', 'přełožowar', 'kěrlušow', 'astronomiska', 'šěrokosć', 'mjez', 'woprawdźitym', 'lotowym', 'směrom', 'ekwatorowej', 'runinu', 'njebjeski', 'ekwator', 'póten', 'słabcyc', 'žywnosći', 'krynuł', 'byli', 'wěkšy', 'dźěl', 'lute', 'lěda', 'role', 'wónej', 'stej', 'byłej', 'jeno', 'peršonje', 'cyłej', 'njejstej', 'mogłej', 'hobstać', 'doprjodka', 'pćić', 'lědym', 'półowicu', 'hobdźěłałej', 'mójeje', 'maćerje', 'bratr', 'kmótr', 'ćota', 'była', 'sostra', 'bratry', 'sostry', 'jeneje', 'athen', 'płoninu', 'najwjetše', 'město', 'kraja', 'přiwšěm', 'gmejna', 'centrumje', 'kopjenišća', 'athen-piraeus', 'poměrnje', 'mała', 'běšo', 'jěšće', 'někotere', 'pjerjej', 'togo', 'drogego', 'lěta…', 'pisane', 'rozdźělene', 'kompozicije', 'poselstwo', 'atomowe', 'tyłowy', 'metala', 'atomy', 'bjez', 'wonkownych', 'elektronow', 'zwjazuja', 'metalowemu', 'lěsycy', 'molekulach', 'zhromadne', 'elektronowe', 'poriki', 'zwjazane', 'wone', 'steja', 'dwěmaj', 'krótkich', 'wurostkach', 'docpěwaja', 'dołhosć', 'awstralski', 'indigo', 'kerk', 'łušćinowcow', 'łaćonsce:', 'indigofera', 'australis', 'fabaceae', 'awtochtone', 'wobydlerstwo', 'słuša', 'ludu', 'nencow', 'hłownje', 'plahowanja', 'sobow', 'žiwy', 'awtor', 'studije', 'podhlad', 'staj', 'internetowa', 'pornografija', 'wumocowanje', 'substitutaj', 'potajkim', 'jedne', 'narunanje', 'druheho', 'babylonskej', 'antiksku', 'mezopotamisku', 'kulturu', 'wobchowachu', 'baczyński', 'spřećeli', 'spisowaćelom', 'jerzymom', 'kamilom', 'weintraubom', 'badiski', 'hódnotna', 'picowanska', 'bahnowa', 'drěstka', 'jednolětna', 'smjetanka', '50-150cm', 'bahnowy', 'hróšik', 'žiwotnik', 'bakterije', 'mikroorganizmy', 'bałcar', 'zawostaji', 'wobšěrne', 'rukopisne', 'dźeniki', 'wažne', 'stawizniske', 'kulturnostawizniske', 'žórła', 'bandmann', 'direktny', 'kandidat', '2009', '38,4', 'woleny', 'banjowcowe', 'rostliny', 'cucurbitaceae', 'swójba', 'symjencowych', 'banjul', 'stejišćo', 'najwjetšeje', 'mošeje', 'gambiji', 'sydło', 'romsko-katolskeho', 'biskopstwa', 'bańkowe', 'membrany', 'wužiwaja', 'tutu', 'kajkosć', 'starosćiwje', 'kontrolowali', 'wzajomne', 'skutkowanje', 'swojimi', 'wobsahami', 'eksternymi', 'chemiskimi', 'wěcami', 'banks', 'skupinu', 'skupinow', 'rhyniophyta', 'trimerophytophyta', 'zosterophyllophyta', 'rozpačił', 'bantuske', 'ludy', 'předstaja', 'zdaću', 'železočasoweje', 'urewe-kultury', 'regionje', 'wulkich', 'wuchodoafriskich', 'jězorow', 'rozšěrjena', 'barba', 'jasno-', 'ćěmnozelena', 'jednobarbiće', 'zelena', 'kremobarbitymi', 'blečkami', 'cyło', 'běła', 'barbizna', 'barbjenje', 'cyroby', 'butra', 'šokolada', 'twarožk', 'tekstilijow', 'wužiwa', 'baribal', 'čornobruny', 'mjeńši', 'zawality', 'bruny', 'mjedwjedź', 'bariki', 'barok', 'historiski', 'směr', 'wuměłstwa', 'popularny', 'kónca', 'lětstotka', 'spočatka', 'renesansy', 'rokoka', 'barokny', 'knježi', 'dźewjeć', 'wóskami', 'jednymi', 'schodami', 'hołym', 'njebjom', 'bartl', '1969', '1971', 'inoficielny', 'sobudźěłaćer', 'statneje', 'bjezstrašnosće', 'baseń', 'pjeć', 'linkow', 'kóždej', 'štučce', 'melodija', 'tomu', 'wopřija', 'sydom', 'taktow', 'nataktom', 'basnje', 'spisał', 'wulcy', 'knihe', 'bazlik', 'italskej', 'kuchinje', 'bazowe', 'łopjena', 'łučneho', 'šišmanca', 'kulojte', 'dołhostołpikate', 'połojcy', 'dźělene', 'beata', 'szydło', 'zmandźelena', 'bipolarneho', 'swětoweho', 'porjada', 'horceje', 'wójny', 'započał', 'centrum', 'awarskeho', 'chanstwa', '1864', 'fazy', 'wulke', 'mócnarstwa', 'dominowane', 'druhe', 'mocy', 'susodnych', 'regionow', 'dobywanske', 'wójnske', 'wuprawy', 'wjedźechu', '1957', 'samostatna', 'budyske', 'tachantstwo', 'krajne', 'bohotstwo', 'feudalne', 'knjejstwo', 'měješe', 'kóžde', 'dwaj', 'burskej', 'statokaj', 'poslednje', 'wólby', 'wjacestronskim', 'prěnjotnje', 'wotwodźenki', 'křćenskich', 'mjenow', 'priwatne', 'wužiće', 'móžachu', 'pozdźišo', 'samostatnymi', 'křćenskimi', 'mjenami', 'stać', 'beethoven', 'dźensnišeho', 'najznatym', 'komponistam', 'brěza', 'zhorbjeny', 'přewisowacy', '20-30', 'čapla', 'casmerodius', 'albus', 'syn.:', 'ardea', 'alba', 'ptak', 'ardeidae', 'pjerinu', 'cycawka', 'zymokruta', 'jěrowc', 'sewjernej', 'balkanskej', 'połkupje', 'lederhaut', 'sclera', 'leži', 'zadnim', 'wobłuku', 'wóčneho', 'jabłuka', 'belfast', 'katolskeho', 'anglikanskeho', 'biskopa', 'uniwersitne', 'přistawne', 'belgica', '1827', 'wužiwane', 'kali', 'soda', 'moench', 'zakładźe', 'staršeho', 'priority', 'woprawnjeneho', 'homonyma', 'scop', 'synonym', 'salsola', 'njepłaćiwe', 'belka', 'porodźi', 'małeho', 'čerwjeneho', 'haplka', 'běłym', 'znamjenjom', 'prědnej', 'noze', 'běły', 'přecozelena', 'trawnikojće', 'rosćaca', 'nižoležacym', 'sukach', 'korjenjenym', 'stołpikom', 'jězončik', 'prunella', 'laciniata', 'cycawkowych', 'lamiaceae', 'porstnik', 'žrawc', 'najbóle', 'škitana', 'žrawcowa', 'družina', 'tohodla', 'sylnje', 'wohroženy', 'benetice', 'leža', 'sewjerozapadnje', 'světlá', 'sázavou', 'słušeja', 'wokrjesej', 'havlíčkův', 'brod', 'benno', 'lipsk', '1996', 'isbn', '3-7462-1118-2', 'napohlad', 'běhu', 'lětstotkow', 'zničenjow', 'wjelekróć', 'změnił', 'njeleži', 'wuznam', 'božeho', 'dźensa', 'twarjenju', 'samym', 'róli', 'centralna', 'měšćanska', 'cyrkej', 'katolskich', 'beno', 'wosta', 'jeničce', 'najmjeńši', 'přećel', 'spěchowar', 'jezuitskeho', 'rjada', 'berezań', 'dwórnišćo', 'železniskej', 'čarje', 'kijew–', 'bergen', 'jedna', 'kulturnych', 'stolicow', 'europy', 'bergsland', 'rozsudnej', 'měrje', 'zamołwity', 'dalše', 'južnosamišćiny', 'spisownej', 'berlinskeho-zhorjelskeho', 'železniskeho', 'wote', 'ležownosć', 'slepo', 'wjedźena', 'běrna', 'kulturje', 'bernauske', 'kónčny', 'dypk', 'linije', 'berlinskeje', 's-bahn', 'běrnjace', 'ryženki', 'krótkim', 'času', 'cyłe', 'poła', 'donaha', 'wužrać', 'bertelsmann', 'verlag', 'münchen', '2002', 'tute', 'zmylki', 'naposledk', 'njedokładnemu', 'postajenju', 'metroweho', 'standarda', 'berylium', 'chemiski', 'element', 'symbolom', 'rjadowej', 'ličbu', 'hodźi', 'wotwodźeć', 'minerala', 'beryl', 'beryliumojteho', 'debjenkoweho', 'kamjenja', 'samo', 'planowane', 'přetwarić', 'b-šulu', 'depsku', 'a-šulu', 'štož', 'ženje', 'njezwoprawdźi', 'bokach', 'wobdata', 'lěsa', 'stolica', 'bywšeho', 'mecklenburg-strelitz', '21.000', 'stajnje', 'zwólniwy', 'loyalnosć', 'napřećo', 'nacionalsocialistiskej', 'wyšnosći', 'pokazać', 'čimž', 'nježněješe', 'pola', 'wšitkich', 'kolegow', 'wothłós', 'nabožinski', 'konflikt', 'wojowanje', 'betta', 'splendens', 'ryba', 'juhowuchodneje', 'azije', '1958', 'premier', 'załožerjom', 'pjateje', 'francoskeje', 'republiki', '1959', 'statny', 'prezident', 'stilist', 'zawjedźe', 'fejeton', 'literatury', 'zmandźeleny', 'johanu', 'thusneldu', 'rodź', 'bienst', 'wólbnym', 'wokrjesu', 'delnjošleska', 'hornja', 'łužica', '31,2', 'biocode', 'chce', 'jednotny', 'system', 'nomenklatury', 'wuwzaćom', 'wirusow', 'zawjesć', 'systemy', 'icbn', 'irzn', 'icnb', 'icncp', 'narunać', 'bislamšćina', 'wokalow', 'nimo', 'diftongi', 'wustupuja', 'bissau', 'załoži', 'lětstotku', 'dokładny', 'datum', 'bjesadźe', '1937', 'domowinje', 'samej', 'zakazana', 'dalša', 'dźěławosć', 'bjezdwěla', 'wobstajace', 'typologiske', 'leksikaliske', 'přezjednosće', 'mongolskimi', 'tunguziskimi', 'turkowskimi', 'rěčemi', 'tola', 'wobwliwowanje', 'rěčnych', 'kontaktow', 'genetiku', 'přiwuznosć', 'wujasnjować', 'wědy', '1922', 'narodnych', 'mjeńšinow', 'prezidentskeho', 'kandidata', 'namjetuje', 'powětra', 'kapalneje', 'wody', 'žiwjenja', 'njepřećelski', 'wobswět', 'swójskeho', 'přičinjenja', 'sobustawom', 'nacionalsocialistiskeho', 'wučerskeho', 'zwjazka', 'nationalsozialistischer', 'lehrerbund', 'nslb', 'wotdźěl', 'nsdap', 'wopłodźenja', 'wuńdźechu', 'gaie', 'uranus', 'njebjo', 'ourea', 'horiny', 'pontus', 'morjo', 'blanche):', 'domizna', 'wuchodny', 'region', 'srjedźneho', 'morja', 'blisko', 'čopa', 'nadeńdźe', 'najwažnišich', 'hraničnych', 'přechodow', 'słowakskej', 'ukrainu', 'šestym', 'chrystusa', 'grjekska', 'kolonija', 'mjenom', 'phasis', 'φάσις', 'gmejnskeho', 'dźěla', 'gruna', 'přeprěkuje', 'přewoz', 'rěku', 'hohenprießnitza', 'jampila', 'moldawskej', 'wojerske', 'zwučowanišćo', 'wittstock']

def preprocess(text):
    text = text.replace('→', '')
    text = text.replace('SUBST', 'N')
    text = text.upper()
    text = text.replace('/DEKL', '')
    text = text.strip()
    text = text.replace('/', ';')
    return text

res = []
for word in unique[:20]:
    try:
        website = 'https://www.soblex.de/?p_w={}&cmd=search_soblex'.format(word)
        page = requests.get(website)
        soup = BeautifulSoup(page.content, features="html.parser")
        tab = soup.find("table", {"class": "table table-striped"})
        span = tab.findAll("tr")

        b = ''
        set = False
        for t in span:
            s = t.findAll("span", {"data-html": "true", "data-toggle": "tooltip"})
            for l in s:
                if l["title"].startswith("Gram. Codes:") or l["title"].startswith("Gram. Code"):
                    b = t
                    set = True
                    break
            if set == True:
                break

        span = b.findAll("span", {"data-html": "true", "data-toggle": "tooltip"})
        b = {'lemma': '', 'word': '', 'morph': ''}
        for t in span:
            if t['title'].startswith('Gram. Code'):
                z = t.getText()
                z = preprocess(z)
                b['morph'] = z
            if t['title'].startswith('Gram. Codes:'):
                z = t['title'].replace('Gram. Codes:', '')
                z = preprocess(z)
                z = z.upper()
                b['morph'] = z
            if t['title'].startswith('Wortstamm'):
                z = t.getText()
                z = z.replace('|', '')
                b['lemma'] = z
        b['word'] = word
        res.append(b)
    except:
        pass

keys = res[0].keys()
with open('test.csv', 'w', newline='', encoding="utf-8") as output_file:
    dict_writer = csv.DictWriter(output_file, keys, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(res)
