from django import template
from django.utils.safestring import mark_safe
from mainapp.models import SmartPhone


register = template.Library()


TABLE_HEAD = """
                <table class="table table-hover" style="margin-left: 25px; width: 90%">
                    <tbody>
             """

TABLE_TAIL = """
                    </tbody>
                </table>
             """

TABLE_CONTENT = """
                <tr>
                  <td>{name}</td>
                  <td>{value}</td>
               </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display',
        'Разрешения экрана': 'resolution',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge',
        'Вид жесткого диска': 'hard_disk',
        'Количесто памяти': 'rom'

    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display',
        'Разрешения экрана': 'resolution',
        'Объем батареи': 'accum_volume',
        'Дополнительная sd-карта': 'sd',
        'Максимальный объем SD карты': 'sd_value_max',
        'Оперативная память': 'ram',
        'Главная камера': 'main_cam_mp',
        'Фронтальная камера': 'frontal_cam_mp',
        'Количесто памяти': 'rom'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, SmartPhone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Максимальный объем SD карты')
        else:
            PRODUCT_SPEC['smartphone']['Максимальный объем SD карты'] = 'sd_value_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

