def get_userid(db, login):
    cur = db.cursor()
    userid = cur.execute("SELECT id from users WHERE login = ?", (login,)).fetchall()
    return userid[0][0]

def get_dict_clothes(db, userid: int):
    cur = db.cursor()
    dict_clothes = {}
    clothes = cur.execute("SELECT id, weather, type, mediumcolor, name from clothes WHERE userid = ?",
                          (userid,)).fetchall()
    for garment in clothes:
        dict_clothes[garment[1]] = dict_clothes.get(garment[1], {})
        dict_clothes[garment[1]][garment[2]] = dict_clothes[garment[1]].get(garment[2], []) + [(garment[0],
                                                                                               garment[3],
                                                                                               garment[4])]
    return dict_clothes
