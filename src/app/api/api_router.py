from fastapi import APIRouter

from src.app.resources.business_resource import Business_resource

router = APIRouter()
resource = Business_resource()



#TODO cpt con mas npi (que mas esta cubierto, no se si conviene meterte a dar el mismo servicio) -> cpt, agrupado por npis y numero de servicios (sumados) EL TOP 10 de eso
@router.get("/api/v1/top_covered_hcps/")
async def get_top_covered_hcps():
    return resource.get_top_covered_hcps()


#TODO cpt que no es cubierto por algun estado (onda: andate a AK a cubrir el CPT XXX poruqe nadie lo da)
@router.get("/api/v1/top_payer_states/{hcpcs_code}")
async def get_top_payers_by_hcpcs_code(hcpcs_code: str):
    return resource.get_top_payers_by_hcpcs_code(hcpcs_code=hcpcs_code)


#TODO top 10 de cpt codes con mas servicios
@router.get("/api/v1/top_hcpcs_code_services/")
async def get_hcpcs_code_by_services():
    return resource.get_hcpcs_code_by_services()


#TODO diferencia de precios entre cpt y por estado? agrupar por estado y cpt y ver el avg de precio (onda: en AK estan pagando mas por el CPT XXX)
@router.get("/api/v1/top_payer_states/{hcpcs_code}")
async def get_top_payers_by_hcpcs_code(hcpcs_code: str):
    return resource.get_top_payers_by_hcpcs_code(hcpcs_code=hcpcs_code)


#TODO top 10 de estados que mejor pagan por un cpt code
@router.get("/api/v1/best_payer_state/{hcpcs_code}")
async def get_best_payer_states_by_hcpcs_code(hcpcs_code: str):
    return resource.get_best_payer_states_by_hcpcs_code(hcpcs_code=hcpcs_code)


#TODO que estados cubren menor cantidad de cpts? agrupar por estado y cpt y ver el distinct(cpt)
@router.get("/api/v1/less_coverage_states/")
async def get_states_less_hcpcs_coverage():
    return resource.get_states_less_hcpcs_coverage()


# TODO los estados donde se paga mas cercano al allowed: los mas "confiables"
@router.get("/api/v1/more_reliable_states/{hcpcs_code}")
async def get_more_reliable_states_by_hcpcs(hcpcs_code: str):
    return resource.get_more_reliable_states_by_hcpcs(hcpcs_code=hcpcs_code)


'''
    los cpts que mas pagan, como para saber que servicios ofrecer
'''
@router.get("/api/v1/more_profitable_hcpcs/")
async def get_more_profitable_hcpcs():
    return resource.get_more_profitable_hcpcs()
