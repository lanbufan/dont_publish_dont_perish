import csv
import re

faculty_data = """
Victor Aguirregabiria
Aguirregabiria, Victor, Professor
Ph.D. CEMFI - Universidad Complutense, Madrid, 1995
victor.aguirregabiria@utoronto.ca
Research fields: Industrial organization, Econometrics, Applied econometrics416-978-4358
Varouj A. Aivazian
Aivazian, Varouj A., Professor
Ph.D. Ohio State, 1975
varouj.aivazian@utoronto.ca
Research fields: Financial economics, Law and economics416-978-2375
Michelle Alexopoulos
Alexopoulos, Michelle, Professor
Ph.D. Northwestern, 1999
malex@chass.utoronto.ca
Research fields: Macroeconomics, Applied econometrics416-978-4962
Carolina Arteaga
Arteaga, Carolina, Assistant Professor
Ph.D. UCLA, 2019
carolina.arteaga@utoronto.ca
Research fields: Labour economics416-978-4620
Lee Bailey
Bailey, Lee, Associate Professor, Teaching Stream
lee.bailey@utoronto.ca905-569-4908
Michael Baker
Baker, Michael, Professor; Canada Research Chair
Ph.D. Michigan, 1990
m.baker@utoronto.ca
Research fields: Labour economics, Public economics, Applied econometrics416-978-4138
Baysan, Ceren, Assistant Professor
ceren.baysan@utoronto.ca
Dwayne Benjamin
Benjamin, Dwayne, Professor
Ph.D. Princeton, 1989
dwayne.benjamin@utoronto.ca
Research fields: Labour economics, Economics of higher education416-978-6130
Arthur Blouin
Blouin, Arthur, Associate Professor
Ph.D. Warwick, 2014
a.blouin@utoronto.ca
Research fields: Economic development, Economic history, Political economy416-946-3404
Gustavo Bobonis
Bobonis, Gustavo, Professor; Canada Research Chair (on leave)
Ph.D. Berkeley, 2005
gustavo.bobonis@utoronto.ca
Research fields: Economic development, Labour economics, Political economy, Economic history416-946-5299
Loren Brandt
Brandt, Loren, Professor; Noranda Chair
Ph.D. Illinois, 1983
loren.brandt@utoronto.ca
Research fields: Economic development, Economic history, Chinese economy416-978-4442
Martin Burda
Burda, Martin, Associate Professor
Ph.D. Pittsburgh, 2007
martin.burda@utoronto.ca
Research fields: Econometrics, Applied econometrics416-978-4479
Gabriel Carroll
Carroll, Gabriel, Professor
PhD M.I.T., 2012
gabriel.carroll@utoronto.ca
Research fields: Microeconomic theory416-978-4181
Murat Celik
Celik, Murat, Assistant Professor
Ph.D. Pennsylvania, 2016
murat.celik@utoronto.ca
Research fields: Macroeconomics416-946-7354
Yanyou Chen
Chen, Yanyou, Assistant Professor
Ph.D. Duke, 2020
yanyou.chen@utoronto.ca
Research fields: Industrial organization416-978-0147
Jason Choi
Choi, Jason, Assistant Professor
jasonhj.choi@utoronto.ca
Research fields: Macroeconomics, Financial economics
Ettore Damiano
Damiano, Ettore, Professor; Chair
Ph.D. Yale, 2000
ettore.damiano@utoronto.ca
Research fields: Microeconomic theory416-978-4724
Rahul Deb
Deb, Rahul, Professor
Ph.D. Yale, 2010
rahul.deb@utoronto.ca
Research fields: Microeconomic theory, Industrial organization416-978-6295
Florian Dendorfer
Dendorfer, Florian, Assistant Professor
florian.dendorfer@utoronto.ca
Research fields: Industrial organization416-978-5133
Olga Denislamova
Denislamova, Olga, Assistant Professor, Teaching Stream
Ph.D. University of California, San Diego
o.denislamova@utoronto.ca
Research fields: Macroeconomics416-946-7974
Margarida Duarte
Duarte, Margarida, Professor; Chair, UTM
Ph.D. University of Rochester, 2001
margarida.duarte@utoronto.ca
Research fields: Macroeconomics, International economics416-978-6208
Sebastian Dyrda
Dyrda, Sebastian, Assistant Professor
Ph.D. Minnesota, 2015
sebastian.dyrda@utoronto.ca
Research fields: Macroeconomics416-978-4189
Shari Eli
Eli, Shari, Associate Professor
Ph.D Berkeley, 2011
shari.eli@utoronto.ca
Research fields: Economic history, Health economics416-946-8825
Abdollah Farhoodi
Farhoodi, Abdollah, Assistant Professor
Ph.D. University of Illinois, Urbana-Champaign
a.farhoodi@utoronto.ca
Research fields: Industrial organization, Urban economics416-946-0245
Kripa Freitas
Freitas, Kripa, Associate Professor, Teaching Stream
Ph.D. Northwestern, 2008
k.freitas@utoronto.ca
Research fields: Economic development416-978-2268
Robert Gazzale
Gazzale, Robert, Professor, Teaching Stream; Associate Chair, Undergraduate Studies
Ph.D. Michigan, 2004
robert.gazzale@utoronto.ca
Research fields: Industrial organization, Behavioral Economics, Experimental Economics416-978-2123
Christian Gourieroux
Gourieroux, Christian, Professor
Ph.D. Rouen, 1982
Christian.Gourieroux@ensae.fr
Research fields: Econometrics416-978-5146
Jiaying Gu
Gu, Jiaying, Associate Professor (on leave)
Ph.D. Illinois, Urbana-Champaign, 2015
jiaying.gu@utoronto.ca
Research fields: Econometrics, Applied econometrics416-978-6655
Yoram Halevy
Halevy, Yoram, Professor (on leave)
Ph.D. Hebrew University of Jerusalem, 1998
yoram.halevy@utoronto.ca
Research fields: Behavioral Economics, Experimental Economics, Microeconomic theory416-978-4417
Jonathan Hall
Hall, Jonathan, Associate Professor (on leave)
Ph.D. Chicago, 2012
jonathan.hall@utoronto.ca
Research fields: Urban economics, Public economics, Applied microeconomics416-978-5110
Gillian C. Hamilton
Hamilton, Gillian C., Associate Professor
Ph.D. Queen's, 1993
gillian.hamilton@utoronto.ca
Research fields: Economic history, Labour economics416-978-3070
Hudja, Stanton, Postdoctoral Fellow
stanton.hudja@utoronto.ca
Ajaz Hussain
Hussain, Ajaz, Associate Professor, Teaching Stream
Ph.D. Brown, 2002
sayed.hussain@utoronto.ca
Research fields: Financial economics, Industrial organization416-978-8997
Gueorgui Kambourov
Kambourov, Gueorgui, Professor
Ph.D. Western Ontario, 2004
g.kambourov@utoronto.ca
Research fields: Macroeconomics, Labour economics, Public economics416-978-8695
Nazanin Khazra
Khazra, Nazanin, Assistant Professor, Teaching Stream
Ph.D. University of Illinois,Urbana-Champaign
nazanin.khazra@utoronto.ca
Research fields: Urban economics, Household finance, Applied machine learning
Koebel, Kourtney, Postdoctoral Fellow
kourtney.koebel@utoronto.ca
Marlene Koffi
Koffi, Marlene, Assistant Professor
Ph.D. Montreal, 2020
marlene.koffi@utoronto.ca416-946-5658
Kory Kroft
Kroft, Kory, Professor
Ph.D. Berkeley, 2007
kory.kroft@utoronto.ca
Research fields: Public economics, Labour economics416-978-4355
Burhanettin Kuruscu
Kuruscu, Burhanettin, Associate Professor (on leave)
PhD Rochester, 2002
burhan.kuruscu@utoronto.ca
Research fields: Macroeconomics, Labour economics, Public economics416-978-8343
Lim, Kevin, Assistant Professor (on leave)
Ph.D Princeton, 2016
kvn.lim@utoronto.ca416-946-0851
Yao Luo
Luo, Yao, Associate Professor
Ph.D. Pennsylvania State University, 2013
yao.luo@utoronto.ca
Research fields: Industrial organization, Applied econometrics416-946-5288
Robert McMillan
McMillan, Robert, Associate Professor; Associate Chair, Graduate Studies
Ph.D. Stanford, 1999
robert.mcmillan@utoronto.ca
Research fields: Public economics, Economics of education416-978-4190
Angelo Melino
Melino, Angelo, Professor
Ph.D. Harvard, 1983
angelo.melino@utoronto.ca
Research fields: Econometrics, Macroeconomics, Financial economics416-978-6541
Jordi Mondria
Mondria, Jordi, Professor; Director, MFE Program
Ph.D. Princeton University, 2006
jordi.mondria@utoronto.ca
Research fields: Financial economics, International economics, Macroeconomics416-978-1494
Peter Morrow
Morrow, Peter, Associate Professor
Ph.D. Michigan, 2007
peter.morrow@utoronto.ca
Research fields: International economics416-978-4375
Ismael Mourifié
Mourifié, Ismael, Professor (on leave)
Ph.D. Montreal, 2014
ismael.mourifie@utoronto.ca
Research fields: Econometrics, Applied econometrics416-978-1495
Jennifer Murdock
Murdock, Jennifer, Professor, Teaching Stream (on leave)
Ph.D. Yale, 2002
jennifer.murdock@utoronto.ca
Research fields: Industrial organization, Environmental economics416-946-0656
Philip Oreopoulos
Oreopoulos, Philip, Professor
Ph.D. Berkeley, 2002
oreo@economics.utoronto.ca
Research fields: Labour economics, Applied econometrics, Economics of education416-946-3776
Robert Owen
Owen, Robert, Professor
Ph.D. Princeton, 1981
robert.owen@utoronto.ca
Research fields: International economics, Industrial organization
Tyler Paul
Paul, Tyler, Assistant Professor, Teaching Stream
tyler.paul@utoronto.ca
Research fields: Macroeconomics416-978-5079
Marcin Pęski
Pęski, Marcin, Professor
Ph.D. Northwestern, 2005
marcin.peski@utoronto.ca
Research fields: Microeconomic theory416-978-1970
David Price
Price, David, Assistant Professor
Ph.D. Stanford, 2017
david.price@utoronto.ca
Research fields: Labour economics, Public economics, Econometrics416-978-5143
Mark Rempel
Rempel, Mark, Assistant Professor
Ph.D. Wisconsin-Madison, 2022
mark.rempel@utoronto.ca
Research fields: Macroeconomics, Financial economics, Industrial organization416-978-7134
Diego Restuccia
Restuccia, Diego, Professor; Canada Research Chair
Ph.D. Minnesota, 1998
diego.restuccia@utoronto.ca
Research fields: Macroeconomics, Economic development416-978-5114
Anne-Katrin Roesler
Roesler, Anne-Katrin, Assistant Professor
Ph.D. Bonn, 2015
ak.roesler@utoronto.ca
Research fields: Microeconomic theory416-978-5283
Xianwen Shi
Shi, Xianwen, Professor
Ph.D. Yale, 2007
xianwen.shi@utoronto.ca
Research fields: Microeconomic theory, Industrial organization416-978-5105
Michael Smart
Smart, Michael, Professor (on leave)
Ph.D. Stanford, 1995
Research fields: Public economics416-978-5119
Eduardo Souza-Rodrigues
Souza-Rodrigues, Eduardo, Associate Professor
Ph.D. Yale, 2012
e.souzarodrigues@utoronto.ca
Research fields: Environmental economics, Industrial organization, Econometrics416-978-4349
Joseph Steinberg
Steinberg, Joseph, Associate Professor
Ph.D. Minnesota, 2013
joseph.steinberg@utoronto.ca
Research fields: Macroeconomics, International economics416-978-5396
Stepner, Michael, Assistant Professor
Ph.D. M.I.T, 2019
michael.stepner@utoronto.ca
Research fields: Public economics, Health economics416-978-8779
Colin Stewart
Stewart, Colin, Professor
Ph.D. Yale, 2007
colin.stewart@utoronto.ca
Research fields: Microeconomic theory, Behavioral Economics416-946-3519
Daniel Trefler
Trefler, Daniel, Professor
Ph.D. UCLA, 1989
dtrefler@rotman.utoronto.ca
Research fields: International economics, Economic development, Technology and productivity416-946-7945
Anton Tsoy
Tsoy, Anton, Assistant Professor
Ph.D. M.I.T, 2015
anton.tsoy@utoronto.ca
Research fields: Financial economics, Microeconomic theory416-978-4965
Karen Ugarte-Bravo
Ugarte-Bravo, Karen, Assistant Professor, Teaching Stream
karen.ugarte@utoronto.ca
Research fields: Health economics, Econometrics416-978-6487
Clementine Van Effenterre
Van Effenterre, Clementine, Assistant Professor
Ph.D. Paris School of Economics, 2017
c.vaneffenterre@utoronto.ca
Research fields: Labour economics416-946-3859
Nathanael Vellekoop
Vellekoop, Nathanael, Assistant Professor
Ph.D. Tilburg, 2013
n.vellekoop@utoronto.ca
Research fields: Macroeconomics, Financial economics416-946-3594
Eva Vivalt
Vivalt, Eva, Assistant Professor (on leave)
eva.vivalt@utoronto.ca
Research fields: Labour economics, Development economics416-946-0505
Yuanyuan Wan
Wan, Yuanyuan, Associate Professor
Ph.D. Pennsylvania State University, 2011
yuanyuan.wan@utoronto.ca
Research fields: Econometrics416-978-4964
Tianyi Wang
Wang, Tianyi, Assistant Professor
tianyiwang.wang@utoronto.ca
Research fields: Political economy, Economic history, Health economics, Labor economics
Ward, Courtney, Assistant Professor, Teaching Stream
Ph.D. Toronto, 2010
courtney.ward@utoronto.ca416-978-8626
Weisbrod, Aaron, Assistant Professor, Teaching Stream
aaron.weisbrod@utoronto.ca
Ronald Wolthoff
Wolthoff, Ronald, Associate Professor; Associate Chair, UTM (on leave)
Ph.D. VU University Amsterdam, 2008
ronald.wolthoff@utoronto.ca
Research fields: Macroeconomics, Labour economics416-978-5588
Adonis Yatchew
Yatchew, Adonis, Professor; Editor-in-Chief, The Energy Journal
Ph.D. Harvard, 1980
adonis.yatchew@utoronto.ca
Research fields: Econometrics, Applied econometrics, Energy economics, Regulatory economics416-978-7128
Kathleen Yu
Yu, Kathleen, Associate Professor, Teaching Stream
PhD Univerisity of California, Irvine, 2009
kathleen.yu@utoronto.ca
Research fields: Labour economics, Health economics905-828-5378
Zammit, Nicholas, Assistant Professor, Teaching Stream
n.zammit@utoronto.ca
Roman Zarate
Zarate, Roman, Assistant Professor
Ph.D. Massachusetts Institute of Technology, 2019
ra.zarate@utoronto.ca
Research fields: Economic development, Labour economics
Yingnan Zhao
Zhao, Yingnan, Assistant Professor
Ph.D. Zurich, 2019
yingnan.zhao@utoronto.ca
Research fields: Macroeconomics, Financial economics, Banking
"""

