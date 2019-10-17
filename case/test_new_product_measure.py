#encoding: utf-8
import pytest
from service.new_product_measure import NewProductMeasureService
from common.tools import yaml_replace_for_filter
import allure


@allure.feature("新品测量")
@allure.tag("新品测量-ARN作业单状态")
class TestNewProductMeasure:
    '''
    新品测量测试类
    '''
    @allure.title("通过货品条码获取料五项")
    @pytest.mark.parametrize("login",yaml_replace_for_filter("login.yml"),indirect=True)
    @pytest.mark.parametrize("get_five_items",yaml_replace_for_filter("get_five_items.yml",dir_case="product_measure",filter="get_five_items"))
    def test_get_five_items(self,login,get_five_items,):
        response = NewProductMeasureService.get_five_items(get_five_items)
        json = response.json()
        print(json['data'][0])
        assert json['data'][0]['codingSystemName']==get_five_items['assert']['codingSystemName']

    @allure.title("根据itemId获取货品信息")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("goods_info",yaml_replace_for_filter("get_goods_info.yml",dir_case="product_measure",
                                                                      filter="goods_info"))
    def test_get_goods_info(self,login,goods_info):
        info = NewProductMeasureService.get_goods_info(goods_info)
        json = info.json()
        print(json['data'][0])
        assert json['data'][0]['storageType']==goods_info['assert']['storageType']

    @allure.title("新品测量-获取单位级别")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("unit_level", yaml_replace_for_filter("get_unit_level.yml", dir_case="product_measure",
                                                                       filter="unit_level"))
    def test_get_unit_level(self,login,unit_level):
        level = NewProductMeasureService.get_unit_level(unit_level)
        json = level.json()
        print(json['data'][0])
        assert json['data'][0]['enumName']==unit_level['assert']['enumName']

    @allure.title("新品测量-获取件型")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("part_type", yaml_replace_for_filter("get_part_type.yml", dir_case="product_measure",
                                                                       filter="part_type"))
    def test_get_part(self,login,part_type):
        get_part_type = NewProductMeasureService.get_part_type(part_type)
        json = get_part_type.json()
        print(json['data'][0])
        assert json['data'][0]['enumName']==part_type['assert']['enumName']

    @allure.title("新品测量-获取单位名称")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("unit_name", yaml_replace_for_filter("get_unit_name.yml", dir_case="product_measure",
                                                                  filter="unit_name"))
    def test_unit_name(self, login, unit_name):
        print(unit_name)
        get_unit_name = NewProductMeasureService.get_unit_name(unit_name)
        json = get_unit_name.json()
        print(json['data'][0])
        assert json['data'][0]['enumName'] == unit_name['assert']['enumName']

    @allure.title("新品测量-获取货品分类")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("goods_type", yaml_replace_for_filter("get_goods_type.yml", dir_case="product_measure",
                                                                  filter="goods_type"))
    def test_goods_type(self,login,goods_type):
        get_goods_type = NewProductMeasureService.get_goods_type(goods_type)
        json = get_goods_type.json()
        print(json)
        assert json['data'][0]['name']==goods_type['assert']['name']

    @allure.title("新品测量-获取存储分类")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("storage_type", yaml_replace_for_filter("get_storage_type.yml", dir_case="product_measure",
                                                                  filter="storage_type"))
    def test_storage_type(self,login,storage_type):
        get_storage_type = NewProductMeasureService.get_storage_type(storage_type)
        json = get_storage_type.json()
        print(json)
        assert json['data'][2]['dataValue']==storage_type['assert']['dataValue']

    @allure.title("新品测量-获取物流类型")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("logistics_type", yaml_replace_for_filter("get_logistics_type.yml", dir_case="product_measure",
                                                                     filter="logistics_type"))
    def test_logistics_type(self, login, logistics_type):
        get_logistics_type = NewProductMeasureService.get_storage_type(logistics_type)
        json = get_logistics_type.json()
        print(json)
        assert json['data'][0]['enumName'] == logistics_type['assert']['enumName']

    @allure.title("新品测量-获取币种")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("currency", yaml_replace_for_filter("get_currency.yml", dir_case="product_measure",
                                                                     filter="currency"))
    def test_currency(self, login, currency):
        get_currency = NewProductMeasureService.get_currency(currency)
        json = get_currency.json()
        print(json)
        assert json['data'][0]['name'] == currency['assert']['name']

    @allure.title("新品测量-获取批次跟踪属性")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("lot_tracking", yaml_replace_for_filter("get_lot_tracking.yml", dir_case="product_measure",
                                                                 filter="lot_tracking"))
    def test_lot_tracking(self, login, lot_tracking):
        get_lot_tracking = NewProductMeasureService.get_lot_tracking(lot_tracking)
        json = get_lot_tracking.json()
        print(json)
        assert json['data'][1]['name'] == lot_tracking['assert']['name']

    @allure.title("新品测量-保存包装单位")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("save_package", yaml_replace_for_filter("save_package_unit.yml", dir_case="product_measure",
                                                                 filter="save_package"))
    def test_save_package_unit(self, login, save_package):
        save_package_unit = NewProductMeasureService.get_lot_tracking(save_package)
        json = save_package_unit.json()
        print(json)
        assert json['code'] == save_package['assert']['code']

    @allure.title("新品测量-提交货品名称ZXCVB，提交成功")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("measure_new_item",
                             yaml_replace_for_filter("measure_new_item.yml", dir_case="product_measure",
                                                     filter="measure_new_item",index=1))
    def test_measure_new_item_001(self, login, measure_new_item):
        get_measure_new_item = NewProductMeasureService.measure_new_item(measure_new_item)
        json = get_measure_new_item.json()
        print(json)
        assert json['code'] == measure_new_item['assert']['code']

    @allure.title("新品测量-提交货品名称sy002，提交成功")
    @pytest.mark.parametrize("login", yaml_replace_for_filter("login.yml"), indirect=True)
    @pytest.mark.parametrize("measure_new_item",
                             yaml_replace_for_filter("measure_new_item.yml", dir_case="product_measure",
                                                     filter="measure_new_item", index=2))
    def test_measure_new_item_002(self, login, measure_new_item):
        get_measure_new_item = NewProductMeasureService.measure_new_item(measure_new_item)
        json = get_measure_new_item.json()
        print(json)
        assert json['code'] == measure_new_item['assert']['code']