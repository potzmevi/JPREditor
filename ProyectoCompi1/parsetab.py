
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightUNOTleftMENORQUEMAYORQUEIGUALIGUALDIFERENTEMAYORIGUALMENORIGUALleftMASMENOSleftPORDIVMODnonassocPOTrightUMENOSAND BOOLEANO CADENA CHARACTER DECIMAL DECREMENTO DIFERENTE DIV ENTERO ID IGUAL IGUALIGUAL INCREMENTO LLAVEA LLAVEC MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MOD NOT OR PARA PARC POR POT PUNTOCOMA RBOOLEAN RBREAK RCASE RCHAR RCONTINUE RDEFAULT RELSE RFLOAT RFOR RFUNC RIF RINT RLENGTH RMAIN RNULL RPRINT RREAD RRETURN RROUND RSTRING RSWITCH RTOLOWER RTOUPPER RTRUNCATE RTYPEOF RVAR RWHILEinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr finins\n                        | declaracion_instr finins\n                        | declaracion_instr2 finins\n                        | asignacion_instr finins\n                        | if_instr\n                        | while_instr\n                        | break_instr finins\n                        | main_instr\n                        | funcion_instr\n                        | llamada_instr finins\n                        | asignacion2_instr finins\n                        | for_instr fininsfinins       : PUNTOCOMA\n                    | instruccion        : error PUNTOCOMA\n    imprimir_instr     : RPRINT PARA expresion PARC PUNTOCOMA\n                    | RPRINT PARA expresion PARC\n    declaracion_instr     : tipo ID IGUAL expresiondeclaracion_instr2     : tipo IDasignacion_instr     : ID IGUAL expresionasignacion2_instr     : ID INCREMENTO\n                            | ID DECREMENTO if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr\n    for_instr : RFOR PARA asignacion_instr PUNTOCOMA expresion PUNTOCOMA asignacion2_instr PARC LLAVEA instrucciones LLAVEC\n    \n        for_instr : RFOR PARA declarar_con_valor_for PUNTOCOMA expresion PUNTOCOMA asignacion2_instr PARC LLAVEA instrucciones LLAVEC\n    \n        for_instr : RFOR PARA expresion PUNTOCOMA expresion PUNTOCOMA asignacion2_instr PARC LLAVEA instrucciones LLAVEC\n    \n    declarar_con_valor_for : tipo_for ID IGUAL expresion\n    while_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVECbreak_instr     : RBREAKmain_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVECfuncion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVECllamada_instr     : ID PARA PARCtipo     : RINT\n                | RFLOAT\n                | RSTRING\n                | RBOOLEAN\n                | RCHAR\n                | RVAR tipo_for    : RINT\n                | RVAR \n    expresion : expresion MAS expresion\n            | expresion MENOS expresion\n            | expresion POR expresion\n            | expresion DIV expresion\n            | expresion POT expresion\n            | expresion MOD expresion\n            | expresion MENORQUE expresion\n            | expresion MAYORQUE expresion\n            | expresion IGUALIGUAL expresion\n            | expresion DIFERENTE expresion\n            | expresion MAYORIGUAL expresion\n            | expresion MENORIGUAL expresion\n            | expresion AND expresion\n            | expresion OR expresion\n            | expresion INCREMENTO\n            | expresion DECREMENTO\n    \n    expresion : MENOS expresion %prec UMENOS \n            | NOT expresion %prec UNOT \n    \n    expresion :   PARA expresion PARC \n    expresion : IDexpresion : CHARACTERexpresion : BOOLEANOexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : RNULL'
    
