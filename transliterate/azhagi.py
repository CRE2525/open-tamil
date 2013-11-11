## -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
# 
# Implementation of Azhagi rules - தமிழ் எழுத்துக்கள்
# Ref: B. Viswanathan, http://www.mazhalaigal.com/tamil/learn/keys.php
# 
class Transliteration:
    table = {}
    # not implemented - many-to-one table

    # Azhagi has a many-to-one mapping - using a Tamil language model and Baye's conditional probabilities
    # to break the tie when two or more Tamil letters have the same English syllable. Currently 
    
    table["a"]="அ"
    table["aa"]="ஆ"
    table["A"]="ஆ"
    table["i"]="இ"
    table["ee"]="ஈ"
    table["I"]="ஈ"
    table["u"]="உ"
    table["oo"]="ஊ"
    table["U"]="ஊ"
    table["e"]="எ"
    table["E"]="ஏ"
    table["ae"]="ஏ"
    table["ai"]="ஐ"
    table["o"]="ஒ"
    table["O"]="ஓ"
    table["oe"]="ஓ"
    table["oa"]="ஓ"
    table["ou"]="ஔ"
    table["au"]="ஔ"
    table["ow"]="ஔ"
    table["q"]="ஃ"
    table["ga"]="க"
    table["ca"]="க"
    table["kha"]="க"
    table["gha"]="க"
    table["ka"]="க"
    table["Ka"]="க"
    table["kaa"]="கா"
    table["gaa"]="கா"
    table["caa"]="கா"
    table["khaa"]="கா"
    table["ghaa"]="கா"
    table["kA"]="கா"
    table["gA"]="கா"
    table["cA"]="கா"
    table["khA"]="கா"
    table["ghA"]="கா"
    table["ki"]="கி"
    table["gi"]="கி"
    table["ci"]="கி"
    table["khi"]="கி"
    table["ghi"]="கி"
    table["kii"]="கீ"
    table["kee"]="கீ"
    table["kI"]="கீ"
    table["gee"]="கீ"
    table["gI"]="கீ"
    table["gii"]="கீ"
    table["cee"]="கீ"
    table["cI"]="கீ"
    table["cii"]="கீ"
    table["khee"]="கீ"
    table["khI"]="கீ"
    table["khii"]="கீ"
    table["ghee"]="கீ"
    table["ghI"]="கீ"
    table["ghii"]="கீ"
    table["gu"]="கு"
    table["cu"]="கு"
    table["khu"]="கு"
    table["ghu"]="கு"
    table["ku"]="கு"
    table["koo"]="கூ"
    table["kU"]="கூ"
    table["goo"]="கூ"
    table["gU"]="கூ"
    table["guu"]="கூ"
    table["coo"]="கூ"
    table["cU"]="கூ"
    table["cuu"]="கூ"
    table["khoo"]="கூ"
    table["khU"]="கூ"
    table["khuu"]="கூ"
    table["ghoo"]="கூ"
    table["ghU"]="கூ"
    table["ghuu"]="கூ"
    table["kuu"]="கூ"
    table["ge"]="கெ"
    table["ce"]="கெ"
    table["khe"]="கெ"
    table["ghe"]="கெ"
    table["ke"]="கெ"
    table["kE"]="கே"
    table["gE"]="கே"
    table["gae"]="கே"
    table["cE"]="கே"
    table["cae"]="கே"
    table["khE"]="கே"
    table["khae"]="கே"
    table["ghE"]="கே"
    table["ghae"]="கே"
    table["kae"]="கே"
    table["gai"]="கை"
    table["cai"]="கை"
    table["khai"]="கை"
    table["ghai"]="கை"
    table["koa"]="கை"
    table["kou"]="கௌ"
    table["kau"]="கௌ"
    table["gow"]="கௌ"
    table["gou"]="கௌ"
    table["gau"]="கௌ"
    table["cow"]="கௌ"
    table["cou"]="கௌ"
    table["cau"]="கௌ"
    table["khow"]="கௌ"
    table["khou"]="கௌ"
    table["khau"]="கௌ"
    table["ghow"]="கௌ"
    table["ghou"]="கௌ"
    table["ghau"]="கௌ"
    table["kow"]="கௌ"
    table["g"]="க்"
    table["c"]="க்"
    table["kh"]="க்"
    table["gh"]="க்"
    table["k"]="க்"
    table["nga"]="ங"
    table["nGa"]="ங"
    table["nGA"]="ஙா"
    table["ngaa"]="ஙா"
    table["ngA"]="ஙா"
    table["nGaa"]="ஙா"
    table["ngi"]="ஙி"
    table["nGi"]="ஙி"
    table["nGee"]="ஙீ"
    table["nGI"]="ஙீ"
    table["ngee"]="ஙீ"
    table["ngI"]="ஙீ"
    table["ngii"]="ஙீ"
    table["nGii"]="ஙீ"
    table["ngu"]="ஙு"
    table["nGu"]="ஙு"
    table["nGoo"]="ஙூ"
    table["nGU"]="ஙூ"
    table["ngoo"]="ஙூ"
    table["ngU"]="ஙூ"
    table["nguu"]="ஙூ"
    table["nGuu"]="ஙூ"
    table["nge"]="ஙெ"
    table["nGe"]="ஙெ"
    table["nGE"]="ஙே"
    table["ngE"]="ஙே"
    table["ngae"]="ஙே"
    table["nGae"]="ஙே"
    table["ngai"]="ஙை"
    table["nGai"]="ஙை"
    table["ngo"]="ஙொ"
    table["nGo"]="ஙொ"
    table["nGO"]="ஙோ"
    table["nGoe"]="ஙோ"
    table["ngO"]="ஙோ"
    table["ngoa"]="ஙோ"
    table["ngoe"]="ஙோ"
    table["nGoa"]="ஙோ"
    table["nGou"]="ஙௌ"
    table["nGau"]="ஙௌ"
    table["ngow"]="ஙௌ"
    table["ngou"]="ஙௌ"
    table["ngau"]="ஙௌ"
    table["nGow"]="ஙௌ"
    table["ng"]="ங்"
    table["nG"]="ங்"
    table["cha"]="ச"
    table["sa"]="ச"
    table["sA"]="சா"
    table["chaa"]="சா"
    table["chA"]="சா"
    table["saa"]="சா"
    table["chi"]="சி"
    table["si"]="சி"
    table["see"]="சீ"
    table["sI"]="சீ"
    table["chee"]="சீ"
    table["chI"]="சீ"
    table["chii"]="சீ"
    table["sii"]="சீ"
    table["chu"]="சு"
    table["su"]="சு"
    table["soo"]="சூ"
    table["sU"]="சூ"
    table["choo"]="சூ"
    table["chU"]="சூ"
    table["chuu"]="சூ"
    table["suu"]="சூ"
    table["che"]="செ"
    table["se"]="செ"
    table["sE"]="சே"
    table["chE"]="சே"
    table["chae"]="சே"
    table["sae"]="சே"
    table["chai"]="சை"
    table["sai"]="சை"
    table["cho"]="சொ"
    table["so"]="சொ"
    table["sO"]="சோ"
    table["soe"]="சோ"
    table["chO"]="சோ"
    table["choa"]="சோ"
    table["choe"]="சோ"
    table["soa"]="சோ"
    table["sou"]="சௌ"
    table["sau"]="சௌ"
    table["chow"]="சௌ"
    table["chou"]="சௌ"
    table["chau"]="சௌ"
    table["sow"]="சௌ"
    table["ch"]="ச்"
    table["s"]="ச்"
    table["gna"]="ஞ"
    table["nja"]="ஞ"
    table["Gna"]="ஞ"
    table["GnA"]="ஞா"
    table["gnaa"]="ஞா"
    table["gnA"]="ஞா"
    table["njaa"]="ஞா"
    table["njA"]="ஞா"
    table["Gnaa"]="ஞா"
    table["gni"]="ஞி"
    table["nji"]="ஞி"
    table["Gni"]="ஞி"
    table["Gnee"]="ஞீ"
    table["GnI"]="ஞீ"
    table["gnee"]="ஞீ"
    table["gnI"]="ஞீ"
    table["gnii"]="ஞீ"
    table["njee"]="ஞீ"
    table["njI"]="ஞீ"
    table["njii"]="ஞீ"
    table["Gnii"]="ஞீ"
    table["gnu"]="ஞு"
    table["nju"]="ஞு"
    table["Gnu"]="ஞு"
    table["Gnoo"]="ஞூ"
    table["GnU"]="ஞூ"
    table["gnoo"]="ஞூ"
    table["gnU"]="ஞூ"
    table["gnuu"]="ஞூ"
    table["njoo"]="ஞூ"
    table["njU"]="ஞூ"
    table["njuu"]="ஞூ"
    table["Gnuu"]="ஞூ"
    table["gne"]="ஞெ"
    table["nje"]="ஞெ"
    table["Gne"]="ஞெ"
    table["GnE"]="ஞே"
    table["gnE"]="ஞே"
    table["gnae"]="ஞே"
    table["njE"]="ஞே"
    table["njae"]="ஞே"
    table["Gnae"]="ஞே"
    table["gnai"]="ஞை"
    table["njai"]="ஞை"
    table["Gnai"]="ஞை"
    table["gno"]="ஞொ"
    table["njo"]="ஞொ"
    table["Gno"]="ஞொ"
    table["GnO"]="ஞோ"
    table["Gnoe"]="ஞோ"
    table["gnO"]="ஞோ"
    table["gnoa"]="ஞோ"
    table["gnoe"]="ஞோ"
    table["njO"]="ஞோ"
    table["njoa"]="ஞோ"
    table["njoe"]="ஞோ"
    table["Gnoa"]="ஞோ"
    table["Gnou"]="ஞௌ"
    table["Gnau"]="ஞௌ"
    table["gnow"]="ஞௌ"
    table["gnou"]="ஞௌ"
    table["gnau"]="ஞௌ"
    table["njow"]="ஞௌ"
    table["njou"]="ஞௌ"
    table["njau"]="ஞௌ"
    table["Gnow"]="ஞௌ"
    table["gn"]="ஞ்"
    table["nj"]="ஞ்"
    table["Gn"]="ஞ்"
    table["da"]="ட"
    table["ta"]="ட"
    table["tA"]="டா"
    table["daa"]="டா"
    table["dA"]="டா"
    table["taa"]="டா"
    table["di"]="டி"
    table["ti"]="டி"
    table["tee"]="டீ"
    table["tI"]="டீ"
    table["dee"]="டீ"
    table["dI"]="டீ"
    table["dii"]="டீ"
    table["tii"]="டீ"
    table["du"]="டு"
    table["tu"]="டு"
    table["too"]="டூ"
    table["tU"]="டூ"
    table["doo"]="டூ"
    table["dU"]="டூ"
    table["duu"]="டூ"
    table["tuu"]="டூ"
    table["de"]="டெ"
    table["te"]="டெ"
    table["tE"]="டே"
    table["dE"]="டே"
    table["dae"]="டே"
    table["tae"]="டே"
    table["dai"]="டை"
    table["tai"]="டை"
    table["do"]="டொ"
    table["to"]="டொ"
    table["tO"]="டோ"
    table["toe"]="டோ"
    table["dO"]="டோ"
    table["doa"]="டோ"
    table["doe"]="டோ"
    table["toa"]="டோ"
    table["tou"]="டௌ"
    table["tau"]="டௌ"
    table["dow"]="டௌ"
    table["dou"]="டௌ"
    table["dau"]="டௌ"
    table["tow"]="டௌ"
    table["d"]="ட்"
    table["T"]="ட்"
    table["t"]="ட்"
    table["nda"]="ண"
    table["Na"]="ண"
    table["NA"]="ணா"
    table["ndaa"]="ணா"
    table["Naa"]="ணா"
    table["ndi"]="ணி"
    table["Ni"]="ணி"
    table["Nee"]="ணீ"
    table["NI"]="ணீ"
    table["ndee"]="ணீ"
    table["ndI"]="ணீ"
    table["ndii"]="ணீ"
    table["Nii"]="ணீ"
    table["ndu"]="ணு"
    table["Nu"]="ணு"
    table["Noo"]="ணூ"
    table["NU"]="ணூ"
    table["ndoo"]="ணூ"
    table["ndU"]="ணூ"
    table["nduu"]="ணூ"
    table["Nuu"]="ணூ"
    table["nde"]="ணெ"
    table["Ne"]="ணெ"
    table["NE"]="ணே"
    table["ndE"]="ணே"
    table["ndae"]="ணே"
    table["Nae"]="ணே"
    table["ndai"]="ணை"
    table["Nai"]="ணை"
    table["ndo"]="ணொ"
    table["No"]="ணொ"
    table["NO"]="ணோ"
    table["Noe"]="ணோ"
    table["ndO"]="ணோ"
    table["ndoa"]="ணோ"
    table["ndoe"]="ணோ"
    table["Noa"]="ணோ"
    table["Nou"]="ணௌ"
    table["Nau"]="ணௌ"
    table["ndow"]="ணௌ"
    table["ndou"]="ணௌ"
    table["ndau"]="ணௌ"
    table["Now"]="ணௌ"
    table["nd"]="ண்"
    table["N"]="ண்"
    table["dha"]="த"
    table["tha"]="த"
    table["thA"]="தா"
    table["dhaa"]="தா"
    table["dhA"]="தா"
    table["thaa"]="தா"
    table["dhi"]="தி"
    table["thi"]="தி"
    table["thee"]="தீ"
    table["thI"]="தீ"
    table["dhee"]="தீ"
    table["dhI"]="தீ"
    table["dhii"]="தீ"
    table["thii"]="தீ"
    table["dhu"]="து"
    table["thu"]="து"
    table["thoo"]="தூ"
    table["thU"]="தூ"
    table["dhoo"]="தூ"
    table["dhU"]="தூ"
    table["dhuu"]="தூ"
    table["thuu"]="தூ"
    table["dhe"]="தெ"
    table["the"]="தெ"
    table["thE"]="தே"
    table["dhE"]="தே"
    table["dhae"]="தே"
    table["thae"]="தே"
    table["dhai"]="தை"
    table["thai"]="தை"
    table["dho"]="தொ"
    table["tho"]="தொ"
    table["thO"]="தோ"
    table["thoe"]="தோ"
    table["dhO"]="தோ"
    table["dhoa"]="தோ"
    table["dhoe"]="தோ"
    table["thoa"]="தோ"
    table["thou"]="தௌ"
    table["thau"]="தௌ"
    table["dhow"]="தௌ"
    table["dhou"]="தௌ"
    table["dhau"]="தௌ"
    table["thow"]="தௌ"
    table["dh"]="த்"
    table["th"]="த்"
    table["na"]="ந"
    table["ndha"]="ந"
    table["ntha"]="ந"
    table["nha"]="ந"
    table["nhA"]="நா"
    table["naa"]="நா"
    table["nA"]="நா"
    table["ndhA"]="நா"
    table["ndhaa"]="நா"
    table["nthaa"]="நா"
    table["nthA"]="நா"
    table["nhaa"]="நா"
    table["ni"]="நி"
    table["ndhi"]="நி"
    table["nthi"]="நி"
    table["nhi"]="நி"
    table["nhee"]="நீ"
    table["nhI"]="நீ"
    table["nee"]="நீ"
    table["nI"]="நீ"
    table["nii"]="நீ"
    table["ndhee"]="நீ"
    table["ndhI"]="நீ"
    table["ndhii"]="நீ"
    table["nthee"]="நீ"
    table["nthi"]="நீ"
    table["nthii"]="நீ"
    table["nhii"]="நீ"
    table["nu"]="நு"
    table["ndhu"]="நு"
    table["nthu"]="நு"
    table["'"]="நு"
    table["this"]="நு"
    table["event"]="நு"
    table["nhu"]="நு"
    table["nhoo"]="நூ"
    table["nhU"]="நூ"
    table["noo"]="நூ"
    table["nU"]="நூ"
    table["nuu"]="நூ"
    table["ndhoo"]="நூ"
    table["ndhU"]="நூ"
    table["ndhuu"]="நூ"
    table["nthoo"]="நூ"
    table["nthU"]="நூ"
    table["nthuu"]="நூ"
    table["nhuu"]="நூ"
    table["ne"]="நெ"
    table["ndhe"]="நெ"
    table["nthe"]="நெ"
    table["nhe"]="நெ"
    table["nhE"]="நே"
    table["nE"]="நே"
    table["nae"]="நே"
    table["ndhE"]="நே"
    table["ndhae"]="நே"
    table["nthE"]="நே"
    table["nthae"]="நே"
    table["nhae"]="நே"
    table["nai"]="நை"
    table["ndhai"]="நை"
    table["nthai"]="நை"
    table["nhai"]="நை"
    table["no"]="நொ"
    table["ndho"]="நொ"
    table["ntho"]="நொ"
    table["nho"]="நொ"
    table["nhO"]="நோ"
    table["nhoe"]="நோ"
    table["nO"]="நோ"
    table["noa"]="நோ"
    table["noe"]="நோ"
    table["ndhO"]="நோ"
    table["ndhoa"]="நோ"
    table["ndhoe"]="நோ"
    table["nthO"]="நோ"
    table["nthoa"]="நோ"
    table["nthoe"]="நோ"
    table["nhoa"]="நோ"
    table["nhou"]="நௌ"
    table["nhau"]="நௌ"
    table["now"]="நௌ"
    table["nou"]="நௌ"
    table["nau"]="நௌ"
    table["ndhow"]="நௌ"
    table["ndhou"]="நௌ"
    table["ndhau"]="நௌ"
    table["nthow"]="நௌ"
    table["nthou"]="நௌ"
    table["nthau"]="நௌ"
    table["nhow"]="நௌ"
    table["n"]="ந்"
    table["ndh"]="ந்"
    table["nth"]="ந்"
    table["nh"]="ந்"
    table["ba"]="ப"
    table["bha"]="ப"
    table["fa"]="ப"
    table["pha"]="ப"
    table["pa"]="ப"
    table["pA"]="பா"
    table["baa"]="பா"
    table["bA"]="பா"
    table["bhaa"]="பா"
    table["bhA"]="பா"
    table["fA"]="பா"
    table["faa"]="பா"
    table["phA"]="பா"
    table["phaa"]="பா"
    table["paa"]="பா"
    table["bi"]="பி"
    table["bhi"]="பி"
    table["fi"]="பி"
    table["phi"]="பி"
    table["pi"]="பி"
    table["pee"]="பீ"
    table["pI"]="பீ"
    table["bee"]="பீ"
    table["bI"]="பீ"
    table["bii"]="பீ"
    table["bhee"]="பீ"
    table["bhI"]="பீ"
    table["bhii"]="பீ"
    table["fee"]="பீ"
    table["fI"]="பீ"
    table["fii"]="பீ"
    table["phee"]="பீ"
    table["phI"]="பீ"
    table["phii"]="பீ"
    table["pii"]="பீ"
    table["bu"]="பு"
    table["bhu"]="பு"
    table["fu"]="பு"
    table["phu"]="பு"
    table["pu"]="பு"
    table["poo"]="பூ"
    table["pU"]="பூ"
    table["boo"]="பூ"
    table["bU"]="பூ"
    table["buu"]="பூ"
    table["bhoo"]="பூ"
    table["bhU"]="பூ"
    table["bhuu"]="பூ"
    table["foo"]="பூ"
    table["fU"]="பூ"
    table["fuu"]="பூ"
    table["phoo"]="பூ"
    table["phU"]="பூ"
    table["phuu"]="பூ"
    table["puu"]="பூ"
    table["be"]="பெ"
    table["bhe"]="பெ"
    table["fe"]="பெ"
    table["phe"]="பெ"
    table["pe"]="பெ"
    table["pE"]="பே"
    table["bE"]="பே"
    table["bae"]="பே"
    table["bhE"]="பே"
    table["bhae"]="பே"
    table["fE"]="பே"
    table["fae"]="பே"
    table["phE"]="பே"
    table["phae"]="பே"
    table["pae"]="பே"
    table["bai"]="பை"
    table["bhai"]="பை"
    table["fai"]="பை"
    table["phai"]="பை"
    table["pai"]="பை"
    table["bo"]="பொ"
    table["bho"]="பொ"
    table["fo"]="பொ"
    table["pho"]="பொ"
    table["po"]="பொ"
    table["pO"]="போ"
    table["poe"]="போ"
    table["bO"]="போ"
    table["boa"]="போ"
    table["boe"]="போ"
    table["bhO"]="போ"
    table["bhoa"]="போ"
    table["bhoe"]="போ"
    table["fO"]="போ"
    table["foa"]="போ"
    table["foe"]="போ"
    table["phO"]="போ"
    table["phoa"]="போ"
    table["phoe"]="போ"
    table["poa"]="போ"
    table["pou"]="பௌ"
    table["pau"]="பௌ"
    table["bow"]="பௌ"
    table["bou"]="பௌ"
    table["bau"]="பௌ"
    table["bhow"]="பௌ"
    table["bhou"]="பௌ"
    table["bhau"]="பௌ"
    table["fow"]="பௌ"
    table["fou"]="பௌ"
    table["fau"]="பௌ"
    table["phow"]="பௌ"
    table["phou"]="பௌ"
    table["phau"]="பௌ"
    table["pow"]="பௌ"
    table["b"]="ப்"
    table["bh"]="ப்"
    table["f"]="ப்"
    table["ph"]="ப்"
    table["p"]="ப்"
    table["ma"]="ம"
    table["mA"]="மா"
    table["maa"]="மா"
    table["mi"]="மி"
    table["mee"]="மீ"
    table["mI"]="மீ"
    table["mii"]="மீ"
    table["mu"]="மு"
    table["moo"]="மூ"
    table["mU"]="மூ"
    table["muu"]="மூ"
    table["me"]="மெ"
    table["mE"]="மே"
    table["mae"]="மே"
    table["mai"]="மை"
    table["mo"]="மொ"
    table["mO"]="மோ"
    table["moe"]="மோ"
    table["moa"]="மோ"
    table["mou"]="மௌ"
    table["mau"]="மௌ"
    table["mow"]="மௌ"
    table["m"]="ம்"
    table["ya"]="ய"
    table["yA"]="யா"
    table["yaa"]="யா"
    table["yi"]="யி"
    table["yee"]="யீ"
    table["yI"]="யீ"
    table["yii"]="யீ"
    table["yu"]="யு"
    table["yoo"]="யூ"
    table["yU"]="யூ"
    table["yuu"]="யூ"
    table["ye"]="யெ"
    table["yE"]="யே"
    table["yae"]="யே"
    table["yai"]="யை"
    table["yo"]="யொ"
    table["yO"]="யோ"
    table["yoe"]="யோ"
    table["yoa"]="யோ"
    table["you"]="யௌ"
    table["yau"]="யௌ"
    table["yow"]="யௌ"
    table["y"]="ய்"
    table["ra"]="ர"
    table["rA"]="ரா"
    table["raa"]="ரா"
    table["ri"]="ரி"
    table["ree"]="ரீ"
    table["rI"]="ரீ"
    table["rii"]="ரீ"
    table["ru"]="ரு"
    table["roo"]="ரூ"
    table["rU"]="ரூ"
    table["ruu"]="ரூ"
    table["re"]="ரெ"
    table["rE"]="ரே"
    table["rae"]="ரே"
    table["rai"]="ரை"
    table["ro"]="ரொ"
    table["rO"]="ரோ"
    table["roe"]="ரோ"
    table["roa"]="ரோ"
    table["rou"]="ரௌ"
    table["rau"]="ரௌ"
    table["row"]="ரௌ"
    table["r"]="ர்"
    table["la"]="ல"
    table["lA"]="லா"
    table["laa"]="லா"
    table["li"]="லி"
    table["lee"]="லீ"
    table["lI"]="லீ"
    table["lii"]="லீ"
    table["lu"]="லு"
    table["loo"]="லூ"
    table["lU"]="லூ"
    table["luu"]="லூ"
    table["le"]="லெ"
    table["lE"]="லே"
    table["lae"]="லே"
    table["lai"]="லை"
    table["lo"]="லொ"
    table["lO"]="லோ"
    table["loe"]="லோ"
    table["loa"]="லோ"
    table["lou"]="லௌ"
    table["lau"]="லௌ"
    table["low"]="லௌ"
    table["l"]="ல்"
    table["wa"]="வ"
    table["va"]="வ"
    table["vA"]="வா"
    table["waa"]="வா"
    table["wA"]="வா"
    table["vaa"]="வா"
    table["wi"]="வி"
    table["vi"]="வி"
    table["vee"]="வீ"
    table["vI"]="வீ"
    table["wee"]="வீ"
    table["wI"]="வீ"
    table["wii"]="வீ"
    table["vii"]="வீ"
    table["wu"]="வு"
    table["vu"]="வு"
    table["voo"]="வூ"
    table["vU"]="வூ"
    table["woo"]="வூ"
    table["wU"]="வூ"
    table["wuu"]="வூ"
    table["vuu"]="வூ"
    table["we"]="வெ"
    table["ve"]="வெ"
    table["vE"]="வே"
    table["wE"]="வே"
    table["wae"]="வே"
    table["vae"]="வே"
    table["wai"]="வை"
    table["vai"]="வை"
    table["wo"]="வொ"
    table["vo"]="வொ"
    table["vO"]="வோ"
    table["voe"]="வோ"
    table["wO"]="வோ"
    table["woa"]="வோ"
    table["woe"]="வோ"
    table["voa"]="வோ"
    table["vou"]="வௌ"
    table["vau"]="வௌ"
    table["wow"]="வௌ"
    table["wou"]="வௌ"
    table["wau"]="வௌ"
    table["vow"]="வௌ"
    table["w"]="வ்"
    table["v"]="வ்"
    table["zha"]="ழ"
    table["za"]="ழ"
    table["zA"]="ழா"
    table["zhaa"]="ழா"
    table["zhA"]="ழா"
    table["zaa"]="ழா"
    table["zhi"]="ழி"
    table["zi"]="ழி"
    table["zee"]="ழீ"
    table["zI"]="ழீ"
    table["zhee"]="ழீ"
    table["zhI"]="ழீ"
    table["zhii"]="ழீ"
    table["zii"]="ழீ"
    table["zhu"]="ழு"
    table["zu"]="ழு"
    table["zoo"]="ழூ"
    table["zU"]="ழூ"
    table["zhoo"]="ழூ"
    table["zhU"]="ழூ"
    table["zhuu"]="ழூ"
    table["zuu"]="ழூ"
    table["zhe"]="ழெ"
    table["ze"]="ழெ"
    table["zE"]="ழே"
    table["zhE"]="ழே"
    table["zhae"]="ழே"
    table["zae"]="ழே"
    table["zhai"]="ழை"
    table["zai"]="ழை"
    table["zho"]="ழொ"
    table["zo"]="ழொ"
    table["zO"]="ழோ"
    table["zoe"]="ழோ"
    table["zhO"]="ழோ"
    table["zhoa"]="ழோ"
    table["zhoe"]="ழோ"
    table["zoa"]="ழோ"
    table["zou"]="ழௌ"
    table["zau"]="ழௌ"
    table["zhow"]="ழௌ"
    table["zhou"]="ழௌ"
    table["zhau"]="ழௌ"
    table["zow"]="ழௌ"
    table["zh"]="ழ்"
    table["z"]="ழ்"
    table["La"]="ள"
    table["LA"]="ளா"
    table["Laa"]="ளா"
    table["Li"]="ளி"
    table["Lee"]="ளீ"
    table["LI"]="ளீ"
    table["Lii"]="ளீ"
    table["Lu"]="ளு"
    table["Loo"]="ளூ"
    table["LU"]="ளூ"
    table["Luu"]="ளூ"
    table["Le"]="ளெ"
    table["LE"]="ளே"
    table["Lae"]="ளே"
    table["Lai"]="ளை"
    table["Lo"]="ளொ"
    table["LO"]="ளோ"
    table["Loe"]="ளோ"
    table["Loa"]="ளோ"
    table["Lou"]="ளௌ"
    table["Lau"]="ளௌ"
    table["Low"]="ளௌ"
    table["L"]="ள்"
    table["tra"]="ற"
    table["dra"]="ற"
    table["Ra"]="ற"
    table["RA"]="றா"
    table["traa"]="றா"
    table["trA"]="றா"
    table["draa"]="றா"
    table["drA"]="றா"
    table["Raa"]="றா"
    table["tri"]="றி"
    table["dri"]="றி"
    table["Ri"]="றி"
    table["Ree"]="றீ"
    table["RI"]="றீ"
    table["tree"]="றீ"
    table["trI"]="றீ"
    table["trii"]="றீ"
    table["dree"]="றீ"
    table["drI"]="றீ"
    table["drii"]="றீ"
    table["Rii"]="றீ"
    table["tru"]="று"
    table["dru"]="று"
    table["Ru"]="று"
    table["Roo"]="றூ"
    table["RU"]="றூ"
    table["troo"]="றூ"
    table["trU"]="றூ"
    table["truu"]="றூ"
    table["droo"]="றூ"
    table["drU"]="றூ"
    table["druu"]="றூ"
    table["Ruu"]="றூ"
    table["tre"]="றெ"
    table["dre"]="றெ"
    table["Re"]="றெ"
    table["RE"]="றே"
    table["trE"]="றே"
    table["trae"]="றே"
    table["drE"]="றே"
    table["drae"]="றே"
    table["Rae"]="றே"
    table["trai"]="றை"
    table["drai"]="றை"
    table["Rai"]="றை"
    table["tro"]="றொ"
    table["dro"]="றொ"
    table["Ro"]="றொ"
    table["RO"]="றோ"
    table["Roe"]="றோ"
    table["trO"]="றோ"
    table["troa"]="றோ"
    table["troe"]="றோ"
    table["drO"]="றோ"
    table["droa"]="றோ"
    table["droe"]="றோ"
    table["Roa"]="றோ"
    table["Rou"]="றௌ"
    table["Rau"]="றௌ"
    table["trow"]="றௌ"
    table["trou"]="றௌ"
    table["trau"]="றௌ"
    table["drow"]="றௌ"
    table["drou"]="றௌ"
    table["drau"]="றௌ"
    table["Row"]="றௌ"
    table["tr"]="ற்"
    table["dr"]="ற்"
    table["R"]="ற்"
    table["nHa"]="ன"
    table["na"]="ன"
    table["nA"]="னா"
    table["nHaa"]="னா"
    table["nHA"]="னா"
    table["naa"]="னா"
    table["nHi"]="னி"
    table["ni"]="னி"
    table["nee"]="னீ"
    table["nI"]="னீ"
    table["nHee"]="னீ"
    table["nHI"]="னீ"
    table["nHii"]="னீ"
    table["nii"]="னீ"
    table["nHu"]="னு"
    table["nu"]="னு"
    table["noo"]="னூ"
    table["nU"]="னூ"
    table["nHoo"]="னூ"
    table["nHU"]="னூ"
    table["nHuu"]="னூ"
    table["nuu"]="னூ"
    table["nHe"]="னெ"
    table["ne"]="னெ"
    table["nE"]="னே"
    table["nHE"]="னே"
    table["nHae"]="னே"
    table["nae"]="னே"
    table["nHai"]="னை"
    table["nai"]="னை"
    table["nHo"]="னொ"
    table["no"]="னொ"
    table["nO"]="னோ"
    table["noe"]="னோ"
    table["nHO"]="னோ"
    table["nHoa"]="னோ"
    table["nHoe"]="னோ"
    table["noa"]="னோ"
    table["nou"]="னௌ"
    table["nau"]="னௌ"
    table["nHow"]="னௌ"
    table["nHou"]="னௌ"
    table["nHau"]="னௌ"
    table["now"]="னௌ"
    table["n"]="ன்"
    table["nH"]="ன்"
    table["La"]="ள"
    table["Laa"]="ளா"
    table["LA"]="ளா"
    table["Li"]="ளி"
    table["Lee"]="ளீ"
    table["LI"]="ளீ"
    table["Lii"]="ளீ"
    table["Lu"]="ளு"
    table["Luu"]="ளூ"
    table["Loo"]="ளூ"
    table["LU"]="ளூ"
    table["Le"]="ளெ"
    table["LE"]="ளே"
    table["Lae"]="ளே"
    table["Lai"]="ளை"
    table["Lo"]="ளொ"
    table["Loa"]="ளோ"
    table["LO"]="ளோ"
    table["Loe"]="ளோ"
    table["Low"]="ளௌ"
    table["Lou"]="ளௌ"
    table["Lau"]="ளௌ"
    table["ja"]="ஜ"
    table["jaa"]="ஜா"
    table["ji"]="ஜி"
    table["jii"]="ஜீ"
    table["ju"]="ஜு"
    table["juu"]="ஜூ"
    table["je"]="ஜெ"
    table["jae"]="ஜே"
    table["jai"]="ஜை"
    table["jo"]="ஜொ"
    table["joa"]="ஜோ"
    table["jow"]="ஜௌ"
    table["j"]="ஜ்"
    table["sha"]="ஷ"
    table["shaa"]="ஷா"
    table["shi"]="ஷி"
    table["shii"]="ஷீ"
    table["shu"]="ஷு"
    table["shuu"]="ஷூ"
    table["she"]="ஷெ"
    table["shae"]="ஷே"
    table["shai"]="ஷை"
    table["sho"]="ஷொ"
    table["shoa"]="ஷோ"
    table["show"]="ஷௌ"
    table["sh"]="ஷ்"
    table["Sa"]="ஸ"
    table["Saa"]="ஸா"
    table["Si"]="ஸி"
    table["Sii"]="ஸீ"
    table["Su"]="ஸு"
    table["Suu"]="ஸூ"
    table["Se"]="ஸெ"
    table["Sae"]="ஸே"
    table["Sai"]="ஸை"
    table["So"]="ஸொ"
    table["Soa"]="ஸோ"
    table["Sow"]="ஸௌ"
    table["S"]="ஸ்"
    table["ha"]="ஹ"
    table["haa"]="ஹா"
    table["hi"]="ஹி"
    table["hii"]="ஹீ"
    table["hu"]="ஹு"
    table["huu"]="ஹூ"
    table["he"]="ஹெ"
    table["hae"]="ஹே"
    table["hai"]="ஹை"
    table["ho"]="ஹொ"
    table["hoa"]="ஹோ"
    table["how"]="ஹௌ"
    table["h"]="ஹ்"
    table["ksha"]="க்ஷ"
    table["kshaa"]="க்ஷா"
    table["kshi"]="க்ஷி"
    table["kshii"]="க்ஷீ"
    table["kshu"]="க்ஷு"
    table["kshuu"]="க்ஷூ"
    table["kshe"]="க்ஷெ"
    table["kshae"]="க்ஷே"
    table["kshai"]="க்ஷை"
    table["ksho"]="க்ஷொ"
    table["kshoa"]="க்ஷோ"
    table["kshow"]="க்ஷௌ"
    table["ksh"]="க்ஷ்"
    table["sri"]="ஸ்ரீ"
    table["sree"]="ஸ்ரீ"
    table["shree"]="ஸ்ரீ"
    table["shri"]="ஸ்ரீ"
    table["fa"]="ஃப"
    table["faa"]="ஃபா"
    table["fi"]="ஃபி"
    table["fii"]="ஃபீ"
    table["fu"]="ஃபு"
    table["fuu"]="ஃபூ"
    table["fe"]="ஃபெ"
    table["fae"]="ஃபே"
    table["fai"]="ஃபை"
    table["fo"]="ஃபொ"
    table["foa"]="ஃபோ"
    table["fow"]="ஃபௌ"
    table["f"]="ஃப்"
    table["Za"]="ஃஜ"
    table["Zaa"]="ஃஜா"
    table["Zi"]="ஃஜி"
    table["Zii"]="ஃஜீ"
    table["Zu"]="ஃஜு"
    table["Zuu"]="ஃஜூ"
    table["Ze"]="ஃஜெ"
    table["Zae"]="ஃஜே"
    table["Zai"]="ஃஜை"
    table["Zo"]="ஃஜொ"
    table["Zoa"]="ஃஜோ"
    table["Zow"]="ஃஜௌ"
    table["Z"]="ஃஜ்"
    table["xa"]="ஃஸ"
    table["xaa"]="ஃஸா"
    table["xi"]="ஃஸி"
    table["xu"]="ஃஸு"
    table["xuu"]="ஃஸூ"
    table["xe"]="ஃஸெ"
    table["xae"]="ஃஸே"
    table["xai"]="ஃஸை"
    table["xo"]="ஃஸொ"
    table["xoa"]="ஃஸோ"
    table["xow"]="ஃஸௌ"
    table["x"]="ஃஸ்"
    table["1"]="௧"
    table["2"]="௨"
    table["3"]="௩"
    table["4"]="௪"
    table["5"]="௫"
    table["6"]="௬"
    table["7"]="௭"
    table["8"]="௮"
    table["9"]="௯"
    table["10"]="௰"
    table["1000"]="௲"
