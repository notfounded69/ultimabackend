from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from .models import Agentes
from .forms import ValidacionForm


def valorant(request):
    # Get all the agents
    agentes = Agentes.objects.all()
    return render(request, 'valorant/agentes.html', {'agentes': agentes})


def formu(request):
    # Crear una instancia del formulario
    form = ValidacionForm()

    if request.method == "POST":
        # Vincular el formulario a los datos de la solicitud
        form = ValidacionForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            
            # Guardar los datos del formulario
            form.save()
            
            # Enviar el correo electrónico con la imagen adjunta
            # Agregar la imagen como un archivo adjunto
            

            subject = 'Bienvenido a valorant {}'.format(nombre)
            body = 'Gracias por registrarte en nuestra página web♥'

            # Crear un mensaje de correo electrónico con formato HTML
            msg = EmailMultiAlternatives(subject, body, 'newnewsvalorant@gmail.com', [correo])

            # Agregar el código HTML para mostrar la imagen
            html_body = '<p>Gracias por registrarte en nuestra página web♥</p>'
            html_body += '<p><img src="https://villagepipol.com/wp-content/uploads/2022/11/valorant-1.png"></p>'
            msg.attach_alternative(html_body, 'text/html')

            # Enviar el correo electrónico
            msg.send()
            
            # Crear una nueva instancia del formulario
            form = ValidacionForm()
            
            # Mostrar un mensaje de éxito
            return render(request, 'valorant/formu.html', {'form_enviado': True, 'form': form})
        else:
            # Mostrar un mensaje de error
            return render(request, 'valorant/formu.html', {'form_enviado': False, 'form': form})
    else:
        return render(request, 'valorant/formu.html', {'form': form})
