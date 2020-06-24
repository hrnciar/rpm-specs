%global packname tibble
%global packver  3.0.1
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((bench)\\)

# Unavailable and/or loops.
%global with_suggests 0

Name:             R-%{packname}
Version:          3.0.1
Release:          2%{?dist}
Summary:          Simple Data Frames

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-cli, R-crayon >= 1.3.4, R-ellipsis >= 0.2.0, R-fansi >= 0.4.0, R-lifecycle >= 0.2.0, R-magrittr, R-methods, R-pillar >= 1.4.3, R-pkgconfig, R-rlang >= 0.4.3, R-utils, R-vctrs >= 0.2.4
# Suggests:  R-bench, R-bit64, R-blob, R-covr, R-dplyr, R-evaluate, R-hms, R-htmltools, R-import, R-knitr, R-mockr, R-nycflights13, R-purrr, R-rmarkdown, R-testthat >= 2.1.0, R-tidyr, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli
BuildRequires:    R-crayon >= 1.3.4
BuildRequires:    R-ellipsis >= 0.2.0
BuildRequires:    R-fansi >= 0.4.0
BuildRequires:    R-lifecycle >= 0.2.0
BuildRequires:    R-magrittr
BuildRequires:    R-methods
BuildRequires:    R-pillar >= 1.4.3
BuildRequires:    R-pkgconfig
BuildRequires:    R-rlang >= 0.4.3
BuildRequires:    R-utils
BuildRequires:    R-vctrs >= 0.2.4
BuildRequires:    R-bit64
BuildRequires:    R-blob
BuildRequires:    R-evaluate
BuildRequires:    R-hms
BuildRequires:    R-htmltools
BuildRequires:    R-import
BuildRequires:    R-knitr
BuildRequires:    R-mockr
BuildRequires:    R-purrr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-withr
%if %{with_suggests}
BuildRequires:    R-tidyr
BuildRequires:    R-bench
BuildRequires:    R-dplyr
BuildRequires:    R-nycflights13
%endif

%description
Provides a 'tbl_df' class (the 'tibble') that provides stricter checking and
better formatting than the traditional data frame.


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
export LANG=C.UTF-8
%if %{with_suggests}
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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 3.0.1-2
- move tidyr under with_suggests to break loop
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.1-1
- Update to latest version

* Fri Apr 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.3-1
- Update to latest version

* Wed May 29 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.2-1
- Update to latest version

* Sun Mar 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-2
- rebuilt

* Tue Aug 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- initial package for Fedora
