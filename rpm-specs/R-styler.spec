%global packname styler
%global packver  1.3.2
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((data\\.tree)\\)

%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Summary:          Non-Invasive Pretty Printing of R Code

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# https://github.com/r-lib/styler/issues/613
Patch0001:        https://github.com/r-lib/styler/pull/614.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-backports >= 1.1.0, R-cli >= 1.1.0, R-magrittr >= 1.0.1, R-purrr >= 0.2.3, R-R.cache >= 0.14.0, R-rematch2 >= 2.0.1, R-rlang >= 0.1.1, R-rprojroot >= 1.1, R-tibble >= 1.4.2, R-tools, R-withr >= 1.0.0, R-xfun >= 0.1
# Suggests:  R-data.tree >= 0.1.6, R-digest, R-dplyr, R-here, R-knitr, R-prettycode, R-rmarkdown, R-rstudioapi >= 0.7, R-testthat >= 2.1.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-backports >= 1.1.0
BuildRequires:    R-cli >= 1.1.0
BuildRequires:    R-magrittr >= 1.0.1
BuildRequires:    R-purrr >= 0.2.3
BuildRequires:    R-R.cache >= 0.14.0
BuildRequires:    R-rematch2 >= 2.0.1
BuildRequires:    R-rlang >= 0.1.1
BuildRequires:    R-rprojroot >= 1.1
BuildRequires:    R-tibble >= 1.4.2
BuildRequires:    R-tools
BuildRequires:    R-withr >= 1.0.0
BuildRequires:    R-xfun >= 0.1
%if %{with_suggests}
BuildRequires:    R-data.tree >= 0.1.6
%endif
BuildRequires:    R-digest
BuildRequires:    R-dplyr
BuildRequires:    R-here
BuildRequires:    R-knitr
BuildRequires:    R-prettycode
BuildRequires:    R-rmarkdown
BuildRequires:    R-rstudioapi >= 0.7
BuildRequires:    R-testthat >= 2.1.0

%description
Pretty-prints R code without changing the user's formatting intent.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch00001 -p1
popd

%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/rstudio


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.2-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
