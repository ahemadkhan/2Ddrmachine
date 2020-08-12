float margin = 7;
float l1,l2,a1,a2;
float x = 0,y = 195;
float px2 = -1, py2 = -1;

int i = 0,p;

PGraphics canvas;

void setup(){
  size(600,400);
  
  canvas = createGraphics(width, height);
  canvas.beginDraw();
  canvas.background(255);
  canvas.endDraw();

}

void draw(){
  background(255);
  //imageMode(CORNER);
  image(canvas,0,0,width,height);
  stroke(0);
  strokeWeight(3);
  translate(margin,height-margin);
  scale(1,-1);
  
  float act_H = height - 2 * margin;
  float act_W = width - 2 * margin;
  
  Table table = loadTable("ll231.csv");  
  TableRow a1_row = table.getRow(0);
  TableRow a2_row = table.getRow(1);
  TableRow p_row = table.getRow(2);

  
  //x = 497;
  //y = 246;
  //y = 195 + 55 * sin(100*PI*(x));
  
  //a1 = (PI/2) + atan(y/x) - (acos(1-(x*x+y*y)/(2*l1*l2)))/2;
  //a2 = acos(1-(x*x+y*y)/(2*l1*l2)) - PI ;
  
  a1 = a1_row.getFloat(i);
  a2 = a2_row.getFloat(i);
  p = p_row.getInt(i);
  
  l1 = sqrt(act_H*act_H+act_W*act_W)/2;
  l2 = sqrt(act_H*act_H+act_W*act_W)/2;
  
  /*
  if (y>(act_H*x/act_W)){ 
    a1 = atan(y/x) - acos(sqrt(x*x+y*y)/(2*l1));
    a2 = acos((x*x+y*y-2*l1*l2)/(2*l1*l2));
  }
  if (y<(act_H*x/act_W)){ 
    a1 = - atan(y/x) + acos(sqrt(x*x+y*y)/(2*l1));
    a2 = - acos((x*x+y*y-2*l1*l2)/(2*l1*l2));
  }
  if (y==(act_H*x/act_W)){
    a1 = atan(act_H/act_W) + acos(sqrt(x*x+y*y)/(2*l1));
    a2 = -acos((x*x+y*y-2*l1*l2)/(2*l1*l2));
  }
  
  print(a1);
  print('\n');
  print(a2);
  print('\n');
  print('\n');  
  */
  
  float x1 = l1 * cos(a1);
  float y1 = l1 * sin(a1);
  
  float x2 = x1 + l2 * cos(a2+a1);
  float y2 = y1 + l2 * sin(a2+a1);
  
  fill(0);
  ellipse(0,0,margin-2,margin-2);
  
  line(0,0,x1,y1);
  ellipse(x1,y1,margin-2,margin-2);
  
  line(x1,y1,x2,y2);
  ellipse(x2,y2,margin-2,margin-2);
  
  //x += 0.1;
  i += 1;
  /*if (x > act_W){
     x = 59;
     y = 195;
     px2 = -1;
     py2 = -1;
  }*/
  
  canvas.beginDraw();
  canvas.translate(margin,height-margin);
  canvas.strokeWeight(3);
  canvas.stroke(0);
  if (frameCount > 1 && p!=0){
    canvas.line(px2, -py2, x2, -y2);
  }
  canvas.endDraw();
  
  px2 = x2;
  py2 = y2;
}
