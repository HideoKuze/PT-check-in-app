<title> PT Sign-In</title>

    <div style="background-color:blue">
    <h1>Enter Id</h1>
    <form method="POST" class= "post-form"> {% csrf_token %}
        {{ form.as_p }}
        <button type='submit' class="save btn-default">Save</button>
    </form>

{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}