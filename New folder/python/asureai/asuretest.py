# https://learn.microsoft.com/en-us/python/api/azure-ai-documentintelligence/azure.ai.documentintelligence?view=azure-python-preview


#Before continue, remember we can always use our mouse for some pop up explain

# =========================================
# STEP 1: imptorts libraries and confirms setup is correct
# =========================================

from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

# =========================================
# STEP 2: 
# =========================================


my_endpoint = ""
my_key = ""

# What is this?
client = DocumentIntelligenceClient(
    endpoint=my_endpoint,
    credential=AzureKeyCredential(my_key)
)

# =========================================
# STEP 3: 
# =========================================

# Why?
use_url = True

# =========================================
# STEP 4: 
# =========================================

if use_url:

    document_url = ""
    print("Using document from URL...")

    request = AnalyzeDocumentRequest(url_source=document_url)
    poller = client.begin_analyze_document("prebuilt-layout", request)
    result = poller.result()

else:

    print("You chose local file input, but it's not set up yet.")
    print("🛠️ Try implementing this part yourself using a file path and open().")
    result = None  # 

# =========================================
# STEP 5: 
# =========================================

if result:
    pages = result.pages
    print("\nTotal pages in the document:")
    print(len(pages))

    print("\nText found in each page:")

    for page in pages:
        for line in page.lines:
            print("Line text:")
            print(line.content)

    print("\nSelection marks (checkboxes):")
    for page in pages:
        for mark in page.selection_marks:
            print("Mark state:", mark.state)
            print("Confidence:", mark.confidence)

    print("\nTables:")
    for table in result.tables:
        print("Table with", table.row_count, "rows and", table.column_count, "columns")
        for cell in table.cells:
            print("Cell:", cell.content)

# =========================================
# ✨ CHALLENGE ZONE
# =========================================

# 1. Change use_url to False.
# 2. Store line contents in a list
# 3. Count how many marks are 'selected'
# 4. Replace model name with "prebuilt-document" and see what changes
# 5. Add a print that tells you how many total lines were found

# =========================================
# 📝 Imposible?
# =========================================

# - Add your own variable to store something new / dynamic variable
# - Create a table
# - Print a custom summary at the end
# - Try changing the document URL or implement the local file input