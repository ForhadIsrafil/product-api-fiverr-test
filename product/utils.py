
def get_object(model, id):
    instance = model.objects.filter(id=id).first()
    return instance