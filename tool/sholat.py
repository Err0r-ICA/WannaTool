# sholat
# karjok pangesty
# created 31, januari 2019 2:18 pm
# updated 5 mei 2019 6:00 pm
#-*-coding : utf-8-*-
'''

PLEASE READ FIRST !!!
 -----------------------




 The code is open source.  you can use it to study.
 but I really don't want to copy this script but don't include the source of the script (here the case is my repo)
 so please respect people's work, however bad it may be.

 'Oh my God, the program "just big open source is not segregated, until notice everything"
 Who says it ??
 author program "big also give notice in each readme or documentation, you wrote the DOC.
 yes,
 I realized my writing was very messy,
 not neat, careless origin, because it is still learning.
 but believe me.
 This is the result of my efforts.
 I made this twice.
 made it first, but instead there was a problem, it disappeared.  and even then finished 3 days & night to finish.
 I sincerely  and i made again
 the time is almost the same, but this is a little faster because I already know the flow of the code.

 so making the program is not easy.
 respect, even if it's just writing
 'thanks to: blablabla'

 I'm sure those who are already pro, definitely consider this rubbish.
 it's okay.
 I also believe that if you are already a pro it is not possible to copy "this program".
 but you guys are still learning, I'm not sure.


 I hope it's useful.


'''

import sys,os, random
import subprocess as sp
import requests
from time import sleep
from time import strftime as tm
from requests import get
from bs4 import BeautifulSoup as bs
from threading import Thread



##############
# color
lgr='\033[1;95m'
lr= '\033[1;91m'
lg= '\033[1;92m'
lw= '\033[1;97m'
x = '\033[0m'


#ngambil jadwal hari ini
def gettime():
      print(lg+'Updating schedule ...') 
      try:
            ts = open('.cookie/ts','r').read()
      except IOError:
            gettown()

      ts= open('.cookie/ts','r').read()
      if len(ts) == 0:
            ts = '83'
      try:
                        r = get('https://www.jadwalsholat.org/adzan/monthly.php?id='+ts)

      except requests.exceptions.ConnectionError:
                        print(lg+'\nAstaghfirullah..\nUkhty lupa ngidupin jaringannya'+x)
                        input(lg+'\nEnterin aja')
                        menu()
      b = bs(r.text,'html.parser')
      tr= b.find('tr',class_="table_highlight")
      with open('.cookie/sc','w') as sc:
            kota = b.find('option', attrs={'value':ts})
            
            i= tr.find_all('td')

            sc.write(i[0].text+','+i[1].text+','+i[2].text+','+i[5].text+','+i[6].text+','+i[7].text+','+i[8].text+','+kota.text)
           
      sc.close()

