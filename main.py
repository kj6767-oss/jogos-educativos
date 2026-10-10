from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from jnius import autoclass, cast

class MeuApp(App):
    def build(self):
        # Layout com um botão
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        botao = Button(text='Abrir Bloco de Notas', font_size=20)
        botao.bind(on_press=self.disparar_intent)
        layout.add_widget(botao)
        return layout

    def disparar_intent(self, instance):
        # Carrega as classes Java necessárias
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        String = autoclass('java.lang.String')

        # Cria o Intent para ENVIAR texto
        intent = Intent()
        intent.setAction(Intent.ACTION_SEND)
        intent.setType("text/plain")
        
        # Adiciona o texto que será "transmitido"
        texto = cast('java.lang.CharSequence', String("ops,você foi hackeado:( "))
        intent.putExtra(Intent.EXTRA_TEXT, texto)

        # Inicia a Activity (abre o seletor de apps do sistema)
        atividade = cast('android.app.Activity', PythonActivity.mActivity)
        atividade.startActivity(Intent.createChooser(intent, "Escolha o Bloco de Notas"))
