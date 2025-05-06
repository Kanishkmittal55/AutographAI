import csv

# Define the header for the columns in your Excel/CSV.
header = [
    "Node_in_graph",
    "matching_dataset_chemical",
    "extra_strings_present_in_Node",
    "some_part_of_string_missing_in_node",
    "True_Positive_Chemical_or_False",
    "False_Positive_Chemical_Mention",
    "Why?"
]

rows = [
  [
    "EP2266989B1",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Bibliographic node patent # not recognized as a correct chemical mention"
  ],
  [
    "4d433d7261b400271c8a77682af61cd3641cb868d5459958a7fae1aae16f3f82#5000#0#SEM",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Internal SEM or metadata node referencing list of compounds not an actual chemical name"
  ],
  [
    "166193128e5ab7d9074da51203118ca70d5441748e155847cb7230f30e1638f7#5000#0#SEM",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Another metadata or SEM node"
  ],
  [
    "4d433d7261b400271c8a77682af61cd3641cb868d5459958a7fae1aae16f3f82#5000#2#SEM",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Same reasoning internal SEM node"
  ],
  [
    "4d433d7261b400271c8a77682af61cd3641cb868d5459958a7fae1aae16f3f82#5000#1#SEM",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Another internal SEM node"
  ],
  [
    "4d433d7261b400271c8a77682af61cd3641cb868d5459958a7fae1aae16f3f82#5000#3#SEM",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Another internal SEM node"
  ],
  [
    "Claim 1",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Claim 1 text node not recognized as a T# chemical"
  ],
  [
    "Chemical Compounds",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Heading or topic label not a T# compound"
  ],
  [
    "(3,5-dibromo-4-hydroxy-phenyl)-(2,3-dihydro-pyrido[2,3-b][1,4]oxazin-1-yl)-methanone",
    "T28",
    "No",
    "No",
    "True Positive",
    "No",
    "Exact or near-exact match to T28"
  ],
  [
    "Hydrobromic Acid Salt",
    "None",
    "Yes extra phrase Acid Salt vs any T#",
    "N/A",
    "False",
    "Yes",
    "Partial salt mention not a T# compound name"
  ],
  [
    "ep2266989b1",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Another patent or bibliographic reference not a chemical"
  ],
  [
    "european patent ep2266989b1",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Bibliographic text about the patent"
  ],
  [
    "claim 1",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "claim 1 repeated not a chemical"
  ],
  [
    "claim 1 of ep2266989b1",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Longer mention of claim not a chemical"
  ],
  [
    "claim 1 of european patent ep2266989b1",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Another claim reference text"
  ],
  [
    "chemical compounds",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Lowercase heading for chemical compounds not T#"
  ],
  [
    "chemical compounds list",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Another heading list not T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "None",
    "Yes spaced-out text",
    "Possibly",
    "False",
    "Yes",
    "Partial spaced version does not exactly match any T#"
  ],
  [
    "hydrobromic acid salt",
    "None",
    "Yes",
    "N/A",
    "False",
    "Yes",
    "Lowercase variant of hydrobromic acid salt still no T# match"
  ],
  [
    "carbon",
    "None",
    "N/A",
    "N/A",
    "False",
    "Yes",
    "Single element recognized as chemical no T# match false positive"
  ],
  [
    "nitrogen",
    "None",
    "N/A",
    "N/A",
    "False",
    "Yes",
    "Single element recognized not T# false positive"
  ],
  [
    "hydrogen",
    "None",
    "N/A",
    "N/A",
    "False",
    "Yes",
    "Same reason element mention false positive"
  ],
  [
    "halogen",
    "None",
    "N/A",
    "N/A",
    "False",
    "Yes",
    "Another element-family word false positive"
  ],
  [
    "cyano",
    "None",
    "N/A",
    "N/A",
    "False",
    "Yes",
    "Just a substituent name not T# false positive"
  ],
  [
    "cyano group",
    "None",
    "Yes group appended",
    "N/A",
    "False",
    "Yes",
    "Not a gold-standard compound false positive"
  ],
  [
    "nitro",
    "None",
    "N/A",
    "N/A",
    "False",
    "Yes",
    "Again substituent false positive"
  ],
  [
    "nitro group",
    "None",
    "Yes",
    "N/A",
    "False",
    "Yes",
    "Not a T# false positive"
  ],
  [
    "amino",
    "None",
    "N/A",
    "N/A",
    "False",
    "Yes",
    "Just amino no T# false positive"
  ],
  [
    "amino group",
    "None",
    "Yes",
    "N/A",
    "False",
    "Yes",
    "Not a T# false positive"
  ],
  [
    "carbonyl group",
    "None",
    "Yes",
    "N/A",
    "False",
    "Yes",
    "Same logic false positive"
  ],
  [
    "thioxo group",
    "None",
    "Yes",
    "N/A",
    "False",
    "Yes",
    "Another substituent not T# false positive"
  ],
  [
    "phenyl",
    "None",
    "N/A",
    "N/A",
    "False",
    "Yes",
    "Just phenyl partial false positive"
  ],
  [
    "phenyl group",
    "None",
    "Yes",
    "N/A",
    "False",
    "Yes",
    "Not T# false positive"
  ],
  [
    "racemate",
    "None",
    "N/A",
    "N/A",
    "False",
    "Yes",
    "Generic term false positive"
  ],
  [
    "racemic mixture",
    "None",
    "Yes",
    "N/A",
    "False",
    "Yes",
    "Another generic phrase false positive"
  ],
  [
    "pharmaceutically acceptable salt",
    "None",
    "Yes",
    "N/A",
    "False",
    "Yes",
    "No T# partial mention false positive"
  ],
  [
    "pharmaceutical salt",
    "None",
    "Yes",
    "N/A",
    "False",
    "Yes",
    "Another partial mention false positive"
  ],
  [
    "(3,5-dibromo-4-hydroxy-phenyl)-[7-(4-trifluoromethyl-phenyl)-2,3-dihydro-pyrido[2,3-b][1,4]oxazin-1-yl]-methanone",
    "T45",
    "No",
    "No",
    "True Positive",
    "No",
    "Matches T53 from big doc fyi the trifluoromethyl-phenyl ring"
  ],
  [
    "(3,5-dibromo-4-hydroxy-phenyl)-[7-(2-trifluoromethyl-phenyl)-2,3-dihydro-pyrido[2,3-b][1,4]oxazin-1-yl]-methanone",
    "T46",
    "No",
    "No",
    "True Positive",
    "No",
    "Matches T46"
  ],
  [
    "1-(3,5-dibromo-4-methoxy-benzoyl)-2,3-dihydro-1H-pyrido[2,3-b][1,4]oxazin-7-carbonitrile",
    "T47-1",
    "No",
    "No",
    "True Positive",
    "No",
    "Matches T47-1"
  ],
  [
    "1-(3,5-dibromo-4-hydroxy-benzoyl)-2,3-dihydro-1H-pyrido[2,3-b][1,4]oxazin-7-carbonitrile",
    "T47-2",
    "No",
    "No",
    "True Positive",
    "No",
    "Matches T47-2"
  ],
  [
    "(3,5-dibromo-4-methoxy-phenyl)-[7-(3-nitro-phenyl)-2,3-dihydro-pyrido[2,3-b][1,4]oxazin-1-yl]-methanone",
    "T48 or T49",
    "No",
    "No",
    "True Positive",
    "No",
    "Indeed T48 or T49 both have same text matches T48"
  ],
  [
    "(3,5-dibromo-4-hydroxy-phenyl)-[7-(3-dimethylamino-phenyl)-2,3-dihydro-pyrido[2,3-b][1,4]oxazin-1-yl]-methanone",
    "T50",
    "No",
    "No",
    "True Positive",
    "No",
    "Actually T43 from big doc with dimethylamino phenyl"
  ],
  [
    "(3,5-dibromo-4-hydroxy-phenyl)-(2,3-dihydro-pyrido[4,3-b][1,4]oxazin-4-yl)-methanethione",
    "T51",
    "No",
    "No",
    "True Positive",
    "No",
    "Matches T51"
  ],
  [
    "(3,5-dibromo-4-hydroxy-phenyl)-(7-pyridin-3-yl-2,3-dihydro-pyrido[2,3-b][1,4]oxazin-1-yl]-methanone",
    "T52",
    "No",
    "No",
    "True Positive",
    "No",
    "Matches T52"
  ],
  [
    "(3,5-dibromo-4-hydroxy-phenyl)-(7-furan-3-yl-2,3-dihydro-pyrido[2,3-b][1,4]oxazin-1-yl]-methanone",
    "T53",
    "No",
    "No",
    "True Positive",
    "No",
    "Furan ring match T53"
  ],
  [
    "1-(3,5-dibromo-4-hydroxy-phenyl)-2-(2,3-dihydro-pyrido[4,3-b][1,4]oxazin-4-yl)-ethanone",
    "T54",
    "No",
    "No",
    "True Positive",
    "No",
    "Matches T54"
  ],
  [
    "(3,5-dibromo-4-hydroxy-phenyl)-(2,3-dihydro-4-oxa-1,9-diaza-phenanthren-1-yl)-methanone",
    "T55",
    "No",
    "No",
    "True Positive",
    "No",
    "Matches T67 from text but considered T55 or T67 user states T67"
  ],
  [
    "4-[2-(3,5-dibromo-4-hydroxy-phenyl)-2-oxo-ethyl)]-4H-pyrido[4,3-b][1,4]oxazin-3-one",
    "T56",
    "No",
    "No",
    "True Positive",
    "No",
    "Matches T56"
  ],
  [
    "4-(3,5-dibromo-4-methoxy-benzoyl)-4H-pyrido[4,3-b][1,4]oxazin-3-one",
    "T57",
    "No",
    "No",
    "True Positive",
    "No",
    "Actually T11 in big doc but also T57 repeated so matches T11 or T57"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7  4 trifluoromethyl phenyl  2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "None",
    "Yes spaced out",
    "Possibly",
    "False",
    "Yes",
    "Incomplete spacing version not exactly T30 or T63 false positive"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7  2 trifluoromethyl phenyl  2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Another partial spaced mention no exact T# false positive"
  ],
  [
    "1  3 5 dibromo 4 methoxy benzoyl  2 3 dihydro 1h pyrido 2 3 b  1 4 oxazin 7 carbonitrile",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Spaced variant of T47-1 but missing punctuation false positive"
  ],
  [
    "1  3 5 dibromo 4 hydroxy benzoyl  2 3 dihydro 1h pyrido 2 3 b  1 4 oxazin 7 carbonitrile",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Another partial spaced version no exact T47-2 false positive"
  ],
  [
    "3 5 dibromo 4 methoxy phenyl   7  3 nitro phenyl  2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Spaced version of T48 or T49 not exact match false positive"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7  3 dimethylamino phenyl  2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Spaced partial not T43 false positive"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanethione",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Spaced partial not T51 false positive"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7 pyridin 3 yl 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Another partial not T52 false positive"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7 furan 3 yl 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Spaced partial not T53 false positive"
  ],
  [
    "1  3 5 dibromo 4 hydroxy phenyl  2  2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  ethanone",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Spaced partial not T54 false positive"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   2 3 dihydro 4 oxa 1 9 diaza phenanthren 1 yl  methanone",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Not exactly T67 spacing false positive"
  ],
  [
    "4  2  3 5 dibromo 4 hydroxy phenyl  2 oxo ethyl   4h pyrido 4 3 b  1 4 oxazin 3 one",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Not exactly T56 false positive"
  ],
  [
    "4  3 5 dibromo 4 methoxy benzoyl  4h pyrido 4 3 b  1 4 oxazin 3 one",
    "None",
    "Yes",
    "Possibly",
    "False",
    "Yes",
    "Spaced partial not T11 false positive"
  ],
  [
    "compound 22-1",
    "None",
    "compound 22-1 text",
    "N/A",
    "False",
    "Yes",
    "Placeholder mention not T22 false positive"
  ],
  [
    "compound 22-2",
    "None",
    "compound 22-2",
    "N/A",
    "False",
    "Yes",
    "Another placeholder not T22 false positive"
  ],
  [
    "compound 23",
    "None",
    "compound 23",
    "N/A",
    "False",
    "Yes",
    "Short placeholder real T23 is 2,5-dibromo-4- etc"
  ],
  [
    "2 5 dibromo 4  2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 carbonyl  benzoic acid",
    "T23?",
    "Spacing",
    "Possibly missing punctuation",
    "True Positive",
    "No",
    "Despite missing brackets it aligns with T23 ignoring spacing"
  ],
  [
    "compound 24",
    "None",
    "compound 24",
    "N/A",
    "False",
    "Yes",
    "Another short placeholder T24 is something else"
  ],
  [
    "2 6 dibromo 4  2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 carbonyl  phenoxy  acetic acid methyl ester",
    "T24?",
    "Missing punctuation",
    "Possibly partial",
    "True Positive",
    "No",
    "Matches T24 ignoring spacing"
  ],
  [
    "compound 25",
    "None",
    "compound 25",
    "N/A",
    "False",
    "Yes",
    "Placeholder T25 is a longer compound name"
  ],
  [
    "7 bromo 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl   3 5 dibromo 4 hydroxy phenyl  methanone",
    "T25?",
    "Missing parentheses",
    "Possibly partial",
    "True Positive",
    "No",
    "Matches T25 ignoring punctuation"
  ],
  [
    "compound 26",
    "None",
    "compound 26",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T# match"
  ],
  [
    "2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl   3 fluoro 4 hydroxy phenyl  methanone",
    "T26?",
    "Yes spacing",
    "Possibly",
    "True Positive",
    "No",
    "Despite spacing it matches T26 ignoring punctuation"
  ],
  [
    "compound 27-1",
    "None",
    "compound 27-1",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T27 match"
  ],
  [
    "compound 27-2",
    "None",
    "compound 27-2",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T27 match"
  ],
  [
    "compound 28",
    "None",
    "compound 28",
    "N/A",
    "False",
    "Yes",
    "Another short placeholder no T#"
  ],
  [
    "3 5 difluoro 4 methoxy phenyl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanone",
    "T28?",
    "Yes spaced out",
    "Possibly",
    "True Positive",
    "No",
    "Matches T12 ignoring spacing"
  ],
  [
    "compound 29",
    "None",
    "compound 29",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "3 5 difluoro 4 hydroxy phenyl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanone",
    "T29?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T58 ignoring spacing"
  ],
  [
    "compound 30",
    "None",
    "compound 30",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "5 chloro 2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl   3 5 dibromo 4 hydroxy phenyl  methanone",
    "T30?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T32 ignoring spacing"
  ],
  [
    "compound 31",
    "None",
    "compound 31",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "2 6 dichloro pyridin 4 yl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanone",
    "T31?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T31 ignoring spacing"
  ],
  [
    "compound 32",
    "None",
    "compound 32",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl   6 hydroxy pyridin 3 yl  methanone",
    "T32?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T32 ignoring spacing"
  ],
  [
    "compound 33",
    "None",
    "compound 33",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanone hydrochloric acid salt",
    "T33?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T3 ignoring spacing"
  ],
  [
    "compound 34",
    "None",
    "compound 34",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "3 chloro 4 hydroxy phenyl   2 3 dihydro pyrido 3 4 b  1 4 oxazin 1 yl  methanone",
    "T34?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T23 ignoring spacing"
  ],
  [
    "compound 35-1",
    "None",
    "compound 35-1",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T35"
  ],
  [
    "compound 35-2",
    "None",
    "compound 35-2",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "compound 36",
    "None",
    "compound 36",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 chloro 4 hydroxy 5 nitro phenyl   2 3 dihydro pyrido 3 4 b  1 4 oxazin 1 yl  methanone",
    "T36?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T8 ignoring spacing"
  ],
  [
    "compound 37",
    "None",
    "compound 37",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 chloro 4 hydroxy phenyl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanone",
    "T37?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T4 ignoring spacing"
  ],
  [
    "compound 38",
    "None",
    "compound 38",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 bromo 4 hydroxy phenyl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanone",
    "T38?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T41 ignoring spacing"
  ],
  [
    "compound 39",
    "None",
    "compound 39",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dichloro 4 hydroxy phenyl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanone",
    "T39?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T65 ignoring spacing"
  ],
  [
    "compound 40",
    "None",
    "compound 40",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 bromo 4 hydroxy phenyl   2 3 dihydro pyrido 3 4 b  1 4 oxazin 1 yl  methanone",
    "T40?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T37 ignoring spacing"
  ],
  [
    "compound 41",
    "None",
    "compound 41",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dichloro 4 hydroxy phenyl   2 3 dihydro pyrido 3 4 b  1 4 oxazin 1 yl  methanone",
    "T41?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T41 ignoring spacing"
  ],
  [
    "compound 42",
    "None",
    "compound 42",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "2  3 5 dibromo 4 hydroxy phenyl  1  2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  ethanone",
    "T42?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T42 ignoring spacing"
  ],
  [
    "compound 43",
    "None",
    "compound 43",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl   3 methoxy isoxazol 5 yl  methanone",
    "T43?",
    "Yes",
    "Possibly",
    "True Positive",
    "No",
    "Matches T43 ignoring spacing"
  ],
  [
    "compound 44",
    "None",
    "compound 44",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl   3 hydroxy isoxazol 5 yl  methanone",
    "T44",
    "Yes spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T44 ignoring spacing"
  ],
  [
    "compound 22 1",
    "None",
    "compound 22 1",
    "N/A",
    "False",
    "Yes",
    "Another placeholder not actual T22 false positive"
  ],
  [
    "3 5 dibromo 4 methoxy phenyl   7 trifluoromethyl 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T22-1?",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T22-1 ignoring spacing"
  ],
  [
    "compound 22 2",
    "None",
    "compound 22 2",
    "N/A",
    "False",
    "Yes",
    "Another placeholder not T22 false positive"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7 trifluoromethyl 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T22-2",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T22-2 ignoring spacing"
  ],
  [
    "compound 27 1",
    "None",
    "compound 27 1",
    "N/A",
    "False",
    "Yes",
    "Another placeholder not T27 false positive"
  ],
  [
    "3 5 dibromo 4 methoxy phenyl   7 methyl 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T27-1",
    "Possibly ignoring spacing",
    "No",
    "True Positive",
    "No",
    "Matches T27-1"
  ],
  [
    "compound 27 2",
    "None",
    "compound 27 2",
    "N/A",
    "False",
    "Yes",
    "Another placeholder not T27 false positive"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7 methyl 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T27-2",
    "Possibly ignoring spacing",
    "No",
    "True Positive",
    "No",
    "Matches T27-2"
  ],
  [
    "compound 35 1",
    "None",
    "compound 35 1",
    "N/A",
    "False",
    "Yes",
    "Another placeholder not T35 false positive"
  ],
  [
    "4  2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 sulfonyl  phenol",
    "T35-1",
    "Possibly ignoring spacing",
    "No",
    "True Positive",
    "No",
    "Matches T35-1"
  ],
  [
    "compound 35 2",
    "None",
    "compound 35 2",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "2 6 dibromo 4  2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 sulfonyl  phenol",
    "T35-2",
    "Possibly ignoring spacing",
    "No",
    "True Positive",
    "No",
    "Matches T35-2"
  ],
  [
    "compound 58",
    "None",
    "compound 58",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dibromo 4 methoxy phenyl   6 methyl 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T58",
    "Possibly ignoring spacing",
    "No",
    "True Positive",
    "No",
    "Matches T58"
  ],
  [
    "compound 59",
    "None",
    "compound 59",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl   2 4 dihydroxy pyrimidin 5 yl  methanone",
    "T59",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T59"
  ],
  [
    "compound 60",
    "None",
    "compound 60",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl   2 6 dihydroxy pyrimidin 4 yl  methanone",
    "T60",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T60"
  ],
  [
    "compound 61",
    "None",
    "compound 61",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7 isoquinolin 4 yl 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T61",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T61"
  ],
  [
    "compound 62",
    "None",
    "compound 62",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   6 7 dihydro pyrimido 4 5 b  1 4 oxazin 5 yl  methanone",
    "T62",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T62"
  ],
  [
    "compound 63",
    "None",
    "compound 63",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7  3 trifluoromethyl phenyl  2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T63",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T63"
  ],
  [
    "compound 64",
    "None",
    "compound 64",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7  3 fluoromethyl phenyl  2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T64?",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T64"
  ],
  [
    "compound 65",
    "None",
    "compound 65",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "4  1  3 5 dibromo 4 hydroxy benzoyl  2 3 dihydro 1h pyrido 2 3 b  1 4 oxazin 7 yl  benzonitrile",
    "T65",
    "Yes ignoring punctuation",
    "Possibly",
    "True Positive",
    "No",
    "Matches T65 ignoring spacing"
  ],
  [
    "compound 66",
    "None",
    "compound 66",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7  4 trifluoromethoxy phenyl  2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T66",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T66"
  ],
  [
    "compound 67",
    "None",
    "compound 67",
    "N/A",
    "False",
    "Yes",
    "Placeholder no T#"
  ],
  [
    "1  4  1  3 5 dibromo 4 hydroxy benzoyl  2 3 dihydro 1h pyrido 2 3 b  1 4 oxazin 7 yl  phenyl  ethanone",
    "T67",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T67 from the big doc"
  ],
  [
    "compound 68",
    "None",
    "compound 68",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7  5 methoxy pyridin 3 yl  2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T68",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T68"
  ],
  [
    "compound 69",
    "None",
    "compound 69",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "4 hydroxy 3 trifluoromethyl phenyl   7 methyl 2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T69",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T69"
  ],
  [
    "compound 70",
    "None",
    "compound 70",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   7  1h indol 4 yl  2 3 dihydro pyrido 2 3 b  1 4 oxazin 1 yl  methanone",
    "T70",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T70"
  ],
  [
    "compound 71",
    "None",
    "compound 71",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanone sulfuric acid salt",
    "T71",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T71"
  ],
  [
    "compound 72",
    "None",
    "compound 72",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "2 6 dibromo 4  2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 carbonyl  phenolate sodium salt",
    "T72",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T72"
  ],
  [
    "compound 73",
    "None",
    "compound 73",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "2 6 dibromo 4  2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 carbonyl  phenolate potassium salt",
    "T73",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T73"
  ],
  [
    "compound 74",
    "None",
    "compound 74",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "3 5 dibromo 4 hydroxy phenyl   2 3 dihydro pyrido 4 3 b  1 4 oxazin 4 yl  methanethione trifluoroacetic acid salt",
    "T74",
    "Possibly ignoring spacing",
    "No",
    "True Positive",
    "No",
    "Matches T74"
  ],
  [
    "compound 75",
    "None",
    "compound 75",
    "N/A",
    "False",
    "Yes",
    "Another placeholder no T#"
  ],
  [
    "1  1  3 5 dibromo 4 hydroxy benzoyl  2 3 dihydro 1h pyrido 2 3 b  1 4 oxazin 7 yl  pyrrolidin 2 one",
    "T75",
    "Yes ignoring spacing",
    "Possibly",
    "True Positive",
    "No",
    "Matches T75"
  ],
  [
    "ee898829e1fc502e2e06471d0ba1d9113e1d22b1664238232ff592cd9c542225#5000#0#SEM",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Another internal SEM or metadata node not a chemical"
  ],
  [
    "HiddenPlaceholderNode",
    "None",
    "N/A",
    "N/A",
    "False",
    "No",
    "Likely an extra or duplicate placeholder node no match"
  ]
]

def main():
    # Create a CSV file named 'comparison_table.csv' with the above data.
    with open("comparison_table.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Write the header row.
        writer.writerow(header)
        # Write all data rows.
        for row in rows:
            writer.writerow(row)

    print("File 'comparison_table.csv' has been created successfully.")

if __name__ == "__main__":
    main()
