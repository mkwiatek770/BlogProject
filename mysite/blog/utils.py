from django.utils.text import slugify


def unique_slug_generator(instance, title, slug_field):
    # replacing polish letters
    title = title.lower().translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))
    slug = slugify(title)
    model_class = instance.__class__

    while model_class.objects.filter(slug=slug).exists():
        object_pk = model_class.objects.latest("pk")
        object_pk = object_pk.pk + 1

        slug = f"{slug}-{object_pk}"
    return slug
