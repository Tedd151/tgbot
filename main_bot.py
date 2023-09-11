import telebot
from telebot import util
from telebot import types
import random 
from time import sleep

bot = telebot.TeleBot("2047488618:AAESmFMai19fUtSYSyVAGKHN1fKqyNVWpRw")

dancehall_xtend = "https://t.me/kdzresources/61"
dancehall_xtend1 = "https://t.me/kdzresources/66"

ps = "https://t.me/kdzresources/13"
ai = "https://t.me/kdzresources/19"
pr = "https://t.me/kdzresources/14"
lr = "https://t.me/kdzresources/13"
pa = "https://t.me/kdzresources/15"
ae = "https://t.me/kdzresources/17"

video_demo = "https://t.me/kdzresources/31"

sony_acid = "https://t.me/kdzresources/8"
sony_acid8 = "https://t.me/kdzresources/24"
sony_acid6 = "https://t.me/kdzresources/67"
sony_acid10 = "https://t.me/kdzresources/26"
sony_acid11 = ""
sony_vegas16 = "https://t.me/kdzresources/35"
sony_vegas15 = "https://t.me/kdzresources/53"
sony_vegas14 = "https://t.me/kdzresources/34"
sony_vegas13 = "https://t.me/kdzresources/57"
sony_vegas20 = ""
vdj_win = "https://t.me/kdzresources/20"
vdj7 = "https://t.me/kdzresources/56"
vdj_mac = "https://t.me/kdzresources/21"
serato_v255 = "https://t.me/kdzresources/3"
serato_v257 = "https://t.me/kdzresources/30"
serato_macos = "https://t.me/kdzresources/54"
passwordz = "https://t.me/f70st"
vext = "https://t.me/kdzresources/62"
vext1 = "https://t.me/kdzresources/63"
vext2 = "https://t.me/kdzresources/64"
vext3 = "https://t.me/kdzresources/65"
kenyaxtends = "https://t.me/kdzresources/46"
kenyaextends1 = "https://t.me/kdzresources/61"
hiphopxtends = "https://t.me/kdzresources/43"
east_acc = "https://t.me/kdzresources/37"
dancehall_acc = "https://t.me/kdzresources/36"
video_ext1 = "https://t.me/kdzresources/63"
video_ext = "https://t.me/kdzresources/36"
video_ext2 = "https://t.me/kdzresources/64"
video_ext3 = "https://t.me/kdzresources/65"
recordbox6 = "https://t.me/kdzresources/58"
mix_emac = "https://t.me/kdzresources/9"
sound_efx ="https://t.me/kdzresources/23"
other = "coming soon.."


#main_menu buttons
main_menu = types.ReplyKeyboardMarkup(row_width=1)
m_b1 = types.KeyboardButton('softwares')
m_b2 = types.KeyboardButton('music')
m_b3 = types.KeyboardButton('graphic_design')
m_b4 = types.KeyboardButton('drops')
m_b5 = types.KeyboardButton('social_media')
m_b6 = types.KeyboardButton('password')
m_b7 = types.KeyboardButton('help')

main_menu.row(m_b1, m_b2)
main_menu.row(m_b3, m_b4)
main_menu.row(m_b5, m_b6)
main_menu.row(m_b7)

#welcome command message_handler

@bot.message_handler(commands=['start'])
def intro(message):
  username = message.from_user.username
  user_id = message.from_user.id
  bot.send_message(message.chat.id, "hello " + str(username))
 # bot.send_message("hello" f"{username} {user_id} "); sleep(2.0)
  large_text = open("intro.txt", "rb").read()
  splitted_text = util.split_string(large_text, 5000)
  bot.send_message(message.chat.id, splitted_text)
  bot.send_message(message.chat.id,"-" ,reply_markup=main_menu)
  #photo = open('keyboard.jpg', 'rb')
  #bot.send_photo(message.chat.id, photo)

  
#message handler "the main work"
@bot.message_handler(commands=['video'])
def help_video(message):
  bot.send_message(message.chat.id, video_demo)
 
