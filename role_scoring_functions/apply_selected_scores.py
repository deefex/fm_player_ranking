from .calculate_afa_scores import calculate_afa_scores
from .calculate_apa_scores import calculate_apa_scores
from .calculate_aps_scores import calculate_aps_scores
from .calculate_ad_scores import calculate_ad_scores
from .calculate_ama_scores import calculate_ama_scores
from .calculate_ams_scores import calculate_ams_scores
from .calculate_bpdc_scores import calculate_bpdc_scores
from .calculate_bpdd_scores import calculate_bpdd_scores
from .calculate_bpds_scores import calculate_bpds_scores
from .calculate_bwmd_scores import calculate_bwmd_scores
from .calculate_bwms_scores import calculate_bwms_scores
from .calculate_b2bs_scores import calculate_b2bs_scores
from .calculate_cars_scores import calculate_cars_scores
from .calculate_cdc_scores import calculate_cdc_scores
from .calculate_cdd_scores import calculate_cdd_scores
from .calculate_cds_scores import calculate_cds_scores
from .calculate_cma_scores import calculate_cma_scores
from .calculate_cmd_scores import calculate_cmd_scores
from .calculate_cms_scores import calculate_cms_scores
from .calculate_cfa_scores import calculate_cfa_scores
from .calculate_cfs_scores import calculate_cfs_scores
from .calculate_cwba_scores import calculate_cwba_scores
from .calculate_cwbs_scores import calculate_cwbs_scores
from .calculate_dlfa_scores import calculate_dlfa_scores
from .calculate_dlfs_scores import calculate_dlfs_scores
from .calculate_dlpd_scores import calculate_dlpd_scores
from .calculate_dlps_scores import calculate_dlps_scores
from .calculate_dmd_scores import calculate_dmd_scores
from .calculate_dms_scores import calculate_dms_scores
from .calculate_dwd_scores import calculate_dwd_scores
from .calculate_dws_scores import calculate_dws_scores
from .calculate_engs_scores import calculate_engs_scores
from .calculate_f9s_scores import calculate_f9s_scores
from .calculate_fba_scores import calculate_fba_scores
from .calculate_fbd_scores import calculate_fbd_scores
from .calculate_fbs_scores import calculate_fbs_scores
from .calculate_gkd_scores import calculate_gkd_scores
from .calculate_hbd_scores import calculate_hbd_scores
from .calculate_ifa_scores import calculate_ifa_scores
from .calculate_ifs_scores import calculate_ifs_scores
from .calculate_ifbd_scores import calculate_ifbd_scores
from .calculate_iwa_scores import calculate_iwa_scores
from .calculate_iws_scores import calculate_iws_scores
from .calculate_iwba_scores import calculate_iwba_scores
from .calculate_iwbd_scores import calculate_iwbd_scores
from .calculate_iwbs_scores import calculate_iwbs_scores
from .calculate_ld_scores import calculate_ld_scores
from .calculate_ls_scores import calculate_ls_scores
from .calculate_meza_scores import calculate_meza_scores
from .calculate_mezs_scores import calculate_mezs_scores
from .calculate_ncbc_scores import calculate_ncbc_scores
from .calculate_ncbd_scores import calculate_ncbd_scores
from .calculate_ncbs_scores import calculate_ncbs_scores
from .calculate_nfbd_scores import calculate_nfbd_scores
from .calculate_pa_scores import calculate_pa_scores
from .calculate_pfa_scores import calculate_pfa_scores
from .calculate_pfd_scores import calculate_pfd_scores
from .calculate_pfs_scores import calculate_pfs_scores
from .calculate_raua_scores import calculate_raua_scores
from .calculate_regs_scores import calculate_regs_scores
from .calculate_rps_scores import calculate_rps_scores
from .calculate_sks_scores import calculate_sks_scores
from .calculate_skd_scores import calculate_skd_scores
from .calculate_ska_scores import calculate_ska_scores
from .calculate_sva_scores import calculate_sva_scores
from .calculate_svs_scores import calculate_svs_scores
from .calculate_ssa_scores import calculate_ssa_scores
from .calculate_tfa_scores import calculate_tfa_scores
from .calculate_tfs_scores import calculate_tfs_scores
from .calculate_trea_scores import calculate_trea_scores
from .calculate_wcba_scores import calculate_wcba_scores
from .calculate_wcbd_scores import calculate_wcbd_scores
from .calculate_wcbs_scores import calculate_wcbs_scores
from .calculate_wma_scores import calculate_wma_scores
from .calculate_wmd_scores import calculate_wmd_scores
from .calculate_wms_scores import calculate_wms_scores
from .calculate_wpa_scores import calculate_wpa_scores
from .calculate_wps_scores import calculate_wps_scores
from .calculate_wtfa_scores import calculate_wtfa_scores
from .calculate_wtfs_scores import calculate_wtfs_scores
from .calculate_wa_scores import calculate_wa_scores
from .calculate_ws_scores import calculate_ws_scores
from .calculate_wba_scores import calculate_wba_scores
from .calculate_wbd_scores import calculate_wbd_scores
from .calculate_wbs_scores import calculate_wbs_scores