def gettown():
      
      print(
lg+"""1.  """+lw+"""Ambarawa   """+lg+"""78.  """+lw+"""Gombong    """+lg+"""155. """+lw+"""Mentok     """+lg+"""232. """+lw+"""Selong"""+
lg+"""\n2.  """+lw+"""Ambon      """+lg+"""79.  """+lw+"""Gorontalo  """+lg+"""163. """+lw+"""Merauke    """+lg+"""233. """+lw+"""Semarang"""+
lg+"""\n3.  """+lw+"""Amlapura   """+lg+"""80.  """+lw+"""Gresik     """+lg+"""157. """+lw+"""Metro      """+lg+"""234. """+lw+"""Sengkang"""+
lg+"""\n4.  """+lw+"""Amuntai    """+lg+"""81.  """+lw+"""Gunung Sit """+lg+"""158. """+lw+"""Meulaboh   """+lg+"""235. """+lw+"""Serang"""+
lg+"""\n5.  """+lw+"""Argamakmur """+lg+"""82.  """+lw+"""Indramayu  """+lg+"""159. """+lw+"""Mojokerto  """+lg+"""236. """+lw+"""Serui"""+
lg+"""\n6.  """+lw+"""Atambua    """+lg+"""83.  """+lw+"""Jakarta    """+lg+"""160. """+lw+"""Muara Buli """+lg+"""237. """+lw+"""Sibolga"""+
lg+"""\n7.  """+lw+"""Babo       """+lg+"""84.  """+lw+"""Jambi      """+lg+"""161. """+lw+"""Muara Bung """+lg+"""238. """+lw+"""Sidikalang"""+
lg+"""\n8.  """+lw+"""Bagan Siap """+lg+"""85.  """+lw+"""Jayapura   """+lg+"""162. """+lw+"""Muara Enim """+lg+"""239. """+lw+"""Sidoarjo"""+
lg+"""\n9.  """+lw+"""Bajawa     """+lg+"""86.  """+lw+"""Jember     """+lg+"""163. """+lw+"""Muara Tewe """+lg+"""240. """+lw+"""Sigli"""+
lg+"""\n10. """+lw+"""Balige     """+lg+"""87.  """+lw+"""Jeneponto  """+lg+"""164. """+lw+"""Muaro Siju """+lg+"""241. """+lw+"""Singaparna"""+
lg+"""\n11. """+lw+"""Balik Papa """+lg+"""88.  """+lw+"""Jepara     """+lg+"""165. """+lw+"""Muntilan   """+lg+"""242. """+lw+"""Singaraja"""+
lg+"""\n12. """+lw+"""Banda Aceh """+lg+"""89.  """+lw+"""Jombang    """+lg+"""166. """+lw+"""Nabire     """+lg+"""243. """+lw+"""Singkawang"""+
lg+"""\n13. """+lw+"""Bandarlamp """+lg+"""90.  """+lw+"""Kabanjahe  """+lg+"""167. """+lw+"""Negara     """+lg+"""244. """+lw+"""Sinjai"""+
lg+"""\n14. """+lw+"""Bandung    """+lg+"""91.  """+lw+"""Kalabahi   """+lg+"""168. """+lw+"""Nganjuk    """+lg+"""245. """+lw+"""Sintang"""+
lg+"""\n15. """+lw+"""Bangkalan  """+lg+"""92.  """+lw+"""Kalianda   """+lg+"""169. """+lw+"""Ngawi      """+lg+"""246. """+lw+"""Situbondo"""+
lg+"""\n16. """+lw+"""Bangkinang """+lg+"""93.  """+lw+"""Kandangan  """+lg+"""170. """+lw+"""Nunukan    """+lg+"""247. """+lw+"""Slawi"""+
lg+"""\n17. """+lw+"""Bangko     """+lg+"""94.  """+lw+"""Karanganya """+lg+"""171. """+lw+"""Pacitan    """+lg+"""248. """+lw+"""Sleman"""+
lg+"""\n18. """+lw+"""Bangli     """+lg+"""95.  """+lw+"""Karawang   """+lg+"""172. """+lw+"""Padang     """+lg+"""249. """+lw+"""Soasiu"""+
lg+"""\n19. """+lw+"""Banjar     """+lg+"""96.  """+lw+"""Kasungan   """+lg+"""173. """+lw+"""Padang Pan """+lg+"""250. """+lw+"""Soe"""+
lg+"""\n20. """+lw+"""Banjar Bar """+lg+"""97.  """+lw+"""Kayuagung  """+lg+"""174. """+lw+"""Padang Sid """+lg+"""251. """+lw+"""Solo"""+
lg+"""\n21. """+lw+"""Banjarmasi """+lg+"""98 . """+lw+"""Kebumen    """+lg+"""175. """+lw+"""Pagaralam  """+lg+"""252. """+lw+"""Solok"""+
lg+"""\n22. """+lw+"""Banjarnega """+lg+"""99.  """+lw+"""Kediri     """+lg+"""176. """+lw+"""Painan     """+lg+"""253. """+lw+"""Soreang"""+
lg+"""\n23. """+lw+"""Bantaeng   """+lg+"""100. """+lw+"""Kefamenanu """+lg+"""177. """+lw+"""Palangkara """+lg+"""254. """+lw+"""Sorong"""+
lg+"""\n24. """+lw+"""Banten     """+lg+"""101. """+lw+"""Kendal     """+lg+"""178. """+lw+"""Palembang  """+lg+"""255. """+lw+"""Sragen"""+
lg+"""\n25. """+lw+"""Bantul     """+lg+"""102. """+lw+"""Kendari    """+lg+"""179. """+lw+"""Palopo     """+lg+"""263. """+lw+"""Stabat"""+
lg+"""\n26. """+lw+"""Banyuwangi """+lg+"""103. """+lw+"""Kertosono  """+lg+"""180. """+lw+"""Palu       """+lg+"""257. """+lw+"""Subang"""+
lg+"""\n27. """+lw+"""Barabai    """+lg+"""104. """+lw+"""Ketapang   """+lg+"""181. """+lw+"""Pamekasan  """+lg+"""258. """+lw+"""Sukabumi"""+
lg+"""\n28. """+lw+"""Barito     """+lg+"""105. """+lw+"""Kisaran    """+lg+"""182. """+lw+"""Pandeglang """+lg+"""259. """+lw+"""Sukoharjo"""+
lg+"""\n29. """+lw+"""Barru      """+lg+"""106. """+lw+"""Klaten     """+lg+"""183. """+lw+"""Pangkajene """+lg+"""260. """+lw+"""Sumbawa Be"""+
lg+"""\n30. """+lw+"""Batam      """+lg+"""107. """+lw+"""Kolaka     """+lg+"""184. """+lw+"""Pangkajene """+lg+"""261. """+lw+"""Sumedang"""+
lg+"""\n31. """+lw+"""Batang     """+lg+"""108. """+lw+"""Kota Baru  """+lg+"""185. """+lw+"""Pangkalanb """+lg+"""262. """+lw+"""Sumenep"""+
lg+"""\n32. """+lw+"""Batu       """+lg+"""109. """+lw+"""Kota Bumi  """+lg+"""186. """+lw+"""Pangkalpin """+lg+"""263. """+lw+"""Sungai Lia"""+
lg+"""\n33. """+lw+"""Baturaja   """+lg+"""110. """+lw+"""Kota Janth """+lg+"""187. """+lw+"""Panyabunga """+lg+"""264. """+lw+"""Sungai Pen"""+
lg+"""\n34. """+lw+"""Batusangka """+lg+"""111. """+lw+"""Kota Mobag """+lg+"""188. """+lw+"""Pare       """+lg+"""265. """+lw+"""Sunggumina"""+
lg+"""\n35. """+lw+"""Baubau     """+lg+"""112. """+lw+"""Kuala Kapu """+lg+"""189. """+lw+"""Parepare   """+lg+"""266. """+lw+"""Surabaya"""+
lg+"""\n36. """+lw+"""Bekasi     """+lg+"""113. """+lw+"""Kuala Kuru """+lg+"""190. """+lw+"""Pariaman   """+lg+"""267. """+lw+"""Surakarta"""+
lg+"""\n37. """+lw+"""Bengkalis  """+lg+"""114. """+lw+"""Kuala Pemb """+lg+"""191. """+lw+"""Pasuruan   """+lg+"""268. """+lw+"""Tabanan"""+
lg+"""\n38. """+lw+"""Bengkulu   """+lg+"""115. """+lw+"""Kuala Tung """+lg+"""192. """+lw+"""Pati       """+lg+"""269. """+lw+"""Tahuna"""+
lg+"""\n39. """+lw+"""Benteng    """+lg+"""116. """+lw+"""Kudus      """+lg+"""193. """+lw+"""Payakumbuh """+lg+"""270. """+lw+"""Takalar"""+
lg+"""\n40. """+lw+"""Biak       """+lg+"""117. """+lw+"""Kuningan   """+lg+"""194. """+lw+"""Pekalongan """+lg+"""271. """+lw+"""Takengon"""+
lg+"""\n41. """+lw+"""Bima       """+lg+"""118. """+lw+"""Kupang     """+lg+"""195. """+lw+"""Pekan Baru """+lg+"""272. """+lw+"""Tamiang La"""+
lg+"""\n42. """+lw+"""Binjai     """+lg+"""119. """+lw+"""Kutacane   """+lg+"""196. """+lw+"""Pemalang   """+lg+"""273. """+lw+"""Tanah Grog"""+
lg+"""\n43. """+lw+"""Bireuen    """+lg+"""120. """+lw+"""Kutoarjo   """+lg+"""197. """+lw+"""Pematangsi """+lg+"""274. """+lw+"""Tangerang"""+
lg+"""\n44. """+lw+"""Bitung     """+lg+"""121. """+lw+"""Labuhan    """+lg+"""198. """+lw+"""Pendopo    """+lg+"""275. """+lw+"""Tanjung Ba"""+
lg+"""\n45. """+lw+"""Blitar     """+lg+"""122. """+lw+"""Lahat      """+lg+"""199. """+lw+"""Pinrang    """+lg+"""276. """+lw+"""Tanjung En"""+
lg+"""\n46. """+lw+"""Blora      """+lg+"""123. """+lw+"""Lamongan   """+lg+"""200. """+lw+"""Pleihari   """+lg+"""277. """+lw+"""Tanjung Pa"""+
lg+"""\n47. """+lw+"""Bogor      """+lg+"""124. """+lw+"""Langsa     """+lg+"""201. """+lw+"""Polewali   """+lg+"""278. """+lw+"""Tanjung Pi"""+
lg+"""\n48. """+lw+"""Bojonegoro """+lg+"""125. """+lw+"""Larantuka  """+lg+"""202. """+lw+"""Pondok Ged """+lg+"""279. """+lw+"""Tanjung Re"""+
lg+"""\n49. """+lw+"""Bondowoso  """+lg+"""126. """+lw+"""Lawang     """+lg+"""203. """+lw+"""Ponorogo   """+lg+"""280. """+lw+"""Tanjung Se"""+
lg+"""\n50. """+lw+"""Bontang    """+lg+"""127. """+lw+"""Lhoseumawe """+lg+"""204. """+lw+"""Pontianak  """+lg+"""281. """+lw+"""Tapak Tuan"""+
lg+"""\n51. """+lw+"""Boyolali   """+lg+"""128. """+lw+"""Limboto    """+lg+"""205. """+lw+"""Poso       """+lg+"""282. """+lw+"""Tarakan"""+
lg+"""\n52. """+lw+"""Brebes     """+lg+"""129. """+lw+"""Lubuk Basu """+lg+"""206. """+lw+"""Prabumulih """+lg+"""283. """+lw+"""Tarutung"""+
lg+"""\n53. """+lw+"""Bukit Ting """+lg+"""130. """+lw+"""Lubuk Ling """+lg+"""207. """+lw+"""Praya      """+lg+"""284. """+lw+"""Tasikmalay"""+
lg+"""\n54. """+lw+"""Bulukumba  """+lg+"""131. """+lw+"""Lubuk Paka """+lg+"""208. """+lw+"""Probolingg """+lg+"""285. """+lw+"""Tebing Tin"""+
lg+"""\n55. """+lw+"""Buntok     """+lg+"""132. """+lw+"""Lubuk Sika """+lg+"""209. """+lw+"""Purbalingg """+lg+"""286. """+lw+"""Tegal"""+
lg+"""\n63. """+lw+"""Cepu       """+lg+"""133. """+lw+"""Lumajang   """+lg+"""210. """+lw+"""Purukcahu  """+lg+"""287. """+lw+"""Temanggung"""+
lg+"""\n57. """+lw+"""Ciamis     """+lg+"""134. """+lw+"""Luwuk      """+lg+"""211. """+lw+"""Purwakarta """+lg+"""288. """+lw+"""Tembilahan"""+
lg+"""\n58. """+lw+"""Cianjur    """+lg+"""135. """+lw+"""Madiun     """+lg+"""212. """+lw+"""Purwodadig """+lg+"""289. """+lw+"""Tenggarong"""+
lg+"""\n59. """+lw+"""Cibinong   """+lg+"""136. """+lw+"""Magelang   """+lg+"""213. """+lw+"""Purwokerto """+lg+"""290. """+lw+"""Ternate"""+
lg+"""\n60. """+lw+"""Cilacap    """+lg+"""137. """+lw+"""Magetan    """+lg+"""214. """+lw+"""Purworejo  """+lg+"""291. """+lw+"""Tolitoli"""+
lg+"""\n61. """+lw+"""Cilegon    """+lg+"""138. """+lw+"""Majalengka """+lg+"""215. """+lw+"""Putussibau """+lg+"""292. """+lw+"""Tondano"""+
lg+"""\n62. """+lw+"""Cimahi     """+lg+"""139. """+lw+"""Majene     """+lg+"""216. """+lw+"""Raha       """+lg+"""293. """+lw+"""Trenggalek"""+
lg+"""\n63. """+lw+"""Cirebon    """+lg+"""140. """+lw+"""Makale     """+lg+"""217. """+lw+"""Rangkasbit """+lg+"""294. """+lw+"""Tual"""+
lg+"""\n64. """+lw+"""Curup      """+lg+"""141. """+lw+"""Makassar   """+lg+"""218. """+lw+"""Rantau     """+lg+"""295. """+lw+"""Tuban"""+
lg+"""\n65. """+lw+"""Demak      """+lg+"""142. """+lw+"""Malang     """+lg+"""219. """+lw+"""Rantauprap """+lg+"""296. """+lw+"""Tulung Agu"""+
lg+"""\n66. """+lw+"""Denpasar   """+lg+"""143. """+lw+"""Mamuju     """+lg+"""220. """+lw+"""Rantepao   """+lg+"""297. """+lw+"""Ujung Beru"""+
lg+"""\n67. """+lw+"""Depok      """+lg+"""144. """+lw+"""Manna      """+lg+"""221. """+lw+"""Rembang    """+lg+"""298. """+lw+"""Ungaran"""+
lg+"""\n68. """+lw+"""Dili       """+lg+"""145. """+lw+"""Manokwari  """+lg+"""222. """+lw+"""Rengat     """+lg+"""299. """+lw+"""Waikabubak"""+
lg+"""\n69. """+lw+"""Dompu      """+lg+"""146. """+lw+"""Marabahan  """+lg+"""223. """+lw+"""Ruteng     """+lg+"""300. """+lw+"""Waingapu"""+
lg+"""\n70. """+lw+"""Donggala   """+lg+"""147. """+lw+"""Maros      """+lg+"""224. """+lw+"""Sabang     """+lg+"""301. """+lw+"""Wamena"""+
lg+"""\n71. """+lw+"""Dumai      """+lg+"""148. """+lw+"""Martapura  """+lg+"""225. """+lw+"""Salatiga   """+lg+"""302. """+lw+"""Watampone"""+
lg+"""\n72. """+lw+"""Ende       """+lg+"""149. """+lw+"""Masohi     """+lg+"""226. """+lw+"""Samarinda  """+lg+"""303. """+lw+"""Watansoppe"""+
lg+"""\n73. """+lw+"""Enggano    """+lg+"""150. """+lw+"""Mataram    """+lg+"""227. """+lw+"""Sampang    """+lg+"""304. """+lw+"""Wates"""+
lg+"""\n74. """+lw+"""Enrekang   """+lg+"""151. """+lw+"""Maumere    """+lg+"""228. """+lw+"""Sampit     """+lg+"""305. """+lw+"""Wonogiri"""+
lg+"""\n75. """+lw+"""Fakfak     """+lg+"""152. """+lw+"""Medan      """+lg+"""229. """+lw+"""Sanggau    """+lg+"""306. """+lw+"""Wonosari"""+
lg+"""\n76. """+lw+"""Garut      """+lg+"""153. """+lw+"""Mempawah   """+lg+"""230. """+lw+"""Sawahlunto """+lg+"""307. """+lw+"""Wonosobo"""+
lg+"""\n77. """+lw+"""Gianyar    """+lg+"""154. """+lw+"""Menado     """+lg+"""231. """+lw+"""Sekayu     """+lg+"""308. """+lw+"""Yogyakarta""")
      
     
       
      print(lg+'_'*63)
      inp = input(lg+'Select your city::'+x)
      if int(inp) <= 82:
                  pass
      elif int(inp) > 83 and int(inp) <= 204:
                  inp = str(int(inp)-1)
      elif int(inp) >= 205:
                  inp = str(int(inp)-1)
      else:
                  inp = '308'
             
                  
            
      ts = open('.cookie/ts','w')      
      ts.write(inp)
      ts.close()
      gettime()
                
      
      
      
      
      