@bot.message_handler()
def text_handler(message):
  if message.text =='softwares' or message.text == 'Softwares':
    s_menu = types.ReplyKeyboardMarkup(row_width=1)
    s_1 = types.KeyboardButton('serato')
    s_2 = types.KeyboardButton('vdj')
    s_3 = types.KeyboardButton('recordbox')
    s_4 = types.KeyboardButton('mix_emergency')
    s_5 = types.KeyboardButton('sony_acid')
    s_6 = types.KeyboardButton('sony_vegas')
    s_7 = types.KeyboardButton('Adobe')
    s_8 = types.KeyboardButton('others')
    back =types.KeyboardButton('back_to_main-menu')
    
    s_menu.row(s_1, s_2)
    s_menu.row(s_3, s_4)
    s_menu.row(s_5, s_6)
    s_menu.row(s_7, s_8)
    s_menu.row(back)
    username = message.from_user.username
    bot.send_message(message.chat.id, "Select an option " + username, reply_markup=s_menu)
    
  if message.text == 'music' or message.text == 'Music':
    music_menu = types.ReplyKeyboardMarkup(row_width=1)
    m_1 = types.KeyboardButton('extended')
    m_2 = types.KeyboardButton('accapella')
    m_3 = types.KeyboardButton('video_extend')
    m_4 = types.KeyboardButton('sound_effects')
    back = types.KeyboardButton('back_to_main-menu')
    
    music_menu.row(m_1, m_2)
    music_menu.row(m_3, m_4)
    music_menu.row(back)
    bot.send_message(message.chat.id, "Select an option", reply_markup=music_menu)
    
 #music category 1
  if message.text == 'extended' or message.text == 'Extended':
    ext = types.ReplyKeyboardMarkup(row_width=1)
    ext1 = types.KeyboardButton('kenyan_xtend')
    ext2 = types.KeyboardButton('hiphop_xtend')
    ext3 = types.KeyboardButton('dancehall_xtend')
    back = types.KeyboardButton('back_to_main-menu')
    
    ext.row(ext1, ext2)
    ext.row(ext3)
    ext.row(back)
    bot.send_message(message.chat.id, "Select an option" , reply_markup=ext)
    
  if message.text == 'kenyan_xtend' or message.text == 'Kenyan_xtend':
    bot.send_message(message.chat.id, kenyaxtends)
  if message.text == 'hiphop_xtend' or message.text == 'Hiphop_xtend':
    bot.send_message(message.chat.id, hiphopxtends)
    
  if message.text == 'dancehall_xtend' or message.text == 'Dancehall_xtend':
    bot.send_message(message.chat.id, dancehall_xtend)
    bot.send_message(message.chat.id, dancehall_xtend1)
 
 #music category 2
  if message.text == 'accapella' or message.text == 'Accapella':
    am = types.ReplyKeyboardMarkup(row_width=1)
    am1 = types.KeyboardButton('east_africa')
    am2 = types.KeyboardButton('dancehall_acc')
    back = types.KeyboardButton('back_to_main-menu')
    
    am.row(am1, am2)
    am.row(back)
    bot.send_message(message.chat.id, "Select an option" , reply_markup=am)
  if message.text == 'east_africa' or message.text == 'East_africa':
    bot.send_message(message.chat.id, east_acc)
  if message.text == 'dancehall_acc' or message.text == 'Dancehall_acc':
    bot.send_message(message.chat.id, dancehall_acc)
  
 #music category 3 
  if message.text == 'video_extend' or message.text == 'Video_extend':
    bot.send_message(message.chat.id, vext)
    bot.send_message(message.chat.id, vext1)
    bot.send_message(message.chat.id, vext2)
    bot.send_message(message.chat.id, vext3)
 
  if message.text == 'sound_effects' or message.text == 'Sound_effects':
    bot.send_message(message.chat.id, sound_efx)
 
 
 #mainmenu cstegory20pl
  if message. text == 'social_media' or message.text == 'Social_media':
    sm_menu = types.ReplyKeyboardMarkup(row_width=1)
    sm1 = types.KeyboardButton('group')
    sm2 = types.KeyboardButton('contact')
    sm3 = types.KeyboardButton('description')
    back = types.KeyboardButton('back_to_main-menu')
    sm_menu.row(sm1, sm2)
    sm_menu.row(sm3)
    sm_menu.row(back)
    bot.send_message(message.chat.id, "Select an option", reply_markup=sm_menu)
 ## group   
  if message.text == 'group' or message.text == 'Group':
    gmenu = types.ReplyKeyboardMarkup(row_width=1)
    g1 = types.KeyboardButton('telegram')
    g2 = types.KeyboardButton('whatsapp')
    back = types.KeyboardButton('back_to_main-menu')
    gmenu.row(g1, g2)
    gmenu.row(back)
    bot.send_message(message.chat.id, "Select an option", reply_markup=gmenu)
    
  if message.text == 'Telegram' or message. text == 'telegram':
    bot.send_message(message.chat.id, "https://t.me/kenyadjszone")
  if message.text == 'Whatsapp' or message.text == 'whatsapp':
    bot.send_message(message.chat.id, "https://chat.whatsapp.com/CuoaVtrDI7nCu73Exa2Sv6")
  if message.text == 'contact' or message.text == 'Contact':
    large_text = open("contact.txt", "rb").read()
    splitted_text = util.split_string(large_text, 5000)
    bot.send_message(message.chat.id, large_text, 5000)
  if message.text == 'description' or message.text == 'Description':
    large_text = open("description.txt", "rb").read()
    splitted_text = util.smart_split(large_text, chars_per_string=3000)
    for text in splitted_text:
	    bot.send_message(message.chat.id, text)
            
  if message.text == 'password' or message.text == 'Password':
    username = message.from_user.username
    bot.send_message(1522292107, "password was requested by " + f"{username}")
    bot.send_message(message.chat.id, "request received you will be contacted or contact  https://t.me/f70st"); sleep(1.0)
    bot.send_message(message.chat.id, "note for some files a small amount of donation is required for maintainance")
    #help
  if message.text == 'help' or message.text == 'Help':
    help_menu = types.ReplyKeyboardMarkup(row_width=1)
    h1 = types.KeyboardButton('demo')
    h2 = types.KeyboardButton('instructions')
    back = types.KeyboardButton('back_to_main-menu')
    help_menu.row(h1, h2)
    help_menu.row(back)
    bot.send_message(message.chat.id, "Select an option", reply_markup=help_menu)
  if message.text == 'instructions' or message.text == 'Instructions':
     large_text = open("instructions.txt", "rb").read()
     splitted_text = util.smart_split(large_text, chars_per_string=3000)
     for text in splitted_text:
	     bot.send_message(message.chat.id, text)
     photo = open('keyboard.jpg', 'rb')
     bot.send_photo(message.chat.id, photo)
  
  if message.text == 'Demo' or message.text == 'demo':
    bot.send_message(message.chat.id, video_demo)
    
    
    #graphic_design
  if message.text == 'graphic_design' or message.text == 'Graphic_design':
    gfx_menu = types.ReplyKeyboardMarkup(row_width=1)
    gfx1 = types.KeyboardButton('comingsoon')
    gfx2 = types.KeyboardButton('contact my owner for the slot')
    back = types.KeyboardButton('back_to_main-menu')
    gfx_menu.row(gfx1)
    gfx_menu.row(gfx2)
    gfx_menu.row(back)
    bot.send_message(message.chat.id, "Select an option", reply_markup=gfx_menu)
    
 #drops  
  if message.text == 'drops' or message.text == 'Drops':
    drop_menu = types.ReplyKeyboardMarkup(row_width=1)
    cat_1 = types.KeyboardButton('wingman&patt')
    cat_3 = types.KeyboardButton('mendy')
    back = types.KeyboardButton('back to main_menu')
    drop_menu.row(cat_1, cat_3)
    drop_menu.row(back)
    bot.send_message(message.chat.id, "Select an dealer", reply_markup=drop_menu)
    
  if message.text == 'wingman&patt' or message.text == 'Wingman&patt':
    wm = types.ReplyKeyboardMarkup(row_width=1)
    wm1 = types.KeyboardButton('nexx_king')
    wm2 = types.KeyboardButton('esco_nation')
    back1 = types.KeyboardButton('back_to_main-menu')
    wm.row(wm1)
    wm.row(wm2)
    wm.row(back1)
    bot.send_message(message.chat.id, "Select a dealer ", reply_markup=wm)
  if message.text == 'nexx_king' or message.text == 'Nexx_king':
    bot.send_message(message.chat.id, "@nexx_king \n wa.me/254 719216473")
  if message.text == 'esco_nation' or message.text == 'Esco_nation':
    bot.send_message(message.chat.id, "wa.me/254113673213")
  if message.text == 'mendy' or message.text == 'Mendy':
    bot.send_message(message.chat.id, "wa.me/254716891749")
    
  if message.text == 'back_to_main-menu':
    bot.send_message(message.chat.id, "main_menu", reply_markup=main_menu)
  
