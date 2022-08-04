#Here we define the regular expression templates
#Next we need to focus on working on the most imprortant part, making better templates
#Updated add more templates
EXPRESSIONS = [("what.*is.*apple.*",     ["apple", "outlook"]), 
								("what.*about.*apple.*",  ["apple", "outlook"]),  
								("what.*good.*apple.*",   ["apple", "outlook"]),
								("what.*bad.*apple.*",    ["apple", "outlook"]),
								("what.*ugly.*apple.*",   ["apple", "outlook"]),
	
								("how.*is.*apple.*",       ["apple", "outlook"]), 
								("how.*about.*apple.*",    ["apple", "outlook"]), 
								("how.*good.*apple.*",    ["apple", "outlook"]),
								("how.*bad.*apple.*",      ["apple", "outlook"]),
								("how.*ugle.*apple.*",     ["apple", "outlook"]), 
								
								("apple.*good.*",       ["apple", "feeling", "good"]), 
								("apple.*bad.*",       	["apple", "feeling",  "bad"]), 
								("apple.*ugly.*",       ["apple", "feeling", "ugly"])]

stop_words = ["is","a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "looking", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours	ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "just", "sure" ,"portfolio", "hell", "knows", "anything", "anymore", "moment", "wouldnt", "agree", "fairly", "look", "looked", "looks"]
# Common misspelling of the word 'apple'
apple_list = ["aaple","aple","aplolo","appled","appl","april19","uppper","peploe","appllo","applica","acappella","peapole","aplid","appoligy","awhlie","opeople","aprel","april15","appera","rappell","april13","applid","applse","apporve","appllied","apolo","appleal","appilque","ocuple","applu","happil","apeall","applay","appite","appaulse","appleid","pupple","appil","eople","aplle","apppeal","appon","apogoly","appeir","appels","apage","unplu","aprul","appliied","apolgy","happely","aapply","aapl","appli","apliy","appelate","appilied","appolgy","pple","peuple","appauled","april1","happiley","apologe","arpil","pepley","appaly","appulse","aplles","airplne","avale","eample","aapple","appial","appluase","applier","azelea","appllate","apper","applled","applye","pople","aplpy","appily","appril","appde","appove","applise","acuple","acouple","apeel","appell","applea","aplay","appone","appied","epeople","appolize","applly","ampel","paople","upthe","appliy","appolige","appolgoy","opole","kuple","appitie","applieed","apllo","upsale","apoll","appky","chapple","applett","papel","afule","appyly","apahled","happley","apul","papuler","applase","caple","apperre","appe","paale","applyl","appolied","appollo","applod","apallo","mapple","appache","piple","appliny","appaih","applity","uppoer","appereal","accappela","appro","pieapple","appea","apptly","aplase","urple","appolo","applief","oeople","popple","appelet","apove","appeear","appluse","apile","appel","applky","appeles","aple","applouse","applyto","applaod","appitte","applogie","apower","uppler","epople","apsule","upsel","appaul","apparl","applide","aplet","aptil","applude","appeled","appal","april09","apoly","appael","applt","appovel","appol","apirl","appiel","appieled","applke","applauce","appere","aplha","puple","appeite","appeaal","acule","aplpe","appals","appare","aparrel","pepple","cple","appauld","spple","appen","appiled","applaid","apploud","appply","apruil","appahy","apperel","oeple","applligy","applis","peeple","eaple","awhle","apoloze","aaple","apeal","applyt","aplise","appolagy","niple","ahppily","aprille","peppole","appolise","apolige","apperr","appliace","appouled","apleal","apoke","applyig","aplly","appnea","aplpha","appele","apprel","apail","parle","appoled","apaper","appetie","apoloy","uppe","appliet","april12","applad","acappela","aplide","upove","applice","appaear","happliey","ahppen","apaulige","apliey","apeil","appologe","anple","ahile","april14","ciuple","appple","athle","peple","popele","aaply","apaly","epoepl","hple","aparel","appeall","applud","appileed","amople","ahole","appleas","applaed","taple","apnoea","popole","apauled","ofpeople","appale","apolegy","applie","applys","atyle","appla","appierd","accappella","saple","april7","appile","epole","toapply","aptley","cupple","pepele","appluade","apolage","apptie","appier","ahpe","apele","capale","appiate","apperce","appaer","appaluse","apologh","apull","ouple","appilogy","apppear","peiple","aplty","niipple","artle","aptely","aplil","appls","applicae","april18","applode","apprella","apprea","awale","applogy","applle","aples","appette","apolize","aopply","poaple","appples","appalogy","aprile","aplose","appiete","happile","appll","appley","aplie","appeln","sple","appausle","appela","cauple","appolgie","appualed","apell","applee","appiles","appole","applyd","appaled","applyyy","apprear","appplied","applo","appuled","april16","carple","azule","apolgie","applozie","aaaaple","atpl","apploige","appolygy","apotille","appaerl","appeae","appiette","applw","appliea","appliey","appyled","appliuqe","apploy","applythe","aspply","ppply","appre","appover","acopl","lappel","napoli","napoly","nppl","pe0ple","pepplo","acale","upply","uppre","paple"]