# Split the raw data by line
lines = faculty_data.strip().split("\n")

# Initialize an empty list to store the parsed data
parsed_data = []

# Helper function to extract the required details
def extract_details(lines):
    name, rank, phd_school, phd_year, email, research_fields = None, None, None, None, None, None
    for line in lines:
        if re.match(r'^[A-Za-z\.\s]+$', line):
            if name:
                parsed_data.append([name, rank, phd_school, phd_year, email, research_fields])
            name = line.strip()
            rank, phd_school, phd_year, email, research_fields = None, None, None, None, None
        elif ',' in line and 'Ph.D.' not in line and '@' not in line and 'Research fields:' not in line:
            rank_info = line.split(',', 2)
            if len(rank_info) > 2:
                rank = rank_info[2].strip()
        elif line.startswith("Ph.D."):
            phd_info = re.search(r'Ph.D. (.+), (\d{4})', line)
            if phd_info:
                phd_school = phd_info.group(1).strip()
                phd_year = phd_info.group(2).strip()
            else:
                phd_school, phd_year = None, None
        elif "@" in line:
            email = line.strip()
        elif line.startswith("Research fields:"):
            research_fields = line.replace("Research fields:", "").strip()

    if name:
        parsed_data.append([name, rank, phd_school, phd_year, email, research_fields])

# Parse the details
extract_details(lines)

# Define the headers for the CSV
headers = ["Name", "Rank", "PhD School", "PhD Year", "Email", "Research Fields"]

# Write the parsed data to a CSV file
with open('university_of_toronto_faculty.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(parsed_data)

print("CSV file created successfully!")
