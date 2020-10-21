%global packname  readxl
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3.1
Release:          8%{?dist}
Summary:          Read Excel Files

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Patch0001:        0001-Unbundle-libxls.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cellranger, R-Rcpp >= 0.12.18, R-tibble >= 1.3.1, R-utils
# Suggests:  R-covr, R-knitr, R-rmarkdown, R-rprojroot >= 1.1, R-testthat
# LinkingTo: R-progress, R-Rcpp
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    libxls-devel >= 1.5.0
#BuildRequires:    rapidxml-devel
BuildRequires:    R-cellranger
BuildRequires:    R-Rcpp-devel >= 0.12.18
BuildRequires:    R-tibble >= 1.3.1
BuildRequires:    R-utils
BuildRequires:    R-progress-devel
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-rprojroot >= 1.1
BuildRequires:    R-testthat

# Patched-in functionality, so not removeable.
Provides: bundled(rapidxml-devel) = 1.13

%description
Import excel files into R. Supports '.xls' via the 'libxls' C library
<https://github.com/libxls/libxls> and '.xlsx' via the embedded
'RapidXML' C++ library <http://rapidxml.sourceforge.net>.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Remove bundled libxls.
%patch0001 -p1
rm src/{endian,ole,xls,xlstool}.c
rm -r src/libxls src/unix src/windows

# Patched-in functionality, so not removeable.
## Remove bundled rapidxml.
#rm src/rapidxml*
chmod -x src/rapidxml*

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


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
%{rlibdir}/%{packname}/extdata


%changelog
* Fri Sep 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-8
- rebuilt for libxls

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Sun Mar 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- initial package for Fedora
