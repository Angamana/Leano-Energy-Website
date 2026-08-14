import glob

files = glob.glob(r'C:\Users\angam\Downloads\Leano Website V1\**\*.html', recursive=True)

pe_fix = """<style id="fuel-widget-pointer-events-fix">
/* Allow clicks to pass through the empty space of the fixed widget container */
.fuel-side-tabs {
    pointer-events: none !important;
}
/* Re-enable clicks on the actual visible button and panel */
.fuel-main-tab-btn, .fuel-panel-container {
    pointer-events: auto !important;
}
</style>"""

missing_pe = []
for f in files:
    if 'Cookie System' in f or 'Donor' in f or 'Archived' in f:
        continue
    with open(f, encoding='utf-8') as fp:
        c = fp.read()
    if 'fuel-widget-pointer-events-fix' not in c:
        missing_pe.append(f)

print(f"Total HTML files missing fuel-widget-pointer-events-fix: {len(missing_pe)}")
for m in missing_pe:
    print(" -", m)