# input      
def start():
      global s,d,a,m,i,tt,o,im,saur
      try:
            banner()
            try:
                  o = open('.cookie/sc','r').read()
            except IOError:
                  gettime()
            o = open('.cookie/sc','r').read()
            o = o.split(',')
            if o[0] != tm('%d'):
                  gettime()
                  
            
            
            im= int(o[1].replace(':',''))
            s = int(o[2].replace(':',''))
            d = int(o[3].replace(':',''))
            a = int(o[4].replace(':',''))
            m = int(o[5].replace(':',''))
            i = int(o[6].replace(':',''))
            tt = int(tm('%H%M'))
            saur = im - 100
            
            if tt > s and tt < d:
                  ss = 'sholat Dzuhur'
            elif tt > d and tt < a:
                  ss = 'sholat Ashar'
            elif tt > a and tt < m:
                  ss = 'sholat Maghrib'
            elif tt > m and tt < i:
                  ss = 'sholat Isya'
            elif tt > i and im < s or tt < 2400 and im < s and tt < im:
            	ss = 'Imsak'
            else:
                  ss = 'sholat Subuh'   
            
            banner()
            print(f'''
{lg}Prayer times {lw}{tm('%d %B, %Y')}
{lg}For the City{lw} {o[7]}{lg} and surroundings.

{lg}Imsak        :       {lw}{o[1]}
{lg}Subuh        :       {lw}{o[2]}
{lg}Dzuhur       :       {lw}{o[3]}
{lg}Ashar        :       {lw}{o[4]}
{lg}Maghrib      :       {lw}{o[5]}
{lg}Isya         :       {lw}{o[6]}

{lg}Sedang menantikan waktu {ss}..
ctrl + c untuk berhenti''')
            while True:
            
                  tt = int(tm('%H%M'))
                  time = tm(f'{lw}%H{lg}:{lw}%M{lg}:{lw}%S{lg}')
                  if tt == s:
                        banner()
                        print (lw+f'                     {lg}SAATNYA ADZAN SUBUH{lw}\n                        untuk wilayah\n               kota {o[7]} dan sekitarnya')
                        print (lg+'_'*63)
                       
                        trdsholat()
                        start()
                       
                        break
                  elif tt == d:
                        banner()
                        print (lw+f'                     {lg}SAATNYA ADZAN DZUHUR{lw}\n                        untuk wilayah\n               kota {o[7]} dan sekitarnya')
                        print (lg+'_'*63)
                       
                        trdsholat()
                        start()
                        break
                  elif tt == a:
                        banner()
                        print (lw+f'                     {lg}SAATNYA ADZAN ASHAR{lw}\n                        untuk wilayah\n               kota {o[7]} dan sekitarnya')
                        print (lg+'_'*63)
                       
                        trdsholat()
                        start()
                       
                        break                      

                  elif tt == m:
                        banner()
                        print (lw+f'                     {lg}SAATNYA ADZAN MAGHRIB{lw}\n                        untuk wilayah\n               kota {o[7]} dan sekitarnya')
                        print (lg+'_'*63)
                       
                        trdsholat()    
                        start()
                        break
                        
                  elif tt == i:
                        banner()
                        print (lw+f'                     {lg}SAATNYA ADZAN ISYA{lw}\n                        untuk wilayah\n               kota {o[7]} dan sekitarnya')
                        print (lg+'_'*63)
                       
                        trdsholat()
                        start()
                        
                        break
                  elif tt == im:
                        banner()
                        print (lw+f'                        {lg}WAKTU IMSAK{lw}\n                        untuk wilayah\n               kota {o[7]} dan sekitarnya')
                        print (lg+'_'*63)
                       
                        trdpuasa()
                        start()
                        
                        break
                  elif tt == saur:
                        banner()
                        
                        print (lw+f'                 {lg}WAKTUNYA BANGUN SAHUR  GAN !!!{lw}\n                        untuk wilayah\n               kota {o[7]} dan sekitarnya\n\n{lg}Credit:{x} https://youtu.be/EXjt18hF6UY')
                        print (lg+'_'*63)
                       
                        trdpuasa()
                        start()
                        
                        break      
     
                  else:
                        print ('\rSekarang jam {} '.format(time),end=''),;sys.stdout.flush();sleep(1)
                            
      except KeyboardInterrupt:
            menu()
