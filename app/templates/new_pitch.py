{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf%}

{% block styles%}
{{ super() }}
{% endblock%}


{% block content%}
<div class="container">
    {{wtf.quick_form(form)}}
</div>
{% endblock %}
