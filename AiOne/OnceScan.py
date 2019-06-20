
def OnceScan(x,y,z,t,s,table,player,column):
    aiX,aiY,aiZ,aiT,aiS,aiTable,aiPlayer,aiColumn=x,y,z,t,s,table,player,column
    score=[]
    score.append(scanHplus(aiX,aiY,aiZ,aiT,aiS,aiTable,aiPlayer,aiColumn))
    score.append(scanHminus(aiX,aiY,aiZ,aiT,aiS,aiTable,aiPlayer,aiColumn))
    score.append(scanVplus(aiX,aiY,aiZ,aiT,aiS,aiTable,aiPlayer,aiColumn))
    score.append(scanVminus(aiX,aiY,aiZ,aiT,aiS,aiTable,aiPlayer,aiColumn))
    score.append(scanLDplus(aiX,aiY,aiZ,aiT,aiS,aiTable,aiPlayer,aiColumn))
    score.append(scanLDminus(aiX,aiY,aiZ,aiT,aiS,aiTable,aiPlayer,aiColumn))
    score.append(scanLTplus(aiX,aiY,aiZ,aiT,aiS,aiTable,aiPlayer,aiColumn))
    score.append(scanLTminus(aiX,aiY,aiZ,aiT,aiS,aiTable,aiPlayer,aiColumn))
    return max(score)

def scanHplus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanHplus(sX+1,sY,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanHplus(sX+1,sY,sZ+1,t,0,sTable,sPlayer,column)
    else:
        return sS
def scanHminus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanHminus(sX-1,sY,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanHminus(sX-1,sY,sZ+1,t,0,sTable,sPlayer,column)
    else:
        return sS
def scanVplus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanVplus(sX,sY+1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanVplus(sX,sY+1,sZ+1,t,0,sTable,sPlayer,column)
    else:
        return sS
def scanVminus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanVminus(sX,sY-1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanVminus(sX,sY-1,sZ+1,t,0,sTable,sPlayer,column)
    else:
        return sS
def scanLDplus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanLDplus(sX+1,sY+1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanLDplus(sX+1,sY+1,sZ+1,t,0,sTable,sPlayer,column)
    else:
        return sS
def scanLDminus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanLDminus(sX-1,sY-1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanLDminus(sX-1,sY-1,sZ+1,t,0,sTable,sPlayer,column)
    else:
        return sS
def scanLTplus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanLTplus(sX+1,sY-1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanLTplus(sX+1,sY-1,sZ+1,t,0,sTable,sPlayer,column)
    else:
        return sS
def scanLTminus(x,y,z,t,s,table,player,column):
    sTable,sPlayer,sX,sY,sZ,sS=table,player,x,y,z,s
    if sX>=0 and sX<column and sY>=0 and sY<column and sZ<=t:
        if sTable.checkbyzero(sX,sY)==player:
            return scanLTminus(sX-1,sY+1,sZ+1,t,sS+1,sTable,sPlayer,column)
        else:
            return scanLTminus(sX-1,sY+1,sZ+1,t,0,sTable,sPlayer,column)
    else:
        return sS