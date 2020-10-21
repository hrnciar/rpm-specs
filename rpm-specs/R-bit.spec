%bcond_without bootstrap

%global packname bit
%global packver  4.0.4
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.0.4
Release:          1%{?dist}
Summary:          Classes and Methods for Fast Memory-Efficient Boolean Selections

License:          GPLv2 or GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-testthat >= 0.11.0, R-roxygen2, R-knitr, R-rmarkdown, R-microbenchmark, R-bit64 >= 4.0.0, R-ff >= 4.0.0
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-testthat >= 0.11.0
BuildRequires:    R-roxygen2
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-microbenchmark
%if %{without bootstrap}
BuildRequires:    R-bit64 >= 4.0.0
BuildRequires:    R-ff >= 4.0.0
%endif
BuildRequires:    tex(framed.sty)

%description
Provided are classes for boolean and skewed boolean vectors, fast boolean
methods, fast unique and non-unique integer sorting, fast set operations on
sorted and unsorted sets of integers, and foundations for ff (range index,
compression, chunked processing).


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with bootstrap}
export _R_CHECK_FORCE_SUGGESTS_=0
%endif
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Tue Aug 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.4-1
- Update to latest version
- Fixes rhbz#1865767

* Fri Jul 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.3-1
- Update to latest version
- Fixes rhbz#1862139

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.15.2-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.15.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.14-1
- Update to latest version

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.1.13-1
- update to 1.1-13, rebuild for R 3.5.0

* Thu Mar 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.12-2
- Fix file encodings and line endings.

* Thu Mar 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.12-1
- initial package for Fedora