#softwares category serato
  if message.text == 'serato' or message.text == 'Serato':
    ser_menu = types.ReplyKeyboardMarkup(row_width=1)
    ser1 = types.KeyboardButton('serato_win')
    ser2 = types.KeyboardButton('serato_mac')
    back = types.KeyboardButton('back_to_main-menu')
    ser_menu.row(ser1, ser2)
    ser_menu.row(back)
    bot.send_message(message.chat.id, "Select an option ", reply_markup=ser_menu)
    #windows
  if message.text == 'serato_win' or message.text == 'Serato_win':
    srt = types.ReplyKeyboardMarkup(row_width=1)
    srt2 = types.KeyboardButton('serato-2_5_7')
    srt3 = types.KeyboardButton('serato-2_5_5')
    back = types.KeyboardButton('back_to_main-menu')
    srt.row(srt2, srt3)
    srt.row(back)
    bot.send_message(message.chat.id, "Select an option " , reply_markup=srt)
  if message.text == 'serato-2_5_7' or message.text =='Serato-2_5_7':
     bot.send_message(message.chat.id, serato_v257)
  if message.text == 'serato-2_5_5' or message.text =='Serato-2_5_5':
    bot.send_message(message.chat.id, serato_v255)
    #mac
  if message.text == 'serato_mac' or message.text == 'Serato_mac':
    bot.send_message(message.chat.id, serato_macos)
    
