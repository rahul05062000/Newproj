import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm

def handle_uploaded_file(file):
    # Read the file using pandas
    if file.name.endswith('.xlsx'):
        data = pd.read_excel(file)
    else:
        data = pd.read_csv(file)

    # Ensure column names match your file's columns
    if 'Cust State' in data.columns and 'DPD' in data.columns:
        summary = data.groupby(['Cust State', 'DPD']).size().reset_index(name='Count')
    else:
        summary = pd.DataFrame(columns=['Cust State', 'DPD', 'Count'])  # Return an empty dataframe if columns not found
    return summary

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            summary = handle_uploaded_file(request.FILES['file'])
            return render(request, 'file_upload_app/report.html', {'summary': summary.to_html()})
    else:
        form = UploadFileForm()
    return render(request, 'file_upload_app/upload.html', {'form': form})
