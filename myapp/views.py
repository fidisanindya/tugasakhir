from django.shortcuts import render, get_object_or_404, redirect
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from .models import Book, Detection, predict_image
# from .utils import predict_image
from .forms import BookForm, DetectionForm
import numpy as np
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'models/classification_model.h5')
model = load_model(model_path)

def predict(request, input_value):
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, 'simple_model.h5')
    
    # Memuat model
    model = load_model(model_path)

    # Melakukan prediksi dengan model
    input_value = float(input_value)
    prediction = model.predict(np.array([input_value]))

    # Menampilkan hasil prediksi
    return render(request, 'prediction.html', {'input_value': input_value, 'prediction': prediction[0][0]})


#crud   
def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'myapp/book_detail.html', {'book': book})

def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'myapp/book_edit.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'myapp/book_edit.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

#TA

def dashboard(request):
    return render(request, 'myapp/dashboard.html')

def detection_form(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            uploaded_image = instance.image
            file_path = uploaded_image.path
            classes = predict_image(file_path, model)
            result = 'Normal' if classes == 0 else 'Positif'    
            instance.result = result
            instance.save()

            return redirect('history')
    else:
        form = DetectionForm()

    return render(request, 'myapp/detection_form.html', {'form': form})

def history(request):
    histories = Detection.objects.all()
    return render(request, 'myapp/history.html', {'histories': enumerate(histories, 1)})

def detail_history(request, pk):
    history = get_object_or_404(Detection, pk=pk)
    return render(request, 'myapp/detail_history.html', {'history': history})