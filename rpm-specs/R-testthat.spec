%bcond_with check

%global packname testthat
%global packver 2.3.2

%global __suggests_exclude ^R\\((devtools)\\)

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{packver}.tar.gz
License:          MIT
URL:              https://cran.r-project.org/package=testthat
Summary:          Unit Testing for R
BuildRequires:    R-devel >= 3.4.0, tetex-latex
BuildRequires:    R-cli
BuildRequires:    R-crayon >= 1.3.4
BuildRequires:    R-digest
BuildRequires:    R-ellipsis
BuildRequires:    R-evaluate
BuildRequires:    R-magrittr
BuildRequires:    R-methods
BuildRequires:    R-pkgload
BuildRequires:    R-praise
BuildRequires:    R-R6 >= 2.2.0
BuildRequires:    R-rlang >= 0.4.1
BuildRequires:    R-withr >= 2.0.0
%if %{with check}
BuildRequires:    R-covr
BuildRequires:    R-curl >= 0.9.5
BuildRequires:    R-devtools
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-usethis
BuildRequires:    R-vctrs >= 0.1.0
BuildRequires:    R-xml2
%endif

%description
A unit testing system designed to be fun, flexible, and easy to set up.

%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
%if %{with check}
export _R_CHECK_FORCE_SUGGESTS_=0 LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/CITATION
# Not the actual license text. Not too useful.
%doc %{_libdir}/R/library/%{packname}/LICENSE
%doc %{_libdir}/R/library/%{packname}/NEWS.md
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/examples/
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/resources/
%{_libdir}/R/library/%{packname}/include/

%changelog
* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 2.3.2-2
- rebuild for R 4

* Tue Mar  3 2020 Tom Callaway <spot@fedoraproject.org> - 2.3.2-1
- update to 2.3.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Tom Callaway <spot@fedoraproject.org> - 2.3.1-1
- update to 2.3.1

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.0-2
- Exclude Suggests for unavailable packages

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 2.3.0-1
- update to 2.3.0

* Fri Aug 16 2019 Tom Callaway <spot@fedoraproject.org> - 2.2.1-1
- update to 2.2.1

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Tom Callaway <spot@fedoraproject.org> - 2.1.1-1
- update to 2.1.1

* Tue Apr 23 2019 Tom Callaway <spot@fedoraproject.org> - 2.1.0-1
- update to 2.1.0

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version
- Enable tests

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 2.0.0-2
- fix Requires (cleanup BR too)

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 2.0.0-1
- gotta go to 2.0.0

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.0.2-6
- rebuild for R 3.5.0

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.0.2-5
- rebuild for now, cannot upgrade due to unpackaged deps

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.2-1
- update to 1.0.2, rebuild for R 3.4.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Tom Callaway <spot@fedoraproject.org> - 0.11.0-2
- fix define to be global

* Wed Nov 4 2015 Tom Callaway <spot@fedoraproject.org> - 0.11.0-1
- Initial package