_lr_action_items = {'error':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[16,16,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,16,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,16,16,16,16,16,16,-35,16,-26,-33,-36,16,-28,16,16,16,16,16,16,16,-27,-29,-31,-30,]),'RPRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[17,17,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,17,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,17,17,17,17,17,17,-35,17,-26,-33,-36,17,-28,17,17,17,17,17,17,17,-27,-29,-31,-30,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,22,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,53,54,56,57,58,59,60,61,62,63,64,65,66,67,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,102,104,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,132,133,134,135,136,137,138,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[19,19,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,44,-34,52,-38,-39,-40,-41,-42,-43,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,58,-22,58,-24,-25,58,58,75,58,58,58,-65,-66,-67,-68,-69,-70,-71,58,-23,-37,107,-44,-45,-20,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-60,-61,-62,-63,-21,19,58,58,58,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,19,19,19,19,58,19,19,-35,19,144,144,144,-26,-33,-36,19,-28,19,19,19,19,19,19,19,-27,-29,-31,-30,]),'RIF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,147,151,152,153,154,155,156,157,158,159,160,161,162,163,],[20,20,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,20,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,20,20,20,20,20,20,-35,20,-26,-33,-36,20,20,-28,20,20,20,20,20,20,20,-27,-29,-31,-30,]),'RWHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[21,21,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,21,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,21,21,21,21,21,21,-35,21,-26,-33,-36,21,-28,21,21,21,21,21,21,21,-27,-29,-31,-30,]),'RBREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[22,22,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,22,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,22,22,22,22,22,22,-35,22,-26,-33,-36,22,-28,22,22,22,22,22,22,22,-27,-29,-31,-30,]),'RMAIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[23,23,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,23,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,23,23,23,23,23,23,-35,23,-26,-33,-36,23,-28,23,23,23,23,23,23,23,-27,-29,-31,-30,]),'RFUNC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[24,24,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,24,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,24,24,24,24,24,24,-35,24,-26,-33,-36,24,-28,24,24,24,24,24,24,24,-27,-29,-31,-30,]),'RFOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[25,25,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,25,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,25,25,25,25,25,25,-35,25,-26,-33,-36,25,-28,25,25,25,25,25,25,25,-27,-29,-31,-30,]),'RINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,53,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[26,26,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,77,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,26,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,26,26,26,26,26,26,-35,26,-26,-33,-36,26,-28,26,26,26,26,26,26,26,-27,-29,-31,-30,]),'RFLOAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[27,27,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,27,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,27,27,27,27,27,27,-35,27,-26,-33,-36,27,-28,27,27,27,27,27,27,27,-27,-29,-31,-30,]),'RSTRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[28,28,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,28,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,28,28,28,28,28,28,-35,28,-26,-33,-36,28,-28,28,28,28,28,28,28,28,-27,-29,-31,-30,]),'RBOOLEAN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[29,29,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,29,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,29,29,29,29,29,29,-35,29,-26,-33,-36,29,-28,29,29,29,29,29,29,29,-27,-29,-31,-30,]),'RCHAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[30,30,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,30,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,30,30,30,30,30,30,-35,30,-26,-33,-36,30,-28,30,30,30,30,30,30,30,-27,-29,-31,-30,]),'RVAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,53,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,102,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,133,134,135,140,141,142,151,152,153,154,155,156,157,158,159,160,161,162,163,],[31,31,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,78,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,31,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,31,31,31,31,31,31,-35,31,-26,-33,-36,31,-28,31,31,31,31,31,31,31,-27,-29,-31,-30,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,134,140,141,142,152,160,161,162,163,],[0,-1,-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-35,-26,-33,-36,-28,-27,-29,-31,-30,]),'LLAVEC':([3,4,5,6,7,8,9,10,11,12,13,14,15,22,32,33,34,35,36,37,38,39,40,41,42,44,47,48,58,59,60,61,62,63,64,66,67,80,95,96,97,98,99,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,132,133,134,135,140,141,142,152,156,157,158,159,160,161,162,163,],[-3,-17,-17,-17,-17,-8,-9,-17,-11,-12,-17,-17,-17,-34,-2,-4,-16,-5,-6,-7,-10,-13,-14,-15,-18,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,-20,-60,-61,-62,-63,-21,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,134,140,141,-35,142,-26,-33,-36,-28,160,161,162,163,-27,-29,-31,-30,]),'PUNTOCOMA':([4,5,6,7,10,13,14,15,16,22,44,47,48,58,59,60,61,62,63,64,66,67,72,73,74,75,80,95,96,97,98,99,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,161,162,163,],[34,34,34,34,34,34,34,34,42,-34,-22,-24,-25,-65,-66,-67,-68,-69,-70,-71,-23,-37,104,105,106,-65,109,-60,-61,-62,-63,-21,-64,-19,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,136,137,138,-32,-29,-31,-30,]),'PARA':([17,19,20,21,23,25,43,45,49,50,52,53,54,56,57,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,131,],[43,46,49,50,51,53,54,54,54,54,71,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'IGUAL':([19,44,75,107,],[45,65,45,131,]),'INCREMENTO':([19,55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,144,],[47,95,-65,-66,-67,-68,-69,-70,-71,95,95,95,95,-65,95,-60,-61,-62,-63,95,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,95,95,95,95,47,]),'DECREMENTO':([19,55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,144,],[48,96,-65,-66,-67,-68,-69,-70,-71,96,96,96,96,-65,96,-60,-61,-62,-63,96,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,96,96,96,96,48,]),'MENOS':([43,45,49,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,75,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,105,106,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,131,139,],[56,56,56,56,56,56,82,56,56,-65,-66,-67,-68,-69,-70,-71,56,82,82,82,82,-65,82,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-60,-61,-62,82,82,56,56,56,-64,-46,-47,-48,-49,-50,-51,82,82,82,82,82,82,82,82,82,82,82,56,82,]),'NOT':([43,45,49,50,53,54,56,57,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,131,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'CHARACTER':([43,45,49,50,53,54,56,57,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,131,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'BOOLEANO':([43,45,49,50,53,54,56,57,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,131,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'ENTERO':([43,45,49,50,53,54,56,57,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,131,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'DECIMAL':([43,45,49,50,53,54,56,57,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,131,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'CADENA':([43,45,49,50,53,54,56,57,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,131,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'RNULL':([43,45,49,50,53,54,56,57,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,131,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'PARC':([46,47,48,51,55,58,59,60,61,62,63,64,68,69,71,79,95,96,97,98,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,143,145,146,],[67,-24,-25,70,80,-65,-66,-67,-68,-69,-70,-71,100,101,103,108,-60,-61,-62,-63,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,148,149,150,]),'MAS':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[81,-65,-66,-67,-68,-69,-70,-71,81,81,81,81,-65,81,-60,-61,-62,81,81,-64,-46,-47,-48,-49,-50,-51,81,81,81,81,81,81,81,81,81,81,81,81,]),'POR':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[83,-65,-66,-67,-68,-69,-70,-71,83,83,83,83,-65,83,-60,-61,-62,83,83,-64,83,83,-48,-49,-50,-51,83,83,83,83,83,83,83,83,83,83,83,83,]),'DIV':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[84,-65,-66,-67,-68,-69,-70,-71,84,84,84,84,-65,84,-60,-61,-62,84,84,-64,84,84,-48,-49,-50,-51,84,84,84,84,84,84,84,84,84,84,84,84,]),'POT':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[85,-65,-66,-67,-68,-69,-70,-71,85,85,85,85,-65,85,-60,-61,-62,85,85,-64,85,85,85,85,None,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'MOD':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[86,-65,-66,-67,-68,-69,-70,-71,86,86,86,86,-65,86,-60,-61,-62,86,86,-64,86,86,-48,-49,-50,-51,86,86,86,86,86,86,86,86,86,86,86,86,]),'MENORQUE':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[87,-65,-66,-67,-68,-69,-70,-71,87,87,87,87,-65,87,-60,-61,-62,87,87,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,87,87,87,87,87,87,]),'MAYORQUE':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[88,-65,-66,-67,-68,-69,-70,-71,88,88,88,88,-65,88,-60,-61,-62,88,88,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,88,88,88,88,88,88,]),'IGUALIGUAL':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[89,-65,-66,-67,-68,-69,-70,-71,89,89,89,89,-65,89,-60,-61,-62,89,89,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,89,89,89,89,89,89,]),'DIFERENTE':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[90,-65,-66,-67,-68,-69,-70,-71,90,90,90,90,-65,90,-60,-61,-62,90,90,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,90,90,90,90,90,90,]),'MAYORIGUAL':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[91,-65,-66,-67,-68,-69,-70,-71,91,91,91,91,-65,91,-60,-61,-62,91,91,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,91,91,91,91,91,91,]),'MENORIGUAL':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[92,-65,-66,-67,-68,-69,-70,-71,92,92,92,92,-65,92,-60,-61,-62,92,92,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,92,92,92,92,92,92,]),'AND':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[93,-65,-66,-67,-68,-69,-70,-71,93,93,93,93,-65,93,-60,-61,-62,-63,93,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,93,93,93,93,93,]),'OR':([55,58,59,60,61,62,63,64,66,68,69,73,75,79,95,96,97,98,99,108,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,],[94,-65,-66,-67,-68,-69,-70,-71,94,94,94,94,-65,94,-60,-61,-62,-63,94,-64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,94,94,94,94,]),'LLAVEA':([70,100,101,103,147,148,149,150,],[102,124,125,127,151,153,154,155,]),'RELSE':([140,],[147,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,102,124,125,127,151,153,154,155,],[2,126,132,133,135,156,157,158,159,]),'instruccion':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[3,32,3,3,3,32,3,32,32,32,3,3,3,3,32,32,32,32,]),'imprimir_instr':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'declaracion_instr':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'declaracion_instr2':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'asignacion_instr':([0,2,53,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[7,7,72,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'if_instr':([0,2,102,124,125,126,127,132,133,135,147,151,153,154,155,156,157,158,159,],[8,8,8,8,8,8,8,8,8,8,152,8,8,8,8,8,8,8,8,]),'while_instr':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'break_instr':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'main_instr':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'funcion_instr':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'llamada_instr':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'asignacion2_instr':([0,2,102,124,125,126,127,132,133,135,136,137,138,151,153,154,155,156,157,158,159,],[14,14,14,14,14,14,14,14,14,14,143,145,146,14,14,14,14,14,14,14,14,]),'for_instr':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'tipo':([0,2,102,124,125,126,127,132,133,135,151,153,154,155,156,157,158,159,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'finins':([4,5,6,7,10,13,14,15,],[33,35,36,37,38,39,40,41,]),'expresion':([43,45,49,50,53,54,56,57,65,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,131,],[55,66,68,69,73,79,97,98,99,110,111,112,113,114,115,116,117,118,119,120,121,122,123,128,129,130,139,]),'declarar_con_valor_for':([53,],[74,]),'tipo_for':([53,],[76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',230),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',234),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',242),
  ('instruccion -> imprimir_instr finins','instruccion',2,'p_instruccion','grammar.py',251),
  ('instruccion -> declaracion_instr finins','instruccion',2,'p_instruccion','grammar.py',252),
  ('instruccion -> declaracion_instr2 finins','instruccion',2,'p_instruccion','grammar.py',253),
  ('instruccion -> asignacion_instr finins','instruccion',2,'p_instruccion','grammar.py',254),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','grammar.py',255),
  ('instruccion -> while_instr','instruccion',1,'p_instruccion','grammar.py',256),
  ('instruccion -> break_instr finins','instruccion',2,'p_instruccion','grammar.py',257),
  ('instruccion -> main_instr','instruccion',1,'p_instruccion','grammar.py',258),
  ('instruccion -> funcion_instr','instruccion',1,'p_instruccion','grammar.py',259),
  ('instruccion -> llamada_instr finins','instruccion',2,'p_instruccion','grammar.py',260),
  ('instruccion -> asignacion2_instr finins','instruccion',2,'p_instruccion','grammar.py',261),
  ('instruccion -> for_instr finins','instruccion',2,'p_instruccion','grammar.py',262),
  ('finins -> PUNTOCOMA','finins',1,'p_finins','grammar.py',267),
  ('finins -> <empty>','finins',0,'p_finins','grammar.py',268),
  ('instruccion -> error PUNTOCOMA','instruccion',2,'p_instruccion_error','grammar.py',272),
  ('imprimir_instr -> RPRINT PARA expresion PARC PUNTOCOMA','imprimir_instr',5,'p_imprimir','grammar.py',279),
  ('imprimir_instr -> RPRINT PARA expresion PARC','imprimir_instr',4,'p_imprimir','grammar.py',280),
  ('declaracion_instr -> tipo ID IGUAL expresion','declaracion_instr',4,'p_declaracion','grammar.py',287),
  ('declaracion_instr2 -> tipo ID','declaracion_instr2',2,'p_declaracion_nula','grammar.py',291),
  ('asignacion_instr -> ID IGUAL expresion','asignacion_instr',3,'p_asignacion','grammar.py',296),
  ('asignacion2_instr -> ID INCREMENTO','asignacion2_instr',2,'p_asignacion2','grammar.py',303),
  ('asignacion2_instr -> ID DECREMENTO','asignacion2_instr',2,'p_asignacion2','grammar.py',304),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC','if_instr',7,'p_if1','grammar.py',310),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC','if_instr',11,'p_if2','grammar.py',314),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr','if_instr',9,'p_if3','grammar.py',318),
  ('for_instr -> RFOR PARA asignacion_instr PUNTOCOMA expresion PUNTOCOMA asignacion2_instr PARC LLAVEA instrucciones LLAVEC','for_instr',11,'p_for_instr','grammar.py',325),
  ('for_instr -> RFOR PARA declarar_con_valor_for PUNTOCOMA expresion PUNTOCOMA asignacion2_instr PARC LLAVEA instrucciones LLAVEC','for_instr',11,'p_for_instr_new_var','grammar.py',331),
  ('for_instr -> RFOR PARA expresion PUNTOCOMA expresion PUNTOCOMA asignacion2_instr PARC LLAVEA instrucciones LLAVEC','for_instr',11,'p_for_instr_var','grammar.py',337),
  ('declarar_con_valor_for -> tipo_for ID IGUAL expresion','declarar_con_valor_for',4,'p_for_declara_con_valor','grammar.py',343),
  ('while_instr -> RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC','while_instr',7,'p_while','grammar.py',352),
  ('break_instr -> RBREAK','break_instr',1,'p_break','grammar.py',358),
  ('main_instr -> RMAIN PARA PARC LLAVEA instrucciones LLAVEC','main_instr',6,'p_main','grammar.py',364),
  ('funcion_instr -> RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC','funcion_instr',7,'p_funcion','grammar.py',371),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada','grammar.py',377),
  ('tipo -> RINT','tipo',1,'p_tipo','grammar.py',385),
  ('tipo -> RFLOAT','tipo',1,'p_tipo','grammar.py',386),
  ('tipo -> RSTRING','tipo',1,'p_tipo','grammar.py',387),
  ('tipo -> RBOOLEAN','tipo',1,'p_tipo','grammar.py',388),
  ('tipo -> RCHAR','tipo',1,'p_tipo','grammar.py',389),
  ('tipo -> RVAR','tipo',1,'p_tipo','grammar.py',390),
  ('tipo_for -> RINT','tipo_for',1,'p_tipo_for','grammar.py',407),
  ('tipo_for -> RVAR','tipo_for',1,'p_tipo_for','grammar.py',408),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','grammar.py',419),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','grammar.py',420),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',421),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','grammar.py',422),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion_binaria','grammar.py',423),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion_binaria','grammar.py',424),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',425),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',426),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',427),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_binaria','grammar.py',428),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',429),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',430),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','grammar.py',431),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','grammar.py',432),
  ('expresion -> expresion INCREMENTO','expresion',2,'p_expresion_binaria','grammar.py',433),
  ('expresion -> expresion DECREMENTO','expresion',2,'p_expresion_binaria','grammar.py',434),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','grammar.py',471),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','grammar.py',472),
  ('expresion -> PARA expresion PARC','expresion',3,'p_expresion_agrupacion','grammar.py',481),
  ('expresion -> ID','expresion',1,'p_expresion_identificador','grammar.py',486),
  ('expresion -> CHARACTER','expresion',1,'p_primitivo_character','grammar.py',490),
  ('expresion -> BOOLEANO','expresion',1,'p_primitivo_booleano','grammar.py',494),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','grammar.py',498),
  ('expresion -> DECIMAL','expresion',1,'p_primitivo_decimal','grammar.py',502),
  ('expresion -> CADENA','expresion',1,'p_primitivo_cadena','grammar.py',506),
  ('expresion -> RNULL','expresion',1,'p_primitivo_null','grammar.py',511),
]
