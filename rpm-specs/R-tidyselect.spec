%global packname tidyselect
%global packver  1.1.0
%global rlibdir  %{_datadir}/R/library

# dplyr requires this package.
%global with_loop 0

Name:             R-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Select from a Set of Strings

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-ellipsis, R-glue >= 1.3.0, R-purrr >= 0.3.2, R-rlang >= 0.4.6, R-vctrs >= 0.2.2
# Suggests:  R-covr, R-crayon, R-dplyr, R-knitr, R-magrittr, R-rmarkdown, R-testthat >= 2.3.0, R-tibble >= 2.1.3, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-ellipsis
BuildRequires:    R-glue >= 1.3.0
BuildRequires:    R-purrr >= 0.3.2
BuildRequires:    R-rlang >= 0.4.6
BuildRequires:    R-vctrs >= 0.2.2
BuildRequires:    R-crayon
%if %{with_loop}
BuildRequires:    R-dplyr
%endif
BuildRequires:    R-knitr
BuildRequires:    R-magrittr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 2.3.0
BuildRequires:    R-tibble >= 2.1.3
BuildRequires:    R-withr

%description
A backend for the selecting functions of the 'tidyverse'. It makes it easy
to implement select-like functions in your own packages in a way that is
consistent with other 'tidyverse' interfaces for selection.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_loop}
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


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Tue Feb 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-2
- Fix install location

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.5-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.5-1
- initial package for Fedora
