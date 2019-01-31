config={'annotation': 'Independent and marginalized limits on 4-fermion tttt eft operators. Combined SL+OS+SS unblinded upper limit of tttt cross section is used.',
 'mode': 'jinja-test',
 'combine_asymptotic_limits_json':'SL_OS_SS_combined_unblind_v2.1.json',
    'tables':{
        'independent':{
            'latex_main':'build/table_independent.tex',
            'template':'resources/common/table_independent_4op.jinja2.tex',
            'operators':['O_R','O_L^1','O_B^1','O_B^8']
        },
        'marginal':{
            'latex_main':'build/table_marginal.tex',
            'template':'resources/common/table_marginal_4op.jinja2.tex',
            'operators':['O_R','O_L^1','O_B^1','O_B^8']
        }
    }
 }
