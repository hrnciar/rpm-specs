%global packname roxygen2
%global packver  7.1.1
%global rlibdir  %{_libdir}/R/library

%bcond_with bootstrap

Name:             R-%{packname}
Version:          7.1.1
Release:          1%{?dist}
Summary:          In-Line Documentation for R

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-brew, R-commonmark, R-desc >= 1.2.0, R-digest, R-knitr, R-methods, R-pkgload >= 1.0.2, R-purrr >= 0.3.3, R-R6 >= 2.1.2, R-Rcpp >= 0.11.0, R-rlang, R-stringi, R-stringr >= 1.0.0, R-utils, R-xml2
# Suggests:  R-covr, R-devtools, R-rmarkdown, R-testthat >= 2.1.0, R-R.methodsS3, R-R.oo
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-brew
BuildRequires:    R-commonmark
BuildRequires:    R-desc >= 1.2.0
BuildRequires:    R-digest
BuildRequires:    R-knitr
BuildRequires:    R-methods
BuildRequires:    R-pkgload >= 1.0.2
BuildRequires:    R-purrr >= 0.3.3
BuildRequires:    R-R6 >= 2.1.2
BuildRequires:    R-Rcpp-devel >= 0.11.0
BuildRequires:    R-rlang
BuildRequires:    R-stringi
BuildRequires:    R-stringr >= 1.0.0
BuildRequires:    R-utils
BuildRequires:    R-xml2
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-R.methodsS3
BuildRequires:    R-R.oo
%if %{without bootstrap}
BuildRequires:    R-devtools
%endif

%description
Generate your Rd documentation, 'NAMESPACE' file, and collation field using
specially formatted comments. Writing documentation in-line with code makes it
easier to keep your documentation up-to-date as your requirements change.
'Roxygen2' is inspired by the 'Doxygen' system for C++.


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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Mon Sep 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.1.1-1
- Update to latest version (#1851631)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 7.1.0-2
- rebuild for R 4
- disable with_suggests to break the loop with devtools

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.1.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.0.2-1
- Update to latest version

* Fri Nov 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.0.1-1
- Update to latest version

* Wed Nov 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 7.0.0-1
- Update to latest version

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.1.1-4
- Exclude Suggests for unavailable packages

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.1.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.0.1-2
- Rebuild for R 3.5.0

* Sun May 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.0.1-1
- initial package for Fedora
