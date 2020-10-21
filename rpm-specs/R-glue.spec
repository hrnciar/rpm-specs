%global packname glue
%global packver  1.4.2
%global rlibdir  %{_libdir}/R/library

# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_with bootstrap

Name:             R-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Interpreted String Literals

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods
# Suggests:  R-testthat, R-covr, R-magrittr, R-crayon, R-knitr, R-rmarkdown, R-DBI, R-RSQLite, R-R.utils, R-forcats, R-microbenchmark, R-rprintf, R-stringr, R-ggplot2, R-dplyr, R-withr, R-vctrs >= 0.3.0
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
%if %{without bootstrap}
BuildRequires:    R-testthat
BuildRequires:    R-magrittr
BuildRequires:    R-crayon
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-DBI
BuildRequires:    R-RSQLite
BuildRequires:    R-R.utils
BuildRequires:    R-forcats
BuildRequires:    R-microbenchmark
BuildRequires:    R-rprintf
BuildRequires:    R-stringr
BuildRequires:    R-ggplot2
BuildRequires:    R-dplyr
BuildRequires:    R-withr
BuildRequires:    R-vctrs >= 0.3.0
%endif

%description
An implementation of interpreted string literals, inspired by Python's
Literal String Interpolation <https://www.python.org/dev/peps/pep-0498/>
and Docstrings <https://www.python.org/dev/peps/pep-0257/> and Julia's
Triple-Quoted String Literals
<https://docs.julialang.org/en/v1.3/manual/strings/#Triple-Quoted-String-Literals-1>.


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
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
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
* Fri Aug 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version (#1820713)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul  3 2020 José Matos <jamatos@fedoraproject.org> - 1.4.1-2
- replace "with_suggests" by "bcond_with bootstrap" since that is really its purpose

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.1-1
- break testthat loop by broadening "with_suggests"
- update to 1.4.1
- rebuild for R 4

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-4
- Exclude Suggests for unavailable packages

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- initial package for Fedora