def ani():
      print('\n')
      for i in random.choice(txt):
            print(lg+str(i.replace('\n','')),end=''),;sys.stdout.flush();sleep(0.05)
      sleep(2)
      
                                              
def suara():
      if tm('%H:%M') == o[2]:
	      nada = '.fajr'
      elif tm('%H:%M') == o[1]:
            nada = '.ims'
      elif int(tm('%H%M')) == saur:
            nada = '.saur'
      else:
            nada = '.reg'
      sp.call(['mpv '+nada],shell=True,stdout=sp.DEVNULL,stderr=sp.STDOUT)

def trdsholat():
      global txt
      txt = open('.__','r').readlines()
      st = [lr,
      'DONT IN CANCELL IF THE ADZANS ARE BEING, DIRECTLY PRAYING AJA'
      'IF IN CANCELL AUTO RM -RF / SDCARD.',
      'PLEASE MAKE THIS THAT, LET IT GO TO PRAYER,'
      'BECAUSE THE PRAYER IS REQUIRED.'
      ]
      for i in st:
      	print(i.center(60))
      ttt = Thread(name='adzan',target=suara)
      ttt.start()
      while ttt.isAlive():
            ani()
def trdpuasa():
      global txt
      if int(tm('%H%M')) == saur:
            txt = open('.___','r').readlines()
      else: 
            txt = open('.____','r').readlines()
      ttx = Thread(name='puasa',target=suara)
      ttx.start()
      while ttx.isAlive():
            ani()
                 