def apply_selected_scores(squad_rawdata, selected_roles):
    for role in selected_roles:
        match role:
            case 'afa':
                squad_rawdata = calculate_afa_scores(squad_rawdata)
            case 'apa':
                squad_rawdata = calculate_apa_scores(squad_rawdata)
            case 'aps':
                squad_rawdata = calculate_aps_scores(squad_rawdata)
            case 'ad':
                squad_rawdata = calculate_ad_scores(squad_rawdata)
            case 'ama':
                squad_rawdata = calculate_ama_scores(squad_rawdata)
            case 'ams':
                squad_rawdata = calculate_ams_scores(squad_rawdata)
            case 'bpdc':
                squad_rawdata = calculate_bpdc_scores(squad_rawdata)
            case 'bpdd':
                squad_rawdata = calculate_bpdd_scores(squad_rawdata)
            case 'bpds':
                squad_rawdata = calculate_bpds_scores(squad_rawdata)
            case 'bwmd':
                squad_rawdata = calculate_bwmd_scores(squad_rawdata)
            case 'bwms':
                squad_rawdata = calculate_bwms_scores(squad_rawdata)
            case 'b2bs':
                squad_rawdata = calculate_b2bs_scores(squad_rawdata)
            case 'cars':
                squad_rawdata = calculate_cars_scores(squad_rawdata)
            case 'cdc':
                squad_rawdata = calculate_cdc_scores(squad_rawdata)
            case 'cdd':
                squad_rawdata = calculate_cdd_scores(squad_rawdata)
            case 'cds':
                squad_rawdata = calculate_cds_scores(squad_rawdata)
            case 'cma':
                squad_rawdata = calculate_cma_scores(squad_rawdata)
            case 'cmd':
                squad_rawdata = calculate_cmd_scores(squad_rawdata)
            case 'cms':
                squad_rawdata = calculate_cms_scores(squad_rawdata)
            case 'cfa':
                squad_rawdata = calculate_cfa_scores(squad_rawdata)
            case 'cfs':
                squad_rawdata = calculate_cfs_scores(squad_rawdata)
            case 'cwba':
                squad_rawdata = calculate_cwba_scores(squad_rawdata)
            case 'cwbs':
                squad_rawdata = calculate_cwbs_scores(squad_rawdata)
            case 'dlfa':
                squad_rawdata = calculate_dlfa_scores(squad_rawdata)
            case 'dlfs':
                squad_rawdata = calculate_dlfs_scores(squad_rawdata)
            case 'dlpd':
                squad_rawdata = calculate_dlpd_scores(squad_rawdata)
            case 'dlps':
                squad_rawdata = calculate_dlps_scores(squad_rawdata)
            case 'dmd':
                squad_rawdata = calculate_dmd_scores(squad_rawdata)
            case 'dms':
                squad_rawdata = calculate_dms_scores(squad_rawdata)
            case 'dwd':
                squad_rawdata = calculate_dwd_scores(squad_rawdata)
            case 'dws':
                squad_rawdata = calculate_dws_scores(squad_rawdata)
            case 'engs':
                squad_rawdata = calculate_engs_scores(squad_rawdata)
            case 'f9s':
                squad_rawdata = calculate_f9s_scores(squad_rawdata)
            case 'fba':
                squad_rawdata = calculate_fba_scores(squad_rawdata)
            case 'fbd':
                squad_rawdata = calculate_fbd_scores(squad_rawdata)
            case 'fbs':
                squad_rawdata = calculate_fbs_scores(squad_rawdata)
            case 'gkd':
                squad_rawdata = calculate_gkd_scores(squad_rawdata)
            case 'hbd':
                squad_rawdata = calculate_hbd_scores(squad_rawdata)
            case 'ifa':
                squad_rawdata = calculate_ifa_scores(squad_rawdata)
            case 'ifs':
                squad_rawdata = calculate_ifs_scores(squad_rawdata)
            case 'ifbd':
                squad_rawdata = calculate_ifbd_scores(squad_rawdata)
            case 'iwa':
                squad_rawdata = calculate_iwa_scores(squad_rawdata)
            case 'iws':
                squad_rawdata = calculate_iws_scores(squad_rawdata)
            case 'iwba':
                squad_rawdata = calculate_iwba_scores(squad_rawdata)
            case 'iwbd':
                squad_rawdata = calculate_iwbd_scores(squad_rawdata)
            case 'iwbs':
                squad_rawdata = calculate_iwbs_scores(squad_rawdata)
            case 'ld':
                squad_rawdata = calculate_ld_scores(squad_rawdata)
            case 'ls':
                squad_rawdata = calculate_ls_scores(squad_rawdata)
            case 'meza':
                squad_rawdata = calculate_meza_scores(squad_rawdata)
            case 'mezs':
                squad_rawdata = calculate_mezs_scores(squad_rawdata)
            case 'ncbc':
                squad_rawdata = calculate_ncbc_scores(squad_rawdata)
            case 'ncbd':
                squad_rawdata = calculate_ncbd_scores(squad_rawdata)
            case 'ncbs':
                squad_rawdata = calculate_ncbs_scores(squad_rawdata)
            case 'nfbd':
                squad_rawdata = calculate_nfbd_scores(squad_rawdata)
            case 'pa':
                squad_rawdata = calculate_pa_scores(squad_rawdata)
            case 'pfa':
                squad_rawdata = calculate_pfa_scores(squad_rawdata)
            case 'pfd':
                squad_rawdata = calculate_pfd_scores(squad_rawdata)
            case 'pfs':
                squad_rawdata = calculate_pfs_scores(squad_rawdata)
            case 'raua':
                squad_rawdata = calculate_raua_scores(squad_rawdata)
            case 'regs':
                squad_rawdata = calculate_regs_scores(squad_rawdata)
            case 'rps':
                squad_rawdata = calculate_rps_scores(squad_rawdata)
            case 'skd':
                squad_rawdata = calculate_skd_scores(squad_rawdata)
            case 'sks':
                squad_rawdata = calculate_sks_scores(squad_rawdata)
            case 'ska':
                squad_rawdata = calculate_ska_scores(squad_rawdata)
            case 'sva':
                squad_rawdata = calculate_sva_scores(squad_rawdata)
            case 'svs':
                squad_rawdata = calculate_svs_scores(squad_rawdata)
            case 'ssa':
                squad_rawdata = calculate_ssa_scores(squad_rawdata)
            case 'tfa':
                squad_rawdata = calculate_tfa_scores(squad_rawdata)
            case 'tfs':
                squad_rawdata = calculate_tfs_scores(squad_rawdata)
            case 'trea':
                squad_rawdata = calculate_trea_scores(squad_rawdata)
            case 'wcba':
                squad_rawdata = calculate_wcba_scores(squad_rawdata)
            case 'wcbd':
                squad_rawdata = calculate_wcbd_scores(squad_rawdata)
            case 'wcbs':
                squad_rawdata = calculate_wcbs_scores(squad_rawdata)
            case 'wma':
                squad_rawdata = calculate_wma_scores(squad_rawdata)
            case 'wmd':
                squad_rawdata = calculate_wmd_scores(squad_rawdata)
            case 'wms':
                squad_rawdata = calculate_wms_scores(squad_rawdata)
            case 'wpa':
                squad_rawdata = calculate_wpa_scores(squad_rawdata)
            case 'wps':
                squad_rawdata = calculate_wps_scores(squad_rawdata)
            case 'wtfa':
                squad_rawdata = calculate_wtfa_scores(squad_rawdata)
            case 'wtfs':
                squad_rawdata = calculate_wtfs_scores(squad_rawdata)
            case 'wa':
                squad_rawdata = calculate_wa_scores(squad_rawdata)
            case 'ws':
                squad_rawdata = calculate_ws_scores(squad_rawdata)
            case 'wba':
                squad_rawdata = calculate_wba_scores(squad_rawdata)
            case 'wbd':
                squad_rawdata = calculate_wbd_scores(squad_rawdata)
            case 'wbs':
                squad_rawdata = calculate_wbs_scores(squad_rawdata)
            case _:
                print('Unknown role')
    return squad_rawdata
