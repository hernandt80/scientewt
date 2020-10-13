from fastapi import APIRouter

from ..resources.business_resource import Business_resource

router = APIRouter()
resource = Business_resource()


@router.get("/api/v1/top_payer_states/{hcpcs_code}")
async def get_top_payers_by_hcpcs_code(hcpcs_code: str):
    return resource.get_top_payers_by_hcpcs_code(hcpcs_code=hcpcs_code)


@router.get("/api/v1/top_hcpcs_code_services/")
async def get_hcpcs_code_by_services():
    return resource.get_hcpcs_code_by_services()


@router.get("/api/v1/top_payer_states/{hcpcs_code}")
async def get_top_payers_by_hcpcs_code(hcpcs_code: str):
    return resource.get_top_payers_by_hcpcs_code(hcpcs_code=hcpcs_code)


@router.get("/api/v1/best_payer_state/{hcpcs_code}")
async def get_best_payer_states_by_hcpcs_code(hcpcs_code: str):
    return resource.get_best_payer_states_by_hcpcs_code(hcpcs_code=hcpcs_code)


@router.get("/api/v1/less_coverage_states/")
async def get_states_less_hcpcs_coverage():
    return resource.get_states_less_hcpcs_coverage()


@router.get("/api/v1/more_reliable_states/{hcpcs_code}")
async def get_more_reliable_states_by_hcpcs(hcpcs_code: str):
    return resource.get_more_reliable_states_by_hcpcs(hcpcs_code=hcpcs_code)


@router.get("/api/v1/more_profitable_hcpcs/")
async def get_more_profitable_hcpcs():
    return resource.get_more_profitable_hcpcs()


@router.get("/api/v1/avg_amounts_by_cpt/{hcpcs_code}")
async def get_avg_amounts_by_cpt(hcpcs_code: str):
    return resource.get_avg_amounts_by_cpt(hcpcs_code=hcpcs_code)


@router.get("/api/v1/create_database/")
async def create_database():
    return resource.create_database()


@router.get("/api/v1/populate_medicare_table/")
async def populate_medicare_table():
    return resource.populate_medicare_table()


@router.get("/api/v1/populate_provider_table/")
async def populate_provider_table():
    return resource.populate_provider_table()
