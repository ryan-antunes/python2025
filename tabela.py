

layout = '''<!DOCTYPE html>
<html lang = "pt-br">
<head>
    <table border ="1">
    <tr>
        <td>Matérias</td>
        <td>1B</td>
        <td>2B</td>
        <td>3B</td>
        <td>4B</td>
        <td>Media</td>
    </tr>
    <tr>
        <td>Português</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Matemática</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Biologia</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Química</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Geografia</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>
    <meta charset = "UTF-8>
    <meta name = "viewport"
    content = "width=device-width, intial-scale=1.0">'''

arquivo_html = open("notas.html", "w")
arquivo_html.write(layout)
arquivo_html.close()