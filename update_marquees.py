import os
import glob

replacements = {
    'id:"a-11-n-2",actionTypeId:"TRANSFORM_MOVE",config:{delay:0,easing:"",duration:4e4,': 'id:"a-11-n-2",actionTypeId:"TRANSFORM_MOVE",config:{delay:0,easing:"",duration:54000,',
    'id:"a-206-n-2",actionTypeId:"TRANSFORM_ROTATE",config:{delay:0,easing:"",duration:6e3,': 'id:"a-206-n-2",actionTypeId:"TRANSFORM_ROTATE",config:{delay:0,easing:"",duration:8100,',
    'id:"a-259-n-2",actionTypeId:"TRANSFORM_MOVE",config:{delay:0,easing:"",duration:1e4,': 'id:"a-259-n-2",actionTypeId:"TRANSFORM_MOVE",config:{delay:0,easing:"",duration:13500,',
    'id:"a-202-n-2",actionTypeId:"TRANSFORM_MOVE",config:{delay:0,easing:"",duration:2e4,': 'id:"a-202-n-2",actionTypeId:"TRANSFORM_MOVE",config:{delay:0,easing:"",duration:27000,'
}

count = 0
for path in glob.glob(r'C:\Users\angam\Downloads\Leano Website V1\**\*.js', recursive=True):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        modified = False
        for old, new in replacements.items():
            if old in new_content:
                new_content = new_content.replace(old, new)
                modified = True
                
        if modified:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {path}")
            count += 1
    except Exception as e:
        pass
        
print(f"Total files updated: {count}")
