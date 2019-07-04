#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import re

root = ET.parse('./assets/spaceshooter/Spritesheet/sheet.xml').getroot()
for st in root.findall('SubTexture'):
    print((re.sub(r'(.*)\.png', r'\1', st.get('name'))), st.get('x'),
          st.get('y'), st.get('width'), st.get('height'))
