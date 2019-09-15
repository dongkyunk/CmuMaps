
from collections import defaultdict

class Graph():
    def __init__(self):
        """0
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        
graph = Graph()
edges = [
  ('3rampramp','3elevators',5),
        ('3elevators','3305',0),
        ('3elevators','3300',0.5),
        ('3elevators','3807stairs',1.7),
        ('3800stairs','cafecluster',2),
        ('3800stairs','3201a',1.5),
        ('3201a','3201b',100),
        ('3800stairs','3000a',1.5),
        ('3cafecluster','3000a',1.5),
        ('3cafecluster',"3TazzaD'Oro",2.5),
        ('3000a',"TazzaD'Oro",1.5),
        ('3000a','3000b',100),
        ("3TazzaD'Oro",'3000b',2),
        ("3TazzaD'Oro",'3helixramp',2.5),
        ('3helixramp','3000b',2),
        ('3helixramp','3rampramp',1.5),
        ('3rampramp','3807stairs',5),
        ('3300','3303',0),
        ('3807stairs','3wb',0),
        ('3807stairs','3805',0.3),
        ('3805','3808',0),
        ('3805','3mb',0),
        ('3805','3helixstairs',1),
        ('3helixstairs','3205',0.3),
        ('3205','3200',0),
        ('3200','3203',1),
        ('3203','3301A',1),
        ('3301A','3301',2),
        ('3301','3209',1),
    ('5001', '5003', 0.5), 
    ('5001', '5800stairs', 0.5), 
    ('5800stairs', '5804', 5),
    ('5800stairs', '5200', 1.5),
    ('5804', '5808', 1),
    ('5808', '5817', 2),
    ('5817', '5115', 3),
    ('5817', '5215', 3),
    ('5115', '5809', 2),
    ('5809', '5117', 1),
    ('5117', '5113', 1),
    ('5113', '5111', 0.5),
    ('5111', '5109', 1.5),
    ('5109', '5107', 0.5),
    ('5107', '5105', 1),
    ('5105', '5103', 1),
    ('5103', '5101', 1),
    ('5101', '5013', 1),
    ('5013', '5007', 1),
    ('5013', '5011', 1.5),
    ('5007', '5005', 0.5),
    ('5005', '5003', 2),
    ('5200', '5208', 2.5),
    ('5208', '5210', 1.5),
    ('5210', '5207', 0.5),
    ('5207', '5215', 3),
    ('5009', '5011', 0),
    ('5202', '5200', 2.5),
    ('5209', '5207', 0),
    ('5211', '5207', 0),
    ('5213', '5207', 0),
    ('5808', '5806', 0),
    ('5808', '5803', 0),
    ('5808', '5805', 0),
    ('5808', '5214', 0),
    ('5808', '5216', 0),
    ('5808', '5807stairs', 0),
    ('5808', '5819', 0),
    ('5808', '5elevators', 0),
    ('5817', '5elevators', 0),
    ('5115', '5116', 0),
    ('5115', '5114', 0),
     ('4101','4103',2.5),
        ('4103','4105',2),
        ('4105','4107',1),
        ('4107','4109',1.1),
        ('4109','4111',0.9),
        ('4111','4113',0.8),
        ('4113','4115',0.8),
        ('4115','4117',0.5),
        ('4117','4120',0.5),
        ('4117','4122',3.8),
        ('4122','4124',1.3),
        ('4124','4126',1.5),
        ('4126','4817',6.5),
        ('4817','4wb',1.5),
        ('4wb','4mb',1),
        ('4mb','4200',6),
        ('4200','4800stairs',3),
        ('4101','4201',3.3),
        ('4201','4205',1.89),
        ('4205','4800stairs',3.7),
        ('4800stairs','4007',3.8),
        ('4007','4005',1.8),
        ('4005','4003',2.2),
        ('4003','4001',2),
        ('4mb','4211',4.1),
        ('4211','4215',4.1),
        ('4215','4301',1),
        ('4301', '4212',3),
        ('4212','4214',0.5),
        ('4817','4elevators',2),
        ('4817','4819',0.5),
        ('4wb','4807stairs',0.5),
        ('4mb','4803',1),
        ('4803','4805',1),
        ('4805','4216',0.5),
        ('4elevators','4302',2),
        ('4302','4814',0.5),
        ('4814','4301',3),
        ('4814','4303',0.5),
        ('4elevators','4307',3),
        ('4307','4305',7.5), 
        ('6001', '6003', 1), 
        ('6001', '6002',0.5),
        ('6002', '6003', 0.5),
        ('6003', '6004', 0.5),
        ('6004', '6005', 1),
        ('6006', '6005', 0),
        ('6005', '6010', 1),
        ('6008', '6005', 0),
        ('6007', '6010', 0),
        ('6010', '6009', 1),
        ('6009', '6023', 1.4),
        ('6023', '6011', 0),
        ('6023', '6021', 0.5),
        ('6021', '6013', 1),
        ('6013', '6019', 0),
        ('6013', '6017', 1),
        ('6017', '6015', 0),
        ('6010', '6027', 1.8),
        ('6027', '6025', 0),
        ('6027', '6029', 1), 
        ('6029', '6201', 1),
        ('6201', '6203', 0),
        ('6203', '6205', 1),
        ('6205', '6207', 1),
        ('6207,', '6101qsa', 2.2),
        ('6101qsa', '6105', 1),
        ('6101qsa', '6107', 1.5),
        ('6809', '6115', 1.5),
        ('6107', '6809', 0.5),
        ('6809', '6111', 0.5),
        ('6111', '6109', 0.8),
        ('6115', '6100', 1.2),
        ('6115', '6117', 1.1),
        ('6117', '6119', 0),
        ('6100', '6121', 0),
        ('6100', '6elevators', 1.2),
        ('6100', '6227', 1.7),
        ('6227', '6225', 0.5), 
        ('6225', '6223', 0.5),
        ('6223', '6217', 1),
        ('6217', '6219', 1),
        ('6219', '6221', 0.8),
        ('6217', '6220', 1),
        ('6220', '6215', 0),
        ('6215', '6218', 0),
        ('6215', '6213', 0.8),
        ('6213', '6211', 0.8),
        ('6211', '6210qsa', 1.1),
        ('6210qsa', '6102', 1.3),
        ('6102', '6101qsa', 2.2),
        ('6227', '6wb', 3),
        ('6wb', '6mb', 0.5),
        ('6mb', '6207', 2.4),
        ('6210qsa', '6211', 1.1),
        ('6210qsa', '6101qsa', 3.5),
        ('6210qsa', '6207', 2.1),
        ('6102', '6207', 1.3),
        ('6023', '6025', 0.5),
        ('6102', '6103', 1),
        ('6103','6115', 2.2), 
        ('6103', '6809', 0.8),
        ('6809', '6111', 0.4),
        ('6010', '6012qsa', 0.8),
        ('6012qsa', '6029', 1),
        ('6807stairs', '6wb', 0),
        ('6800stairs', '6029', 0.5),
        ('7111','7113',0),
        ('7113','7115',0.5),
        ('7115','7117',0.5),
        ('7117','7119',0.5),   
        ('7119','7121',0.5),
        ('7121','7123',0.5),
        ('7123','7122',0),
        ('7123','7125',0.5),
        ('7125','7127',0.5),
        ('7127','7126',0),
        ('7127','7128',0.5),
        ('7128','7129',0),
        ('7129','7elevators',1.5),
        ('7129','7227',1.5),
        ('7elevators','7227',1),
        ('7227','7225',0.5),
        ('7225','7223',0.5),
        ('7223','7219',1),
        ('7219','7221',0.5),
        ('7223','7217',1),
        ('7217','7219',0.5),
        ('7217','7215',0.5),
        ('7215','7224',0),
        ('7215','7218',0),
        ('7215','7213',0.5),
        ('7213','7211',0.7),
        ('7211','7210qsa',1.5),
        ('7210qsa','7214',0),
        ('7210qsa','7200',2),
        ('7200','7216',0),
        ('7200','7805',0),
        ('7200','7803',0),
        ('7200','7806',0),
        ('7200','7mb',0),
        ('7200','7807stairs',0.5),
        ('7807stairs','7wb',0),
        ('7807stairs','7elevators',1.5),
        ('7210','7207',2),
        ('7200','7207',2),
        ('7207','7205',0.5),
        ('7205','7203',0.5),
        ('7203','7201',0),
        ('7203','7029',0.7),
        ('7029','7012qsa',0.5),
        ('7012qsa','7800stairs',0),
        ('7012qsa','7027',0.6),
        ('7027','7025',0.5),
        ('7025','7023',0.5),
        ('7023','7021',0.2),
        ('7021','7019',0.5),
        ('7019','7015',0),
        ('7019','7017',0.5),
        ('7027','7011',0.5),
        ('7012qsa','7011',0.7),
        ('7011','7009',0.3),
        ('7009','7000',0),
        ('7009','7010',0.5),
        ('7010','7007',0),
        ('7010','7008',0.5),
        ('7008','7006',0.3),
        ('7006','7005',0),
        ('7006','7004',0.5),
        ('7004','7003',0),
        ('7004','7002',0.5),
        ('7002','7001',0),
        ('7207','7208',0.5),
        ('7208','7101',1),
        ('7208','7103',0.7),
        ('7103','7101',0.5),
        ('7103','7105',0.5),
        ('7103','7108',0.5),
        ('7105','7108',0.5),
        ('7108','7107qsa',0),
        ('7108','7110',0.5),
        ('7110','7112',0.5),
        ('7112','7114',0.7),
        ('7114','7100stairs',1),
        ('7114','7119',2),
        ('7100stairs','7119',0.7),
        ('7100stairs','7117',0.6),
        ('7100stairs','7115',0.7),
        
        ('7elevators','6elevators',100),
        ('6elevators','5elevators',100),
        ('5elevators','4elevators',100),
        ('4elevators','3elevators',100),
        
        ('7800stairs','6800stairs',100),
        ('6800stairs','5800stairs',100),
        ('5800stairs','4800stairs',100),
        ('4800stairs','3800stairs',100),

        ('7807stairs','6807stairs',100),
        ('6807stairs','5807stairs',100),
        ('5807stairs','4807stairs',100),
        ('4807stairs','3807stairs',100),    
]



for edge in edges:
    graph.add_edge(*edge)
    
def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

coordinateDict = {'5011': (344, 903), '5013': (350, 817), '5101': (357, 770),'5103': (364, 719), '5105': (383, 552), '5107': (395, 445), '5109': (397, 406), '5111': (408, 277), '5113': (448, 282), '5117': (627, 270), '5809': (699, 346), '5115': (697, 142), '5817': (942, 125), '5808': (926, 262), '5807stairs': (926, 262), '5804': (911, 321), '5800': (790, 801), '5001': (708, 809), '5003': (647, 815), '5005': (499, 815), '5007': (457, 815), '5200': (951, 773), '5208': (1086, 588), '5202': (1168, 747), '5210': (1121, 481), '5207': (1150, 415), '5215': (1233, 128)
,"4101": (545,863),
"4103": (518,799),
"4105": (524,729),
"4107": (533,669),
"4109": (541,603),
"4111": (549,555),
"4113": (549,511),
"4115": (559,464),
"4117": (562,427),
"4120": (605,442),
"4122": (642,384),
"4124": (694,381),
"4126": (738,375),
"4817": (907,363),
"4wb": (892,458),
"4mb": (887,483),
"4200": (864,710),
"4800stairs": (850,796),
"4201": (615,832),
"4205": (684,827),
"4800stairs": (807,817),
"4007": (930,769),
"4005": (995,762),
"4003": (1062,753),
"4001": (1123,744),
"4211": (949,583),
"4215": (1004,578),
"4elevators": (959,360),
"4819": (899,417),
"4807stairs": (937,451),
"4302": (1040,364),
"4814": (1071,379),
"4301": (1132,396),
"4303": (1066,341),
"4307": (1045,246),
"4305": (1230,88),
"4101": (545,863),
"4103": (518,799),
"4105": (524,729),
"4107": (533,669),
"4109": (541,603),
"4111": (549,555),
"4113": (549,511),
"4115": (559,464),
"4117": (562,427),
"4120": (605,442),
"4122": (642,384),
"4124": (694,381),
"4126": (738,375),
"4817": (907,363),
"4wb": (892,458),
"4mb": (887,483),
"4200": (864,710),
"4800stairs": (850,796),
"4201": (615,832),
"4205": (684,827),
"4800stairs": (807,817),
"4007": (930,769),
"4005": (995,762),
"4003": (1062,753),
"4001": (1123,744),
"4211": (949,583),
"4215": (1004,578),
"4elevators": (959,360),
"4819": (899,417),
"4807stairs": (937,451),
"4302": (1040,364),
"4814": (1071,379),
"4301": (1132,396),
"4303": (1066,341),
"4307": (1045,246),
"4305": (1230,88),
"6001": (1066,877),
"6002": (1035,864),
"6003": (1002,857),
"6005": (953,838),
"6008": (908,824),
"6010": (880,811),
"6009": (841,814),
"6023": (767,809),
"6021": (763,852),
"6019": (763,897),
"6017": (753,961),
"6027": (772,743),
"6029": (778,697),
"6201": (802,622),
"6205": (827,550),
"6207": (843,486),
"6101qsa": (648,482),
"6107": (733,396),
"6105": (647,425),
"6103": (733,396),
"6809": (745,322),
"6111": (698,323),
"6109": (635,334),
"6115": (752,231),
"6100": (836,202),
"6117": (761,157),
"6elevators": (929,216),
"6227": (983,168),
"6225": (1024,170),
"6223": (1065,169),
"6217": (1092,197),
"6219": (1107,142),
"6221": (1119,101),
"6220": (1071,246),
"6213": (1048,309),
"6211": (1030,365),
"6210qsa": (963,416),
"6102": (852,413),
"6mb": (879,346),
"6wb": (887,304),
'7113': (501.75, 117.0), '7111': (501.75, 117.0), '7115': (541.125, 113.625), '7117': (597.375, 112.5), '7119': (644.625, 113.625), '7121': (689.625, 113.625), '7123/7122': (727.875, 106.875), '7125': (768.375, 110.25), '7127/7126': (821.25, 106.875), '7129/7128': (856.125, 111.375), '7227': (949.5, 105.75), '7225': (985.5, 109.125), '7223': (1028.25, 102.375), '7219': (1069.875, 76.5), '7221': (1082.25, 41.625), '7217': (1051.875, 130.5), '7224': (1037.25, 181.125), '7215': (1037.25, 181.125), '7218': (1037.25, 181.125), '7213': (1017.0, 236.25), '7211': (996.75, 295.875), '7210qsa': (945.0, 345.375), '7214': (945.0, 345.375), '7mb': (858.375, 275.625), '7200': (858.375, 275.625), '7216': (858.375, 275.625), '7806': (858.375, 275.625), '7803': (858.375, 275.625), '7805': (858.375, 275.625), '7808': (860.625, 237.375), '7807stairs': (860.625, 237.375), '7elevators': (914.625, 147.375), '7207': (813.375, 418.5), '7205': (794.25, 472.5), '7203': (775.125, 527.625), '7029': (751.5, 615.375), '7012qsa': (787.5, 649.125), '7800stairs': (787.5, 649.125), '7027': (744.75, 709.875), '7025': (741.375, 753.75), '7023': (740.25, 794.25), '7021': (734.625, 820.125), '7019': (735.75, 857.25), '7015': (735.75, 857.25), '7017': (780.75, 862.875), '7011': (797.625, 716.625), '7009': (821.25, 724.5), '7000': (821.25, 724.5), '7010': (868.5, 742.5), '7007': (868.5, 742.5), '7008': (904.5, 752.625), '7006': (923.625, 759.375), '7005': (923.625, 759.375), '7004': (970.875, 777.375), '7003': (970.875, 777.375), '7002': (1024.875, 792.0), '7001': (1024.875, 792.0), '7208': (752.625, 412.875), '7101': (688.5, 454.5), '7103': (668.25, 405.0), '7105': (605.25, 399.375), '7108': (637.875, 371.25), '7107qsa': (637.875, 371.25), '7110': (642.375, 331.875), '7112': (644.625, 291.375), '7114': (630.0, 240.75), '7100stairs': (594.0, 173.25)
}


curr=0
dest=0
imageIndex= 1
def setup():
    fullScreen()
    global curr
    global dest
    
    textSize(32);
    curr = input('Current Location (Nearest room)')
    if curr:
        message('Current Location: ' + curr)
        dest = input('Destination')
        if dest:
            message('Current Location: ' + curr+ ' Destination: ' + dest)
    
    print(str(displayWidth)+','+str(displayHeight))
    drawShortestPath(graph,curr,dest, imageIndex)

def draw():
    global imageIndex
    fill(204, 102, 0)
    stroke(204, 102, 0);
    rect(0,0,200,100)
    if(mousePressed):
        print(str(mouseX))
        if(0<mouseX and mouseX<200 and 0<mouseY and mouseY<100):
            imageIndex= -imageIndex
            drawShortestPath(graph,curr,dest,imageIndex)
        print(str(imageIndex))
        

      
x =0
y=0
name_before =''
def mouseClicked():
    '''
    global x
    global y
    global name_before
    ellipseMode(CENTER)
    ellipse(mouseX, mouseY, 30, 30)
    name = input('name')
    with open('/Users/dongkyunkim/Desktop/Map/sketch_190914d/coordata.txt','a') as f:
        f.write('"'+name+'"'+': ('+str(mouseX)+','+str(mouseY)+'),'+'\n')

    with open('/Users/dongkyunkim/Desktop/Map/sketch_190914d/nodedata.txt','a') as f:
        f.write('('+'"'+name_before+'"'+',"'+name+'"'+','+str(dist(x, y, mouseX, mouseY))+'),'+'\n')  

    x = mouseX
    y = mouseY
    name_before = name  
    '''

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
def message(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showMessageDialog(frame, message)

def imageconvert(img):
        imageMode(CENTER)
        w = float(img.width)
        h = float(img.height)
        hwRatio = h / w
        if(w > displayWidth):
            w = displayWidth
            h = w * hwRatio
        if(h > displayHeight):
            h = displayHeight
            w = h / hwRatio
        image(img,displayWidth/2,displayHeight/2, w, h)
        
def drawShortestPath(graph,curr,dest,imageIndex):
    print(dijsktra(graph, curr, dest))
    wratio = float(displayWidth/1680)
    hratio = float(displayHeight/1050)
    originalList=[]
    splitList=[]
    for x in range(0,len(dijsktra(graph, curr, dest))):
        originalList.append(dijsktra(graph, curr, dest)[x])
    for x in range(0,len(originalList)):
        if(x>0 and originalList[x][0]!=originalList[x-1][0]):
            splitList.append(x)
    res = [originalList[i : j] for i, j in zip([0] + splitList, splitList + [None])] 
    print(str(res))
    '''
    nodeList1=[]
    for y in range(0,len(res[0])):
            if(res[0][y] in coordinateDict):
                    nodeList1.append(y)    
    for i in range(0,len(nodeList1)):
                w =(coordinateDict[dijsktra(graph, curr, dest)[nodeList1[i]]][0]*wratio)
                h= (coordinateDict[dijsktra(graph, curr, dest)[nodeList1[i]]][1]*hratio)
                ellipseMode(CENTER)
                fill(255,0,0)
                if(i<2):
                    ellipse(w, h, 25,25)    
                else:
                    ellipse(w, h, 15,15)    
                if(i!=0):
                    strokeWeight(10)
                    stroke(255, 0, 0);
                    line(coordinateDict[dijsktra(graph, curr, dest)[nodeList1[i-1]]][0], coordinateDict[dijsktra(graph, curr, dest)[nodeList1[i-1]]][1], coordinateDict[dijsktra(graph, curr, dest)[nodeList1[i]]][0], coordinateDict[dijsktra(graph, curr, dest)[nodeList1[i]]][1]);
    '''
    if(imageIndex==1):
        drawAcutal(0, res, graph, curr, dest, wratio, hratio)
    print(str(imageIndex))
    if(imageIndex==-1):
        drawAcutal(len(res)-1, res, graph, curr, dest, wratio, hratio)
        
    
def drawFloor(curr):
    if(curr[0]=='3'):
        img = loadImage("0004.jpg")
        imageconvert(img)
    elif(curr[0]=='4'):
        img = loadImage("0004.jpg")
        imageconvert(img)
    elif(curr[0]=='5'):
        img = loadImage("0005.jpg")
        imageconvert(img)
    elif(curr[0]=='6'):
        img = loadImage("0006.jpg")
        imageconvert(img)
    elif(curr[0]=='7'):
        img = loadImage("0007.jpg")
        imageconvert(img)

def drawAcutal(x, res, graph, curr, dest, wratio, hratio):
    drawFloor(res[x][0])
    nodeList1=[]
    for y in range(0,len(res[x])):
        if(res[x][y] in coordinateDict):
            nodeList1.append(res[x][y])    
    for i in range(0,len(nodeList1)):
                w =(coordinateDict[nodeList1[i]][0]*wratio)
                h= (coordinateDict[nodeList1[i]][1]*hratio)
                ellipseMode(CENTER)
                fill(255,0,0)
                if(i<2):
                    ellipse(w, h, 25,25)    
                else:
                    ellipse(w, h, 15,15)    
                if(i!=0):
                    strokeWeight(10)
                    stroke(255, 0, 0);
                    line(coordinateDict[nodeList1[i-1]][0], coordinateDict[nodeList1[i-1]][1], w, h);
