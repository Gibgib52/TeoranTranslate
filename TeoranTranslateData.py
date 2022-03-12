"""
Contains translation tables and other data.
"""

# dictionary for translation
translateDict = {
    # lowercase letters and space
    "a": "<:Teoran_a:949162522148216882> ",
    "b": "<:Teoran_b:949162522198556692> ",
    "c": "<:Teoran_c:949162522336956436> ",
    "d": "<:Teoran_d:949162521829441547> ",
    "e": "<:Teoran_e:949162522160791552> ",
    "f": "<:Teoran_f:949162522173374464> ",
    "g": "<:Teoran_g:949162522173386752> ",
    "h": "<:Teoran_h:949162522223730688> ",
    "i": "<:Teoran_i:949162522261454898> ",
    "j": "<:Teoran_j:949162522538303508> ",
    "k": "<:Teoran_k:949162522269851688> ",
    "l": "<:Teoran_l:949162522135629854> ",
    "m": "<:Teoran_m:949162522282430524> ",
    "n": "<:Teoran_n:949162522165002320> ",
    "o": "<:Teoran_o:949162522169184326> ",
    "p": "<:Teoran_p:949162522169212968> ",
    "q": "<:Teoran_q:949162522328576000> ",
    "r": "<:Teoran_r:949162522211127307> ",
    "s": "<:Teoran_s:949162522303426560> ",
    "t": "<:Teoran_t:949162521871413279> ",
    "u": "<:Teoran_u:949162522223722527> ",
    "v": "<:Teoran_v:949162522353762365> ",
    "w": "<:Teoran_w:949162522215321660> ",
    "x": "<:Teoran_x:949162521854607381> ",
    "y": "<:Teoran_y:949162522169192488> ",
    "z": "<:Teoran_z:949162521955299349> ",
    " ": "<:Teoran_space:949164879405780997> ",
    # uppercase letters
    "A": "<:Teoran_ac:951687057435156500> ",
    "B": "<:Teoran_b:949162522198556692> ",
    "C": "<:Teoran_cc:951687057359663155> ",
    "D": "<:Teoran_dc:951687057573548102> ",
    "E": "<:Teoran_ec:951687057468719124> ",
    "F": "<:Teoran_fc:951687057422557194> ",
    "G": "<:Teoran_gc:951687057074434069> ",
    "H": "<:Teoran_h:949162522223730688> ",
    "I": "<:Teoran_i:949162522261454898> ",
    "j": "<:Teoran_jc:951687057409970206> ",
    "K": "<:Teoran_k:949162522269851688> ",
    "L": "<:Teoran_lc:951687057414172712> ",
    "M": "<:Teoran_mc:951687057292525610> ",
    "N": "<:Teoran_nc:951687057640661042> ",
    "O": "<:Teoran_o:949162522169184326> ",
    "P": "<:Teoran_pc:951687057510649876> ",
    "Q": "<:Teoran_qc:951687057409970266> ",
    "R": "<:Teoran_rc:951687057393197177> ",
    "S": "<:Teoran_s:949162522303426560> ",
    "T": "<:Teoran_tc:951687057384824912> ",
    "U": "<:Teoran_uc:951687057485480006> ",
    "V": "<:Teoran_vc:951687057565184040> ",
    "W": "<:Teoran_wc:951687057414189066> ",
    "X": "<:Teoran_x:949162521854607381> ",
    "Y": "<:Teoran_yc:951687057472913418> ",
    "Z": "<:Teoran_z:949162521955299349> ",
    # numbers
    "1": "<:Teoran_1:949476249309425675> ",
    "2": "<:Teoran_2:949476249208774736> ",
    "3": "<:Teoran_3:949476248860643349> ",
    "4": "<:Teoran_4:949476249225531392> ",
    "5": "<:Teoran_5:949476249133256724> ",
    "6": "<:Teoran_6:949476249275879454> ",
    "7": "<:Teoran_7:949476249183612928> ",
    "8": "<:Teoran_8:949476248898379827> ",
    "9": "<:Teoran_9:949476248957095977> ",
    "0": "<:Teoran_0:949476249301024818> ",
    # punctuation and symbols
    "?": "<:Teoran_question:949476249070366761> ",
    ";": "<:Teoran_semicolon:949476249082937404> ",
    ":": "<:Teoran_colon:949476249095528480> ",
    "#": "<:Teoran_hash:949476248680284191> ",
    "!": "<:Teoran_exclamation:949476248831291423> ",
    ".": "<:Teoran_period:949476249166811216> ",
    "&": "<:Teoran_and:951664227557466194>",
    "@": "<:Teoran_at:951664227838484580>",
    "(": "<:Teoran_roundo:951664227586801765> ",
    ")": "<:Teoran_roundc:951664227855237160> ",
    "[": "<:Teoran_squareo:951664228018823208> ",
    "]": "<:Teoran_squarec:951664227951738910> ",
    "*": "<:Teoran_asterisk:951664227888795688> ",
    "=": "<:Teoran_equal:951664227574251602> ",
    "#": "<:Teoran_hash:951664227838468176> ",
    "{": "<:Teoran_curlyo:951664227863633970> ",
    "}": "<:Teoran_curlyc:951664227859443742> ",
    "+": "<:Teoran_plus:951664227892985856> ",
    "-": "<:Teoran_minus:951664227884609536> ",
    "$": "<:Teoran_dollar:951686257560387584> ",
    '"': "<:Teoran_doublequote:951686257828827136> ",
    "'": "<:Teoran_quote:951686257447161957> ",
    ">": "<:Teoran_greaterthan:951686257535234058> ",
    "<": "<:Teoran_lessthan:951686257619124264> ",
    "_": "<:Teoran_underscore:951686257187119185> ",
    "%": "<:Teoran_percent:951686257380057110> ",
    "^": "<:Teoran_pow:951686257275195424> "
}

# help message for the {prefix}help command
helpmsg = """<:Teoran_c:949162522336956436> Commands:
        Dont forget quotes!
        - `{p}help` : Echoes help
        - `{p}echo "string"` : Echoes a string
        - `{p}ping` : Echoes latency
        - `{p}translate "string"` : Translates a string into Teoran
        - `{p}translateRaw "string"` : Translates a string into Teoran emoji ids (for copying, if you have nitro)
        Examples
        Correct: `$translate "Geo Ami"` translates "Geo Ami"
        Incorrect: `$translate "Marlow" "Deva"` only translates "Marlow"

<:Teoran_g:949162522173386752> Info:
    - Supports letters, symbols and 0-9
    - Does not support fancy quotes or apostrophes.
    - Contact me if you find a bug. `Gibgib52#6473`. I'm usually available from 4pm - 11pm CST

<:Teoran_g:949162522173386752> <:Teoran_i:949162522261454898> <:Teoran_tc:951687057384824912> : `https://github.com/Gibgib52/TeoranTranslate`
"""