def banner():
      sp.call('clear')
      print(f'''     
      {lgr}:::::::{lg}╗{lgr}::{lg}╗  {lgr}::{lg}╗ {lgr}::::::{lg}╗ {lgr}::{lg}╗      {lgr}:::::{lg}╗ {lgr}::::::::{lg}╗
      {lgr}::{lg}╔════╝{lgr}::{lg}║  {lgr}::{lg}║{lgr}::{lg}╔═══{lgr}::{lg}╗{lgr}::{lg}║     {lgr}::{lg}╔══{lgr}::{lg}╗╚══{lgr}::{lg}╔══╝
      {lgr}:::::::{lg}╗{lgr}:::::::{lg}║{lgr}::{lg}║   {lgr}::{lg}║{lgr}::{lg}║     {lgr}:::::::{lg}║   {lgr}::{lg}║   
      ╚════{lgr}::{lg}║{lgr}::{lg}╔══{lgr}::{lg}║{lgr}::{lg}║   {lgr}::{lg}║{lgr}::{lg}║     {lgr}::{lg}╔══{lgr}::{lg}║   {lgr}::{lg}║   
      {lgr}:::::::{lg}║{lgr}::{lg}║  {lgr}::{lg}║╚{lgr}::::::{lg}╔╝{lgr}:::::::{lg}╗{lgr}::{lg}║  {lgr}::{lg}║   {lgr}::{lg}║   
      ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝
              {lw}Programmer Muslim Nggak Lupa Ibadah{lg}
                  {lg}[{x}Special Thanks, ERR0R H{lg}]
_______________________________________________________________
''')                                                  

            