#software category 2 virtual dj
  if message.text == 'vdj' or message.text == 'Vdj':
    vm = types.ReplyKeyboardMarkup(row_width=1)
    v1 = types.KeyboardButton('vdj_win')
    v2 = types.KeyboardButton('vdj_mac')
    back = types.KeyboardButton('back_to_main-menu')
    vm.row(v1, v2)
    vm.row(back)
    bot.send_message(message.chat.id, "Select an option", reply_markup=vm)    
  if message.text == 'vdj_win' or message.text == 'Vdj_win':
    vw = types.ReplyKeyboardMarkup(row_width=1)
    v1 = types.KeyboardButton('vdj_pro7')
    v2 = types.KeyboardButton('vdj_pro8')
    back = types.KeyboardButton('back_to_main-menu')
    vw.row(v1, v2)
    vw.row(back)
    bot.send_message(message.chat.id, "Select an option ", reply_markup=vw)
  if message.text == 'vdj_pro7' or message.text == 'Vdj_pro7':
    bot.send_message(message.chat.id, vdj7)
  if message.text == 'vdj_pro8' or message.text == 'Vdj_pro8':
    bot.send_message(message.chat.id, vdj_win)
  if message.text == 'vdj_mac' or message.text == 'Vdj_mac':
    
    bot.send_message(message.chat.id, vdj_mac)
    
#software category 3 acid
  if message.text == 'sony_acid' or message.text == 'sony_acid':
    acid = types.ReplyKeyboardMarkup(row_width=1)
    
    back = types.KeyboardButton('back_to_main-menu')
    vn6 = types.KeyboardButton('acidpro_6')
    vn7 = types.KeyboardButton('acidpro_7')
    vn8  = types.KeyboardButton('acidpro_8')
    vn10 = types.KeyboardButton('acidpro_10')
    vn11 = types.KeyboardButton('acidpro_11')
    acid.row(vn6, vn7)
    acid.row(vn8, vn10)
    acid.row(vn11)
    acid.row(back)
    bot.send_message(message.chat.id, "Select version", reply_markup=acid)
    
  if message.text == 'acidpro_7' or message.text == 'Acidpro_7':
    bot.send_message(message.chat.id, sony_acid)
  if message.text == 'acidpro_6' or message.text == 'Acidpro_6':
    bot.send_message(message.chat.id, sony_acid6)
  if message.text == 'acidpro_8' or message.text == 'Acidpro_8':
    bot.send_message(message.chat.id, sony_acid8)
  if message.text == 'acidpro_10' or message.text == 'Acidpro_10':
    bot.send_message(message.chat.id, sony_acid10)
  if message.text == 'acidpro_11' or message.text == 'Acidpro_11':
    comingsoon = open("coming.txt", "rb").read()
    bot.send_message(message.chat.id, comingsoon)
