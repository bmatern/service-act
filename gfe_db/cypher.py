'''
Created on Feb 8, 2017

@author: mhalagan
'''


def sequence_search(locus, sequence):
    seq_query = "MATCH (hla:IMGT)-[:HAS_GFE]-(gfe:GFE)-[:HAS_FEATURE]-(seq:SEQUENCE)"
    seq_query1 = " WHERE seq.sequence = \"" + sequence + "\""
    seq_query2 = " AND hla.locus = \"" + locus + "\""
    seq_query3 = " RETURN hla.name AS HLA, gfe.name AS GFE"
    query = seq_query + seq_query1 + seq_query2 + seq_query3
    return(query)


def gfe_search(gfe):
    seq_query = "MATCH (hla:IMGT)-[:HAS_GFE]-(gfe:GFE)"
    seq_query1 = " WHERE gfe.name = \"" + gfe + "\""
    seq_query2 = " RETURN hla.name AS HLA, gfe.name AS GFE"
    query = seq_query + seq_query1 + seq_query2
    return(query)


def similar_gfe(gfe, exon2, exon3):

    [locus, feature_accessions] = gfe.split("w")
    typing_match = "MATCH (gfe1:GFE)-[f1:HAS_FEATURE]->(feat1:FEATURE)," \
        + " (gfe2:GFE)-[f2:HAS_FEATURE]->(feat1:FEATURE)," \
        + " (gfe1:GFE)-[f3:HAS_FEATURE]->(feat2:FEATURE)," \
        + " (gfe2:GFE)-[f4:HAS_FEATURE]->(feat2:FEATURE)," \
        + " (gfe1:GFE)-[f5:HAS_FEATURE]->(feat3:FEATURE)," \
        + " (gfe2:GFE)-[f6:HAS_FEATURE]->(feat3:FEATURE)" \
        + " WHERE gfe1.locus = \"" + locus + "\"" \
        + " AND gfe2.locus = gfe1.locus" \
        + " AND f1.accession = f2.accession" \
        + " AND f3.accession = f4.accession" \
        + " AND f1.accession = \"" + exon2 + "\"" \
        + " AND f3.accession = \"" + exon3 + "\"" \
        + " AND feat1.name = \"EXON\"" \
        + " AND feat2.name = \"EXON\"" \
        + " AND feat1.rank = \"2\"" \
        + " AND feat2.rank = \"3\"" \
        + " AND f5.accession = f6.accession" \
        + " WITH gfe1.name AS GFE1, gfe2.name AS GFE2,collect(DISTINCT feat3.name) AS Names," \
        + " collect(DISTINCT {accesion:f6.accession,rank:feat3.rank, name: feat3.name}) AS Accession " \
        + " return GFE1,GFE2,Names,Accession,size(Accession) AS Count" \
        + " ORDER BY Count DESC"

    return(typing_match)


def hla_Ggroups(hla):
    matchq = "MATCH (G:G_GROUP)-[:IN_GROUP]-(hla:IMGT) WHERE hla.name = \"" + hla + "\""
    returnq = " RETURN DISTINCT G.name as G_GROUP"
    cyper_query = matchq + returnq
    return(cyper_query)


def gfe_Ggroups(gfe):
    matchq = "MATCH (G:G_GROUP)-[:IN_GROUP]-(hla:IMGT)-[:HAS_GFE]-(gfe1:GFE) WHERE gfe1.name = \"" + gfe + "\""
    returnq = " RETURN DISTINCT G.name as G_GROUP"
    cyper_query = matchq + returnq
    return(cyper_query)


def gfe_hla(gfe):
    matchq = "MATCH (hla:IMGT)-[:HAS_GFE]-(gfe1:GFE) WHERE gfe1.name = \"" + gfe + "\""
    withq = " WITH collect(DISTINCT hla.name) as HLA"
    returnq = " RETURN HLA"
    cyper_query = matchq + withq + returnq
    return(cyper_query)


def groups(locus, exon2, exon3):

    match = "MATCH (hla:IMGT)-[:HAS_GFE]-(gfe1:GFE)-[f1:HAS_FEATURE]->(feat1:FEATURE)"
    match2 = ",(gfe1:GFE)-[f2:HAS_FEATURE]->(feat2:FEATURE) "
    where = " WHERE feat1.rank = '2' AND feat2.name = \"EXON\" AND feat1.name = \"EXON\" AND hla.locus = \"" + locus + "\""
    where2 = " AND feat2.rank = '3' AND f2.accession = \"" + exon3 + "\" AND f1.accession = \"" + exon2 + "\""
    withst = " WITH collect(DISTINCT hla.name) as HLA,collect(DISTINCT gfe1.name) as GFE"
    returnc = " RETURN HLA,GFE"
    cypher = match + match2 + where + where2 + withst + returnc
    return(cypher)


def hla_gfe(hla):
    seq_query = "MATCH (hla:IMGT)-[:HAS_GFE]-(gfe:GFE)"
    seq_query1 = " WHERE hla.name = \"" + hla + "\""
    seq_query2 = " RETURN DISTINCT gfe.name AS GFE"
    query = seq_query + seq_query1 + seq_query2
    return(query)


def hla_ars(group, hla):
    matchq = "MATCH (group:" + group + ")-[:IN_GROUP]-(hla:IMGT) WHERE hla.name = \"" + hla + "\""
    returnq = " RETURN DISTINCT group.name as ARS"
    cyper_query = matchq + returnq
    return(cyper_query)


def get_sequence(seqtype, allele):
    seq_query = "MATCH (allele:" + seqtype + ")-[:HAS_FEATURE]-(seq:SEQUENCE)"
    seq_query1 = " WHERE allele.name = \"" + allele + "\""
    seq_query2 = " RETURN DISTINCT seq.sequence AS SEQ"
    query = seq_query + seq_query1 + seq_query2
    return(query)