def menu():
      banner()
      print(f'''
{lg}1.{lw} Aktifkan
{lg}2.{lw} Ganti kota
{lg}3.{lw} Update
{lg}4.{lw} Tentang
{lg}0.{lw} Keluar''')
      
      p = input(lg+'\nSholat # '+x)
      if p == '1':
         
            start()
      elif p == '2':
            try:
                  sp.call('rm .cookie/ts')
            except:
                  pass
            gettown()
            start()
      elif p == '3':
            update()
      elif p == '4':
            tentang()
      else:
            exit()           
      
def update():
      banner()
      print(lr+'Jangan di cancell ya ukhty.. biar nggak error :*')
      print(lg+'Cek jaringan..')
      try:
            get('https://github.com')
      except requests.exceptions.ConnectionError:
            print(lg+'Astaghfirullah.. Ukhty lupa ngidupin jaringannya')
            exit()
      print(lg+'Mengupdate..\nLama tidaknya tergantung jaringan, sabarr :)')
      
      os.system('cd .. && rm -rf sholat')     
      sp.call(['cd .. && git clone https://github.com/karjok/sholat'],shell=True, stdout=sp.DEVNULL,stderr=sp.STDOUT)
      print(lg+'Selesai mengupdate')
      print(lg+'Memulai ulang..')
      sleep(2)
      os.system('cd ../sholat && python sholat.py')    
def tentang():
      banner()
      print(f'''
         
{lg}Nama        : {lw}Sholat
{lg}Versi       : {lw}2.0 (update: 5 Mei 2019, 6:00PM)
{lg}Tanggal     : {lw}31 Januari 2020, 2:18PM
{lg}Author      : {lw}Nggak Lupa Ibadah
{lg}Coder       : {lw}ERR0R
              waktu sholat
{lg}Team        : {lw}ITALIA CYBER ARMY
              Eka Pangesty, CRABS dan semua
              umat Muslim seplanet bumi.
{lg}NB          : {lw}Manusia nggak ada yang sempurna,
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              ke:  - https://t.me/termuxxhacking
                   - https://facebook.com/termuxxhacking
                   - @termux_hacking''')
      input(lg+'Enterin aja ')
      menu()     
      

             
                                                
                                                                                          
def exit():
      print(lg+'_'*63)
      print('Makasih ukhty,\nSemoga sehat selalu  😙'+x)



if __name__=='__main__':
      try:
            os.mkdir('.cookie')
      except OSError:
            pass
      
      menu()
     
