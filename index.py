from validator import validColor
import deco

#startup
deco.clear()
print(deco.center(deco.color(' rgba test values ', "green"), "="))


#test values output: true -->
validColor('rgb(0,0,0)');
validColor('rgb(255,255,255)');
validColor('rgba(0,0,0,0)');
validColor('rgba(255,255,255,1)');
validColor('rgba(0,0,0,0.123456789)');
validColor('rgba(0,0,0,.8)');
validColor('rgba(    0 , 127    , 255 , 0.1    )');
validColor('rgb(0%,50%,100%)');

#test values output: false -->
validColor('rgb(0,,0)');    
validColor('rgb (0,0,0)');
validColor('rgb(0,0,0,0)');
validColor('rgba(0,0,0)');
validColor('rgb(-1,0,0)');
validColor('rgb(255,256,255)');
validColor('rgb(100%,100%,101%)');
validColor('rgba(0,0,0,-1)');
validColor('rgba(0,0,0,1.1)');
validColor('rgb(0,0,,0)');
validColor('abc(0,0,0)');


