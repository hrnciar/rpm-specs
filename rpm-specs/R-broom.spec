%global packname broom
%global packver  0.5.6
%global rlibdir  %{_datadir}/R/library

# Too many optional things.
%bcond_with suggests

%if %{without suggests}
%global __suggests_exclude ^R\\((AER|Hmisc|Kendall|Lahman|akima|bbmle|betareg|binGroup|brms|btergm|caret|e1071|emmeans|ergm|gam|gamlss|gamlss\.data|glmnet|gmm|irlba|ks|lavaan|lfe|lme4|lsmeans|maptools|mclust|muhaz|network|ordinal|plm|psych|quantreg|robust|rsample|rstan|rstanarm|speedglm|survey|tseries)\\)
%endif

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          Convert Statistical Analysis Objects into Tidy Tibbles

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-backports, R-dplyr, R-generics >= 0.0.2, R-methods, R-nlme, R-purrr, R-reshape2, R-stringr, R-tibble >= 3.0.0, R-tidyr
# Suggests:  R-AER, R-akima, R-AUC, R-bbmle, R-betareg, R-biglm, R-binGroup, R-boot, R-brms, R-btergm, R-car, R-caret, R-coda, R-covr, R-e1071, R-emmeans, R-ergm, R-gam >= 1.15, R-gamlss, R-gamlss.data, R-gamlss.dist, R-geepack, R-ggplot2, R-glmnet, R-gmm, R-Hmisc, R-irlba, R-Kendall, R-knitr, R-ks, R-Lahman, R-lavaan, R-lfe, R-lme4, R-lmodel2, R-lmtest, R-lsmeans, R-maps, R-maptools, R-MASS, R-Matrix, R-mclust, R-mgcv, R-muhaz, R-multcomp, R-network, R-nnet, R-orcutt >= 2.2, R-ordinal, R-plm, R-plyr, R-poLCA, R-psych, R-quantreg, R-rgeos, R-rmarkdown, R-rsample, R-rstan, R-rstanarm, R-sp, R-speedglm, R-statnet.common, R-survey, R-survival, R-testthat, R-tseries, R-zoo
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-backports
BuildRequires:    R-dplyr
BuildRequires:    R-generics >= 0.0.2
BuildRequires:    R-methods
BuildRequires:    R-nlme
BuildRequires:    R-purrr
BuildRequires:    R-reshape2
BuildRequires:    R-stringr
BuildRequires:    R-tibble >= 3.0.0
BuildRequires:    R-tidyr

BuildRequires:    R-AUC
BuildRequires:    R-biglm
BuildRequires:    R-boot
BuildRequires:    R-car
BuildRequires:    R-coda
BuildRequires:    R-gamlss.dist
BuildRequires:    R-ggplot2
BuildRequires:    R-knitr
BuildRequires:    R-lmodel2
BuildRequires:    R-lmtest
BuildRequires:    R-maps
BuildRequires:    R-MASS
BuildRequires:    R-Matrix
BuildRequires:    R-mgcv
BuildRequires:    R-multcomp
BuildRequires:    R-nnet
BuildRequires:    R-orcutt >= 2.2
BuildRequires:    R-plyr
BuildRequires:    R-rgeos
BuildRequires:    R-rmarkdown
BuildRequires:    R-sp
BuildRequires:    R-statnet.common
BuildRequires:    R-survival
BuildRequires:    R-testthat
BuildRequires:    R-zoo
%if %{with suggests}
BuildRequires:    R-AER
BuildRequires:    R-bbmle
BuildRequires:    R-betareg
BuildRequires:    R-binGroup
BuildRequires:    R-brms
BuildRequires:    R-btergm
BuildRequires:    R-caret
BuildRequires:    R-e1071
BuildRequires:    R-emmeans
BuildRequires:    R-ergm
BuildRequires:    R-gam >= 1.15
BuildRequires:    R-gamlss
BuildRequires:    R-gamlss.data
BuildRequires:    R-geepack
BuildRequires:    R-glmnet
BuildRequires:    R-gmm
BuildRequires:    R-Hmisc
BuildRequires:    R-irlba
BuildRequires:    R-Kendall
BuildRequires:    R-ks
BuildRequires:    R-Lahman
BuildRequires:    R-lavaan
BuildRequires:    R-lfe
BuildRequires:    R-lme4
BuildRequires:    R-lsmeans
BuildRequires:    R-maptools
BuildRequires:    R-mclust
BuildRequires:    R-muhaz
BuildRequires:    R-network
BuildRequires:    R-ordinal
BuildRequires:    R-plm
BuildRequires:    R-poLCA
BuildRequires:    R-psych
BuildRequires:    R-quantreg
BuildRequires:    R-rsample
BuildRequires:    R-rstan
BuildRequires:    R-rstanarm
BuildRequires:    R-speedglm
BuildRequires:    R-survey
BuildRequires:    R-tseries
%endif

%description
Summarizes key information about statistical objects in tidy tibbles. This
makes it easy to report results, create plots and consistently work with large
numbers of models at once. Broom provides three verbs that each provide
different types of information about a model. tidy() summarizes information
about model components such as coefficients of a regression. glance() reports
information about an entire model, such as goodness of fit measures like AIC
and BIC. augment() adds information about individual observations to a dataset,
such as fitted values or influence measures.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION

# Fix line endings.
for file in %{packname}/NEWS.md %{packname}/inst/doc/*.R*; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata


%changelog
* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 0.5.6-2
- rebuild for R 4
- move geepack under with_suggests to break loop

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.6-1
- Update to latest version

* Sun Mar 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.5-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.4-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.3-2
- Fix line endings

* Wed Jan 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.3-1
- initial package for Fedora