#software category 4 sony sony sony_vegas
  if message.text == 'sony_vegas' or message.text == 'sony_vegas':
    sv_menu = types.ReplyKeyboardMarkup(row_width=1)
    sv1 = types.KeyboardButton('sonyvegas_pro13')
    sv2 = types.KeyboardButton('sonyvegas_pro14')
    sv3 = types.KeyboardButton('sonyvegas_pro15')
    sv4 = types.KeyboardButton('sonyvegas_pro16')
    sv5 = types.KeyboardButton('sonyvegas_pro20')
    back = types.KeyboardButton('back_to_main-menu')
    sv_menu.row(sv1, sv2)
    sv_menu.row(sv3, sv4)
    sv_menu.row(sv5)
    sv_menu.row(back)
    bot.send_message(message.chat.id, "Select an option " , reply_markup=sv_menu)
  if message.text == 'sonyvegas_pro13' or message.text == 'Sonyvegas_pro13':
    bot.send_message(message.chat.id, sony_vegas13)
  if message.text == 'sonyvegas_pro14' or message.text == 'Sonyvegas_pro14':
    bot.send_message(message.chat.id, sony_vegas14)
  if message.text == 'sonyvegas_pro15' or message.text == 'Sonyvegas_pro15':
    bot.send_message(message.chat.id, sony_vegas15)
  if message.text == 'sonyvegas_pro16' or message.text == 'Sonyvegas_pro16':
    bot.send_message(message.chat.id, sony_vegas16)
  if message.text == 'sonyvegas_pro20' or message.text == 'Sonyvegas_pro20':
    comingsoon = open("coming.txt", "rb").read()
    bot.send_message(message.chat.id, comingsoon)
    
 #softwares category 5
  if message.text == 'adobe' or message.text == 'Adobe':
    markupa = types.ReplyKeyboardMarkup(row_width=1)
    itema = types.KeyboardButton('photoshop')
    itemb = types.KeyboardButton('after_effects')
    itemc = types.KeyboardButton('lightroom')
    itemd = types.KeyboardButton('premier_pro')
    iteme = types.KeyboardButton('audition')
    itemk = types.KeyboardButton('newer-verson')
    back = types.KeyboardButton('back_to_main-menu')
    
    markupa.row(itema, itemb)
    markupa.row(itemc, itemd)
    markupa.row(iteme)
    markupa.row(itemk)
    markupa.row(back)
    
    bot.send_message(message.chat.id, "Select the software", reply_markup=markupa)
  if message.text == 'photoshop' or message.text =='Photoshop':
    bot.send_message(message.chat.id, ps)
      
  if message.text == 'after_effects' or message.text =='After_effects':
    bot.send_message(message.chat.id, ae)
      
  if message.text == 'lightroom' or message.text =='Lightroom':
    bot.send_message(message.chat.id, lr)
      
  if message.text == 'premier_pro' or message.text =='Premier_pro':
    bot.send_message(message.chat.id, pr)
      
  if message.text == 'audition' or message.text =='Audition':
    bot.send_message(message.chat.id, pa)
  if message.text == 'newer-verson' or message.text == 'Newer-verson':
    comingsoon = open("coming.txt", "rb").read()
    bot.send_message(message.chat.id, comingsoon)

#recordbox    
  if message.text == 'recordbox' or message.text =='Recordbox':
   comingsoon = open("coming.txt", "rb").read()
   bot.send_message(message.chat.id, comingsoon)
 #category 7
  if message.text == 'mix_emergency' or message.text =='mix_emergency':
    bot.send_message(message.chat.id, mix_emac)
 
  if message.text == 'others' or message.text == 'Others':
    bot.send_message(message.chat.id, "in development coming soon")
    
    
    
bot.infinity_polling()

print("bot is up and running..")