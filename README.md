## science WT

### Endpoints details:

:octocat: Get Top Payers By Hcpcs Code (states that better pay for a given cpt code)
- GET /api/v1/top_payer_states/{hcpcs_code}

:octocat: Get Hcpcs Code By Services (cpt with more number of services)
- GET /api/v1/top_hcpcs_code_services/

:octocat: Get Best Payer States By Hcpcs Code (states that shoud pay better a cpt, acording to the allowed amount)
- GET /api/v1/best_payer_state/{hcpcs_code}

:octocat: Get States Less Hcpcs Coverage (states that cover less cpts)
- GET /api/v1/less_coverage_states/

:octocat: Get More Reliable States By Hcpcs (highest % of payment comparing with allowed amount)
- GET /api/v1/more_reliable_states/{hcpcs_code}

:octocat: Get More Profitable Hcpcs (cpt with highest payment by provider state)
- GET /api/v1/more_profitable_hcpcs/

:octocat: Get Avg Amounts By Cpt (using RBQL proccesing .cvs file)
- GET /api/v1/avg_amounts_by_cpt/{hcpcs_code}
