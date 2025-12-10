
import json

path = 'Pre-processing/word_pos_tagging.ipynb'
try:
    with open(path, 'r') as f:
        nb = json.load(f)

    modified = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell.get('source', [])
            new_source = []
            changed_this_cell = False
            for line in source:
                new_source.append(line)
                if 'from nltk.corpus import stopwords' in line:
                    # Check if already added to avoid duplication
                    # Look ahead? simple check:
                    if len(source) > source.index(line) + 1 and 'stop_words =' in source[source.index(line) + 1]:
                        pass
                    else:
                        new_source.append('stop_words = set(stopwords.words("english"))\n')
                        changed_this_cell = True
            
            if changed_this_cell:
                cell['source'] = new_source
                modified = True
                break # Only fix the first occurrence
    
    if modified:
        with open(path, 'w') as f:
            json.dump(nb, f, indent=1)
        print("Fixed")
    else:
        print("No change needed")

except Exception as e:
    print(f"Error: {e}")
